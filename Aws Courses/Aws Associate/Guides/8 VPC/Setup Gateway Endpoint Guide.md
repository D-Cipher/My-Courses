## Setup a Gateway Endpoint Guide
This is a guide on setting up a Gateway Endpoint for your VPCs as a way of communicating between instances in your private VPC subnet with other AWS services without availability risks or bandwidth constraints on your network traffic.

### Objective
Once set up, we should have a good understanding of the process of configuring a Gateway Endpoint to connect your private subnet with S3. We should be able to test this endpoint by running the following command:
```
aws s3 ls --region us-east-1
```

### Prerequisites
In order do this guide you must have knowledge of how to set up a custom VPC with a private subnet. See Setup VPC Private Subnet Guide for more details. Further, you must first alreay created a VPC with both a public and private subnet created with an EC2 instance in each.

### Create an S3 Role
We will set up our Gateway Endpoint to allow access to S3. 
1. In order to do this we need to make sure we have a role in our IAM that allows EC2 instances full access to S3. See Setup IAM Guide on how to create roles.
2. Attach the created role to the EC2 instance in your private subnet. Select your EC2 instance, click on Actions > Instance Settings > Attach/Replace IAM Role. Then slect the role you created.

### Create Endpoint
Now we will create an endpoint.
1. In the VPC dashboard click on Endpoint and then Create Endpoint.
2. Find the amazon S3 gateway.
```
Servie Name = "com.amazonaws.us-east-1.s3"
```
3. Select your VPC.
4. Select the route table that your private instance is sitting in.
5. Leave the Policy as "Full Access"
6. Click Create Endpoint.
This will create your endpoint.

### Remove NAT Gateway For Testing
In order to test your endpoint, be sure to remove the NAT Gateways attached to your private subnet. Since the NAT Gateway allows the private subnet to access the internet, it also allows it to access aws resources given role premissions. However, if we detach it then the only way our VPC will be able to access those resources is through our newly created endpoint.
1. Go to Route Tables and select the private subnet.
2. Then click Actions > Edit Routes
3. Then click "x" next to the NAT Gateway in order to detatch, then click Save.

### Results
Now that we have our Gateway Endpoint set up we should be able to access S3 from our instance in our private subnet. To test this, simply use the following command to see all your buckets (with this setup you need to add a region flag to the command specifying the region you are in):
```
aws s3 ls --region us-east-1
```