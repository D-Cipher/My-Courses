//
//  ProfileViewController.swift
//  Tab Bar Nav Controller
//
//  Created by Tingbo Chen on 2/22/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ProfileViewController: UIViewController {

    @IBAction func editButton(sender: AnyObject) {///////
        performSegueWithIdentifier("editProfileSegue", sender: self)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
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
