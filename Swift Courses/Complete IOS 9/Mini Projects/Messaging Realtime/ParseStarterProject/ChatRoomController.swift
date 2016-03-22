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

class ChatRoomController: UIViewController, UITextFieldDelegate {
    
    let firebase = Firebase(url: "https://msg-realtimeapp.firebaseio.com/")
    
    var childAddHandler = FirebaseHandle()
    
    var messageKey_dict = NSMutableDictionary()
    
    @IBOutlet var tableViewOutlet: UITableView!
    
    @IBOutlet var textFieldFirebase: UITextField!

    @IBAction func sendMessage(sender: AnyObject) {
        
        let details = ["message":textFieldFirebase.text, "senderID":firebase.authData.uid]
        
        //Send Message to Firebase
            //need to make a lookup for conversationID
        firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").childByAppendingPath("messages").childByAutoId().setValue(details)
        
        //print(firebase.authData.uid)
        
        textFieldFirebase.text = ""
    
    }
    
    func firebaseUpdate(snapshot: FDataSnapshot){
        if let newMessages = snapshot.value["messages"] as? NSDictionary {
            //print(snapshot)
            
            for newMessage in newMessages {
                let key = newMessage.key as! String
                let messageExist = (self.messageKey_dict[newMessage.key as! String] != nil)
                
                if messageExist == false {
                    self.messageKey_dict.setValue(newMessage.value, forKey: key)
                }
                
            }
            
            //print(self.messageKey_dict)
            
        }
        
        dispatch_async(dispatch_get_main_queue(), { () -> Void in
            self.tableViewOutlet.reloadData()
        })

    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.textFieldFirebase.delegate = self
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillShow:"), name: UIKeyboardWillShowNotification, object: nil)
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillHide:"), name: UIKeyboardWillHideNotification, object: nil)
        
        childAddHandler = firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").queryOrderedByChild("messages").observeEventType(.Value, withBlock: { (snapshot: FDataSnapshot!) -> Void in
            
            self.firebaseUpdate(snapshot)
            
        })
        
        childAddHandler = firebase.childByAppendingPath("conversations").queryOrderedByChild("conversationID").observeEventType(.ChildChanged, withBlock: { (snapshot: FDataSnapshot!) -> Void in
            
            self.firebaseUpdate(snapshot)
            
        })
        
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return messageKey_dict.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        
        let cell = UITableViewCell(style: UITableViewCellStyle.Default, reuseIdentifier: "Cell")
        
        let arrayOfKeys = messageKey_dict.allKeys
        let key = arrayOfKeys[indexPath.row]
        let value = messageKey_dict[key as! String]
        
        cell.textLabel?.text = (value as! NSDictionary)["message"] as? String
        
        //Reverse the Table View
        tableViewOutlet.transform = CGAffineTransformMakeScale(1, -1)
        
        cell.transform = CGAffineTransformMakeScale(1, -1)
        
        return cell
    }
    
    
    //Track User's selected row
    func tableView(tableView: UITableView, willSelectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath? {
        
        self.tableViewOutlet.cellForRowAtIndexPath(indexPath)
        
        return indexPath
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
    
    //Tapping Outside the keyboard will close it:
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        
        self.view.endEditing(true)
    }
    
    //Tapping "Return" will close the keyboard:
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        
        textField.resignFirstResponder()
        
        return true
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
