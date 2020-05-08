## Setup EC2 Guide
This is a guide on launching an instance of Amazon Web Services' EC2 Virtual Server.

### Objective
Once set up, we should be able to SSH into our EC2 via the command line (Linux, MAC). For windows, PuTTY (see PuTTY guide).

In the command line:
```
ssh ec2-user@54.209.96.172 -i MyEC2Key.pem
```

### Selecting AMI
1. In the AWS console select EC2.
2. Choose a virtual machine, ei: "Amazon Linux AMI 2016.09.1 (HVM)".
3. Choose a virtual disk, ei: "General purpose t2.micro".


### Configure instance details
* Network - By default our EC2 instance will be set up in the default virtual private cloud (VPC). However, it is highly recommended that you provision your own virtual private cloud (VPC) and provision your resources the the virtual data center. To learn how to create your own VPC see the "Setup VPC Guide". For this example, we can just use the default VPC.
* IAM role - Select an IAM role. If you do not have a role create a new IAM role. This will allow you to CLI using roles instead using credentials. This way no credentials are stored on the instance. For more details see "Setup IAM Guide". For example, we created an "S3-Admin-Access" role that allows EC2 instances to access S3. We attach that role here:
```
IAM role = "S3-Admin-Access"
```
*Advanced Details - in user data, add bash script, ei: yum update, install/run apache, copy an index.html file from your s3 bucket. See Setup S3 Guide for details.
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
aws s3 cp s3://dcy-bashscripts/index.html /var/www/html
```

### Add Storage and Tags
1. Add storage. The root volume type cannot be HDD. General Purpose SDD (GP2) is standard and will be fine. Also, note that root volume cannot be encrypted.
2. Add a tags. Typical tags include:
```
Key = "Name", Value = "Easy-Machine" 
Key = "Type", Value = "t2-micro_1gig"
Key = "Department", Value = "Network Scaling Integration"
Key = "Team", Value = "Data Analytics"
Key = "StaffID", Value = "23554" 
```

### Security Config
Very importantly, we need to setup security group.
1. Select create new security group.
2. Give the security group a name, ei: "WebDMZ".
3. Add inbound rules, standard are SSH, HTTP, HTTPS.
```
Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "Custom", "72.21.196.0/24"
Type = "HTTP", Protocol = "TCP", Port Range = "80", Source = "Custom", "0.0.0.0/0, ::/0"
Type = "HTTPS", Protocol = "TCP", Port Range = "443", Source = "Custom", "0.0.0.0/0, ::/0"
```

### Key Pair
We now need to set up a EC2 key on our computer. 

1. Hit Launch and a pop up will prompt you for a key pair. If you have a key you can select "Choose an existing key pair".
2. If you do not have a key pair choose "Create new key pair" and download key pair. 
3. Save key and note the location, ei: "MyEC2Key.pem".

For windows users you will need to convert key pair to PuTTY key. See PuTTY guide for instructions on this.

For Mac users in the terminal you will need to change the permissions on the key pair.
```
chmod 400 MyEC2Key.perm
```


### Result
Congrats your first EC2 is Launched. Now you should be able to SSH into EC2 (for Linux and Mac), in the command line type in "ssh ec2-user@" and the public ip address of your EC2 instance, ei:
```
ssh ec2-user@54.209.96.172 -i MyEC2Key.pem
```

~