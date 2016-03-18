//
//  ProfileTabController.swift
//  ParseStarterProject
//
//  Created by Tingbo Chen on 2/16/16.
//  Copyright © 2016 Parse. All rights reserved.
//

import UIKit
import Parse

class ProfileTabController: UIViewController {
    
    @IBOutlet var profilePic: UIImageView!
    
    @IBOutlet var nameOutlet: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Gets information about the user from Facebook.
        let graphRequest = FBSDKGraphRequest(graphPath: "me", parameters: ["fields": "id, name, first_name, last_name, gender, locale"])
        
        graphRequest.startWithCompletionHandler { (connection, result, error) -> Void in
            if error != nil {
                print(error)
            } else if let result = result {
                
                dispatch_async(dispatch_get_global_queue(QOS_CLASS_BACKGROUND, 0)) { () -> Void in
                    
                    print(result)
                    
                    let query = PFQuery(className: "_User")
                    
                    query.getObjectInBackgroundWithId(PFUser.currentUser()!.objectId!, block: { (object, error) -> Void in
                        if error != nil {
                            print(error)
                            
                        } else if let object = object {
                            
                            PFUser.currentUser()?["gender"] = result["gender"]
                            PFUser.currentUser()?["name"] = result["name"]
                            
                            PFUser.currentUser()?.save()
                            
                            
                            let userID = result["id"] as! String
                            
                            let facebookProfilePictureUrl = "https://graph.facebook.com/" + userID + "/picture?type=large"
                            
                            if let fbpicUrl = NSURL(string: facebookProfilePictureUrl) {
                                if let data = NSData(contentsOfURL: fbpicUrl) {
                                    
                                    self.profilePic.image = UIImage(data: data)
                                    
                                    self.nameOutlet.text = result["first_name"] as? String
                                    
                                    //Save Image File to Parse
                                    let imageFile: PFFile = PFFile(data: data)
                                    PFUser.currentUser()?["image"] = imageFile
                                    PFUser.currentUser()?.save()
                                }
                            }
                        }
                    })
                
                }
                
            }
        }
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}
