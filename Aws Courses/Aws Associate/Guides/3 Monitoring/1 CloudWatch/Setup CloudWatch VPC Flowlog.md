## Setup CloudWatch VPC Flowlog
This is a guide on setting up CloudWatch monitoring for our VPC. CloudWatch flow logs keeps track of all the network traffic within your VPC. CloudWatch is an AWS service that monitors your AWS account and any services on their performance. 

### Objective
Once set up, we should have a good understanding of the process of setting up a flow log to keep track of your network traffic with your VPCs. We should be able to go into Cloudwatch flow logs to see the logs of traffic.

### Prerequisites
In order do this guide you must have knowledge of how to set up an VPCs. See Setup EC2 Guide for more details.

### Create CloudWatch Log Group
Go to CloudWatch to create a flow log. 
1. In Cloudwatch click on logs and create a log group and give it a name:
```
Log Group Name = "matrix_flowlog"
```

### Create Flow Log
Next we will create our flow log.
1. In the AWS console navigate to VPC > Create flow log. 
2. Set up the configurations as the following:
```
Filter = "All"
Destination = "Send to CloudWatch Logs"
Destination log group = "matrix_flowlog"
```
3. For IAM role, click "Set Up Permissions" and create a new "flowlogsRole".
4. Select your "flowlogsRole, then click Create.

### Result
Now you should have your Flow Logs set up. To see the logs go to Cloudwatch and click on Logs, then click into "matrix_flowlog" to see the logs. 