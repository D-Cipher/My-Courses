## Serverless Rest API Guide
This is a guide on setting a Serverless Rest API using API Gateway, Lambda, and DynamoDB. The API we will build takes post requests from a client in the form of JSON and stores the data into DynamoDB and when a client makes get requests it will send the client data from DynamoDB.

The scenario is we have several motion sensors around the house for monitoring activity. When a motion sensor detects activity it will hit our API endpoint and the data will be recorded. We can then use the API endpoint to pull down the data to get the latest activity.

The architecture of our web app will be:
1. Get or Post request hits API Gateway.
2. This will trigger a Lambda function to write the data to DynamoDB if it is a Post.
3. If it is a Get request then a second Lambda function will pull data from DynamoDB and deliver it to the user via API Gateway.

### Objective
Once set up, we should have a good understanding of the process of setting up a Rest API with API Gateway, Lambda and DynamoDB. We should be able to make a Post request to our API endpoint and the data will be recorded. We should also be able make a Get request and see the latest data in DynamoDB.

### Prerequisites
In order do this guide you must have alittle bit of experience with Lambda, DynamoDB, Python. It is recommended that you do the "Serverless Website Guide" first.

You will need to create a role that allows Lambda full access to API Gateway, DynamoDB, and CloudWatch for logs. See Setup IAM Guide for more details on creating roles. The lambda role we created is called as follows:
```
 IAM role = "sensor-role"
 ```

Next you will also need to create a DynamoDB table. To create a DynamoDB table:
1. Go to DynamoDB in the console and click "Create Table".
2. Set your table name, primary key, and sort key. Leave rest as default.
```
Table name = "sensor_table"
Primary key = "timestamp"
Sort key = "device_id"
```

You will not need an actual motion sensor device for this project, we will simulate sending the API call by using Reqbin (https://reqbin.com/). However, you will need a sample data from a device, here it is:
```
{"sensor_state": "Triggered", "device_name": "BackDoor", "device_id": "w34j9p5gp4kqf"}
```

### Create Two Lambda Functions
First we will create a lambda function.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch", give the function a name, select Python 3.7 for the runtime.
```
Name = "sensor-post-lambda"
Runtime = "Python 3.7"
```
3. Select "Use an existing role" and select your role and click "Create function".
```
Existing role = "sensor-role"
```
4. Create another function called "sensor-get-lambda", repeat steps 1 through 3.
```
Name = "sensor-get-lambda"
```

### Write Post Execution Code
Now we can write our post execution code. Go to your "sensor-post-lambda" and scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
import boto3
from datetime import datetime
dynamodb = boto3.resource('dynamodb', 'us-east-1')

def lambda_handler(event, context):

	table = dynamodb.Table('sensor_table')

	try:
		table.put_item(Item={
			'timestamp' : (datetime.now()).strftime('%Y-%m-%d %H:%M:%S'),
			'device_id' : event['device_id'],
			'device_name' : event['device_name'],
			'sensor_state' : event['sensor_state']})
		return {'statusCode': 200,'body': json.dumps('Event recorded.')}
	except:
		print('DynamoDB insert was unsuccessful.')
		return {'statusCode': 400,'body': json.dumps('Error when trying to record event.')}
```

Our code uses boto3 to interact with AWS resources. We use the dynamodb resource to put the data from our event into our table. Remember to click save to save the code.

### Event Testing
Once you have written the code you will want to use a test event to test it.
1. Click on "Configure test event".
2. Select "Create new test event", use the event template as "Hello World" and give it a name.
```
Event template = "Hello World"
Event name = "sensortest"
```
3. In the code, paste in your test json data set and then click "Create".
```
{"sensor_state": "Triggered", "device_name": "BackDoor", "device_id": "w34j9p5gp4kqf"}
```
4. Once created click "Test" and if successful you should see in the execution results the following:
```
Response: {"statusCode": 200,"body": "\"Event recorded.\""}
```

### Write Get Execution Code
Next we can write our get execution code. Go to your "sensor-get-lambda" and scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
import boto3
dynamodb = boto3.resource('dynamodb', 'us-east-1')

def lambda_handler(event, context):

	table = dynamodb.Table('sensor_table')
	response = table.scan()

	return {'statusCode': 200,'body': json.dumps(response['Items'])}
```
Our code uses the dynamodb table scan functionality to pull the data from our table and deliver it as json using json dumps. Remember to click save to save the code.

Next we can test it. We don't need any test events, but lambda requires you to configure a test event to test. Follow the steps in the previous Event Testing section and create another test event. It does not matter the test json data you use. Once created, click "Test" and if you set up the code correctly you should see a 200 response and the data in your DynamoDB table.
```
Response: {"statusCode": 200,"body": "[{\"device_id\": \"w34j9p5gp4kqf\"...}]"
```

### Create API Endpoint
Now we will create the endpoint in API Gateway. We will configure a REST API that handles get and post requests.
1. In the console, go to API Gateway and click "Create API".
2. Click "New API", choose REST for the protocol, configure the following, and click "Create":
```
API name = "sensor-api"
Description = "API for motion sensors"
Endpoint Type = "Regional"
```

Create Post Method
1. Go to your "sensor-api" and click "Resources" > "/"
2. Then click "Actions" > "/" and in the dropdown under "/" select "POST" and click the check mark.
3. Now configure the post with the following and click "Save":
```
Integration Type = "Lambda Function"
Use Lambda Proxy Integration = "False"
Lambda Region = "us-east-1"
Lambda Function = "sensor-post-lambda"
Use Default Timeout = "True"
```
4. Once saved we can test the post method. In your Post click the "Test" button. and in the "Request Body" paste in your sample data.
```
{"sensor_state": "Triggered", "device_name": "BackDoor", "device_id": "w34j9p5gp4kqf"}
```
5. Click "Test" and if successful you should see in the request results the following:
```
Response: {"statusCode": 200,"body": "\"Event recorded.\""}
```

Create Get Method
1. Repeate the previous steps 1 through 4, but for the Get Method.
2. When testing, if successful you should see in the request results the following:
```
Response: {"statusCode": 200,"body": "[{\"device_id\": \"w34j9p5gp4kqf\"...}]"
```

### Deploy the Endpoint
Once tested, we can deploy our API endpoint.
1. Go to your "sensor-api" and click "Resource" > "/"
2. Click "Actions" > "Deploy API", configure as follows, and click Deploy.
```
Deployment stage = "[New Stage]"
Stage name = "default"
Stage description = "default"
Deployment description = "default"
```
3. Then click "Stages" > "default" to find your "Invoke URL".
```
Invoke URL = "https://c6f36kkwr6.execute-api.us-east-1.amazonaws.com/default"
```

### Result
Now you should be able to make a Post request to our API endpoint and the data will be recorded. We should also be able make a Get request and see the latest data in DynamoDB.

We can use Reqbin to make the requests.
1. Go to https://reqbin.com, select POST, and paste in our endpoint URL.
```
https://c6f36kkwr6.execute-api.us-east-1.amazonaws.com/default
```
2. In "Content", select JSON, and paste in your sample data.
```
{"sensor_state": "Triggered", "device_name": "BackDoor", "device_id": "w34j9p5gp4kqf"}
```
3. Click send. If configured correctly, we should be able to see your DynamoDB table populated with the JSON data. Also, the output content you should see your response code.
```
Response: {"statusCode": 200,"body": "\"Event recorded.\""}
```
4. Do steps 1 to 3, but change the request to GET. If it has configured correctly, in the output content you should see your data in the response code.
```
Response: {"statusCode": 200,"body": "[{\"device_id\": \"w34j9p5gp4kqf\"...}]"
```
