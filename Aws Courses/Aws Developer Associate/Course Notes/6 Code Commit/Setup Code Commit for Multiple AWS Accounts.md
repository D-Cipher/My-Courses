## Setup Code Commit for Multiple AWS Accounts
This is a guide on setting up a Code Commit SSH on computer for multiple AWS accounts. If you have two AWS accounts and have git repositories on both on CodeCommit, there are a few options that allow you to and you want to have ssh access to both repositories from the same computer.

### Unique SSH Public Keys
For this method, substitute Host Name in config file. If you have a unique SSH Public key for each AWS Account, you can upload them separately to IAM and get two unique SSH Key Ids back. Your ~/.ssh/config file will need to look something like this:

```
Host codecommit-work
    Hostname git-codecommit.us-east-1.amazonaws.com
    User <SSH-KEY-ID-1>
    IdentityFile ~/.ssh/codecommit_rsa (path to associated public key)
 
Host codecommit-personal
    Hostname git-codecommit.us-east-1.amazonaws.com
    User <SSH-KEY-ID-2>
    IdentityFile ~/.ssh/codecommit_2_rsa (path to other key)
```

In this configuration, you will be able to replace 'git-codecommit.us-east-1.amazonaws.com' with 'codecommit-2'. For example, to clone a repository in your second account, do:
```
git clone ssh://codecommit-personal/v1/repos/<repository_name>
```

You can set up a remote for your repository by executing:
```
git remote add origin ssh://codecommit-personal/v1/repos/<repository_name>
```

If your repository already has a remote for CodeCommit, you can modify the url in the .git/config file to fit the above syntax.


### Config for One Account
Configure ~/.ssh/config for one account only. If you use one of your AWS accounts much more frequently than the other, this option might be right for you. You can configure your ~/.ssh/config file as you would normally with the account you use most frequently. When you need to access a repository in your other account, you can prefix your git command to override the SSH configuration used (as of git 2.3) with:
```
GIT_SSH_COMMAND='ssh -i <IdentityFile> -l <SSH-Key-Id-2>'
```

For example, for a clone, you could say:
```
GIT_SSH_COMMAND='ssh -i ~/.ssh/codecommit-2_rsa -l APKA...' git clone ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/<repository_name>
```

### Same public key for both accounts
This method works but is NOT recommend because it is re-using public/private key pairs across accounts. This allows you to have only one ssh config entry for codecommit, which would look like this:
```
Host git-codecommit.*.amazonaws.com
      IdentityFile ~/.ssh/codecommit_rsa (path to public key)
```

When you upload the public key to IAM, you get back a unique SSH Key Id for each account. Each repository you use will need to be configured with a remote containing one of these SSH key ids, depending on which account the repository is in. You can do this with:
```
git remote add origin ssh://<SSH-KEY-ID-1>@git-codecommit.us-east-1.amazonaws.com/V1/repos/<repository-name>
```

Once the push is successful, your repos are now linked. Note that the first push may require "--set-upstream ... master", but successive pushes can be initiated with just "git push".
~