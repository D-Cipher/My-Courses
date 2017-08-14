## PuTTy Key Guide

This guide is for Windows users to create a PuTTy Key to access Amazon Web Service's EC2.

### Objective
Once set up, you will be able to access EC2 via PuTTy:
1. Select saved session, ei: "ec2-user@54.209.96.172".
2. Load and Open.

### Prerequisites
1. Launch your instance of EC2. See guide "Setup EC2 Guide" for details.
2. After clicking launch, in the pop up window, create a new key pair and download the file. Note the download location.
3. Go ahead and hit Launch Instance.
4. Download PuTTy client from http://www.putty.org/.
5. Create desktop shortcut for the PuTTY launcher and the PuTTYgen launcher.

### Creating PuTTy Key
We need to create a PuTTy key from the EC2 key we downloaded.

1. In PuTTYgen press Load and find the EC2 key (.pem file).
2. press Save Private Key, name it "MyPuttyKey.ppk".

### Set up PuTTy Session
Now we need to set up a connection between EC2 and PuTTy with our PuTTy key authentication.

1. Open your EC2 instance and get the IPv4 Public IP address (bottom left).
2. In PuTTy, under Sessions category in the "Host Name (or IP address)" create a session name called "ec2-user@" and your EC2 instance IPv4 Public IP address. ei:
```
ec2-user@54.209.96.172
```

3. Under category click the + next to SSH, under that click on Auth. In the "Private key file for authentication" click browse and select the "MyPuttyKey.ppk".
4. Go back to session, press save to save the session.


### Result
Now hit open and you should be able to run your EC2 instance via putty.

~