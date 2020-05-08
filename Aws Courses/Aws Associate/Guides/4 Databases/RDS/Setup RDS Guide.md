## Setup RDS Guide
This is a guide on setting up an RDS for a webserver on Amazon Web Services.

### Objective
The goal of this guide is to gain a good understanding of the proper way to create an RDS for a webserver. We will be using MySql for the RDS database and WordPress for the content management system.

Once set up, you will be able to type into your browser your instance's IP address and it will bring you to the WordPress dashboard that is connected to a MySQL RDS database. This will allow you to create web apps.

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details.

### Provisioning RDS
1. Go to the RDS Dashboard and click create database.
2. Select the Engine type as MySQL
3. Select version MySQL 5.7.22, and select Free Tier Template
5. In Settings, give the DB instance identifier a name, ex: mytestrds
6. Then set up the credentials to the DB: master username: admin, and set a master password
7. In Availabilty & durability section you can turn on Multi-AZ deployment which is recommended. For free tier you will need to launch the db instance first and then click on it and click modify. This step is completely optional. 
8. Skip down to VPC security group and click create a new VPC give it a name, ex: testrds-vpc. Make sure that the security group allows MySQL inbound traffic.
9. In Additional configurations, specify an Initial Database Name, ex: mytestdb
10. In Backups, set Backup retention period to 7 days and set a window for backup
11. In Maintenance Window, click on select window and set a window for maintenance
12. Finally click create database

### Create an EC2 Instance
1. Setup your EC2 instance, see Setup EC2 Guild for details.
2. During setup add the following bootstrap script in the user data section to install WordPress in your instance:
```
#!/bin/bash
yum install httpd php php-mysql -y
cd /var/www/html
wget https://wordpress.org/wordpress-5.1.1.tar.gz
tar -xzf wordpress-5.1.1.tar.gz
cp -r wordpress/* /var/www/html/
rm -rf wordpress
rm -rf wordpress-5.1.1.tar.gz
chmod -R 755 wp-content
chown -R apache:apache wp-content
service httpd start
chkconfig httpd on
```
3. Note the security group that you use, it should allow HTTP and HTTPS for all inbound traffic and allow SSH for your IP address. Give it a name, ex: myEC2webaccess

### Allow EC2 Security Group to Talk to RDS Security Group
1. Go to your RDS security group, in our case it's the security group for testrds-vpc.
2. Add inbound traffic to this security group allowing MySQL/Aurora for your EC2 security group, in our case: sg-0d16dbdea2f846f5f (myEC2webaccess).

### Set up WordPress
Once your RDS is innitialized then you can go to the dashboard, select the RDS that you created, click on connectivity, and find the Endpoint in our case it's mytestrds.cqfiokbasunq.us-east-1.rds.amazonaws.com. We will use this for the connection.

1. Go to your EC2 instance and find the public IP address and then copy and paste it into your browser, in our case it's: 35.153.135.48. Once connected, you should be able to see the Wordpress Setup page.
2. Click lets go in the Wordpress Setup page and type in all of the connection details.
```
Database Name: mytestdb
Username: admin
Password: ***
Database Host: mytestrds.cqfiokbasunq.us-east-1.rds.amazonaws.com
Table Prefix: wp_
```
3. If you get a page that says "Sorry, but I can't write the wp-config.php file." And it will give you a php code to create the wp-config.php file. You will need to create the wp-config.php file in your instance. 
4. Go to your EC2 instance and create the wp-config.php file in your /var/www/html directory, and paste the php code into this file. Then hit run the installation. 
5. You should be able to see the Welcome Install WordPress page. Give your site a title, create username, password, and email address.
6. Once it's installed you should be able to launch wordpress and log in.

### Creating Read Replica (Optional)
Creating read replicas can increase the performance of the database. In order to do this make sure you have set a backup retention window.

1. Select your database and click Modify > Create Read Replica
2. Give it a DB instance identifier, ex: testrds-replica
3. You can leave the other settings as default
4. Then click Modify DB Instance and the read replica will be created

### Result
Now you should be able to go to log into Wordpress and build your site. Simple go to your instance's IP address (in our case: 35.153.135.48) and log in using the username and password you created.

~