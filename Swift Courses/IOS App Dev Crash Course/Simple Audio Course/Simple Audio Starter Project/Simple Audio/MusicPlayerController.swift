//
//  ViewController.swift
//  Simple Audio
//
//  Created by Tingbo Chen on 5/4/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class MusicPlayerController: UIViewController {
    
    @IBOutlet var scrubControlContainer: UIView!
    @IBOutlet var volumeControlContainer: UIView!
    @IBOutlet var mediaControlContainer: UIView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Border around containers
        let containers = [mediaControlContainer,scrubControlContainer]
        for container in containers {
            container.layer.borderWidth = 1
            container.layer.borderColor = UIColor.lightGrayColor().CGColor
        }
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }


}

