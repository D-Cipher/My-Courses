## Serverless Json Parser Guide
This is a guide on setting a serverless JSON parser using AWS Lambda and DynamoDB. AWS Lambda allows you to upload your code and create a lambda function. AWS takes care of provisioning managing the servers that you need to run the code. You don't need to worry about OS, patching, scaling, etc. The architecture of our app will be:
1. User drops a JSON file into an S3 bucket.
2. This triggers a Lambda function which parses the file.
3. Then the lambda function stores the data into DynamoDB.

### Objective
Once set up, we should have a good understanding of how to set up a JSON parser with Lambda and DynamoDB. We should be able to drop a JSON file into our S3 bucket and see the data in DynamoDB. We should be able to see and interact with our data in a DynamoDB table.

### Prerequisites
In order do this guide you must have a little bit of experience with Lambda, DynamoDB, Python, and how to create S3 buckets. You will need to create a role that allows Lambda full access to S3, DynamoDB, and CloudWatch for logs. See Setup IAM Guide for more details on creating roles. The lambda role we created is called as follows:
```
 IAM role = "json-parser-role"
 ```
Next, you will also need to create an S3 bucket and a DynamoDB table. To create a S3 bucket go to S3 and click create bucket and give the bucket a name.
```
Bucket name = "json-parser-bucket"
```
To create a DynamoDB table:
1. Go to DynamoDB in the console and click "Create Table".
2. Set your table name and primary key. Leave rest as default.
```
Table name = "parser_table"
Primary key = "user_id"
```

In addtion you will also need a JSON file. Make sure your JSON file has the "user_id" as a key. We will use the follow JSON saved as "parser_data.json".
```
{"user_id":"j34kxen4dfh","First Name":"Mike","Last Name":"Lambda","Location":["USA"]}
```

### Create Lambda Function
First we will create a lambda function.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch", give the function a name, select Python 3.7 for the runtime.
```
Name = "json-parser-lambda"
Runtime = "Python 3.7"
```
3. Select "Use an existing role" and select your role and click "Create function".
```
Existing role = "json-parser-role"
```

### Add Trigger
Now we need to create a trigger to call our lambda function. We will use S3 as the trigger. Essentially when users drop a JSON file into the bucket, S3 will trigger the function we created.
1. In your lambda function "Designer" click "Add trigger" and select "S3".
2. Under S3, configure the bucket to be your "json-parser-bucket", event type is "All object create events", and add .json to the suffix. Basically, where there is a .json file uploaded to the bucket this trigger will be activated.
```
Bucket = "json-parser-bucket"
Event type = "All object create events"
Suffix = ".json"
```
3. Then click Add to add the trigger to your Lambda function.

### Testing the Trigger
Next we can test this trigger to see if the trigger is working and to see what the output of the event looks like.

1. Scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
def lambda_handler(event, context):
	print(str(event))
	return {'statusCode': 200,'body': json.dumps('Hello from Lambda!')}
```
2. Go to your "json-parser-bucket" and upload your "parser_data.json" into the bucket. If your trigger worked then you should see the event logged in CloudWatch.
3. Go to CloudWatch > Logs > /aws/lambda/json-parser-lambda to see the logs.
4. Open up the latest entry and you should see a message in the form of json data that looks like the following:
```
{'Records': [{'event... 'bucket': {'name': 'json-parser-bucket', 'ownerIdentity': {'principalId'... 'object': {'key': 'parser_data.json'...
```
This is what the lambda handler event looks like. Now we can uses boto3 and python's dictionary in our code to extract out the key information that we need.

### Write the Execution Code
Now we can write our execution code. Scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
import boto3
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb', 'us-east-1')

def lambda_handler(event, context):

	#Get bucket name and file name from event
	bucket = event['Records'][0]['s3']['bucket']['name']
	file_name = event['Records'][0]['s3']['object']['key']

	#Get the object, read object, convert to json
	s3_object = s3.get_object(Bucket=bucket,Key=file_name)
	reader = s3_object['Body'].read()
	json_data = json.loads(reader)

	#Put json data into dynamodb table
	table = dynamodb.Table('parser_table')

	try:
		table.put_item(Item=json_data)
		return {'statusCode': 200,'body': json.dumps('Data inserted.')}
	except:
		print('DynamoDB insert was unsuccessful')
		return {'statusCode': 400,'body': json.dumps('Error when trying to insert data.')}
```
Our code uses boto3 to interact with AWS resources. We use the s3 client to get the object that was dropped into our bucket, read it, and convert it into json using the json package. Then we use the dynamodb resource to put the data into our table. Once the code is saved the function is ready to go.

### Result
Now you should be able to drop a JSON file into your S3 bucket and the data will be written to DynamoDB. Simply go to your S3 bucket and drop your JSON file. Then go to your DynamoDB table and view your items.

If configured correctly, we should be able to see your table populated with the JSON data.
