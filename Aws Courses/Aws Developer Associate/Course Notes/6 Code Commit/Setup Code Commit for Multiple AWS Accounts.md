## Setup Code Commit for Multiple AWS Accounts
This is a guide on setting up a Code Commit SSH on computer for multiple AWS accounts. If you have two AWS accounts and have git repositories on both on CodeCommit, there are a few options that allow you to and you want to have ssh access to both repositories from the same computer.

### Objective
Once set up, you should have a good understanding of the process of creating and configuring Code Commit on multiple accounts. You will be able to git commit to two different Aws accounts with different access keys one the same computer. 

We'll set up one commit for your work account and one for your personal account and you will be able to use the following command to test each ssh connection:
```
$ ssh codecommit-work
$ ssh codecommit-personal
```
You will be able to use the following commands to push contents of the local directory up to the code commit repos in different accounts.
```
$ git push ssh://YOUR_SSH_KEY_ID_FIRST_ACCOUNT@codecommit-work/v1/repos/Aws-Work-Repo
$ git push ssh://YOUR_SSH_KEY_ID_SECOND_ACCOUNT@codecommit-personal/v1/repos/Aws-Personal-Repo
```

### Prerequisites
In order to create a commit to a code commit repository, you first need Git. If you do not already have Git installed, first install the latest version at the Git website: https://git-scm.com/.

Furthermore, you must already have gone through the "Setup Code Commit Guide" or have a prior understanding of how to commit to AWS codecommit.

Finally, you must have two AWS accounts. For this guide, assume that one of our accounts we will be using for personal reasons and the other will be a work account.

### Generate Two SSH Keys
In order to connect to CodeCommit on each of your accounts, you need to generate two SSH Key pairings. Go to your Git bash terminal and create an ssh key pair.

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
3. Once created, read the codecommit_rsa.pub file and take note of this public key. You will need it later.
```
$ cat codecommit_rsa.pub
```
4. Repeat steps 1 through 3, but this time name the ssh-keygen codecommit_rsa_2.

### Attaching and Pairing the Key for each Account
With the ssh key created, now you need to attach it to the IAM user's security credentials on each account. Then get the SSH Key ID for each account.

1. Go to the IAM > Users and select the user that will be accessing the repository.
2. Then click on the "Security credentials" tab and under "SSH keys for AWS CodeCommit", click "Upload SSH public key".
3. Paste the created key into the field.
4. Once uploaded, an "SSH Key ID" will be created in the section under the "Upload SSH public key" button. Note this SSH Key ID.
5. Again, repeat the above steps for your second account.

### Configure .ssh dir
There are many ways to configure the .ssh dir to make connecting work. This guide will focus on the method that allows you to have a unique SSH Public key for each AWS Account, you can upload them separately to IAM and get two unique SSH Key Ids back.

Now create and configure the .ssh config file with the proper permissions.

1. Use touch config and edit the config file.
```
$ touch config
$ chmod 600 config
$ nano config
```
2. In the config file, paste in the following block.
```
Host codecommit-work
  Hostname git-codecommit.us-east-1.amazonaws.com
  User YOUR_SSH_KEY_ID_FIRST_ACCOUNT
  IdentityFile ~/.ssh/codecommit_rsa
 
Host codecommit-personal
  Hostname git-codecommit.us-east-1.amazonaws.com
  User YOUR_SSH_KEY_ID_SECOND_ACCOUNT
  IdentityFile ~/.ssh/codecommit_rsa_2
```

### Establish Authentication
Establish authentication and test to make sure you have a successful authentication using the following:
```
$ ssh codecommit-work
$ ssh codecommit-personal
```
Once the output reads "You have successfully authenticated over SSH", your connection to Code Commit is setup and ready to go.  

### Creating a repository
For each account, in the console navigate to Code Commit and click on "Create Repository". Then give the repository a unique name and add a description and note the ssh link. For example:
```
Repository Name = "Aws-Work-Repo"
Description = "Repository for Aws Work files"
```
The SSH link can be found by "clicking on connect to reposititory":
```
ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/Aws-Work-Repo
```

### Result
Once the repo has been created, you can link your local files to the repository. Navigate to the directory you want associate with the newly created repo.

1. Innitializes an empty local git repo the directory and add the orgin as the code commit repo link.
```
$ git init
$ git remote add orgin ssh://YOUR_SSH_KEY_ID_FIRST_ACCOUNT@codecommit-work/v1/repos/Aws-Work-Repo
$ git init
$ git remote add orgin ssh://YOUR_SSH_KEY_ID_SECOND_ACCOUNT@codecommit-work/v1/repos/Aws-Personal-Repo
```
2. Use the following commands to add commit and push contents of the local directory up to the code commit repo. 
```
$ git push --set-upstream ssh://YOUR_SSH_KEY_ID_FIRST_ACCOUNT@codecommit-work/v1/repos/Aws-Work-Repo master
$ git push --set-upstream ssh://YOUR_SSH_KEY_ID_SECOND_ACCOUNT@codecommit-work/v1/repos/Aws-Personal-Repo master
```
Once the push is successful, your repos are now linked. Note that the first push may require "--set-upstream ... master", but successive pushes can be initiated with just "git push".
~