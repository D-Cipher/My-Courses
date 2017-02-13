//
//  ViewController.swift
//  Web Content
//
//  Created by Tingbo Chen on 1/4/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

/*

Note - To allow for http requests add in Info.plist:

1) Add the following:
App Transport Security Settings {Type: Dictionary}

2) Add under the App Transport Security Settings:
Allow Arbitrary Loads {Type: Boolean} {Value: Yes}

*/

import UIKit

class ViewController: UIViewController {

    @IBOutlet var webView: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let url = NSURL(string: "https://ipoke.herokuapp.com")!
        
        //Simple Display Web Content
        webView.loadRequest(NSURLRequest(URL: url))
        
        /* //Loading Content and displaying it
        
        let task = NSURLSession.sharedSession().dataTaskWithURL(url) { (data, response, error) -> Void in
            //Completion handler. Creates a session and fetch the URL. Run a code when task completes.
            
            if let urlContent = data { //Checking if data exists
                
                let webContent = NSString(data: urlContent, encoding: NSUTF8StringEncoding) //Decode message
                
                //print(webContent) //prints the html
                dispatch_async(dispatch_get_main_queue(), { () -> Void in
                        self.webView.loadHTMLString(String(webContent!), baseURL: nil)
                }) //displays the content into webView
                
                
            } else {
                //Show an error message
            }
        }
        
        task.resume()

    */
        
    }


    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }


}

