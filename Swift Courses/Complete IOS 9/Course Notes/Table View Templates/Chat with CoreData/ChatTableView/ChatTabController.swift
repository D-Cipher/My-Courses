//
//  ChatTabController.swift
//  Chat with CoreData
//
//  Created by Tingbo Chen on 4/9/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import CoreData

class ChatTabController: UIViewController {
    
    var context: NSManagedObjectContext?
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        
        let nav = segue.destinationViewController as! UINavigationController
        let msgVC = nav.topViewController as! MessageViewController
        
        msgVC.context = context
        
    }
    
}
