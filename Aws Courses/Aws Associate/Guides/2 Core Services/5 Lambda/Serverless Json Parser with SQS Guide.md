## Serverless Json Parser with SQS Guide
This is a guide on building a serverless JSON parser with a resilient architecture by using SQS queue along with AWS Lambda and DynamoDB. In the current architecture, our lambda function that parses the JSON data and writes it to the DynamoDB table is directly triggered by S3. While this works, it maybe an issue when trying to scale. Imagine if our S3 bucket is connected to an App that is used by millions of users. At any given time there maybe millions of objects that are dropped into the bucket which triggers lambda to write to DynamoDB. This setup could cause our DynamoDB table to be flooded with too many writes at one time. SQS allows us to queue up those requests, letting us process them in batches, spreading the job over time. The architecture of our app will be:
1. User drops a JSON file into an S3 bucket.
2. This triggers a "listener" Lambda function which will grab the path/name and bucket of the file.
3. Our "listener" Lambda will then send that information to SQS as a message.
4. Our "parser" Lambda function will be polling SQS for messages and when it finds this message it will perform the job.
5. "Parser" Lambda will go to the specified bucket and path/name to grab the file, parse it, and write it into our DynamoDB table.

### Objective
Once set up, we should have a good understanding of how to use SQS to build a more resilient JSON parser that protects our backend systems. We should be able to drop a JSON file into our S3 bucket, see the message being set to SQS, and see the data in DynamoDB.

### Prerequisites
In order do this guide you must have already completed the "Serverless Json Parser Guide". As part of that guide you should already have a "parser" lambda function named "json-parser-lambda". Further, you should have a bucket set up named "json-parser-bucket", a table in DynamoDB named "parser_table", and a sample json file named "parser_data.json", the contents being:
```
{"user_id":"j34kxen4dfh","First Name":"Mike","Last Name":"Lambda","Location":["USA"]}
```
Finally, you should have a IAM role called "json-parser-role". In order to do this guide, you will need to add another permission to this role: "SQS Full Access". This will allow your lambda functions to access SQS. See Setup IAM Guide for more details on creating roles.

### Create the SQS Queue
First we will need to create our SQS queue.
1. Go to SQS in the AWS console and click "Create New Queue".
2. Give the queue a name and select "Standard Queue"
```
Queue Name = "json_parser_queue"
Type = "Standard Queue"
```
3. Once created, select your queue and take note of the URL. We will use it in our code.
```
URL = "https://sqs.us-east-1.amazonaws.com/1234567890/json_parser_queue"
```

### Create Listener Lambda Function
First we will create a "listener" lambda function.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch", give the function a name, select Python 3.7 for the runtime.
```
Name = "json-listener-lambda"
Runtime = "Python 3.7"
```
3. Select "Use an existing role" and select your role and click "Create function".
```
Existing role = "json-parser-role"
```

### Add Trigger and Write the Execution Code
Now we need to create an S3 trigger to call our "listener" lambda function. Essentially when users drop a JSON file into the bucket, S3 will trigger the function we created. Our function will grab the path/name and bucket name of the file and send it as a message to our SQS queue.
1. In your lambda function "Designer" click "Add trigger" and select "S3".
2. Under S3, configure the bucket to be your "json-parser-bucket", event type is "All object create events", and add .json to the suffix. Basically, where there is a .json file uploaded to the bucket this trigger will be activated.
```
Bucket = "json-parser-bucket"
Event type = "All object create events"
Suffix = ".json"
```
3. Then click Add to add the trigger to your Lambda function.

Now we will write the code. scroll down to the Environment Editor, paste in the following code in the editor, and click "Save". In this code, you will need to replace the "queue_url" with your specific url you noted earlier.
```
import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
	sqs = boto3.client('sqs')

	#Get bucket name and file name from event of S3
	bucket = event['Records'][0]['s3']['bucket']['name']
	file_name = event['Records'][0]['s3']['object']['key']
	message = json.dumps({'bucket': bucket, 'file_name': file_name})

	# Send the SQS message
	queue_url = 'https://sqs.us-east-1.amazonaws.com/1234567890/json_parser_queue'

	try:
		response = sqs.send_message(QueueUrl=queue_url,MessageBody=message)
		return {'statusCode': 200,'body': json.dumps(response)}

	except ClientError as error:
		return {'statusCode': 400,'body': error}
```

### Testing the Listener
To test our "listener" Lambda function, go to your "json-parser-bucket" S3 bucket and delete all contents. Then drop your "parser_data.json" into the bucket. Next go to your SQS queue, "json_parser_queue", and you should see a "1" under "Messages Available". To verify this message:
1. Select your "json_parser_queue"
2. Click "Queue Actions" > "View/Delete Messages" then in the popup click "Start Polling for Messages".
3. You should see your message which reads:
```
{"bucket": "json-parser-bucket", "file_name": "parser_data.json"}
```

### Modify Parser Lambda Lambda Function
Now we need to modify our "parser" Lambda function. You should have created this function as part of the prerequisites of this guide, in our case our parser function is named "json-parser-lambda".

Remove the original S3 trigger and in its place add SQS as the trigger. In the "Designer" click "Add trigger" and select "SQS". Then select your queue ARN and leave the rest as default. Then click "Add".
```
SQS queue = "arn:aws:sqs:us-east-1:1234567890:json_parser_queue"
Batch size = "10"
Enable trigger = "True"
```

Now we will modify our code. in the Environment Editor, replace the existing code with the following and click "Save".
```
import json
import boto3

def lambda_handler(event, context):
	s3 = boto3.client('s3')
	dynamodb = boto3.resource('dynamodb')

	#Parse SQS message to get bucket and file name
	message = json.loads(event['Records'][0]['body'])
	bucket = message['bucket']
	file_name = message['file_name']

	#Get the object, read object, convert to json
	s3_object = s3.get_object(Bucket=bucket,Key=file_name)
	reader = s3_object['Body'].read()
	json_data = json.loads(reader)

	#Put json data into dynamodb table
	table = dynamodb.Table('parser_table_sqs')

	try:
		result = table.put_item(Item=json_data)
	except:
		print('DynamoDB insert was not successful.')
	#print(json.dumps(result))
	return {'statusCode': 200,'body': json.dumps(result)}
```

This code is very similar to the previous code, except instead of grabbing the file and bucket details from the S3 trigger it gets this information from the message in the SQS queue. Then it follows the information from the message and goes to the S3 bucket to grab the file, parses it, and writes it to DynamoDB.

### Result
Now you should be able to drop a JSON file into your S3 bucket, that will trigger the "listener" to send a message to the SQS queue. From there your "parser" will follow the instructions on the message to parse the data and write it to DynamoDB.

Before testing this, make sure to go to your DynamoDB table and delete all data, then go to your bucket and remove the files there, and go to your SQS queue and make sure that there are no messages in the queue.

To test, go to your S3 bucket and drop your JSON file. Then go to your DynamoDB table and view your items. If configured correctly, we should be able to see your table populated with the JSON data.
