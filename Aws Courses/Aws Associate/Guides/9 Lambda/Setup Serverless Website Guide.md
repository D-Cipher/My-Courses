## Setup Serverless Website
This is a guide on setting a Serverless Website using AWS Lambda. AWS Lambda allows you to upload your code and create a lambda function. AWS takes care of provisioning managing the servers that you need to run the code. You don't need to worry about OS, patching, scaling, etc. The architecture of our web app will be:
1. User goes to a web URL which its Route53 to get the DNS address.
2. They will access the static contents of the web page hosted in an S3 bucket. There will be a button on the page and when activated it will give dynamic content.
3. Pressing the button will send a request to API Gateway. 
4. API Gateway is going to send that request to a Lambda function which will return a result.
5. API Gateway will return that result to the user.

### Objective
Once set up, we should have a good understanding of the process of setting up a serverless website with Lambda and API Gateway. We should be able to see a web page with a "Hello World" message and a button. By clicking on the button in the webpage it will trigger the lambda function which will change "Hello World" to your custom message. See the following example:
```
pathfinder.io
```

### Prerequisites
In order do this guide you must have knowledge of how to set up Route53. See Setup Route53 Guide for more details. You must also have alittle bit of experience with Python and how to create S3 buckets. Further, you must already have created a registered domain with hosted zones set up.

### Setting up Lambda
First we will create a lambda function that will trigger the dynamic content of our website.
1. Go to lambda in the AWS console and click "Create function".
2. Select "Author from scratch"
3. Give the function a name, select Python 3.6 for the runtime.
```
Name = "HelloWorldFunction"
Runtime = "Python 3.6"
```
4. Select "Create a new role from AWS policy template" and select the policy template "Simple microservice permissions". Then click create.
```
Role name = "LambdaMicroservicesExecutionRole"
Policy templates = "Simple microservices permissions"
```

### Upload Execution Code
We'll need an S3 bucket to hold all of the resources for our website. Then we will need to write the code that our lambda function is going to execute when it is triggered. We will save this code into our bucket. The execution code we will create is a very simple Python function that returns JSON data that says hello to you. Specifically, the JSON data enables cross-orgin resource sharing (CORS) and changes the body text to "Hello [YOUR NAME HERE]". Here are the steps:
1. Create an S3 bucket, in our case:
```
S3 Bucket Name = "hello-world-webpage"
```
2. Create a folder in the bucket called "Controller". We'll put our execution code in here.
3. Create a python file called "helloworldlambda.py" and in the file paste in the following python code.
```
import json

def lambda_handler(event, context):
    print("In lambda handler")

    result = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps("Hello [YOUR NAME HERE]")
    }

    return result
```
3. Put this python file into a zip file. We will name it: "helloworldlambda.zip".
4. Upload this zip file into the bucket folder you created, in our case it's "Controller". Then note the bucket path, in our case:
```
Object URL = "https://hello-world-webpage.s3.amazonaws.com/Controller/helloworldlambda.zip"
``` 

Next, we'll need to upload the code into our lambda function. 
1. In your lambda function scroll down to function code. 
2. For Code entry type select "Upload a file from Amazon S3" then past in you bucket URL.
```
Amazon S3 link URL = "https://hello-world-webpage.s3.amazonaws.com/Controller/helloworldlambda.zip"
```
2. For the Runtime make sure it is "Python 3.6" and for the Handler change it to "helloworldlambda.lambda_handler".
```
Runtime = "Python 3.6"
Handler = "helloworldlambda.lambda_handler"
```

### Add Trigger
Now we need to create a trigger to call our lambda function. We will use API Gateway as the trigger. Essentially when users interact with the website and press the button on the webpage it will send a request to API Gateway which will trigger the function we created.
1. In your lambda function's "Designer" click "Add trigger" and select "API Gateway".
2. Under API, select "Create a new API" and for Security select "AWS IAM".
```
API = "Create a new API"
Security = "AWS IAM"
```
3. Then click Add to add the trigger to your Lambda function.

### Configure API Gateway
The specific API call that we want to trigger our Lamba function is a GET request coming from our user. We will need to configure this in our API Gateway.
1. Click on the API you just created, this will take you to the API Gateway dashboard.
2. Select your function in our case it's the "/HelloWorldFunction", then select the method "ANY" and delete it (we will create our own method). 

Next we will need to create a new "GET" method. 
1. Select your function ("/HelloWorldFunction") and click Actions > Create Method. In the dropdown select "GET" and create it.
2. For Integration type select "Lambda Function", check "Use Lambda Proxy integration", select your lambda function, leave rest as default and click "Save".
```
Integration type = "Lambda Function"
Use Lambda Proxy integration = "TRUE"
Lambda Region = "us-east-1"
Lambda Function = "HelloWorldFunction"
Use Default Timeout = "TRUE"
```

Now that we have created the API we need to deploy it. 
1. Click Actions > Deploy API.
2. For Deployment stage select default and add a description.
```
Deployment stage = "default"
Deployment description = "prod deployment"
```

Once deployed we can now test our API.
1. Click on Stages and expand "default" > "/" > "/HelloWorldFunction" > "GET".
2. Click on "GET" and click on the "Invoke URL"
3. Open the URL in your browser and you should see the message "Hello [YOUR NAME HERE]".

Take note of the Invoke URL link, in our case it is: 
```
Invoke URL = "https://rf08hhuowb.execute-api.us-east-1.amazonaws.com/default/HelloWorldFunction"
```

### Create Static Website
Now that our lambda function is working, we'll create the contents of our static website. Our webpage will be a simple webpage the has a "Hello World" with a button that activates a script. This script hits the API gateway which triggers the lambda function and changes the "Hello World" to the message you created.
1. Create an "index.html" file and add the following code to the file:
```
<html>
	<head>
		<script>
			function myFunction() {
				var xhttp = new XMLHttpRequest();
				xhttp.onreadystatechange = function() {
					if (this.readyState == 4 && this.status == 200) {
					document.getElementById("hello-user").innerHTML = this.responseText.replace(/['"]+/g, '');
					}
				};
				xhttp.open("GET", "[YOUR API INVOKE URL HERE]", true);
				xhttp.send();
			}
		</script>
	</head>
<body>
	<div align="center">
		<br><br><br><br>
		<h1>Hello World<br><span id="hello-user"></span></h1>
		<button onclick="myFunction()">Click me</button>
		<br>
	</div>
	</body>
</html>
```
2. In the "index.html" code make sure to replace the "[YOUR API INVOKE URL HERE]" with your invoke URL. In our case it looks like this:
```
xhttp.open("GET", "https://rf08hhuowb.execute-api.us-east-1.amazonaws.com/default/HelloWorldFunction", true);
```
3. Create an "error.html" file and add the following code:
```
<html>
   <head></head>
   <body>
      <h1>Error! There was a problem loading the page.</h1>
   </body>
</html>
```
4. Upload your "index.html" and "error.html" file into your S3 bucket, in our case it is the "hello-world-webpage" bucket.

Next we will configure the bucket to allow for static website hosting.
1. Select your bucket and click "Edit public access settings" and uncheck "Block all public access".
2. Click into your bucket and click on the "Properties" tab and click on "Static website hosting".
3. Select "Use this bucket to host a website" and Use the following:
```
Index document = "index.html"
Error document = "error.html"
```
4. Select both the "index.html" and the "error.html" files then click Actions > Make public.

Now you should be able to see your website by clicking on your S3 link for your "index.html" in our case:
```
https://hello-world-webpage.s3.amazonaws.com/index.html
```

### Connect to Route53
Now we can connect our domain to this address using Route53. We will use the one we created in the Setup Route53 Guide. In our case it's "pathfinder.io".
1. Go to Route53, select your domain, click "Hosted zones" > "Create Record Set".
2. Under "Alias" click yes then for "Alias Target" select your S3 website endpoint and click create.
```
Alias = "Yes"
Alias Target = "s3-website.us-east-2.amazonaws.com"
```

### Result
Now for testing, you should be able to access your website by accessing your domain from your browser. We should be able to see a web page with a "Hello World" message and a button. By clicking on the button in the webpage it will trigger the lambda function which will change "Hello World" to your custom message. In our case our page is the following:
```
pathfinder.io
```
If it has been configured correctly, we should be able to see the "Hello World" and after clicking the button we should see that the message has changed to "Hello [YOUR NAME HERE]".