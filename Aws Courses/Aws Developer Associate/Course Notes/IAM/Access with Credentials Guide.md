##Access with Credentials Guide

Note: connecting with user credentials is generally NOT recommended because user credentials can be accessed within the EC2 instance. Better is to connect through roles.

In the command line (or PuTTY) type:
```
aws configure
AWS Access Key ID: *****
AWS Secret Access Key: *****
Default region name: us-east-1
Default output format: json
```

You can see see credentials using the following:
```
cd ~/.aws - access file containing credentials
nano credentials - read credentials
```