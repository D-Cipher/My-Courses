## Apache Guide
This is a guide on setting up Apache on an instance of you Amazon Web Services' EC2 Virtual environment.

### Objective
Once set up, you will be able to view publicly the index.html webpage of your EC2 from your browser by pasting in the IPv4 Public IP address. This is found in your instance dashboard (bottom left). 

Note: Your EC2 must be given security group permissions for HTTP and HTTPS input and output. See Setup EC2 Guide for more details. 

### Prerequisites
You must be in root and be sure to update machine then install Apache.
```
sudo su
yum update
yum install httpd -y
```

Alternatively, you can also add the following script to the user data section when creating the EC2 instance. This will run the bash script upon launching the instance.
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
yum install amazon-efs-utils -y
```

### Starting Apache
Start Apache and make sure it starts every time we boot up the EC2 instance.
```
service httpd start
chkconfig httpd on
```

### Create a website
Go to "/var/www/html" anything in this directory is publicly accessible.
```
cd /var/www/html
```

Then create an "index.html". Note on nano: use [ctrl]+x to exit, they Y to save.
```html
nano index.html

<html><h1>Hello World</h1></html>
```

### Result
Now test the result, from your browser by pasting in the IPv4 Public IP address and you should be able to view your index.html file from your browser.

~
