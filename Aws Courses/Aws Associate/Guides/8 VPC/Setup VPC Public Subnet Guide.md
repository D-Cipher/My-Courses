## Setup VPC Guide
This is a guide on setting up your own VPCs that let you provision an isolated section of AWS where you can launch your AWS resources in a virtual network that you define. You chave full control over the virtual network.

### Objective
Once set up, we should have a good understanding of the process of creating your own VPC and configuring your public subnet properly. If all works correctly, create an instance in your new VPC, use the following bash script, and you should be able to view your index.html via the public IP address. 
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1>Hello World</h1></html>" > index.html
```

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details.

### Create a VPC
There are two ways to create a VPC, first is through the "Start VPC Wizard" and the second is "Create VPC", this guide will focus on the "Create VPC" method, which is more customizable.
1. In the VPC dashboard, go to "Your VPC" then click on "Create VPC".
2. Give the vpc a name, and use "10.0.0.0/16" for the IPv4 CIDR block.
3. Leave IPv6 CIDR as default.
4. Tenancy allows us to run our VPC in a private hardware, but it is more expensive. we can leave as default.
```
Name Tag = "theMatrix-VPC"
IPv4 CIDR block = "10.0.0.0/16"
IPv6 CIDR block = "No"
Tenancy = "Default"
```

### Create Subnets
Next we need two subnets, one main subnet which will be private and one public. We can create multiple subnets, however, only one subnet can be created per availability zone.
1. Go to Subnets and click on "Create Subnet".
2. Give the subnet a name. Naming convention is the address range and availability zone.
3. Select our VPC, ei: "theMatrix-VPC".
4. Select the availability zone, ei: "us-east-1d".
5. Let IPv4 CIDR block be the address range and "/24".
```
Name Tag = "10.0.1.0-us-east-1a"
VPC = "theMatrix-VPC"
Availability Zone = "us-east-1a"
IPv4 CIDR block = "10.0.1.0/24"
```
Repeat these steps for your public subnet.
```
Name Tag = "10.0.2.0-us-east-1b"
VPC = "theMatrix-VPC"
Availability Zone = "us-east-1b"
IPv4 CIDR block = "10.0.2.0/24"
IPv6 CIDR block = "default"
```

### Auto-Assign IP Address
In order for instances inside the public subnet to access the internet we need to have the instance assign ip addresses to them.
1. Go to "Subnets" and select your public subnet, in our case 10.0.2.0-us-east-1b. Then click on "Subnet Actions" > "Modify auto-assign IP settings".
2. Check "Enable auto-assign public IPv4 address", then click save.

### Attach Internet Gateway
To allow a subnet access to the internet we can attach an Internet Gateway to our VPC. Note that only one Internet Gateway per VPC.
1. Go to Internet Gateway and click "Create Internet Gateway".
2. Name it your VPC name plus "IGW".
```
Name Tag = "theMatrix-IGW"
```
3. Then click "Attach to VPC" and select the VPC.

### Create a Route Table
Route tables allow us to create route-in and route-outs into our subnets. Note that by default when we created our VPC a main route table was created for it. It's best practice to keep this main route table private, and create seperate public route tables.
1. Go to Route Tables and rename your main route table that was created automatically to "theMatrix-route-main" to identify it as the main routing table.
2. Create a new route table by clicking on "Create Route Table".
3. Name it "theMatrix-route-public" and associate it with your VPC in the dropdown and click create.
```
Name Tag = "theMatrix-route-public"
VPC = "theMatrix-VPC"
```
4. Select your public route (theMatrix-route-public), go to the "Routes" tab and click "Edit routes" then click "Add another route", allowing all traffic with the target as your IGW. For destination type in "0.0.0.0/0", for target select your internet gateway from the dropdown.
5. Add another route for IPv6. Click "Add route" and for destination type in "::/0", for target select your internet gateway from the dropdown. Then click "Save Routes".
```
Destination = "0.0.0.0/0"; Target = "igw-fe243c99"
Destination = "::/0"; Target = "igw-fe243c99"
```

### Associate Subnets
Now that we have our route tables we need to associate our subnets into them. By default our subnets will be associated with the main route table if no associations are assigned. However, it is recommended that you specify all assignments.
1. Select your private route table and go to "Subnet Associations" > "Edit", and select the one you want public, 10.0.1.0-us-east-1a. Then click "Save".
```
subnet-1b464b36 | 10.0.1.0-us-east-1a
```
2. Select your public route table and go to "Subnet Associations" > "Edit", and select the one you want public, 10.0.2.0-us-east-1b. Then click "Save".
```
subnet-43fb937f | 10.0.2.0-us-east-1b
```

### Create Flow Log
It is important to track the traffic in your VPC. Flow logs will log all activity in your VPC and send it to cloud watch.
1. Go to your main dashboard and click on "Cloud Watch" under "Management Tools".
2. In Cloud Watch click on "Logs" and click "Actions" > "Create Log Group", give it a name, and click "Create".
```
Log Group Name = "theMatrix-logs"
```
3. Go back to your VPC dashboard and select your custom VPC.
4. Then click "Actions" > "Create Flow Log".
5. Use te following specifications:
```
Resources = "vpc-7de1c61b | theMatrix-VPC"
Filter = "Accept"
Destination = "Send to CloudWatch Logs"
Destination log group = "theMatrix-logs"
IAM Role = "flowlogsRole"
IAM Role ARN = "arn:aws:iam::117730920402:role/flowlogsRole"
```

### Create Security Group
Next, create a security group inside our VPC that specifically allows internet traffic, HTTP and HTTPS. Remember that security groups are stateful, meaning all inbound traffic automatically allow the corresponding outbound traffic.
1. Go to "Security Groups" and click "Create Security Group".
2. Configure the following and click "Create":
```
Security group name = "theMatrix-sg-webDMZ"
Description = "SSH,HTTP,HTTPS"
VPC = "vpc-7de1c61b | theMatrix-VPC"
```
3. Select the security group, click on the tab "Inbound Rules" and click "Edit Rules" and add the following. Then click "Save".
```
Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "72.21.196.0/24"
Type = "HTTP", Protocol = "TCP", Port Range = "80", Source = "Custom", "0.0.0.0/0, ::/0"
Type = "HTTPS", Protocol = "TCP", Port Range = "443", Source = "Custom", "0.0.0.0/0, ::/0"
```

### Provision EC2 Instance
Now that our VPC is set up we need to provision an EC2 Instance into our public VPC to test the public subnet. See "Setup EC2 Guide" for details. 

When configuring the instance details make sure to put it in the VPC that we just created and into the public subnet. Also you need to make sure Auto-assign Public IP is enabled. Use these specifications:
```
Network = "theMatrix-VPC"
Subnet = "subnet-43fb937f | 10.0.2.0-us-east-1b"
Auto-assign Public IP = "Use subnet setting (Enable)"
```
For testing purposes, in "Advanced Details" use the following bootstrap script, this will install Apache and allow us to see a simple web page when we go to our instance's public IP address.
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1>Hello World</h1></html>" > index.html
```
Then, in the "Configure Security Group" section be sure to assign the security group we created earlier to this instance. 

### Result
To test the VPC public subnet, we should be able to connect to our public subnet instance via the IPv4 Public IP associated with our instance. Paste the IP address to your instance into your browser and you should see your index.html, ei:
```
54.87.210.157
```