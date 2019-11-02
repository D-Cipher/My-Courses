## Configure VPC Private Subnet
This is a guide on configuring your VPCs' private subnets allowing your private subnets to communicate out to the internet via a network address translation (NAT) and allow you to adminster your private subnet through a bastion host.

### Objective
Once set up, we should have a good understanding of the process of configuring your VPC's private subnet. From your public instance, we should be able to SSH into your private instance with your private ip address.
```
ssh 10.0.1.57
```
If VPC has been configured correctly, we should be inside our private subnet. We can also have access the internet via our NAT gateway. To test this, perform a yum update and it should update all security patches. Also use "yum install mysql", and we should be able to download mySQL.
```
sudo su
yum update -y
yum install mysql -y
```

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details. You must also have knowledge of how to set up VPCs and have gone through the Setup VPC Public Subnet Guide. Further, you must first already have created a VPC with both a public and private subnet created with an EC2 instance in each.

### Setting up two EC2 Instances
If you haven't done so already, create one public EC2 instance (this is your Bastion Host) in your public subnet and one private EC2 instance (this is your Private Host) in your private subnet. We will set up the private instance to only recieve traffic from your public subnet. To do this we will need a new security group for our VPC, in our case theMatrix-VPC.

1. Set up the bastion host. To do this simply create an EC2 instance in your public subnet. For the security group make sure it only allows SSH traffic from your IP address. You should be very familiar with how to do this before attempting this guide. See Setup EC2 Guide for more details. Note the public ip address in our case it is: 54.87.210.157
2. Next create an EC2 instance in your private subnet. When configuring this private instance make sure you selected your VPC's private subnet, in our case:
```
Network = "theMatrix-VPC"
Subnet = "subnet-1b464b36 | 10.0.1.0-us-east-1a"
Auto-assign Public IP = "Use subnet setting (Disable)"
```
3. For the security group configurations use allow SSH, MYSQL/Aurora, and All ICMP - IPv4. Set the source for each to ONLY allow traffic from your public subnet's ip, in our case it's 10.0.2.0/24:
```
Type = "SSH", Protocol = "TCP", Port Range = "22", Source = "10.0.2.0/24"
Type = "MYSQL/Aurora", Protocol = "TCP", Port Range = "3306", Source = "10.0.2.0/24"
Type = "All ICMP - IPv4", Protocol = "ICMP", Port Range = "ALL", Source = "10.0.2.0/24"
```
4. For the key pair make sure to create a new key pair. Do not use the same key pair that you used for the EC2 instance in your public subnet. In our case, "MyPuttyKey" is the key pair for our bastion host, so we will create a new key called "Matrix-PrivateHostKey".
```
Key pair name = "Matrix-PrivateHostKey"
```
5. Provision the private instance and make a note of the PRIVATE ip address, in our case:
```
Private IPs = "10.0.1.57"
```
6. Test the connection. To test ssh into the instance you created in your public subnet, in our case the instance's public IP address that we ssh into is 54.173.175.210. Then run the following ping command on the ec2 instance in your private subnet using the ec2 instance's private IP address, 10.0.1.57. Note that since this instance is sitting in a private subnet it doesn't have a public IP address.
```
ping 10.0.1.57
```
If the setup is correct you should see a response from the instance in the private subnet, ei:
```
PING 10.0.3.57 (10.0.1.57) 56(84) bytes of data.
64 bytes from 10.0.1.57: icmp_seq=1 ttl=255 time=1.11 ms
64 bytes from 10.0.1.57: icmp_seq=2 ttl=255 time=0.803 ms
```

### Configure SSH Key Forwarding (Windows PuTTY)
Now that we know that our Bastion Host is talking to our Private Host. We will need to set up a key forwarding in order for our us to SSH into our Private Host from our Bastion Host. For Windows, we will need to configure our PuTTY to allow key forwarding. See PuTTy Guide for the basics of PuTTy.
1. Go to PuTTy and go to the PuTTy profile of your Bastion Host. In our case: 
```
Host Name (or IP address) = "ec2-user@54.87.210.157"
```
2. On the left pannel, expand "SSH" and click on "Auth" and in the "Private key file for authentication" make sure that the key pair to your Bastion Host is selected.
```
Private key file for authentication: "c/users/neo/Documents/Keys/MyPuttyKey.ppk
```
3. Check "Allow agent forwarding" in the "Authentication parameters".
4. Open up the Pageant app. This app should be preinstalled if you have PuTTy simply search for it in your start menu and open it. Then in Pageant click "Add Key" and select the key to your Private Host "c/users/neo/Documents/Keys/Matrix-PrivateHostKey.ppk".
5. Now in PuTTy click open to SSH into your Bastion Host.
6. You should now be able to SSH into your Private Host from your Bastion Host. In your Bastion Host simply use the ssh command on the private IP address of your Private Host.
```
ssh 10.0.1.57
```
If everything is set up correctly, you should now be SSH'd into your Private Host. 

### Configure SSH Key Forwarding (Mac OS)
Now that we know that our Bastion Host is talking to our Private Host. We will need to set up a key forwarding in order for our us to SSH into our Private Host from our Bastion Host. For Mac, we will need to configure SSH agent forwarding.
1. Create an ssh agent in your local directory and add the key pair for your Private Host. 
```
ssh-add -K Matrix-PrivateHostKey.pem
ssh-add -l
```
2. SSH into your Bastion Host.
```
ssh ec2-user@54.87.210.157 -i MyPuttyKey.pem
```
3. Check to see if ssh agent forwarded the key pair for your Private Host. You should be able to see the key with the following command.
```
ssh-add -l
```
4. Now SSH into your Private Host using it's private ip address.
```
ssh -A 10.0.1.57
```
If everything is set up correctly, you should now be SSH'd into your Private Host. 

### Create NAT Gateway
Although we can connect into our private subnet, our private subnet has no internet connection. We can prove this by running the command "sudo yum update" and the command should FAIL. In order for our private subnet to securely access the internet for software updates and patches, we will need a Network Address Translation (NAT). This can be achieved in one of two ways: 1) Configure an instance to perform NAT called a NAT instance, or 2) deploy a NAT gateway. NAT instances are very involved and require manager scripts and updating to prevent bottlenecks. NAT gateways will be managed by Amazon so once setup Amazon will handle all of the updates and sizing. For this reason, NAT gateways are prefered and will be the method we use in this guide.
1. We will first need a new elastic ip address for a NAT gateway. In the VPC dashboard click on "Elastic IPs"
2. Leave settings as default.
```
Scope = "VPC"
IPv4 address pool = "Amazon pool"
```
3. Click "Allocate" and note the Elastic IP Allocation ID of your new elastic IP.
4. Click on "NAT Gateways" and click create NAT Gateway, deploy it into your PUBLIC subnet. Then select your elastic IP.
```
Subnet = "subnet-43fb937f | 10.0.2.0-us-east-1b"
Elastic IP Allocation ID = "eipalloc-2ce4761d"
```
4. Then click "Create a NAT Gateway".

### Edit Route Table
Now we want to add a route in our private subnet to the NAT gateway.

1. Go to "Route Tables" then select your private subnet, ei: "theMatrix-route-main".
2. Click on the "Routes" tab, then click "Edit".
3. Click "Edit routes" and put "0.0.0.0/0" as the destination and add the NAT gateway as the target. Then click "Save".
```
Destination = "0.0.0.0/0", Target = "nat-04d4fb40a0ba620a8"
```

### Setup the Network ACL (Recommended)
For an additional layer of security, it's highly recommended to set up a Network ACL for your private subnet. See the Setup Network ACL Guide for more details. 

### Result
In order to test our NAT gateway, we will simply SSH into our Private Host through our Bastion Host and run the updates and install mysql. From your public instance, SSH into your private instance with your private ip address.
```
ssh 10.0.1.57
```
If VPC has been configured correctly, we should be inside our private subnet. We can also have access the internet via our NAT gateway. To test this, perform a yum update and it should update all security patches. Also use "yum install mysql", and we should be able to download mySQL.
```
sudo su
yum update -y
yum install mysql -y
```