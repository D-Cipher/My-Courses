#Kivy IOS Build Guide for Xcode 6.4

I had a lot of trouble building my kivy project for IOS and after weeks of tinkering and tediously troubleshooting through the issues I finally got it to work. This is a detailed guide to what worked for me and some of the hurdles that I found along the way.

This guide will be focused on building the Touchtracer app, which is an demo app that should have already be included when you installed Kivy. Assuming you put Kivy into the applications folder when you installed it, the Touchtracer example should be located in this path: 

```
/Applications/Kivy.app/Contents/Resources/kivy/examples/demo/touchtracer
```

Make sure it is there and make sure that there is a file called “main.py” in the folder. I would also open it up in your python IDE and run it. This way you will know how the app is suppose to work after it is compiled for the Xcode IOS simulator.

##Prerequisites

This is the most important part of the guide. I have found that most of the issues revolve around not getting one of the prerequsites right.

First, you can only compile for IOS on a Mac. Python 2.7 comes preinstalled with your Mac, you will need to use that version. You will need Kivy 1.9 obviously. 

Next you will need Xcode version 6.4, not Xcode 7.1. I tried many different versions of Xcode and as of now, I have only found Xcode 6.4 to work. Xcode 6.4 can be found here: https://developer.apple.com/downloads/. 

You do need to have a developer ID, but you do not need to pay the $99, unless you want to publish apps.

You will also need Homebrew, which will make getting the additional dependencies a lot easier. Link to Homebrew is here: http://brew.sh.

Once you have Homebrew set up, use the following codes in your terminal:

```
xcode-select --install 
brew install autoconf automake libtool pkg-config 
brew link libtool 
sudo easy_install pip 
sudo pip install cython==0.21.2
sudo xcode-select --switch /Applications/Xcode.app
brew doctor
```

A couple notes here: 
* I think the official guide on the kivy website does not include "xcode-select --install". It is really import to run this and make sure there are no errors that pop up.
* Double check "brew link libtool" make sure it's linked.
* Cython is the source of a lot of problems, make sure that you have the correct version of cython and there are no errors. There was an annoying issue with not having the right admin premission using just "pip install". I think "sudo pip install" works the best. 
* I would select xcode again once everything is set up. I found a lot of issues with xcode somehow not being selected or being incorrectly selected. First, make sure xcode is version 6.4 and it is in your applications folder and that "/Applications/Xcode.app" is the right path. Then run "sudo xcode-select —switch /Applications/Xcode.app". 
* Lastly, run "brew doctor" to make sure there are no other outstanding errors.

If everything is working “brew doctor” should just give you one warning telling you your Xcode 6.4 is out of date.

Next you are ready to clone the distribution package from github. Use:

```
$ git clone git://github.com/kivy/kivy-ios
```

##Compiling Kivy

Once all of the prerequisites are met, you can start compiling. This will process will take your computer some time.  

```
$ cd kivy-ios
$ ./toolchain.py build kivy
```

##Creating Projects

Once the compile is complete you can start creating Xcode projects. 

Use the following code to create the Touchtracer demo app. Make sure that the path refers to the location of the “main.py” file. 

```
$ cd kivy-ios
$ ./toolchain.py create Touchtracer /Applications/Kivy.app/Contents/Resources/kivy/examples/demo/touchtracer
$ open touchtracer-ios/touchtracer.xcodeproj
```

To create other projects, simply replace “Touchtracer” with the name you want to call your new project, followed by the file path of the python file for your project. Again make sure that the python file is named “main.py”.

If everything works, when you press the “play” button in Xcode and you will be able to play with the touchtracer in the IOS simulator. 

Use this code to update the project once you have already created it:

```
$ cd kivy-ios
$ ./toolchain.py update touchtracer-ios
```

There might be three non-fatal “Apple Mach-O Linker Warnings” that will pop up in your Xcode, something like: “ld: warning: directory not found for option '-F/Users/tingbochen/kivy-ios/dist/frameworks’”, these can be ignored. 

Good Luck!

