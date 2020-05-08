## Setup CloudWatch EC2 Monitoring
This is a guide on setting up CloudWatch monitoring for EC2 instances. CloudWatch alerts you when you go over the CPU utilization that you set. CloudWatch is an AWS service that monitors your AWS account and any services on their performance. 

### Objective
Once set up, we should have a good understanding of the process of setting up a billing alarms to keep track of your charges within the AWS cloud. We should be able recieve a notification message once we reach a certain threshhold in terms of charges.

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details.


### Enabling Monitoring
When creating an EC2 instance make sure to click on "Enable CloudWatch detailed monitoring" in your configuration instance details. Also, make sure to add a tag to your instance to note that it has monitoring turned on because it is more of a charge. Once enabled launch your EC2 instance.

### Set Monitoring Alarms
Creating billing alarms is under CloudWatch.
1. In the AWS console navigate to Cloudwatch > Select Metric. Then find the EC2 instance id for the instance you just created.
2. Scroll down to find the specific metric for your EC2 instance on "CPUUtilization" and click select.
3. In configuring the alarm so that when ever the CPUUtilization is greater than 90% send alarm.
4. For SNS topic, select "Create new topic" then configure the following, then click "Create Topic", and click Next:
```
Create a new topic = "CPUUtilization_Notifiers"
Email endpoint = "[YOUR EMAIL HERE]"
```
6. Give you alarm a name, add description, and click create.
```
Alarm name = "CPUUtilization_90"
Alarm description = "[YOUR ACCOUNT NAME] account's EC2 Instance has exceeded 90% utilization"
```

### Configure SNS
To add additional subscriber or other devices to this alarm, go to SNS to manage the "CPUUtilization_Notifiers" topic.
1. In the AWS console navigate to SNS > Topics.
2. Click on your topic, in our case it's "Billing_Notifiers".
3. Click "Create Subscription" and add the following to add an SMS notification, then click Create.
```
Protocol = "SMS"
Endpoint = "[YOUR PHONE NUMBER HERE]"
```

### Result
Now you should have your CPUUtilization alarm set up. To test the SNS simply click on "CPUUtilization_Notifiers" and click on "Public Message". For the subject type "Test Message" and in the body type "test". If everything is configured correctly you should recieve the notification.