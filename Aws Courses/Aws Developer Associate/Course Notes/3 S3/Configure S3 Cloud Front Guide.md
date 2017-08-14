## Configure S3 Cloud Front Guide
This is a guide on configuring S3 bucket Cloud Front Distributions in Amazon Web Services, allowing your users to access your S3 buckets via caches in AWS' edge locations.

### Objective
Once set up, we should have a good understanding of the process of creating and configuring Cloud Front Distributions. We should be able to see a significant load speed increase for users farther away from your data center because they will be loading from their nearest edge location rather than from the data center that houses your data. 

### Prerequisites
Create one S3 bucket, but make the region of the bucket in a location far from you current location, ei:
```
Bucket Name = "dcy-cdntest"
Region = "Singapore"
```
Then Upload a picture file into the bucket and open the picture file via its link, observing the slow load speed, ei:
```
https://s3-ap-southeast-1.amazonaws.com/dcy-cdntest/Penguins.jpg
```

### Creating Cloud Front Distribution
Creating a cloud front distribution we have two options, 1) Web distribution - which is the general distribution for static and dynamic content, or 2) RTMP - which is for Adobe Flash and video media files.

1. Go to your console and select Cloud Front under Networking. Then click on Create Distribution.
2. Select distribution type, we will use Web.

### Configuring Distribution
There are many settings and specifications available, we'll configure for basic simplicity.

1. Orgin Domain Name is the S3 bucket url, ei:
```
Orgin Domain Name = "dcy-cdntest.s3.amazonaws.com"
```
2. Orgin Path is if you have folders inside your bucket. Leave blank in our example.
3. Restrict Bucket Access forces users to use the cloud front url. We want this turned on.
```
Restrict Bucket Access = "Yes"
Orgin Access Identity = "Create a New Identity"
Comment = "access-identity-dcy-cdntest.s3.amazonaws.com
Grant Read Permissions on Bucket = "Yes Update Bucket Policy"
```
4. Viewer Protocol Policy select redirect HTTP to HTTPS.
```
Viewer Protocol Policy = "Redirect HTTP to HTTPS"
```
5. Allowed HTTP Methods allows for accellerating user uploads. For our example, default is fine.
6. Object Caching allows us to customize how often the caches in the edge locations are updated. Leave as default for our example.
7. Restrict View Access (Use Signed URLs or Signed Cookies) allows us to restrict to certain users, for example restrict to only paid users. Leave as "No" for our example.

Once configured, click the "Create Distribution" button. It should take 20 mins or so to create the distribution.

### Result
Go back to your S3 bucket and note that the url to the bucket no longer works. This is because we now must the contents of our bucket via Cloud Front's domain.

In cloud front, click on your distribution and find the "Domain Name", then copy it into a new tab and add the path to your picture file, ei:
```
d3139hypkmfzej.cloudfront.net/Penguins.jpg
```
If all is configured, you should see that the picture now loads faster.

~