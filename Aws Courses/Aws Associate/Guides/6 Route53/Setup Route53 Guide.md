## Setup Route53
This is a guide on setting up a domain with Route53 on Amazon Web Services.

### Objective
The goal of this guide is to gain a good understanding of the proper way to register a domain and deploy it. We will be using Route53 for both the domain registration and configuring its routing policies.

With this guide you will configure a domain that users can use to access your website from all over the world using different routing policies and you will have the ability to test them. 

Once set up, you should be able to type your domain into your browser and access your webpage. 

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details.

### Register Domain
1. Go to Route53 in the console and click on Register Domain.
2. Type in a domain name, click check, and continue.
```
pathfinder.io
```
3. Fill out the registration detail and click continue.
4. Next read and accept the terms and conditions and click complete purchase.
5. Domain names may take up to three days to be ready. Once it's ready it will appear in the Registered Domains section and in Hosted Zone.

### Provision EC2 Instances
Next we will provision three EC2 instances in three different regions for testing the latency of our domain. First instance provision it in the region closes to you, in our case it's Northern Virginia. Second instance provision it in a region farthest away from you, in our case Singapore. Third instance, pick a region in between, Stockholm.

See Setup EC2 Guide for details on how to set up EC2 instances. To switch regions simply change the region on the top right of the dashboard. When provisioning each instance, add the following bootstrap script during setup (replace the XXX with the region):
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1>This is what the webpage looks like from XXX Region</h1></html>" > index.html
```

Once your three instances are setup, take note of each one's public IP address and paste them in a notepad, we will need them later.
```
3.93.15.112
13.229.231.246
13.48.132.29
```

### Configuring Simple Routing
The easiest way to configure routing is to use a simple routing policy. This will randomly pick a server to send the user to. This can be done with the following steps.
1. Go to Route53 and click on Hosted Zones.
2. Click on Create Record Set
3. In the right panel paste in the three IP addresses into the Value text box.
4. Make sure A - IPv4 address is selected as the type, leave Name blank, lower the TTL to 60 seconds.
5. Make sure Simple is selected for Routing Policy, then click Create.
6. Now go to your browser and type in your domain name, in our case: pathfinder.io
You should see the webpage and if you wait 60 seconds (as long as you set the TTL to 60 seconds) and refresh you should see a different webpage, this is because you are being set to a different web server in a random order. 

### Multivalue Answer Routing
In order to add a health check to simple routing we have to use the Multivalue Answer Routing policy.
1. Go to Route53 and click on Hosted Zones and make sure to delete your previously created routing record sets.
2. Create record set for one of the IP addresses. 
3. In the right panel paste in one of the IP addresses into the Value text box.
4. Make sure A - IPv4 address is selected as the type, leave Name blank, lower the TTL to 60 seconds.
5. Repeat steps 2 through 4 for the remaining two IP addresses.
6. Go to each of the created record sets, select Multivalue for Routing Policy.
7. For the Set ID type in a name, we'll use the name of the region that the IP address belongs to: N-Virginia, Singapore, Stockholm.
8. For each record click yes for Associate with Health Check and select your health check.

To create a health check:
1. Click on Health Checks at the left panel.
2. Give it a name, we'll use the name of our region.
3. What to monitor, select Endpoint.
4. Specify endpoint by, select IP address
5. Paste in the IP address.
6. Paste in the domain name, in our case: pathfinder.io
7. Port is 80.
8. Path is index.html
9. Leave the rest as default and click Create health check.
10. Repeat 1 through 9 for the other two IP addresses.

### Configuring Weighted Routing
You can split traffic base on different weights assigned. (Note: Steps 1 through 5 same as Multivalue Routing)
6. Go to each of the created record sets, select Weighted for Routing Policy.
7. Create a Set ID, and associate a health check.
8. For the weight type in a weight for each, we'll do 50 for N-Virginia, 30 for Singapore, 30 for Stockholm. 
Once complete, this configuration will send 50% of the traffic to N-Virginia, 30% to Singapore, 20% to Stockholm. 

### Configuring Failover Routing
You can create an active passive setup for disaster recovery. Route53 will monitor the health of your primary site using a health check and send user to the passive if it's down. (Note: Steps 1 through 5 same as Multivalue Routing)
6. Go to each of the created record sets, select Failover for Routing Policy, 
7. For one of the record sets select Primary for the Failover Record Type, for the other two select Secondary.
8. Create a Set ID, and associate a health check.
To test this simply stop the instance in your primary region and try connecting to your domain. It should automatically failover and send you to the secondary region's web server.

### Configuring Latency Routing
You can route traffic based on the lowest network latency for your user based on fastest response time irrespective of location and proximity. (Note: Steps 1 through 5 same as Multivalue Routing)
6. Go to each of the created record sets, select Latency for Routing Policy
7. Create a Set ID, and associate a health check.

### Configuring Geolocation Routing
You can choose where the traffic will be sent based on the location of the users. For example, you can send all traffic from Europe to your Frankfort server. (Note: Steps 1 through 5 same as Multivalue Routing)
6. Go to each of the created record sets, select Geolocation for Routing Policy, 
7. For each of the record set select the Location. The location you can select the country or continent of that web server.
8. Create a Set ID, and associate a health check.
To test this use a VPN and change your region and connect to your domain you should see your connecting to the domain based on location.

### Configuring Geoproximity Routing
You can configure traffic to optimally route to minimize the distance between the user and the server. For example, if your user is in Spain you might want his traffic to Route to your North Africa Server rather than to Frankfort as it is closer. It is only configurable for Traffic Flow at this time. To do this you will need to create a Traffic Policy. (Note: Steps 1 through 5 same as Multivalue Routing)
6. In DNS go to Traffic Policy > Create a Policy 
7. Create your policy rules.
8. Once set, attach the policy to your routing.

### Result
Depending on how you configured your routing, you should be able to go to your domain and be able to connect to your web server. Simple type your domain into your browser (in our case: pathfinder.io) and you should be able to see your web page.

~