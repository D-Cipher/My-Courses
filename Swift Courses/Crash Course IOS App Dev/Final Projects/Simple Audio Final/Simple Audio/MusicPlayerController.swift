//
//  ViewController.swift
//  Simple Audio
//
//  Created by Tingbo Chen on 5/4/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import AVFoundation

class MusicPlayerController: UIViewController {
    
    var av_player: AVAudioPlayer = AVAudioPlayer()
    
    var song_samples = ["Battle at the misty valley", "Twilight Poem", "Dawn of a New Era", "Classical-bwv-bach", "Breath of Freedom", "High Hopes",
                        "Intro-Sonet", "Neverending Dream", "Path of Loneliness", "The silent Force"]
    
    var songNum = 0

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
        
        if av_player.playing == false {
            av_player.play()
            
            playButtonState(0)
            
            //print(av_player.duration)
            
        } else if av_player.playing == true {
            av_player.pause()
            
            playButtonState(1)
            
        }

    }
    
    @IBAction func nextButtonAction(sender: AnyObject) {
        //print("next")
        nextSong()
        
        
    }
    
    
    @IBAction func backButtonAction(sender: AnyObject) {
        //print("back")
        if songNum == 0 {
            songNum = song_samples.count - 1
        } else {
            songNum = (songNum - 1)%song_samples.count
        }
        
        //print(songNum)
        
        if av_player.playing == false {
            avPlyr_init()
            av_player.pause()
        } else if av_player.playing == true {
            avPlyr_init()
            av_player.play()
        }
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
        av_player.currentTime = Double(scrubberOutlet.value) * (av_player.duration)
    }
    
    @IBAction func volumeAction(sender: AnyObject) {
        av_player.volume = volumeOutlet.value
    }
    
    func avPlyr_init() {
        
        /*nameLabel.text = song_samples[songNum]*/
        navigationController?.navigationBar.topItem?.title = song_samples[songNum]
        
        //Create a path to the mp3 player
        let audioPath = NSBundle.mainBundle().pathForResource(song_samples[songNum], ofType: "mp3")!
        
        do {
            try av_player = AVAudioPlayer(contentsOfURL: NSURL(fileURLWithPath: audioPath))
            
        } catch {
            print("error")
        }
        
        let timer = NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: Selector("updateScrubSlider"), userInfo: nil, repeats: true)
        
    }
    
    func updateScrubSlider(){
        scrubberOutlet.value = Float(av_player.currentTime/(av_player.duration))
        //print(scrubberOutlet.value)
        
        currentTimeLabel.text = hsmConverter(Int(av_player.currentTime)).1 + ":" + hsmConverter(Int(av_player.currentTime)).2
        
        durationLabel.text = hsmConverter(Int(av_player.duration)).1 + ":" + hsmConverter(Int(av_player.duration)).2
        
        if scrubberOutlet.value >= 0.99 {
            
            if loop == 1 {
                av_player.currentTime = 0
                av_player.play()
            } else if loop == 0{
                nextSong()
            }
            
        }
        
        if av_player.playing == true {
            playButtonState(0)
            
            
        } else if av_player.playing == false {
            playButtonState(1)
        }
    }
    
    func nextSong() {
        
        //Determines what the next song is
        if shuffle == 0 {
            songNum = (songNum + 1)%song_samples.count
        } else if shuffle == 1 {
            let songNum_og = songNum
            
            while songNum_og == songNum {
                
                let randomNum = arc4random_uniform(UInt32(song_samples.count))
                
                songNum = Int(randomNum)
            }
        }
        
        //Determines whether to play the next song
        if av_player.playing == false {
            avPlyr_init()
            av_player.pause()
        } else if av_player.playing == true {
            avPlyr_init()
            av_player.play()
        }
        av_player.volume = volumeOutlet.value
    }
    
    func hsmConverter (seconds : Int) -> (String, String, String) {
        let hr = String(seconds / 3600)
        
        let min = String((seconds % 3600) / 60)
        
        let sec = (seconds % 3600) % 60
        
        var sec_formatted = "00"
        
        if sec <= 9 {
            sec_formatted = "0" + String(sec)
        } else {
            sec_formatted = String(sec)
        }
        return (hr, min, sec_formatted)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        ui_defaults()
        shuffleButtonState(1)
        loopButtonState(0)
        
        avPlyr_init()
        
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

