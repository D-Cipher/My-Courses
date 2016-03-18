//
//  ChatTabController.swift
//  Firebase Starter Project
//
//  Created by Tingbo Chen on 3/16/16.
//  Copyright © 2016 Parse. All rights reserved.
//

import UIKit
import Firebase
import Social

class ChatTabController: UIViewController {
    
    let firebase = Firebase(url: "https://crackling-inferno-3276.firebaseio.com/")

    override func viewDidLoad() {
        super.viewDidLoad()

        //Read from firebase
        firebase.observeEventType(FEventType.Value) { (snapshot: FDataSnapshot!) -> Void in
            
            print(snapshot.value)
            //self.firebase.setValue("Computer says no")
        }
        
        //Write value to firebase
        firebase.setValue("you too")
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
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
