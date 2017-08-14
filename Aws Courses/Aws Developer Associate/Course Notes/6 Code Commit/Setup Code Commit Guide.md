##Setup S3 Web Host Guide
This is a guide on setting up a Code Commit repository for using the aws cloud as version control.

###Objective
Once set up, you should have a good understanding of the process of creating and configuring Code Commit and be able to git commit to the Aws cloud. 
You will be able to use the following command to test the ssh connection to code commit:
```
$ ssh git-codecommit.us-east-1.amazonaws.com
```
You will be able to use the following commands to add commit and push contents of the local directory up to the code commit repo.
```
$ git add .
$ git commit -m "test push"
$ git push ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/Aws-Files-Repo
```

###Prerequisites
In order to create a commit to a code commit repository, you first need Git. If you do not already have Git installed, first install the latest version at the Git website: https://git-scm.com/.

###Generate SSH Key
In order to connect to Code Commit you need to generate an SSH Key pairing. Go to your Git bash terminal and create an ssh key pair.

1. In the Git bash terminal type:
```
$ cd ~/.ssh
```
Note that if there is no such directory, then create it using (chmod 700 is the important step here):
```
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh
$ cd ~/.ssh
```
2. Generate the key using the command ssh-keygen, and create the name codecommit_rsa, leave passcode field empty:
```
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/cawen/.ssh/id_rsa): codecommit_rsa
```
3. Once created, read the codecommit_rsa.pub file and copy the key.
```
$ cat codecommit_rsa.pub
```

###Attaching and Pairing the Key
With the ssh key created, now you need to attach it to the IAM user's security credentials and then getting the SSH Key ID.

1. Go to the IAM > Users and select the user that will be accessing the repository.
2. Then click on the "Security credentials" tab and under "SSH keys for AWS CodeCommit", click "Upload SSH public key".
3. Paste the created key into the field.
4. Once uploaded, an "SSH Key ID" will be created in the section under the "Upload SSH public key" button. Note this SSH Key ID.

###Configure .ssh dir
Now create and configure the .ssh config file with the proper permissions.

1. Use touch config and edit the config file.
```
$ touch config
$ chmod 600 config
$ nano config
```
2. In the config file, paste in the following block. For the User, use the "SSH Key ID" you noted earlier.
```
Host git-codecommit.*.amazonaws.com
  User YOUR_SSH_KEY_ID
  IdentityFile ~/.ssh/codecommit_rsa
```

###Establish Authentication
Establish authentication and test to make sure you have a successful authentication using the following:
```
$ ssh git-codecommit.us-east-1.amazonaws.com
```
Once the output reads "You have successfully authenticated over SSH", your connection to Code Commit is setup and ready to go.  

###Creating a repository
In the console navigate to Code Commit and click on "Create Repository". Then give the repository a unique name and add a description and note the ssh link.
```
Repository Name = "Aws-Files-Repo"
Description = "Repository for Aws files"
```
The SSH link can be found by "clicking on connect to reposititory":
```
ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/Aws-Files-Repo
```

###Result
Once the repo has been created, you can link your local files to the repository. Navigate to the directory you want associate with the newly created repo.

1. Innitializes an empty local git repo the directory and add the orgin as the code commit repo link.
```
$ git init
$ git remote add orgin ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/Aws-Files-Repo
```
2. Use the following commands to add commit and push contents of the local directory up to the code commit repo. 
```
$ git add .
$ git commit -m "test push"
$ git push --set-upstream ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/Aws-Files-Repo master
```
Once the push is successful, your repos are now linked. Note that the first push may require "--set-upstream ... master", but successive pushes can be initiated with just "git push".
~