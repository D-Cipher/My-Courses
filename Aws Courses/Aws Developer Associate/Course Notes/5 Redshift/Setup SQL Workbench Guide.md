##Setup Redshift Guide
This is a guide on how to properly setup SQL Workbench/J as your client for connecting to your Redshift clusters. SQL Workbench/J is the recommended free client by Amazon. For more information on other partner tools, visit: https://aws.amazon.com/redshift/partners/. This guide will focus on setting up your client and connecting to a public Redshift cluster. It is highly recommended that you make your clusters private, but for setting up SQL Workbench/J purposes, we will build a public cluster. For more inforation on setting up a private cluster, see "Setup Redshift Guide".

###Objective
Once set up, we should have a good understanding of the process of connecting your SQL Workbench client to Redshift. We should then be able to connect directly from our SQL client into our public Redshift cluster. 

Simply configure your SQL client with the following and connect:
```
Driver = "Redshift (com.amazon.redshift.jdbc42.Driver)"
URL = "jdbc:redshift://localhost:5439/dcydatabase"
Username = "admin"
Password = "*****"
```

###Prerequisites
For this guide, please have SQL workbench and Java Runtime Environment already installed. Also, it is recommended that you have experience working with VPCs.

1. SQL Workbench/J can be installed at: http://www.sql-workbench.net/.
2. Java Runtime Environment can be installed at: http://www.oracle.com/technetwork/java/javase/downloads/.

###Create a Cluster
Now we will provision a Redshift cluster into the public subnet in the default VPC.

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
4. Under "Configure network options", choose the "Default VPC". Also, keep it as publically accessible. It is highly recommended that you build your own VPC and put it in a private subnet, but for purposes of testing, we will use the default and public. 

```
Choose a VPC = "Default VPC (vpc-02491a64)"
Cluster Subnet Group = "default"
Publicly Accessible = "Yes"
Choose a public IP address = "No"
Enhanced VPC Routing = "No"
Availability Zone = "No Preference"
```
5. VPC security groups should be left as default.
6. Leave CloudWatch Alarm as default. Then attach a role to allow Redshift to access S3. See "Setup IAM Guide" for details on creating roles. Then click "Continue".
```
Available Roles = "Redshift_S3-Admin"
```
7. Review and click "Create". The cluster should take a few mins to create.

###Configure SQL Workbench
In order to connect SQL Workbench to our cluster, we need to download the jdbc driver and configure it with SQL. Then we will connect to our database using our cluster's JDBC url.

1. Go to the Redshift dashboard and click on "Connect client". Then next to JDBC Driver select "JDBC 4.2 (.jar)" and note the file path that it downloads to. Note, you can also use ODBC driver if that is your preference.
2. Open up SQL Workbench and click on "File" > "Connect Window" to open up the connection profile window.
3. Click "Manage Drivers" at the bottom left. Then create a new driver profile named "Redshift" with the file path to the JDBC we downloaded earlier. Then click "OK".
```
Name = "Redshift"
Library = "C:\Users\cawen\Documents\Aws Files\Aws KEYS\Redshift Drivers\RedshiftJDBC42-1.1.17.1017.jar"
Classname = "com.amazon.redshift.jdbc42.Driver"
```
4. Create a new connection profile (top-left first button) and give it a name. Then select your Redshift driver.
5. In Redshift, click on your cluster, and under the "Cluster Database Properties" section copy your "JDBC URL". Then SQL workbench, paste the "JDBC URL" in the URL field. 
6. For username and password, use the username and password you configured when creating the cluster.
```
Driver = "Redshift (com.amazon.redshift.jdbc42.Driver)"
URL = "jdbc:redshift://dcy-cluster.c4wtwtuews1y.us-east-1.redshift.amazonaws.com:5439/dcydatabase"
Username = "admin"
Password = "*****"
```
7. Finally, make sure to check "Autocommit".

###Result
To test the VPC private subnet, we need to provision a new EC2 instance into it. See "Setup EC2 Guide". When configuring the instance details make sure to put it in the VPC, ei:
```
Network = "theMatrix-VPC"
Subnet = "subnet-1b464b36 | 10.0.1.0-us-east-1d"
Auto-assign Public IP = "Use subnet setting (Disable)"
```
Then, be sure to select the security group we created earlier, and click launch instance. Important, make a note of the EC2 key pair that you are using and its location. Also, don't include a bootstrap script for this instance.

Once the instance is launched, click on the private instance and notice that it has no IPv4 Public IP address. Whereas, if you click on the public instance it does have one. In order to access our instance in the private subnet, we must SSH into our public subnet instance, then from there, SSH into our private subnet instance. 

1. Click on your private instance and make a note of the PRIVATE ip address, ei:
```
Private IPs = "10.0.1.111"
```
2. Navigate to the location where you saved your EC2 key pair for your private instance. Then use vi and copy to your clipboard of all of the contents in the file. Copy from "------BEGIN RSA..." all the way to the end, "...PRIVATE KEY------". Note: to use vi type "i" to enter instert text mode and "esc" key to exit instert text mode. Then type ":w" to write the text into the file. Use "y" to copy and "p" to paste. Finally, type ":q" to exit vi.
```
cd /Documents/Aws Files/Aws KEYS/EC2 Key Pairs/
vi EC2TestKey.pem
```
3. Then SSH into your public instance. See "Setup EC2 Guide" on how to SSH into an instance.
4. Elevate your privileges to su and create the key pair inside your instance, ei: use nano "EC2TestKey.pem", then paste in the contents on your clipboard. Note: to use nano right click to paste, [ctrl] + "x" then "y" and [enter] to save and exit.
```
sudo su
nano EC2TestKey.pem
```
5. Now from your public instance, SSH into you private instance, using the key and the private ip address.
```
chmod 0600 EC2TestKey.pem
ssh ec2-user@10.0.1.111 -i EC2TestKey.pem
```
If VPC has been configured correctly, we should be inside our private subnet instance, which should have access the internet via our NAT gateway. To test this, perform a yum update and it should update all security patches. Also, yum install mysql, it should be able to download mySQL.   
```
sudo su
yum update -y
yum install mysql -y
```