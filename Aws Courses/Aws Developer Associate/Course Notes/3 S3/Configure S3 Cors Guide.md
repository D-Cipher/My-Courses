##Configure S3 Cors Guide
This is a guide on configuring S3 bucket Cross Orgin Resources Sharing (CORS) in Amazon Web Services, allowing one S3 bucket to access contents of another S3 bucket.

###Objective
Once set up, we should have a good understanding of the process of creating and configuring S3 bucket CORS. You will be able to view a static webpage on one s3 that runs a javascript that is in another s3.

###Prerequisites
Setup two s3 buckets that host static websites. For details on how to setup s3 buckets see "Setup S3 Web Host Guide", ei:

1. Create dcy-mainpage bucket and configure it to view static webpages.
2. Create dcy-loadingpage bucket and configure it to view static webpages.

###Add Script for Testing
For testing CORS, add the following index.html to your main page bucket. Make sure the link: "http://dcy-loadingpage.s3-website-us-east-1.amazonaws.com/loadpage.html" is the link to your loading page bucket.
```html
<html><body>
<script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
<script src="https://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>

<html><body><h1>Welcome to the Main Page!</h1>

<div id="get-html-from-other-s3"></div>

<script>
$("#get-html-from-other-s3").load("http://dcy-loadingpage.s3-website-us-east-1.amazonaws.com/loadpage.html")
</script>
</body></html>
```
Now add the following loadpage.html file to your load page bucket:
```html
<html><body><h2>It worked! We have successfully linked the two buckets.</h2></body></html>
```

###Configure CORS
Next, configure CORS in your loading page bucket. Under "Properties", expand "Permissions", and click on "Add CORS Configuration". Paste the following permission into the field:
```html
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>http://dcy-mainpage.s3-website-us-east-1.amazonaws.com</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```
Make sure that the Allowed Orgin is the url of your main page, ei: "http://dcy-mainpage.s3-website-us-east-1.amazonaws.com".

###Result
Go to the url to your index.html in your main page, ei: 
```
http://dcy-mainpage.s3-website-us-east-1.amazonaws.com/index.html
```
If all is configured, you should see that the linked loading page javascript run.

~