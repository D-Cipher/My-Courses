## Configure S3 Cloud Front Guide
This is a guide on configuring S3 bucket Cloud Front Distributions in Amazon Web Services, allowing your users to access your S3 buckets via caches in AWS' edge locations.

### Objective
Once set up, we should have a good understanding of the process of creating and configuring CloudFront Distributions. With CloudFront our users should see a significant load speed increase even if they are farther away from the orgin of our web server. They will be loading our website that is cached their nearest edge location rather than from the data center that houses our website. 

We should also be able to access our stactic website hosted in our private S3 bucket via our cloud distribution link through Orgin Access Identity:
```
http://dses1gtkjha6s.cloudfront.net/
```

### Prerequisites
In order do this guide you must have knowledge of how to set up S3 buckets and know how to setup the bucket as a static website. See Setup S3 Static Website Guide for more details. You'll want to have a bucket created, enable static hosting, and have an index.html and error.html in the bucket. To do this:

1. Create a bucket.
```
Bucket Name = "hello-world-webpage"
```
2. Go to Properties > Static Website Hosting > Use this bucket to host a website.
```
Index document = "index.html"
Error document = "error.html"
```
3. Create the index.html file with the following and put it into the bucket.
```
<html><head></head><body>
	<div align="center">
	<br><br><br><br><h1>Hello World</h1>
	</div>
</body></html>
```
4. Crete the error.html file with the following and put it into the bucket.
```
<html><head></head><body>
	<h1>Error! There was a problem loading the page.</h1>
</body></html>
```
5. Note that we did not change any of the default permissions of our bucket. It continues to be a private bucket with all public access turned off and blocked to the outside.

### Create Orgin Access Identity
Create an Orgin Access Identity will allow us to restrict bucket access to only come from Cloudfront.

1. Go to your console and go to CloudFront, then click on Origin Access Identity then click on "Create Origin Access Identity"
2. Give your OAI a name.
```
Comment = "oai-hello-world-webpage"
```

### Creating Cloud Front Distribution
Creating a CloudFront distribution we have two options, 1) Web distribution - which is the general distribution for static and dynamic content, or 2) RTMP - which is for Adobe Flash and video media files.

Selecting Distribution
1. Go to your console and select CloudFront under Networking. Then click on Create Distribution. 
2. Select distribution type, we will use the web distribution which is the HTTP/HTTPS.

Configuring Orgin Settings
1. Orgin Domain Name is the S3 bucket url, select it from the list. In our case:
```
Orgin Domain Name = "hello-world-webpage.s3.amazonaws.com"
```
2. Orgin Path is if your orgin path is within a sub-folder inside your bucket. In our case, it's just the root so leave it blank.
3. Orgin ID is a description. We can keep it default.
4. Select yes to restrict bucket access.
5. Select "Use an Existing Identity" and select the OAI you just created.
```
Your Identities = "oai-hello-world-webpage"
``` 
6. Select "Yes, Update Bucket Policy" to automatically update the bucket policy to allow access to the OAI.
7. Origin Custom Headers allows you to identify your users and what responses your sending. 

Default Cache Behavior Settings
1. Viewer Protocol Policy select "Redirect HTTP and HTTPS".
2. Allowed HTTP Methods select "Get, Head, Options".
3. Leave the encryption in as none.
4. Leave cached based on select request headers as none.
5. Object Caching select "Use Origin Cache Headers". Note: if you need to customize the TTL, click "Customize".
6. Smooth Streaming select No.
7. Restrict Viewer Access select No. Note: if you are going to use Signed URLs click yes for this. 
8. Compress Object Automatically select No.

Distribution Settings
1. Price Class leave as default.
2. AWS WAF Web ACL leave as none. This provides protection against SQL injection and XSS attacks at the application layer.
3. CNAMEs leave as blank. If you own a domain name that you want to use you can add it here.
4. Select Default for SSL Certificate. If you like to use your own you need to store it in AWS certificate manager.
5. Supported HTTP Versions select HTTP/2, HTTP/1.1, HTTP/1.0.
6. Default Root Object, this is your index.html.
```
Default Root Object = "index.html"
```
7. Logging select Off. If you would like to enable logging select On and select a bucket and prefix you want to save the logs to. 
8. Add a comment.
```
Comment = "hello-world-webpage"
```
8. Leave the remaining settings as default.

Once configured, click the "Create Distribution" button. It should take 20 mins or so to create the distribution.

###Configure Custom Error Pages
While the distribution is being deployed, you can create a custom error response.

1. In CloudFront Distribution, click on the distribution you just created.
2. In your destribution, click on the tab Error Pages, then click "Create Custom Error Response".
3. For HTTP Error Code select "404: Not Found".
4. Leave Error Caching Minimum TTL as the default 300 seconds.
5. Click Yes for Customize Error Response.
6. Type in the path to your error.html file in the Response Page Path.
```
Response Page Path = "/error.html"
```
7. For HTTP Response Code select "200: OK". Then click Create.

###Geo-Restrictions
You can also create restrictions based on location.

1. In CloudFront Distribution, click on the distribution you just created.
2. In your destribution, click on the tab Restrictions, then check Geo Restriction then click Edit.
3. Enable Geo-Restriction, click yes.
4. You can now select the Countries you want to Blacklist or Whitelist

### Result
Now we should be able to access our website via our CloudFront Distribution link. Note that we did not change any of the default permissions of our bucket. It continues to be a private bucket with all public access turned off and blocked to the outside. The only thing that changed about our bucket is the bucket policy that is now only allowing CloudFront to access it via OAI and CloudFront is serving the content to the user. This is not only faster, but also happens to be far more secure. 

In CloudFront, click on your distribution and find the "Domain Name", then copy the into your browser. With the link, you should be able to see your index.html a web page which has a "Hello World" message. In our case, our CloudFront distribution link is the following:
```
http://dses1gtkjha6s.cloudfront.net/
```
~