##Setup Redshift Guide
This is a guide on how to properly setup a Redshift cluster, focusing primarily on setting it up inside your custom VPC's private subnet for enhanced security. 

###Objective
Once set up, we should have a good understanding of the process of configuring your Redshift cluster inside a private subnet. We should then be able to connect directly from our SQL client into our Redshift cluster via tunneling through our bastion host. 

1. Simply, open a connection to your bastion host with tunneling configured.
2. Then, configure your SQL client with the following and connect.
```
Driver = "Redshift (com.amazon.redshift.jdbc42.Driver)"
URL = "jdbc:redshift://localhost:5439/dcydatabase"
Username = "admin"
Password = "*****"
```

###Prerequisites
This guide is fairly involved and requires quite a bit of prerequsite knowledge before attempting this guide.

1. You must have a good understanding of VPCs and you must alreay have created a VPC with both a public and private subnet. See "Setup VPC Guide" and "Configure VPC Private Subnet" for details. 
2. You must already have a bastion host provisioned that can access your private subnet. See "Configure VPC Private Subnet" for details. 
3. In order to test our cluster, you will also need to have a SQL client setup on our computer. See "Setup SQL Workbench Guide" for details.
4. You will also need to have a good understanding of S3 and EC2. You must know how to create EC2 instances. See guides: "Setup S3 Web Host Guide" and "Setup EC2 Guide" for details.
5. If you are using Linux or Mac you must have a good understanding of SSH and how to SSH into your EC2 instances. If you are using Windows you must have PuTTy installed and know how to use PuTTy to access your EC2 instances. See guides: "Setup EC2 Guide" and "PuTTy Key Guide" for details.

###Create a Redshift S3 Role
We will be using a Redshift role to access our data stored on S3 rather than user credentials. Roles are far more secure because they do not require exposing user credentials and user secret access keys.

1. Go to the IAM dashboard, select "Roles" on the side panel, and then click "Create New Role". 
2. Name the role and click "Next Step".
```
Role Name = "Redshift_S3-Admin"
```
3. Under "AWS Service Roles", select "Amazon Redshift".
4. Then attach the "AmazonS3FullAccess" policy. Then click "Next Step" and "Create Role".

###Create Cluster In Your VPC
In the prerequsite section your should already have a custom VPC with a publcic and a private subnet created. Now we will provision a Redshift cluster into the private subnet. 

1. Go to your Redshift dashboard and click "Create Cluster" and configure the details. Make a note of the "Master user name" and "Master user password" you configure. Then click "Continue".
```
Cluster Identifier = "dcy-cluster"
Database Name = "dcydatabase"
Database Port = "5439"
Master User Name = "admin"
Master User Password = "*****"
Confirm Password = "*****"
```
2. In the node specifications, for testing purposes we will use "dc1.large". See http://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html for the specifications of the different cluster types. For node, we will use multi-node with 2 nodes, this is pretty standard. Then click "Coninue".
```
Node Type = "dc1.large"
Cluster Type = "Multi Node"
Number of compute nodes = "2"
```
3. For this example, default parameter group is fine and do not encrypt the database.
4. Under "Configure network options", choose your custom VPC and the private subnet. Then, make it inaccessible to the public with enhanced VPC routing turned on. Also, specify the availability zone, this should be the same as the availability zone of your private subnet.
```
Choose a VPC = "vpc-7de1c61b"
Cluster Subnet Group = "thematrix-private"
Publicly Accessible = "No"
Enhanced VPC Routing = "Yes"
Availability Zone = "us-east-1d"
```
5. Select your security group. Important: make sure your security group is configured as to allow Redshift on port 5439. See "Configure VPC Private Subnet" guide for more details. Also, make sure that the security group allows only traffic into your private subnet from the your public subnet. Again, see "Configure VPC Private Subnet" guide for details.
```
VPC Security Groups = "theMatrix-sg-RDSSG"
```
6. Leave CloudWatch Alarm as default. Then attach the role we created earlier. Then click "Continue".
```
Available Roles = "Redshift_S3-Admin"
```
7. Review and click "Create". The cluster should take a few mins to create.

###Create an Endpoint
Now that our Redshift cluster is sitting inside our VPC, we need to create an endpoint that will allow our VPC to communicate with S3. 

1. Go to your VPC dashboard, and open up the "Endpoints" section. Then click "Create Endpoint".
2. Select your custom VPC and select the S3 service that it will connect to. Then click "Next Step".
```
VPC = "vpc-7de1c61b | theMatrix-VPC"
Service = "com.amazonaws.us-east-1.s3"
Policy = "Full Access"
```
3. In "Configure Route Tables" select your private route. In our example it is our main route: "theMatrix-route-main", which we configured in the "Setup VPC Guide". 

###Provision a Bastion Host
Since our cluster sits inside our private subnet we can only access it through our bastion host. As a prerequsite, you should already have a bastion host. If not, see "Configure VPC Private Subnet" to set up a bastion host.

Once set up, test to make sure you can access your private instance:
```
sudo su -s /bin/bash neo
chmod 600 ~/.ssh/authorized_keys
chmod go-w ~/ ~/.ssh
ssh ec2-user@10.0.1.111 -i ~/.ssh/authorized_keys
```

###Start Tunneling
With our bastion host created, we need build a tunnel from our localhost to our Redshift cluster. This process is different for Linux/Mac and Windows.

For Windows users, you need to have PuTTy. See "PuTTy Key Guide" for more details. 

1. Inside PuTTy, expand "SSH" and click on "Tunnels".
2. Go to your Redshift cluster and copy the "Endpoint" link, ei:
```
dcy-cluster.cmgjkrnrf8l7.us-east-1.redshift.amazonaws.com:5439
```
3. In the "Source Port" field type in "5439" and make the "Destination" that endpoint link. Note that the source port does not have to match the port associated with the endpoint port. The souce port simply must be an unused port on your computer. 
```
Source Port = "5439"
Destination = "dcy-cluster.cmgjkrnrf8l7.us-east-1.redshift.amazonaws.com:5439"
```
4. Click "Add" to add to your forwarded ports.
5. Now go back to your session and open a connection to your bastion host.

For Linux/Mac users, we can invoke a local port forwarding directly to our bastion host with: 
```
ssh bastion.us-east1.amazonaws.com \
  -L5439:dcy-cluster.cmgjkrnrf8l7.us-east-1.redshift.amazonaws.com:5439 -nNT
```

###Connect to SQL Client
Now we can connect directly from our SQL client into our Redshift cluster via the tunnel. For our example, we will use SQL Workbench/J, which is Aws' recommended client. For instructions on setting up SQL Workbench/J, see "Setup SQL Workbench Guide".

1. Important: keep the connection to our bastion host open. 
2. Open up you SQL workbench client. Then go to File > Connect Window. Click on the "Create a New Connection Profile" icon and give it a name, ei: "dcy-cluster".
3. Now specify the driver as the Amazon Redshift driver that you should have installed when setting up your SQL Workbench. 
4. Then specify the URL as "jdbc:redshift://localhost:5439/dcydatabase". Note that the "/dcydatabase" is the database name and not the database identifier. For username and password, it is the "Master user name" and "Master user password" you made a note of earlier.
```
Driver = "Redshift (com.amazon.redshift.jdbc42.Driver)"
URL = "jdbc:redshift://localhost:5439/dcydatabase"
Username = "admin"
Password = "*****"
```
5. Make sure to check Autocommit and add the following Connet Script under "Statement to keep connection alive". Then specifiy an idle time.
```
Statement to keey connection alive = "select version();"
Idle time = "15"
```
6. Now click ok and we should be connected to our Redshift cluster.

Note that if there is an error, common issue is often that the VPC security group attached to your cluster was not configured to allow Redshift traffic. To check this:

1. Select your Redshift cluster and under "Cluster Properties" make sure you have the correct VPC security group attached:
```
VPC Security Groups = "theMatrix-sg-RDSSG"

```
2. Now go to VPC, and click on "Security Groups" and select the security group and go to the "Inbound Rules" tab. Make sure that the security group allows Redshift traffic from your bastion host, ei:
```
Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "10.0.2.0/24"
Type = "MYSQL/Aurora", Protocol = "TCP", Port Range = "3306", Source = "10.0.2.0/24"
Type = "Redshift", Protocol = "TCP", Port Range = "5439", Source = "10.0.2.0/24"
Type = "All ICMP - IPv4", Protocol = "ICMP", Port Range = "ALL", Source = "10.0.2.0/24"
```

###Result
Once connected, we can now preform import data from S3 and run SQL queries on our cluster from our SQL client. We can run some tests to make sure Redshift is communicating with S3 and our SQL client properly.

1. Create a table in your cluster and check the "Database Explorer" in SQL workbench to make sure the create was successful. This tests shows that SQL workbench is properly connected to our Redshift cluster.
```sql
CREATE TABLE cxc_csv
(
  bid_descrip   VARCHAR(200) NOT NULL,
  bid_model     VARCHAR(40) NOT NULL,
  bid_quant     INTEGER NOT NULL,
  bid_price     DECIMAL NOT NULL,
  bid_categ     VARCHAR(40) NOT NULL
)
DISTSTYLE EVEN;
```

2. Use the copy command to load from S3 the csv file named that we created in the "Setup SQL Workbench Guide", named "csv_bidFakeData.csv". This tests shows that our Redshift cluster is properly communicating with S3 via our VPC Endpoint. Note, that it make take a few seconds to load the data in. For production level databases we will need a more powerful bastion host than our t2-micro.
```sql
copy bid_csv
from 's3://dcy-database/Big data/csv_bidFakeData.csv'
credentials 'aws_iam_role=arn:aws:iam::117730920402:role/Redshift_S3-Admin'
IGNOREHEADER 1
ACCEPTINVCHARS '~'
ROUNDEC
DELIMITER ','
CSV QUOTE ''''
```
