//
//  TableViewController.swift
//  Static Table Images
//
//  Created by Tingbo Chen on 3/13/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class TableViewController: UITableViewController {
    
    @IBOutlet var bgImageOutlet: UIImageView!
    
    @IBOutlet var profileImageOutlet: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.tableView.separatorStyle = UITableViewCellSeparatorStyle.None
        
        //Round out corner of images
        profileImageOutlet.layer.masksToBounds = true
        profileImageOutlet.layer.cornerRadius = CGRectGetWidth(self.profileImageOutlet.frame)/6.0
        
        profileImageOutlet.layer.borderWidth = 5
        profileImageOutlet.layer.borderColor = UIColor.whiteColor().CGColor
        
        //Set background image
        bgImageOutlet.image = UIImage(named: "blacktexture.png")
        bgImageOutlet.layer.masksToBounds = true
        bgImageOutlet.contentMode = .ScaleAspectFill
        
        /*
        //create blur effect
        let visualEffectView = UIVisualEffectView(effect: UIBlurEffect(style: .Light)) as UIVisualEffectView
        visualEffectView.frame = bgImageOutlet.bounds
        visualEffectView.autoresizingMask = [.FlexibleWidth, .FlexibleHeight]
        visualEffectView.alpha = 0.6
        bgImageOutlet.addSubview(visualEffectView)
        */
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source
    
    override func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
        if indexPath.section == 0 && indexPath.row == 0 {
            return view.frame.height * (207/736)
        }
        else {
            return 80
        }
    }
    
    
    /*
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 0
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return 0
    }
    */
    /*
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("reuseIdentifier", forIndexPath: indexPath)

        // Configure the cell...

        return cell
    }
    */

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
