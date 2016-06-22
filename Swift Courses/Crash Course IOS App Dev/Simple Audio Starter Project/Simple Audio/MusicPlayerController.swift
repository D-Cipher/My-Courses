//
//  ViewController.swift
//  Simple Audio
//
//  Created by Tingbo Chen on 5/4/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class MusicPlayerController: UIViewController {
    
    var shuffle = 1
    var loop = 0
    
    let lightBlueColor = UIColor(red: 0, green: 122/255, blue: 1, alpha: 1)
    
    @IBOutlet var scrubControlContainer: UIView!
    @IBOutlet var volumeControlContainer: UIView!
    @IBOutlet var mediaControlContainer: UIView!
    
    /*@IBOutlet var nameLabel: UILabel!*/
    @IBOutlet var scrubberOutlet: UISlider!
    @IBOutlet var volumeOutlet: UISlider!
    @IBOutlet var playButtonOutlet: UIButton!
    @IBOutlet var nextButtonOutlet: UIButton!
    @IBOutlet var backButtonOutlet: UIButton!
    @IBOutlet var shuffleButtonOutlet: UIButton!
    @IBOutlet var loopButtonOutlet: UIButton!
    
    @IBOutlet var durationLabel: UILabel!
    @IBOutlet var currentTimeLabel: UILabel!
    
    @IBAction func playButtonAction(sender: AnyObject) {
        
    }
    
    @IBAction func nextButtonAction(sender: AnyObject) {
        print("next")
    }
    
    
    @IBAction func backButtonAction(sender: AnyObject) {
        print("back")
    }
    
    
    @IBAction func shuffleButtonAction(sender: AnyObject) {
        if shuffle == 1 {
            shuffleButtonState(0)
            shuffle = 0
            
        } else if shuffle == 0 {
            shuffleButtonState(1)
            shuffle = 1
        }
        
    }
    
    @IBAction func loopButtonAction(sender: AnyObject) {
        if loop == 1 {
            loopButtonState(0)
            loop = 0
            
        } else if loop == 0 {
            loopButtonState(1)
            loop = 1
        }
    }
    
    @IBAction func scrubberAction(sender: AnyObject) {

    }
    
    @IBAction func volumeAction(sender: AnyObject) {

    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        ui_defaults()
        shuffleButtonState(1)
        loopButtonState(0)
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }
    
    private func ui_defaults() {
        
        //Border around containers
        let containers = [mediaControlContainer,scrubControlContainer]
        for container in containers {
            container.layer.borderWidth = 1
            container.layer.borderColor = UIColor.lightGrayColor().CGColor
        }
        
        //Button tinting
        let button_assets = ["Rewind Filled", "Fast Forward Filled", "Play Filled"]
        
        let button_iboutlet = [backButtonOutlet,nextButtonOutlet,playButtonOutlet]
        
        for (index, _) in button_assets.enumerate() {
            let origImg = UIImage(named: button_assets[index])!
            
            let tintedImg = origImg.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            
            button_iboutlet[index].setImage(tintedImg, forState: .Highlighted)
            button_iboutlet[index].tintColor = UIColor.grayColor()
        }
        
    }
    
    private func playButtonState(state: Int = 1) {
        
        var origImg_play = UIImage()
        
        if state == 0 {
            origImg_play = UIImage(named: "Pause Filled")!
            
        } else {
            origImg_play = UIImage(named: "Play Filled")!
        }
        
        let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
        playButtonOutlet.tintColor = UIColor.blackColor()
        
    }
    
    private func shuffleButtonState(state: Int = 1) {
        
        let origImg_shuffle = UIImage(named: "Shuffle")!
        let tintedImg_shuffle = origImg_shuffle.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        shuffleButtonOutlet.setImage(tintedImg_shuffle, forState: .Normal)
        shuffleButtonOutlet.tintColor = lightBlueColor
        
        if state == 0 {
            shuffleButtonOutlet.tintColor = UIColor.blackColor()
        }
        
    }
    
    private func loopButtonState(state: Int = 1) {
        let origImg_loop = UIImage(named: "Repeat")!
        let tintedImg_loop = origImg_loop.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        loopButtonOutlet.setImage(tintedImg_loop, forState: .Normal)
        loopButtonOutlet.tintColor = lightBlueColor
        
        if state == 0 {
            loopButtonOutlet.tintColor = UIColor.blackColor()
        }
    }

}

