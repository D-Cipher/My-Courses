##Configure VPC Private Subnet
This is a guide on configuring your VPCs' private subnets allowing your private subnets to communicate out to the internet via a network address translation (NAT).

###Objective
Once set up, we should have a good understanding of the process of configuring your VPC's private subnet with the ability to communicate with your public subnet via a network address translation (NAT).

From our public instance, we will be able to SSH into our private instance, using its EC2 key pair and its private ip address.
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

###Prerequisites
You first already have a VPC with a public subnet and a private subnet created. See "Setup VPC Guide" for details.   

###Allocate Elastic IP
1. In the VPC dashboard click on "Elastic IPs"
2. Click "Allocate new address" and note the allocation ID of your new elastic IP.

###Create NAT
A NAT can be created in one of two ways: 1) Configure an instance to perform NAT called a NAT instance, 2) deploy a NAT gateway. NAT instances are very involved and require manager scripts and updating to prevent bottlenecks. NAT gateways will be managed by Amazon so once setup Amazon will handle all of the updates and sizing. For this reason, NAT gateways are prefered and will be the method we use in this guide.

1. In the VPC dashboard click on "NAT Gateways".
2. Click create NAT Gateway and deploy it into your PUBLIC subnet. Then select your elastic IP.
```
Subnet = "subnet-43fb937f | 10.0.2.0-us-east-1e"
Elastic IP Allocation ID = "eipalloc-2ce4761d"
```
3. Then click "Create a NAT Gateway".

###Edit Route Table
Now we want to add a route in our private subnet to the NAT gateway.

1. Go to "Route Tables" then select your private subnet, ei: "theMatrix-route-main".
2. Click on the "Routes" tab, then click "Edit".
3. Click "Add another route" and add the NAT gateway as the target, and destination as "0.0.0.0/0". Then click "Save".
```
Destination = "0.0.0.0/0", Target = "nat-04d4fb40a0ba620a8"
```

###Create New Security Group
In order to test our NAT gateway, we need to create a new security group for the EC2 instance we will set up in our private subnet. This is important because we need to specify the type of traffic we are going to allow in. A private SQL server, for example, we will allow SSH, ICMP, and mySQL. Important note, the source will always be coming from our public subnet's ip address.

1. Go to "Security Groups", click "Create Security Group".
```
Name Tag = "theMatrix-sg-RDSSG"
Group Name = "theMatrix-sg-RDSSG"
Desciption = "SSH, MYSQL, All ICMP"
VPC = "vpc-7de1c61b | theMatrix-VPC"
```
2. Once created, select the security group, click the "Inbound Rules" tab. Then click "Edit". Then configure the following rules. Again, for source, use our public subnet's ip:
```
Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "10.0.2.0/24"

Type = "MYSQL/Aurora", Protocol = "TCP", Port Range = "3306", Source = "10.0.2.0/24"

Type = "All ICMP - IPv4", Protocol = "ICMP", Port Range = "ALL", Source = "10.0.2.0/24"
```

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