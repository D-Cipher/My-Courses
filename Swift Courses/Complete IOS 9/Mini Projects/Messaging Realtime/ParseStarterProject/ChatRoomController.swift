//
//  ChatRoomController.swift
//  Firebase Starter Project
//
//  Created by Tingbo Chen on 3/16/16.
//  Copyright © 2016 Parse. All rights reserved.
//

import UIKit
import Firebase
import Social

class ChatRoomController: UIViewController {
    
    @IBOutlet var textLabel: UILabel!
    
    @IBOutlet var textFieldFirebase: UITextField!
    
    let firebase = Firebase(url: "https://msg-realtimeapp.firebaseio.com/")

    @IBAction func sendMessage(sender: AnyObject) {
        
        let details = ["message":textFieldFirebase.text, "sender":firebase.authData.uid]
        
        //Send Message to Firebase
            //need to make a lookup for conversationID
        firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").childByAppendingPath("messages").childByAutoId().setValue(details)
        
        print(firebase.authData.uid)
        
        textFieldFirebase.text = ""
    
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillShow:"), name: UIKeyboardWillShowNotification, object: nil)
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillHide:"), name: UIKeyboardWillHideNotification, object: nil)
        
        //Read from firebase
        firebase.observeEventType(FEventType.Value) { (snapshot: FDataSnapshot!) -> Void in
            
            //print(snapshot.value)
            /*
            if let snapshot = snapshot.value["user"] {
                if let name = snapshot?.objectForKey("name") {
                    self.textLabel.text = name as? String
                }
                
                if let isOnline = snapshot?.objectForKey("isOnline") as? Bool {
                    if isOnline == true {
                        self.view.backgroundColor = UIColor.greenColor()
                    } else if isOnline == false {
                        self.view.backgroundColor = UIColor.redColor()
                    }
                }
            }
            */
        }
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func keyboardWillShow(notification: NSNotification) {
        
        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.CGRectValue() {
            self.view.frame.origin.y -= keyboardSize.height
        }
        
    }
    
    func keyboardWillHide(notification: NSNotification) {
        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.CGRectValue() {
            self.view.frame.origin.y += keyboardSize.height
        }
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
