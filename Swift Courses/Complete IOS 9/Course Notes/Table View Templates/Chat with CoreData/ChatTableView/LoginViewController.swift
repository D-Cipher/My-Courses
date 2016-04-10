//
//  LoginViewController.swift
//  Chat with CoreData
//
//  Created by Tingbo Chen on 4/7/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import CoreData

class LoginViewController: UIViewController {
    
    var context: NSManagedObjectContext?

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        
        let tab = segue.destinationViewController as! UITabBarController
        let nav = tab.viewControllers![0] as! UINavigationController
        let chatTabVC = nav.topViewController as! ChatTabController
        
        chatTabVC.context = context

    }
    
}
