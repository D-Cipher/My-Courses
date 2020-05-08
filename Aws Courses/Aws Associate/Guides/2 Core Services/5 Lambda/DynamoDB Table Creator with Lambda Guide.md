## Deploying DynamoDB Tables with Lambda Guide
This is a guide on deploying DynamoDB tables using AWS Lambda. AWS Lambda allows you to upload your code and create a lambda function. AWS takes care of provisioning managing the servers that you need to run the code. We can use Lambda to quickly deploy tables and insert test data into our tables.

### Objective
Once set up, we should have a good understanding of how to deploy DynamoDB tables with Lambda. We should be able to have three DynamoDB test tables with three rows of sample data in each.

### Prerequisites
In order do this guide you must have a little bit of experience with Lambda and Python. It is recommended that you have completed the "Serverless Json Parser Guide" first. You will also need to create a role that allows Lambda full access to DynamoDB, and CloudWatch for logs. See Setup IAM Guide for more details on creating roles. The lambda role we created is called as follows:
```
IAM role = "lambda-dynamodb-role"
```

### Create Lambda Function
First we will create a lambda function.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch", give the function a name, select Python 3.7 for the runtime.
```
Name = "sample-table-creator"
Runtime = "Python 3.7"
```
3. Select "Use an existing role" and select your role and click "Create function".
```
Existing role = "lambda-dynamodb-role"
```
4. Important: In your lambda, scroll down to "Basic settings" and change "Timeout" to 45 sec. By default the execution code has a time delay of up to 25 seconds in between creating the table and inserting the data. The reason is the execution code needs to give the table creation a chance to finish before it can insert data into the table. Hence, you will need to increase the timeout of your lambda function to at least more than 25 seconds.

### Write the Execution Code
Now we can write our execution code. Scroll down to the Environment Editor, paste in the following code in the editor, and click "Save".
```
import json
import boto3
import uuid
import time
from datetime import datetime

class TableCreator:
	"""Creates Dynamodb tables and sample data into the table."""

	def __init__(self, tablenames, primarykey, sortkey):
		self.dynamodb = boto3.resource('dynamodb')
		self.dynamodb_client = boto3.client('dynamodb')
		self.tablenames = tablenames
		self.primarykey = primarykey
		self.sortkey = sortkey

	def _create_table(self, tablename, primarykey, sortkey):
		"""Creates the Dynamodb table with a given table name, primary Key
		and sort key. Example: tablename = 'tablename'
		primarykey = {name: 'transaction_id, type: 'S'}
		sortkey = {name: 'access_timestamp', type: 'N'}"""

		try:
			self.dynamodb_client.describe_table(TableName=tablename)
			return {tablename:'Table already exists.'}
		except:
			pass

		try:
			response = self.dynamodb.create_table(
				TableName=tablename,
				KeySchema=[
					{'AttributeName':primarykey['name'],'KeyType':'HASH'},
					{'AttributeName':sortkey['name'],'KeyType':'RANGE'}],
				AttributeDefinitions=[
					{'AttributeName':primarykey['name'],'AttributeType': primarykey['type']},
					{'AttributeName':sortkey['name'],'AttributeType': sortkey['type']}],
					ProvisionedThroughput={'ReadCapacityUnits': 5,'WriteCapacityUnits': 5})
			return {tablename:'Create successful.'}
		except:
			return {tablename:'Create failed.'}

	def _insert_data(self, tablename, data, timedelay):
		"""Inserts data into a DynamoDB table given table name. data, and a time delay.
		The time delay is to allow the table create a chance to finish before trying to
		insert the data."""

		found = False
		timeout = time.time() + timedelay

		# Keeps trying to find table until timeout
		while time.time() < timeout and found == False:
			try:
				self.dynamodb_client.describe_table(TableName=tablename)
				found = True
			except:
				found = False

		if found==False:
			return {tablename:'Table does not exist.'}

		# Keeps trying to insert data into table until timeout
		while time.time() < timeout:
			try:
				table = self.dynamodb.Table(tablename)
				table.put_item(Item=data)
				return {tablename:'Insert successful.'}
			except:
				pass

		return {tablename:'Insert failed.'}

	def _create_multiple_tables(self):
		return [self._create_table(name,
				self.primarykey,self.sortkey) for name in self.tablenames]

	def create3(self, timedelay):
		"""Creates tables and inserts three data points into tables. The sample
		data inserted example is:
		{'transaction_id':'2afsd33jfoi85495jf','access_timestamp':123298347584,
		'user_id':'djfi43j09fpk3jf39k'}"""

		response = {'create':[], 'insert':[]}
		response['create'].append(self._create_multiple_tables())

		for name in self.tablenames:
			for i in range(3):
				sampledata = {self.primarykey['name']:str(uuid.uuid1()),
					self.sortkey['name']:int(datetime.now().timestamp()),
					'user_id':str(uuid.uuid4())}
				insert_response = self._insert_data(name,sampledata,timedelay)
				response['insert'].append(insert_response)

		return response

def lambda_handler(event, context):

	tablenames = ['webapp_user_logs','mobile_user_logs','utilityapp_user_logs']
	primarykey = {'name':'transaction_id','type':'S'}
	sortkey = {'name':'access_timestamp','type':'N'}

	sample_table_creator = TableCreator(tablenames,primarykey,sortkey)
	response = sample_table_creator.create3(timedelay=25)

	return {'statusCode': 200,'body': json.dumps(response)}
```
The way this code works is it creates a number of tables with a primary key and a sort key. This can be customized in the lambda handler. By default, this code will attempt to create three tables: "webapp_user_logs", "mobile_user_logs", "utilityapp_user_logs". Then it will attempt to insert three pieces of data into each table. The data that are inserted into the tables look like the following:
```
{'transaction_id':'2afsd33jfoi85495jf','access_timestamp':123298347584,'user_id':'djfi43j09fpk3jf39k'}
```

### Run the code
We will not need a trigger for this lambda function since we will be triggering it manually. To do this create a test event.
1. In lambda click "Configure test event". Then configure as follows and click "Create". Note that the actual event code we can leave as default. It does not matter what the event code is since our execution code does not use any event inputs.
```
Create new test event = "True"
Event template = "testevent"
Event code = {"key1":"value1","key2":"value2","key3":"value3"}
```
2. Click "Test" and in DynamoDB you should see that your tables and data have been created.

### Result
Now you should be able to create DynamoDB tables using AWS Lambda. Simply run your code in Lambda and go to your DynamoDB to view your tables and the data in your table.

If configured correctly, we should be able to see three tables "webapp_user_logs", "mobile_user_logs", "utilityapp_user_logs" and in each table three lines of data that look like the following:
```
{'transaction_id':'2afsd33jfoi85495jf','access_timestamp':123298347584,'user_id':'djfi43j09fpk3jf39k'}
```
