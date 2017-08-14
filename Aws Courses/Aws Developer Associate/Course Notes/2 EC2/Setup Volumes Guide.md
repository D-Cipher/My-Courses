## Setup Volumes Guide
This is a guide on setting up additional volumes for your EC2 instance on of Amazon Web Service.

### Objective
The goal of this guide is to gain a good understanding of the proper way to create volumes, attach and mount volumes to an EC2 instance, take a snapshot of the volume and storing the contents in S3, unmount and detach volumes from the instance.

Once set up, you will have a volume attached to your EC2 instance with an index.html and a readme.txt file inside.

### Prerequisites
In order to set up volumes you must have a running instance of EC2. See Setup EC2 Guide for more details.

### Create / Configure Volume
1. On the EC2 Dashboard click on Volumes (under Elastic Block Store).
2. Click Create Volume at the top.
3. Select volume type, eg: Cold HDD (SC1).
4. Set size, default is fine.
5. Important: Choose the availability zone as the same zone as your EC2 Instance.
6. Check encrypt volume.

### Attach the Volume
1. Select the volume and go to Actions > Attach Volume
2. In the pop-up click in Instance field and the instance ID should automatically populate. (If it does not, your volume may not have been created in the same availability zone as our EC2 Instance.
3. Click Attach Volume

### Format the Volume
1. SSH into your EC2 instance. See Setup EC2 Guide for details. If you on Windows PuTTY into your EC2. See PuTTy Key Guide for details. 
```
ssh ec2-user@54.209.96.172 -i MyEC2Key.pem
```
2. Elevate privileges to root and take check the virtual disks on your EC2.
```
sudo su
lsblk
```
3. Check that there is no data on your volume. If it says data then there is no data on it. Then format the volume. If your instance is linux use ext4, which is the most common file system for linux. If it is Windows then ntfs. Once mounted, cd into the file server directory and ls. Expect to see a create "lost+found" directory.
```
file -s /dev/xvdf
mkfs -t ext4 /dev/xvdf
```

### Mounting and Unmounting
Now that the volume is formatted, we can mount it to our EC2 instance and create files on it. We can also unmount it and keep a snapshot of the storage items in S3. 

1. Create a directory for your file server.
```
cd /
mkdir myfileserver
```

2. Mount the volume to the directory. When mounted the directory should have a file called "lost+found".
```
mount /dev/xvdf /myfileserver
cd /myfileserver/
ls
```
3. Create index.html and readme.txt in the file server directory. Note on nano: use [ctrl]+x to exit, they Y to save.
```html
cd /myfileserver/
nano index.html
<html><h1>Hello World</h1></html>
```
```
echo "This is the read me file." > readme.txt
```
4. To unmount, simply use:
```
cd /
umount /dev/xvdf
```

### Taking a Snapshot
1. In the AWS EC2 Dashboard, select the volume and go to Actions > Detach Volume. Then click detach.
2. Then go to Actions > Create Snapshot. In the popup, give it a name and descrip, ei:
```
Name = "MyFileServer_Snapshot"
Description = "Snapshot of MyFileServer."
```
3. In the right panel go to Snapshots. Let the snapshot complete. Then the contents will now be stored on S3.
4. Once the snapshot is taken, you are free to delete the volume. Select the volume, go to Actions > Delete Volume.

### Creating Volume from Snapshot
1. Select the snapshot. Then click Actions > Create Volume.
2. In the pop-up select Volume Type. Notice, you are not locked into the storage medium. We created the snapshot from a Cold HDD (SC1), but we can now make it a General Purpose SSD (GP2). 
3. Make sure Availability Zone is the same as your EC2 instance.
4. Then click create volume, and go to volumes and you should see the volume being created.
5. Now attach the volume to the instance, Actions > Attach Volume.
6. In the command line confirm that the new volume has been created. Also, check to make sure the "myfileserver" directory that you created earlier still exists:
```
lsblk
ls
```
7. Always check to see if there is data on the volume. Notice that there is a file system on there, so that means we do not need to go in and format another file system.  Then, mount the volume to the instance.
```
file -s /dev/xvdf
mount /dev/xvdf /myfileserver
```
8. Now check to make sure your files are in the directory.
```
cd /myfileserver/
ls
```

### Result
Now you should have a volume attached to your EC2 instance with an index.html and a readme.txt file inside.

~