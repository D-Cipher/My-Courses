## Setup CloudWatch Billing Alarm
This is a guide on setting a Billing Alarm using CloudWatch. Billing alarms alerts you when you go over the amounts that you set. CloudWatch is an AWS service that monitors your AWS account and any services on their performance. 

### Objective
Once set up, we should have a good understanding of the process of setting up a billing alarms to keep track of your charges within the AWS cloud. We should be able recieve a notification message once we reach a certain threshhold in terms of charges.

### Creating the Alarm
Creating billing alarms is under CloudWatch.
1. In the AWS console navigate to Cloudwatch > Billing. Then click "Create Alarm".
2. In "Specify metric and conditions" configure the following: 
```
Namespace = "AWS/Billing"
Metric name = "EstimatedCharges"
Currency = "USD"
Statistic = "Maximum"
Period = "6 hours"
Threshold Type = "Static"
Alarm Condition = "Greater/Equal"
```
3. Set your amount you want the threshold to be in USD and click Next.
```
Threshold Value (USD) = 10
```
4. Select "in Alarm" for alarm state.
5. For SNS topic, select "Create new topic" then configure the following, then click "Create Topic", and click Next:
```
Create a new topic = "Billing_Notifiers"
Email endpoint = "[YOUR EMAIL HERE]"
```
6. Give you alarm a name, add description, and click create.
```
Alarm name = "Billing_10"
Alarm description = "[YOUR ACCOUNT NAME] account has exceeded 10 USD"
```

### Configure SNS
To add additional subscriber or other devices to this alarm, go to SNS to manage the "Billing_Notifiers" topic.
1. In the AWS console navigate to SNS > Topics.
2. Click on your topic, in our case it's "Billing_Notifiers".
3. Click "Create Subscription" and add the following to add an SMS notification, then click Create.
```
Protocol = "SMS"
Endpoint = "[YOUR PHONE NUMBER HERE]"
```

### Result
Now you should have your billing alarm set up. To test the SNS simply click on "Billing_Notifiers" and click on "Public Message". For the subject type "Test Message" and in the body type "test". If everything is configured correctly you should recieve the notification.