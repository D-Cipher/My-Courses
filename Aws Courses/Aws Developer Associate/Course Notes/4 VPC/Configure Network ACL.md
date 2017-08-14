## Configure Network ACL Guide
This is a guide on setting up a Network ACL for your VPCs as a second layer of security. Network ACLs operate at the subnet level where as security groups operate at the instance level. They support allow and deny rules, so you can deny a specific address to access your subnet. Network ACLs are stateless, inbound and outbound must be specified. Also, one subnet can only be associated with one network ACL.

### Objective
Once set up, we should have a good understanding of the process of configuring your own custom Network ACL for you VPCs as another layer of protection. 

### Prerequisites
In order to create a Network ACL, you first need a VPC. You must already have a custom VPC created and it is recommended that you have a public subnet with an instance for testing purposes. See "Setup VPC Guide" for details. 

### Create Network ACL
When you created your custom VPC a default network ACL was created for you. It's recomended you give it a name, ei: "theMatrix-acl-allTraffic". Note: when you create VPC, the network ACL created by default allows all traffic. However, when you create your own custom ACL it will have deny all traffic until you specify the traffic allowed.

1. In your VPC dashboard, click on "Network ACLs". Then click "Create Network ACL".
2. Give it a name and make sure to put it in your custom VPC. Then click "Yes, Create".
```
Name Tag = "theMatrix-acl-webDMZ"
VPC = "vpc-7de1c61b | theMatrix-VPC"
```

### Specify Rules
Network ACL contain a numbered list of rules and they are evaluated in order. That means if rule 99 is block a specific ip address and rule 100 is allow all traffic then the ACL will block the 99 address and allow all other addresses. It is recommended that the allow rules are in increments of 100, allowing for block rules inbetween. 

1. Select your ACL, then click on the "Inbound Rules" tab.
2. Click "Edit" and add the following rules. We will add the standard webDMZ access rules. Also, we need open up ephemeral ports ranging from "1024-65535".
```
Rule = "100", Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "72.21.196.0/24", Allow/Deny = "ALLOW"
Rule = "200", Type = "HTTPS", Protocol = "TCP", Port Range = "443", Source = "72.21.196.0/24", Allow/Deny = "ALLOW"
Rule = "300", Type = "HTTP", Protocol = "TCP", Port Range = "80", Source = "72.21.196.0/24", Allow/Deny = "ALLOW"
Rule = "400", Type = "RDP", Protocol = "TCP", Port Range = "3389", Source = "72.21.196.0/24", Allow/Deny = "ALLOW"
Rule = "500", Type = "Custom TCP Rule", Protocol = "TCP", Port Range = "1024-65535", Source = "72.21.196.0/24", Allow/Deny = "ALLOW"
```
3. Important, now we need to also set the outbound rules. Remember network ACLs are stateless. Click the "Outbound Rules" tab and add the following. 
```
Rule = "100", Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "0.0.0.0/0", Allow/Deny = "ALLOW"
Rule = "200", Type = "HTTPS", Protocol = "TCP", Port Range = "443", Source = "0.0.0.0/0", Allow/Deny = "ALLOW"
Rule = "300", Type = "HTTP", Protocol = "TCP", Port Range = "80", Source = "0.0.0.0/0", Allow/Deny = "ALLOW"
Rule = "400", Type = "RDP", Protocol = "TCP", Port Range = "3389", Source = "0.0.0.0/0", Allow/Deny = "ALLOW"
Rule = "500", Type = "Custom TCP Rule", Protocol = "TCP", Port Range = "1024-65535", Source = "0.0.0.0/0", Allow/Deny = "ALLOW"
```

Important note: In order to establish endpoint connections to S3 or allow instances inside your subnet to access yum updates etc., your network ACL must allow http and https traffic. 

### Associate Subnet
Now associate your ACL with your subnet. Note that only one subnet can be assocated wit one network ACL.

1. Click on the "Subnet Associations" tab then click "Edit"
2. Select your subnet, ei: "subnet-43fb937f | 10.0.2.0-us-east-1e". Then click "Save".

### Result
To test our APC, we need to have an instance inside our subnet. If you don't have one, see "Setup EC2 Guide". When configuring the instance details make sure to put it in the VPC, ei:
```
Network = "theMatrix-VPC"
Subnet = "subnet-43fb937f | 10.0.2.0-us-east-1e"
Auto-assign Public IP = "Use subnet setting (Enable)"
```
For testing purposes, in "Advanced Details" use the following bootstrap script. Then, be sure to select the security group we created earlier, and click launch instance. 
```
#!/bin/bash
yum install httpd -y
yum update -y
service httpd start
chkconfig httpd on
echo "<html><h1>Hello World!</h1></html>" > /var/www/html/index.html
```

If your network ACL has been configured correctly, we should be able to connect to our public subnet instance via the IPv4 Public IP associated with our instance. Paste the IP address into your browser and you should see your index.html, ei:
```
54.87.210.157
```
Now to test, to see if we can block using our network ACL, simply add a rule above HTTP at rule 299 specifying your address and "DENY". Then try connecting again and the connection should fail.
```
Rule = "299", Type = "HTTP", Protocol = "TCP", Port Range = "80", Source = "72.21.196.0/24", Allow/Deny = "DENY"
```