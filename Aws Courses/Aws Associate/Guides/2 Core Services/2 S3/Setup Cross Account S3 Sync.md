## Setup Cross Account S3 Sync Guide
This is a guide on setting up cross account S3 buckets that are synced together on Amazon Web Services and then automating the sync.

### Objective
Once set up, we should have two S3 buckets in two different AWS accounts that are auto-synced allowing you to drop an object in your source account bucket and have it copied over to a destination account bucket.

You will be able to run the s3 ls command from your destination account to see the contents of your source account:
```
aws s3 ls s3://source-bucket-dev
```
Further, you will be able to sync the buckets together by running the following from your destination account:
```
aws s3 sync s3://source-bucket-dev s3://destination-bucket-prod --source-region us-west-2 --region us-west-2
```

### Prerequisites
In order do this guide, you will need two AWS accounts with an S3 bucket in each account. For our first account we will call it the "SOURCE ACCOUNT" and our second account will be the "DESTINATION ACCOUNT". You will also need to know how to create an EC2 instance. See Setup EC2 Instances guide for more details.

1. Create a bucket in the source account.
```
Bucket Name = "source-bucket-dev"
Region = "us-west-2"
```
2. Create a bucket in the destination account.
```
Bucket Name = "destination-bucket-prod"
Region = "us-west-2"
```
3. Launch an EC2 instance in the destination account.
```
Name = "auto-sync-instance"
```

### Add Bucket Policy to Source Bucket
Now set up your source bucket policy to allow access from your destination account.

1. Go to your source account and click on your source bucket: ```source-bucket-dev```
2. Click on the "Permissions" tab and click on Bucket Policy.
3. Paste in the following policy statement, and click "Save".
```
{"Version": "2012-10-17",
    "Statement": [
            {"Sid": "SourceBucketAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<DESTINATION ACCOUNT NUMBER>:root"},
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"],
            "Resource": [
                "arn:aws:s3:::source-bucket-dev/*",
                "arn:aws:s3:::source-bucket-dev"]}]}
```

### Setup Policy and Role in Destination Account
Now we will create a policy and role that will allow our EC2 instance in our destination account to access our source account bucket.

1. Go to your destination account and in IAM create a policy.
2. Paste in the following policy statement.
```
{"Version": "2012-10-17",
    "Statement": [
            {"Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"],
            "Resource": [
                "arn:aws:s3:::source-bucket-dev",
                "arn:aws:s3:::source-bucket-dev/*"]},
            {"Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:PutObject",
                "s3:PutObjectAcl"],
            "Resource": [
                "arn:aws:s3:::destination-bucket-prod",
                "arn:aws:s3:::destination-bucket-prod/*"]}]}
```
3. Now give your policy a name and description, then click "Create Policy".
```
Name = "cross-account-s3-sync-policy"
Description = "Cross account s3 sync between source-bucket-dev and destination-bucket-prod"
```

Next we will create our cross account role and add our policy to the role.

1. In IAM go to Roles and click "Create Role".
2. Select AWS Service and EC2 as the service to use the role.
```
Select type of trusted entity = "AWS Service"
Choose service to use role = "EC2"
```
3. Attach the permission we created in the previous step: ```cross-account-s3-sync-policy```
4. Give the role a name and description.
```
Role name: "cross-account-s3-sync-role"
Role description: "Allows EC2 to perform cross account S3 sync"
```

### Attach Role to EC2 Instance
Once our role has been configured we can attach it to the EC2 instance in our destination account.

1. In EC2, select the instance we created earlier: ```auto-sync-instance```
2. Click "Actions" > "Instance Settings" > "Attach/Replace IAM Role"
3. Select the account we created and click "Apply":
```
IAM role: "cross-account-s3-sync-role"
```

### Perform Manual Sync
Next, we will test to make sure our EC2 account can access the S3 bucket in our source account and perform a manual sync.

1. SSH into the EC2 instance and use s3 ls on the bucket in your source account. You should be able to see the contents of your bucket.
```
aws s3 ls s3://source-bucket-dev
```
2. Perform a manual s3 sync to sync the two buckets together.
```
aws s3 sync s3://source-bucket-dev s3://destination-bucket-prod --source-region us-west-2 --region us-west-2
```

### Configure Automated Sync
Now we can automate this process by setting up a cron job to automate the sync.

1. Create an sh file in your EC2 instance and configure it to chmod 700. To do this, run the following:
```
cd /home/ec2-user
touch auto-sync-file.sh
chmod 700 auto-sync-file.sh
```
2. Configure the sh file we created by adding the following commands to the file. You can use ```vim auto-sync-file.sh``` to write to the file.
```
#!/bin/bash
aws s3 sync s3://vm-bid-upload-prod s3://bid-analysis-report-prod --source-region us-west-2 --region us-west-2
```
3. Create a directory to store logs.
```
mkdir auto-sync-logs
```
4. Now create a cron job with crontab. Use ```crontab -e``` to configure crontab and paste in the following to run the sh file every day at 1:00UTC. You can customize the frequency by editing the cron expression. See https://crontab.guru/ for more details.
```
0 1 * * * /home/ec2-user/auto-sync-file.sh >> /home/ec2-user/auto-sync-logs/cron_log\_`date +20\%y\%m\%d\%H\%M\%S` 2>&1 &
```
5. Optionally, you can add another cron job to continuously remove log files older than 30 days to prevent the log folder from growing too big.
```
0 7 * * * /usr/bin/find /home/ec2-user/auto-sync-logs -type f -mtime +30 -exec rm -f {} \;
```
6. Use ```crontab -l``` to see your newly installed cron jobs.

### Result
Now you should have two S3 buckets in two different AWS accounts that are auto-synced together. This allows you to drop an object in your source account bucket and have it copied over to a destination account bucket. Depending on the frequency of your cron job, you should be able to drop a file into your source bucket and see it in your destination bucket once the cron job refreshes.

Further, you should be able to sync the buckets together by running the following from your destination account:
```
aws s3 sync s3://source-bucket-dev s3://destination-bucket-prod --source-region us-west-2 --region us-west-2
```
~
