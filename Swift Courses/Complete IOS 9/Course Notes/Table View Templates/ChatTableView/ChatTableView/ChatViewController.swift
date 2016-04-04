//
//  ViewController.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ChatViewController: UIViewController {

    private let tableView = UITableView(frame: CGRectZero, style: .Grouped)
    
    private let newMessageField = UITextView()
    
    private var sections = [NSDate: [Message]]()
    
    private var dates = [NSDate]()
    
    private var bottomConstraint: NSLayoutConstraint!
    
    private let cellIdentifier = "Cell"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Add dummy data
        var localIncoming = true
        var date = NSDate(timeIntervalSince1970: 1100000000)
        
        for i in 0...10 {
            let m = Message()
            //m.text = String(i) for testing
            m.text = "this is a long message. a very very long message. feel free to ignore this message."
            m.timestamp = date
            m.incoming = localIncoming
            localIncoming = !localIncoming
            
            addMessage(m)
            
            if i%2 == 0 {
                date = NSDate(timeInterval: 60*60*24, sinceDate: date)
            }
            
            /*
            //For Testing Date
            let formatter = NSDateFormatter()
            formatter.dateFormat = "MMM dd, YYYY"
            print(formatter.stringFromDate(m.timestamp!))
            */
        }
 
        
        //Create Message Field Area and Message Field and sendButton
        let newMessageArea = UIView()
        newMessageArea.backgroundColor = UIColor(red: 235/255, green: 235/255, blue: 235/255, alpha: 1.0)
        newMessageArea.layer.borderWidth = 2
        newMessageArea.layer.borderColor = UIColor.lightGrayColor().CGColor
        newMessageArea.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(newMessageArea)
        
        newMessageField.translatesAutoresizingMaskIntoConstraints = false
        newMessageField.scrollEnabled = false
        newMessageField.layer.borderWidth = 2
        newMessageField.layer.borderColor = UIColor.lightGrayColor().CGColor
        newMessageField.layer.cornerRadius = 10
        newMessageField.layer.masksToBounds = true
        newMessageField.font = UIFont(name: "Helvetica", size: 16)
        newMessageArea.addSubview(newMessageField)
        
        
        let sendButton = UIButton()
        sendButton.translatesAutoresizingMaskIntoConstraints = false
        sendButton.setContentHuggingPriority(251, forAxis: .Horizontal)
        sendButton.setContentCompressionResistancePriority(751, forAxis: .Horizontal)
        sendButton.setTitle("Send", forState: .Normal)
        sendButton.titleLabel?.font = UIFont(name: "Helvetica-Bold", size: 18)
        sendButton.setTitleColor(UIColor(red: 0/255, green: 122/255, blue: 255/255, alpha: 1.0), forState: .Normal)
        sendButton.setTitleColor(UIColor.grayColor(), forState: .Highlighted)
        
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
        
        tableView.separatorStyle = UITableViewCellSeparatorStyle.None //Removes all separators
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
        message.timestamp = NSDate()
        addMessage(message)
        newMessageField.text = ""
        
        tableView.reloadData()
        tableView.scrollToBottom(false)
        
        /*
        //For testing message text
        for eachMessage in messages {
            print(eachMessage.text)
        }
        */
    }
    
    //Create message
    func addMessage(message: Message) {
        guard let date = message.timestamp else {return}
        let calendar = NSCalendar.currentCalendar()
        let startDay = calendar.startOfDayForDate(date)
        
        var messages = sections[startDay]
        if messages == nil {
            dates.append(startDay)
            messages = [Message]()
        }
        messages!.append(message)
        sections[startDay] = messages
    }
    
    
    //Hides keyboard on tap (Not Used)
    func handleSingleTap(recongnizer: UITapGestureRecognizer) {
        view.endEditing(true)
    }
    
    
}

extension ChatViewController: UITableViewDataSource {
    
    func getMessages(section: Int) -> [Message] {
        let date = dates[section]
        
        return sections[date]!
    }
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return dates.count
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return getMessages(section).count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! ChatCell
        
        let messages = getMessages(indexPath.section)
        let message = messages[indexPath.row]
        
        cell.messageLabel.text = message.text
        cell.messageLabel.textAlignment = .Left
        
        if message.incoming == true {
            cell.messageLabel.textColor = UIColor.blackColor()
        } else if message.incoming == false {
            cell.messageLabel.textColor = UIColor.whiteColor()
        }
        
        cell.incoming(message.incoming)
        
        cell.backgroundColor = UIColor.clearColor()
        
        return cell
    }
    
    func tableView(tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
        
        let view = UIView()
        view.backgroundColor = UIColor.clearColor()
        
        let paddingView = UIView()
        paddingView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(paddingView)
        
        let dateLabel = UILabel()
        dateLabel.translatesAutoresizingMaskIntoConstraints = false
        paddingView.addSubview(dateLabel)
        
        let constraints: [NSLayoutConstraint] = [
            paddingView.centerXAnchor.constraintEqualToAnchor(view.centerXAnchor),
            paddingView.centerYAnchor.constraintEqualToAnchor(view.centerYAnchor),
            dateLabel.centerXAnchor.constraintEqualToAnchor(view.centerXAnchor),
            dateLabel.centerYAnchor.constraintEqualToAnchor(view.centerYAnchor),
            
            paddingView.heightAnchor.constraintEqualToAnchor(dateLabel.heightAnchor, constant: 5),
            paddingView.widthAnchor.constraintEqualToAnchor(dateLabel.widthAnchor, constant: 10),
            
            view.heightAnchor.constraintEqualToAnchor(paddingView.heightAnchor)
        ]
        
        NSLayoutConstraint.activateConstraints(constraints)
        
        let formatter = NSDateFormatter()
        formatter.dateFormat = "MMM dd, YYYY"
        
        dateLabel.text = formatter.stringFromDate(dates[section])

        paddingView.layer.cornerRadius = 10
        paddingView.layer.masksToBounds = true
        paddingView.backgroundColor = UIColor(red: 243/255, green: 243/255, blue: 243/255, alpha: 1.0)
        dateLabel.textColor = UIColor(red: 190/255, green: 190/255, blue: 190/255, alpha: 1.0)
        
        return view
    }
    
    //Correct for spacing between sections
    func tableView(tableView: UITableView, viewForFooterInSection section: Int) -> UIView? {
        return UIView()
    }
    func tableView(tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat {
        return 0.01
    }
    
}

extension ChatViewController: UITableViewDelegate {
    func tableView(tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        return false
    }
}



