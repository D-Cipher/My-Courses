//
//  ViewController.swift
//  Tab Bar Nav Controller
//
//  Created by Tingbo Chen on 2/22/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBAction func loginButton(sender: AnyObject) {
        performSegueWithIdentifier("loginSegue", sender: self)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    
    /*
    //Unwind Segue example function
    @IBAction func unwindSegue(segue: UIStoryboardSegue) {
    }
    */
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

