##Setup Boto3 Guide

This is a guide on setting up Boto3 with your Amazon Web Service allowing you to access Aws via Python.

###Objective
Once set up, we should be able to access Aws through a Python shell. 

Use the following to print out all buckets in Aws S3:
```python
import boto3
s3 = boto3.resource("s3")
print(s3) #Expected: s3.ServiceResource()

for bucket in s3.buckets.all():
	print(bucket.name) #Expect to see all your buckets in S3
```

Create and upload a new file to S3:
```python
with open("readme.txt", "w") as f:
	f.write("Hello World")
	f.write("This is a new text file!")

with open("readme.txt", "rb") as f:
	s3.Bucket("my-bucket").put_object(Key="readme.txt", Body=f)
```

###Prerequisites
Create a user in Aws IAM with atleast S3 permissions. It is highly recommended that you create a group with S3 permissions and assign your user to that group. DO NOT use your root account. See "Setting up IAM Guide" for more details. 

###Installing and Configuring
1. Install boto3.
```python
pip install boto3
```

2. Go to your home directory and create a directory ".aws":
```
$ cd ~/
$ mkdir .aws
$ cd ~/.aws
```

3. Create two files inside ".aws", "credentials" and "config". Note: to use vi type "i" to enter instert text mode and "esc" key to exit instert text mode. Then type ":w" to write the text into the file. Finally, type ":q" to exit vi.
```
$ vi credentials
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
$ vi config
[default]
region=us-east-1
```

###Result
Now open up Python shell and make a connection to S3 to check that your credentials are working properly. If everything is workign properly it should print out all buckets you have on S3.

```python
import boto3
s3 = boto3.resource("s3")
print(s3) #Expected: s3.ServiceResource()

for bucket in s3.buckets.all():
	print(bucket.name) #Expect to see all your buckets in S3
```

~