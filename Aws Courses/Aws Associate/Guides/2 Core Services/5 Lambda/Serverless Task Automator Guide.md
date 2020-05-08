## Serverless Task Automator Guide
This is a guide on building a serverless task automator that uses AWS Lambda and CloudWatch to schedule daily automated tasks. AWS Lambda allows you to upload your code and create a lambda function. AWS takes care of provisioning managing the servers that you need to run the code. While CloudWatch lets you create events that trigger on a schedule. By making CloudWatch trigger Lambda we can simulate a Cron job.

For this guide we will create an automated task that scan a DynamoDB table every day, then converts the results into a Json file, and drop it into an S3 bucket. This application can be very useful for pulling data out of DynamoDB for your reporting databases or other systems to consume. We always want to prevent people from querying the live application databases for metrics and reporting purposes since our application database is optimized for our live application to use and not for backend users to run reports on. A better way is to have an automator incrementally read the data on a regular schedule and dump it into an S3 bucket for our reporting databases or analysis tools to consume.

The architecture of our app will be:
1. CloudWatch triggers the Lambda on a daily schedule.
2. Lambda access DynamoDB and pulls the data, converts it to JSON.
3. Lambda then gives the file a timestamp and drops it into S3.

### Objective
Once set up, we should have a good understanding of how to use CloudWatch with Lambda to create a task automator. We should be able to have a daily scheduled job that pulls data from DynamoDB and drops it into an S3 bucket.

### Prerequisites
In order do this guide you must have a little bit of experience with CloudWatch, Lambda, and Python. It is recommended that you have completed the "DynamoDB Table Creator with Lambda Guide" first. You will also need to create a role that allows Lambda full access to S3, DynamoDB, and CloudWatch. See Setup IAM Guide for more details on creating roles. The lambda role we created is called as follows:
```
IAM role = "task-automator-role"
```
You will also need an S3 bucket. We created one named:
```
Bucket name = "simple-metrics-bucket"
```
In addition, you will need to have create a DynamoDB table with data in it. We will create a table that simulates a table of user logs for a "Hello World" web application. The table is configured as follows:
```
Table name = "webapp_user_logs"
Sample Data = "{'transaction_id':'2afsd33jfoi85495jf','access_timestamp':123298347584,'user_id':'djfi43j09fpk3jf39k'}"
```
Note that if you have already completed the "DynamoDB Table Creator with Lambda Guide", you should have a this table and its data already set up.

### Create Lambda Function
First we will create a lambda function.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch", give the function a name, select Python 3.7 for the runtime.
```
Name = "task-automator-lambda"
Runtime = "Python 3.7"
```
3. Select "Use an existing role" and select your role and click "Create function".
```
Existing role = "task-automator-role"
```

### Create CloudWatch Event Rules
Now we will create a CloudWatch Event.
1. Go to CloudWatch in the AWS console, click "Events" > "Rules".
2. In "Event Source", select "Schedule", and in "Cron Expression" create an expression. This expression represents the time day that the event will trigger. See https://crontab.guru/ to see how Cron expressions work. For example, the following Cron expression represents every day at 5pm UTC.
```
Cron Expression = "0 17 * * ? *"
```
3. Next click "Add Target", select "Lambda Function" for target, and select your function. Then click "Configure Details".
```
Target = "Lambda function"
Function = "taks-automator-lambda"
```
4. Give your CloudWatch event a name, description, and click "Create Rule".
```
Name = "daily-datapull"
Description = "daily-datapull"
State = "Enabled"
```

### Write the Execution Code
Now we can write our execution code. Go to your lambda function Scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    s3 = boto3.resource('s3')

    # Get Time Stamp
    nowdt = datetime.now()
    now = nowdt.strftime('%Y-%m-%d %H:%M:%S') + 'Z'

    # Scan DynamoDB and get the data
    table = dynamodb.Table('webapp_user_logs')
    response = table.scan()
    data = response['Items']

    # Convert to Json and drop into S3 bucket.
    objectpath = 'usermetrics/simple_user_logs' + now + '.json'
    jsonfile = json.dumps({'user_metrics':data}).encode('UTF-8')
    result = s3.Object('simple-metrics-bucket', objectpath).put(Body=(bytes(jsonfile)))
    output = 'Uploaded to s3.' if result else 'S3 upload error.'

    return {'statusCode': 200,'body': json.dumps(output)}
```
This code simply scans your "webapp_user_logs" DynamoDB table for data, then converts the data into Json, timestamps the file, and saves it to the "simple-metrics-bucket".

To test the code, create a test event. In lambda click "Configure test event". Then configure as follows and click "Create". Note that the actual event code we can leave as default. It does not matter what the event code is since our execution code does not use any event inputs. Click "Test" and check your "simple-metrics-bucket". You should see the JSON file with timestamp saved to your bucket.

### Result
Now you should have a daily scheduled job that pulls data from DynamoDB and drops it into an S3 bucket. If configured correctly, at 5pm UTC we should be able to see a newly created JSON file of the data in our DynamoDB table. In the next "Serverless Task Automator Advanced Guide" we will build on top of this project to make our task automator pull from multiple tables. Further, we will configure the code to check to make sure there isn't already a job that ran today and then pull only the new entries from DynamoDB.
