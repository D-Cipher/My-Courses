//
//  ViewController.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

/*
 ====Notes On adding Core Data=====
 
 1) Add "CDHelper.swift" addon to project.
 *Note: If project was set up with core data:
 -clear out any items related to core data in AppDelegate.swift
 -delete the model file
 
 2) In CDHelper.swift, add your project's name to .sqlite
 """
 let url = self.storesDirectory.URLByAppendingPathComponent("Your Project Name.sqlite")
 """
 
 3) In MessageViewController.swift add:
 """
 var context: NSManagedObjectContext?
 """
 
 4) In AppDelegate.swift add:
 """
 //Core Data: Setup Context
 let root = window!.rootViewController as! LoginViewController
 let context = NSManagedObjectContext(concurrencyType: .MainQueueConcurrencyType)
 context.persistentStoreCoordinator = CDHelper.sharedInstance.coordinator
 root.context = context
 """
 
 5) Pass the context set up in root to MessageViewController.swift
 User prepareForSegue to pass the context variable till it reaches the Message VC. Example:
 """
 override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
 
 let tab = segue.destinationViewController as! UITabBarController
 let nav = tab.viewControllers![0] as! UINavigationController
 let chatTabVC = nav.topViewController as! ChatTabController
 
 chatTabVC.context = context
 }
 """
 
 6) Set up Core Data Model:
 -Add model:
 File > New File > IOS > Core Data > Data Model > Name: "Model" > Save
 
 -DELETE Message.swift
 
 -Create a new Message.swift with Model:
    (+) Add Entity -> Name: "Message"
    Under Attributes add (+):
        +Attribute: text ; Type: String
        +Attribute: incoming ; Type: Bool
        +Attribute: timestamp ; Type: Date
 
 Editor > Create NSManagedObject Subclass... > Select Model > Select Message > Create
 
 *This will generate the new Message.swift and Message+CoreDataProperties.swift
 
 7) Set up new Message.swift file:
 """
 class Message: NSManagedObject {
 
 var isIncoming: Bool {
    get {
        guard let incoming = incoming else {return false}
        return incoming.boolValue
    } set (incoming) {
        self.incoming = incoming
        }
    }
 }
 """
 
 8) Update message entity in the MessageViewController.swift
 -In viewDidLoad DELETE the dummy data, everything from "var localIncoming ...." to end of the for loop.
 -In pressedSend DELETE "let message = Message()" and add new initialization using core data:
 """
 guard let context = context else {return}
 guard let message = NSEntityDescription.insertNewObjectForEntityForName("Message", inManagedObjectContext: context) as? Message else {return}
 """
 -Change all instances of .incoming to .isIncoming:
 -Under pressedSent: "message.incoming = false" to "message.isIncoming = false"
 -cellforRowAtIndexPath: "cell.incoming(message.incoming)" to "cell.incoming(message.isIncoming)"
 
 9) Get saved messages from core data. In viewDidLoad add:
 """
 do {
    let request = NSFetchRequest(entityName: "Message")
 
    request.sortDescriptors = [NSSortDescriptor(key: "timestamp", ascending: false)]
 
    if let result = try context?.executeFetchRequest(request) as? [Message] {
 
        for message in result {
            addMessage(message)
            }
        }
    } catch {
        print("fetch error")
    }
 """
 
 10) Save new messages in the pressedSend method to core data:
 after "addMessage(message)" add:
 """
 do {
    try context.save()
 } catch {
    print("save context error")
    return
 }
 
 11) Sort messages by time:
 Add following to addMessage function after "dates.append(startDay)"
 """
 dates = dates.sort({$0.earlierDate($1) == $0})
 """
 
 Add following to addMessage function after "messages!.append(message)"
 """
 messages!.sortInPlace{$0.timestamp!.earlierDate($1.timestamp!) == $0.timestamp!}
 """
 */


import UIKit

class MessageViewController: UIViewController {

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
        
        //Add Message Field
        newMessageField.translatesAutoresizingMaskIntoConstraints = false
        newMessageField.scrollEnabled = false
        newMessageField.layer.borderWidth = 2
        newMessageField.layer.borderColor = UIColor.lightGrayColor().CGColor
        newMessageField.layer.cornerRadius = 10
        newMessageField.layer.masksToBounds = true
        newMessageField.font = UIFont(name: "Helvetica", size: 16)
        newMessageArea.addSubview(newMessageField)
        
        //Add Send Button
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
        
        //Add Camera Button
        let origImage = UIImage(named: "camera.png")
        let tintedImage = origImage?.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        let cameraButton = UIButton()
        cameraButton.translatesAutoresizingMaskIntoConstraints = false
        cameraButton.setContentHuggingPriority(251, forAxis: .Horizontal)
        cameraButton.setContentCompressionResistancePriority(751, forAxis: .Horizontal)
        cameraButton.setImage(tintedImage, forState: .Normal)
        cameraButton.tintColor = UIColor(red: 0.25, green: 0.25, blue: 0.25, alpha: 1)
        cameraButton.addTarget(self, action: Selector("someAction:"), forControlEvents: .TouchUpInside)
        newMessageArea.addSubview(cameraButton)
        
        //Set up constraints
        bottomConstraint = newMessageArea.bottomAnchor.constraintEqualToAnchor(view.bottomAnchor)
        bottomConstraint.active = true
        
        let messageAreaConstraints: [NSLayoutConstraint] = [
            newMessageArea.leadingAnchor.constraintEqualToAnchor(view.leadingAnchor),
            newMessageArea.trailingAnchor.constraintEqualToAnchor(view.trailingAnchor),
            //newMessageArea.bottomAnchor.constraintEqualToAnchor(view.bottomAnchor),
            //newMessageArea.heightAnchor.constraintEqualToConstant(50)
            
            cameraButton.leadingAnchor.constraintEqualToAnchor(newMessageArea.leadingAnchor, constant: 10),
            newMessageField.leadingAnchor.constraintEqualToAnchor(cameraButton.trailingAnchor, constant: 10),
            newMessageField.trailingAnchor.constraintEqualToAnchor(sendButton.leadingAnchor, constant: -10),
            sendButton.trailingAnchor.constraintEqualToAnchor(newMessageArea.trailingAnchor, constant: -10),
            
            newMessageField.centerYAnchor.constraintEqualToAnchor(newMessageArea.centerYAnchor),
            cameraButton.centerYAnchor.constraintEqualToAnchor(newMessageField.centerYAnchor),
            sendButton.centerYAnchor.constraintEqualToAnchor(newMessageField.centerYAnchor),
            newMessageArea.heightAnchor.constraintEqualToAnchor(newMessageField.heightAnchor, constant: 20)
        ]
        
        NSLayoutConstraint.activateConstraints(messageAreaConstraints)
        
        //Create Table for Chat Bubbles
        tableView.registerClass(MessageCell.self, forCellReuseIdentifier: cellIdentifier) //register ChatCell for reuse
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
    
    //Test action
    func someAction(button: UIButton) {
       print("test")
    }
    
    //Hides keyboard on tap (Not Used)
    func handleSingleTap(recongnizer: UITapGestureRecognizer) {
        view.endEditing(true)
    }
    
    
}

extension MessageViewController: UITableViewDataSource {
    
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

        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath: indexPath) as! MessageCell
        
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

extension MessageViewController: UITableViewDelegate {
    func tableView(tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        return false
    }
}



