## Setup IAM Guide

This is a guide on setting up IAM in your Amazon Web Service allowing you to create Users, Groups, Roles, etc.

### Objective
Once set up, we should have a good understanding of the process of creating Users, Groups, Roles, etc.

### Activate MFA on your root account.
1. On your mobile device download Google Authenticator. 
2. Click on Activate MFA and go to next step. Then scan the QR code with your Google Authenticator.
3. Type in the two codes from Authenticator to activate.

### Create individual IAM users
1. Click on Users. Create a user name and check Programmatic access.
2. For permissions go ahead and skip. (we can give permission via groups).
3. Review and Create users. 
4. Download csv credentials and keep it in a safe and secret place.
*IMPORTANT:* You will never see these credentials again! Also, DO NOT keep these credentials in a folder with git to prevent being pushed to Github!

### Create Groups and Assign Premissions
1. Click Groups. Create a group, for example: "system-admins". 
2. Attach a Policy that fits permissions you want that group to have. For example: "system-admins" should have the policy permission "SystemAdministrator".
3. Finally, in Groups, under the Users tab, go ahead and add the user you created to your group. Now the user will have all of the permissions of that group.

### Apply Password policy
Go to Account Settings and apply any rules you wish for the passwords your users can set.

### Create Roles
Roles are a very important feature that allows one Aws service to talk to a services. This becomes very important in accessing Aws without having to save credentials within virtual machines.

1. Click Roles. Add a role name, for example: "S3-Admin-Access".
2. Select a Service Role (the service that you want to own the permission you will assign next.), for example: "Amazon EC2".
3. Attach the "AmazonS3FullAccess". This will give EC2 the permission to interact with S3.


### Result
Congrats, now you should have a User, Group, and a Role set up in IAM. 


