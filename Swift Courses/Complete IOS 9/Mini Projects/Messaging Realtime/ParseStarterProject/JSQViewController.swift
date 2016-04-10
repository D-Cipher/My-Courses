//
//  JSQViewController.swift
//  Messaging Realtime
//
//  Created by Tingbo Chen on 3/19/16.
//  Copyright © 2016 Parse. All rights reserved.
//

import UIKit
import Firebase
import JSQMessagesViewController

class JSQViewController: JSQMessagesViewController {
    
    //Firebase Vars
    let firebase = Firebase(url: "https://msg-realtimeapp.firebaseio.com/")
    var childAddHandler = FirebaseHandle()
    var messageKey_ls = [String]()
    
    //JSQ Vars
    var incomingBubble: JSQMessagesBubbleImage!
    var outgoingBubble: JSQMessagesBubbleImage!
    var avatars = [String: JSQMessagesAvatarImage]()
    var jsqMessages_ls = [JSQMessage]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.senderId = firebase.authData.uid
        self.senderDisplayName = "UserName"
        self.inputToolbar?.contentView?.leftBarButtonContainerView?.hidden = true
        //self.inputToolbar?.contentView?.leftBarButtonItemWidth = 0
        
        let bubbleFactory = JSQMessagesBubbleImageFactory()
        
        incomingBubble = bubbleFactory.incomingMessagesBubbleImageWithColor(UIColor.jsq_messageBubbleGreenColor())
        outgoingBubble = bubbleFactory.outgoingMessagesBubbleImageWithColor(UIColor.jsq_messageBubbleLightGrayColor())
        
        createAvatar(senderId, senderDisplayName: senderDisplayName, color: UIColor.lightGrayColor(), textcolor: UIColor.blackColor())
        
        //Firebase Observer
        firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").childByAppendingPath("messages").queryLimitedToLast(50).observeSingleEventOfType(FEventType.Value) { (snapshot: FDataSnapshot!) -> Void in
            //print(snapshot)
            
            let values = snapshot.value
            
            for value in values as! NSDictionary {
                self.messageKey_ls.append(value.key as! String)
                if let message = value.value as? NSDictionary {
                    
                    //let date = message["date"] as! NSTimeInterval
                    
                    let recieveSenderId = message["senderID"] as! String
                    
                    //let recieveDisplayName = message["senderDisplayName"] as! String
                    
                    let recieveDisplayName = "aaa"
                    
                    
                    self.createAvatar(recieveSenderId, senderDisplayName: recieveDisplayName, color: UIColor.greenColor(), textcolor: UIColor.whiteColor())
                    
                    //let jsqMessage = JSQMessage(senderId: recieveSenderId, senderDisplayName: recieveDisplayName, date: NSDate(timeIntervalSince1970: date), text: message["message"] as! String)
                    
                    let jsqMessage = JSQMessage(senderId: recieveSenderId, senderDisplayName: recieveDisplayName, date: NSDate(), text: message["message"] as! String)
                    
                    self.jsqMessages_ls.append(jsqMessage)
                    
                    ///NEED TO learn how to sort jsqMessages by date.
                }
                
            }
            
            //self.collectionView?.reloadData()
            self.finishReceivingMessageAnimated(true)
        }
        
        firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").childByAppendingPath("messages").queryLimitedToLast(1).observeEventType(.ChildAdded) { (snapshot: FDataSnapshot!) -> Void in
            //print(snapshot)
            
            self.messageKey_ls.append(snapshot.key as String)
            if let message = snapshot.value as? NSDictionary {
                
                let date = message["date"] as! NSTimeInterval
                
                let recieveSenderId = message["senderID"] as! String
                
                let recieveDisplayName = message["senderDisplayName"] as! String
                
                self.createAvatar(recieveSenderId, senderDisplayName: recieveDisplayName, color: UIColor.greenColor(), textcolor: UIColor.whiteColor())
                
                let jsqMessage = JSQMessage(senderId: recieveSenderId, senderDisplayName: recieveDisplayName, date: NSDate(timeIntervalSince1970: date), text: message["message"] as! String)
                
                self.jsqMessages_ls.append(jsqMessage)
                
                if recieveSenderId != self.senderId {
                    JSQSystemSoundPlayer.jsq_playMessageSentSound()
                }
                
            }
            self.finishReceivingMessageAnimated(true)
            
        }
    }

    func createAvatar(senderID: String, senderDisplayName: String, color: UIColor, textcolor: UIColor) {
        if avatars[senderID] == nil {
            
            //Get user innitials
            let initials = senderDisplayName.substringToIndex(senderDisplayName.startIndex.advancedBy(min(2, senderDisplayName.characters.count)))
            
            //Create avatar with Innitials
            let avatar = JSQMessagesAvatarImageFactory.avatarImageWithUserInitials(initials, backgroundColor: color, textColor: textcolor, font: UIFont.systemFontOfSize(14), diameter: UInt(kJSQMessagesCollectionViewAvatarSizeDefault))
            
            avatars[senderID] = avatar
            
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func didPressSendButton(button: UIButton!, withMessageText text: String!, senderId: String!, senderDisplayName: String!, date: NSDate!) {
        
        //For testing JSQ
        //let message = JSQMessage(senderId: senderId, displayName: senderDisplayName, text: text)
        //jsqMessages_ls.append(message)
        
        //Send to Firebase
        let details = ["message":text, "senderID":senderId, "senderDisplayName":senderDisplayName, "date":date.timeIntervalSince1970, "messageType":"txt"]
        
        firebase.childByAppendingPath("conversations").childByAppendingPath("conversationID").childByAppendingPath("messages").childByAutoId().setValue(details)
        
        JSQSystemSoundPlayer.jsq_playMessageSentSound()
        finishSendingMessage()
    }
    
    //Importing Collection Views
    
    override func collectionView(collectionView: JSQMessagesCollectionView!, messageDataForItemAtIndexPath indexPath: NSIndexPath!) -> JSQMessageData! {
        
        
        return jsqMessages_ls[indexPath.row]
    }
    
    override func collectionView(collectionView: JSQMessagesCollectionView!, messageBubbleImageDataForItemAtIndexPath indexPath: NSIndexPath!) -> JSQMessageBubbleImageDataSource! {
        
        let message = jsqMessages_ls[indexPath.row]
        
        if message.senderId == senderId {
            return outgoingBubble
        }
        
        return incomingBubble
    }
    
    override func collectionView(collectionView: JSQMessagesCollectionView!, avatarImageDataForItemAtIndexPath indexPath: NSIndexPath!) -> JSQMessageAvatarImageDataSource! {
        let message = jsqMessages_ls[indexPath.row]
        
        return avatars[message.senderId]
    }
    
    override func collectionView(collectionView: JSQMessagesCollectionView!, attributedTextForMessageBubbleTopLabelAtIndexPath indexPath: NSIndexPath!) -> NSAttributedString! {
        
        let message = jsqMessages_ls[indexPath.row]
        
        if indexPath.row <= 1 {
            return NSAttributedString(string: message.senderDisplayName)
        }
        
        return nil
    }
    
    override func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell {
        let cell = super.collectionView(collectionView, cellForItemAtIndexPath: indexPath) as! JSQMessagesCollectionViewCell
        
        let message = jsqMessages_ls[indexPath.row]
        
        if message.senderId == senderId {
            cell.textView?.textColor = UIColor.blackColor()
        } else {
            cell.textView?.textColor = UIColor.whiteColor()
        }
        
        cell.textView?.linkTextAttributes = [NSForegroundColorAttributeName:(cell.textView?.textColor)!]
        
        return cell
    }
    
    override func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        
        return jsqMessages_ls.count
    }

}
