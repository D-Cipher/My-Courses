//
//  ViewController.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ChatViewController: UIViewController {

    private let tableView = UITableView()
    
    private let newMessageField = UITextView()
    
    private var messages = [Message]()
    
    private var bottomConstraint: NSLayoutConstraint!
    
    private let cellIdentifier = "Cell"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Add dummy data
        var localIncoming = true
        
        for i in 0...10 {
            let m = Message()
            //m.text = String(i) for testing
            m.text = "this is a longer message."
            m.incoming = localIncoming
            localIncoming = !localIncoming
            messages.append(m)
        }
        
        //Create Message Field Area and Message Field and sendButton
        let newMessageArea = UIView()
        newMessageArea.backgroundColor = UIColor.lightGrayColor()
        newMessageArea.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(newMessageArea)
        
        newMessageField.translatesAutoresizingMaskIntoConstraints = false
        newMessageField.scrollEnabled = false
        newMessageArea.addSubview(newMessageField)
        
        
        let sendButton = UIButton()
        sendButton.translatesAutoresizingMaskIntoConstraints = false
        sendButton.setContentHuggingPriority(251, forAxis: .Horizontal)
        sendButton.setContentCompressionResistancePriority(751, forAxis: .Horizontal)
        sendButton.setTitle("Send", forState: .Normal)
        sendButton.addTarget(self, action: Selector("pressedSend:"), forControlEvents: .TouchUpInside)
        newMessageArea.addSubview(sendButton)
        
        //Set up constraints
        bottomConstraint = newMessageArea.bottomAnchor.constraintEqualToAnchor(view.bottomAnchor)
        bottomConstraint.active = true
        
        let messageAreaConstraints: [NSLayoutConstraint] = [
            newMessageArea.leadingAnchor.constraintEqualToAnchor(view.leadingAnchor),
            newMessageArea.trailingAnchor.constraintEqualToAnchor(view.trailingAnchor),
            //newMessageArea.bottomAnchor.constraintEqualToAnchor(view.bottomAnchor),
            //newMessageArea.heightAnchor.constraintEqualToConstant(50)
            
            newMessageField.leadingAnchor.constraintEqualToAnchor(newMessageArea.leadingAnchor, constant: 10),
            newMessageField.centerYAnchor.constraintEqualToAnchor(newMessageArea.centerYAnchor),
            sendButton.trailingAnchor.constraintEqualToAnchor(newMessageArea.trailingAnchor, constant: -10),
            newMessageField.trailingAnchor.constraintEqualToAnchor(sendButton.leadingAnchor, constant: -10),
            sendButton.centerYAnchor.constraintEqualToAnchor(newMessageField.centerYAnchor),
            newMessageArea.heightAnchor.constraintEqualToAnchor(newMessageField.heightAnchor, constant: 20)
            
        ]
        
        NSLayoutConstraint.activateConstraints(messageAreaConstraints)
        
        
        //Create Table for Chat Bubbles
        tableView.registerClass(ChatCell.self, forCellReuseIdentifier: cellIdentifier) //register ChatCell for reuse
        tableView.dataSource = self
        tableView.delegate = self
        tableView.estimatedRowHeight = 44
        tableView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(tableView)
        
        let tableViewConstraints: [NSLayoutConstraint] = [
            
            tableView.topAnchor.constraintEqualToAnchor(view.topAnchor),
            tableView.leadingAnchor.constraintEqualToAnchor(view.leadingAnchor),
            tableView.trailingAnchor.constraintEqualToAnchor(view.trailingAnchor),
            tableView.bottomAnchor.constraintEqualToAnchor(newMessageArea.topAnchor)
            
        ]
        
        NSLayoutConstraint.activateConstraints(tableViewConstraints)
        
        //Detect when keyboard pops up and hides
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillShow:"), name: UIKeyboardWillShowNotification, object: nil)
        NSNotificationCenter.defaultCenter().addObserver(self, selector: Selector("keyboardWillHide:"), name: UIKeyboardWillHideNotification, object: nil)
        
        /*
        //Tap Recognizer to close keyboard
        let tapRecognizer = UITapGestureRecognizer(target: self, action: "handleSingleTap:")
        tapRecognizer.numberOfTapsRequired = 1
        view.addGestureRecognizer(tapRecognizer)
        */
        
        tableView.keyboardDismissMode = UIScrollViewKeyboardDismissMode.OnDrag //Close keyboard on drag
        
    }
    
    override func viewDidAppear(animated: Bool) {
        tableView.scrollToBottom(true)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //Animates the Message Text Field Area when keyboard shows and hides
    func keyboardWillShow(notification: NSNotification) {
        updateBottomConstraint(notification)
        tableView.scrollToBottom(true)
    }
    func keyboardWillHide(notification: NSNotification) {
        updateBottomConstraint(notification)
    }
    
    //Updates Bottom Constraint of Message Text Field Area
    func updateBottomConstraint(notification: NSNotification) {
        if let userInfo = notification.userInfo, frame = userInfo[UIKeyboardFrameEndUserInfoKey]?.CGRectValue, animationDuration = userInfo[UIKeyboardAnimationDurationUserInfoKey]?.doubleValue {
            
            let newFrame = view.convertRect(frame, fromView: (UIApplication.sharedApplication().delegate?.window)!)
            
            bottomConstraint.constant = newFrame.origin.y - CGRectGetHeight(view.frame) //Get the height of the keyboard
            
            UIView.animateWithDuration(animationDuration, animations: {
                self.view.layoutIfNeeded()
            })
            
        }
    }
    
    //Function that controls send button
    func pressedSend(button: UIButton) {
        guard let text = newMessageField.text where text.characters.count > 0 else {return}
        let message = Message()
        message.text = text
        message.incoming = false
        messages.append(message)
        newMessageField.text = ""
        tableView.reloadData()
        tableView.scrollToBottom(false)
        
        /*
        //For testing
        for eachMessage in messages {
            print(eachMessage.text)
        }
        */
    }
    
    
    //Hides keyboard on tap (Not Used)
    func handleSingleTap(recongnizer: UITapGestureRecognizer) {
        view.endEditing(true)
    }
}

extension ChatViewController: UITableViewDataSource {
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return messages.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! ChatCell
        
        let message = messages[indexPath.row]
        
        cell.messageLabel.text = message.text
        cell.incoming(message.incoming)
        
        cell.separatorInset = UIEdgeInsetsMake(0, tableView.bounds.size.width, 0, 0) //removes tableView seperators
        
        return cell
    }
    
}

extension ChatViewController: UITableViewDelegate {
    func tableView(tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        return false
    }
}



