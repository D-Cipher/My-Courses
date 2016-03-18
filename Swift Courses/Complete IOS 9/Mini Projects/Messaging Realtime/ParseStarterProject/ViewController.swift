//
//  ViewController.swift
//
//  Copyright 2011-present Parse Inc. All rights reserved.
//

import UIKit
import Parse
import FBSDKCoreKit
import FBSDKLoginKit
import Firebase

class ViewController: UIViewController {
    
    let firebase = Firebase(url: "https://msg-realtimeapp.firebaseio.com/")

    @IBAction func FBloginButton(sender: AnyObject) {
        
        let permission = ["public_profile"]
        
        PFFacebookUtils.logInInBackgroundWithReadPermissions(permission) { (user: PFUser?, error: NSError?) -> Void in
            
            if let error = error {
                print(error)
            } else {
                if let user = user {
                    print(user)
                    
                    self.firebaseAuthwithFB()
                }
            }
        }
        
    }
    
    func firebaseAuthwithFB() {
        
        let accessToken = FBSDKAccessToken.currentAccessToken().tokenString
        
        firebase.authWithOAuthProvider("facebook", token: accessToken) { (error, authData) -> Void in
            if let error = error {
                print(error)
            } else {
                if let authData = authData {
                    print(authData.uid)
                    
                    //Read from firebase
                    self.firebase.observeEventType(FEventType.Value) { (snapshot: FDataSnapshot!) -> Void in
                        
                        if let snapshot = snapshot.value["users"] {
                            if ((snapshot?.objectForKey(authData.uid)) != nil) {
                                print("existing user")
                                
                                //self.firebase.childByAppendingPath("users").childByAppendingPath(authData.uid).updateChildValues(["isOnline":true])
                                
                                self.firebase.removeAllObservers()
                                
                                //put an activity indicator here
                                
                                self.performSegueWithIdentifier("tabBarSegue", sender: self)
                            } else {
                                print("new user")
                                self.firebase.childByAppendingPath("users").childByAppendingPath(authData.uid).setValue(["isOnline":true, "name":""])
                                
                                self.firebase.removeAllObservers()
                                
                                //put an activity indicator here
                                
                                self.performSegueWithIdentifier("tabBarSegue", sender: self)
                            }
                        }
                    }
                }
            }
        }
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        /*
        let testObject = PFObject(className: "TestObject")
        testObject["foo"] = "bar"
        testObject.saveInBackgroundWithBlock { (success, error) -> Void in
        print("Object has been saved.")
        }
        */
    }
    
    override func viewDidAppear(animated: Bool) {
        
        //PFUser.logOut() //For testing
        
        if let username = PFUser.currentUser()?.username {
            
            if firebase.authData != nil {
                self.performSegueWithIdentifier("tabBarSegue", sender: self)
            }
            
            //self.firebaseAuthwithFB()
        }
    }
    
    //@IBAction func unwindViewController(segue:UIStoryboardSegue) {
        
    //}

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

