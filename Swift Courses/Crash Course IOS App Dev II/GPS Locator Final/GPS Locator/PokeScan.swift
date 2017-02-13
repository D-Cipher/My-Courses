//
//  ViewController.swift
//  GPS Locator
//
//  Created by Tingbo Chen on 7/30/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

//NOTE: PokeScan no longer works because Niantic has closed it's pokemon API.

import UIKit

/*
 
 Note - To allow for http requests add in Info.plist:
 
 1) Add the following:
 App Transport Security Settings {Type: Dictionary}
 
 2) Add under the App Transport Security Settings:
 Allow Arbitrary Loads {Type: Boolean} {Value: Yes}
 
 */

class PokeScan: UIViewController {

    @IBOutlet var webView: UIWebView!
    
    @IBAction func backButton(sender: AnyObject) {
        
        dismissViewControllerAnimated(true, completion: nil)
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let url = NSURL(string: "https://ipoke.herokuapp.com")!
        
        //Simple Display Web Content
        webView.loadRequest(NSURLRequest(URL: url))
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        
    }

}
