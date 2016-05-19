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
    
    var av_plyr: AVAudioPlayer = AVAudioPlayer()
    
    @IBOutlet var scrubControlContainer: UIView!
    @IBOutlet var volumeControlContainer: UIView!
    @IBOutlet var mediaControlContainer: UIView!
    
    
    var av_player: AVAudioPlayer = AVAudioPlayer()
    
    var song_samples = ["Battle at the misty valley", "Twilight Poem", "Classical-bwv-bach"]
    
    var songNum = 0
    var shuffle = 1
    var loop = 0
    
    //@IBOutlet var nameLabel: UILabel!
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
        //print("play")
        
        if av_player.playing == false {
            av_player.play()
            
            //playButtonOutlet.setTitle("Pause", forState: UIControlState.Normal)
            
            let origImg_play = UIImage(named: "Pause Filled")!
            let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
            playButtonOutlet.tintColor = UIColor.darkGrayColor()
            
        } else if av_player.playing == true {
            av_player.pause()
            
            //playButtonOutlet.setTitle("Play", forState: UIControlState.Normal)
            
            let origImg_play = UIImage(named: "Play Filled")!
            let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
            playButtonOutlet.tintColor = UIColor.darkGrayColor()
            
        }
        
        /*
         if playButtonOutlet.titleLabel?.text == "Play" {
         playButtonOutlet.setTitle("Pause", forState: UIControlState.Normal)
         } else if playButtonOutlet.titleLabel?.text == "Pause" {
         playButtonOutlet.setTitle("Play", forState: UIControlState.Normal)
         }*/
        
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
        //print("shuffle")
        if shuffle == 0 {
            
            //shuffleButtonOutlet.setTitle("Unshuffle", forState: UIControlState.Normal)
            
            let origImg_shuffle = UIImage(named: "Shuffle")!
            let tintedImg_shuffle = origImg_shuffle.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            shuffleButtonOutlet.setImage(tintedImg_shuffle, forState: .Normal)
            shuffleButtonOutlet.tintColor = UIColor.blackColor()
            
            shuffle = 1
            
        } else if shuffle == 1 {
            
            //shuffleButtonOutlet.setTitle("Shuffle", forState: UIControlState.Normal)
            
            let origImg_shuffle = UIImage(named: "Shuffle")!
            let tintedImg_shuffle = origImg_shuffle.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            shuffleButtonOutlet.setImage(tintedImg_shuffle, forState: .Normal)
            shuffleButtonOutlet.tintColor = UIColor.darkGrayColor()
            
            shuffle = 0
            
        }
    }
    
    @IBAction func loopButtonAction(sender: AnyObject) {
        //print("loop")
        if loop == 0 {
            //loopButtonOutlet.setTitle("Unloop", forState: UIControlState.Normal)
            let origImg_loop = UIImage(named: "Repeat")!
            let tintedImg_loop = origImg_loop.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            loopButtonOutlet.setImage(tintedImg_loop, forState: .Normal)
            loopButtonOutlet.tintColor = UIColor.blackColor()
            
            loop = 1
        } else if loop == 1 {
            //loopButtonOutlet.setTitle("Loop", forState: UIControlState.Normal)
            let origImg_loop = UIImage(named: "Repeat")!
            let tintedImg_loop = origImg_loop.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            loopButtonOutlet.setImage(tintedImg_loop, forState: .Normal)
            loopButtonOutlet.tintColor = UIColor.darkGrayColor()
            
            loop = 0
        }
    }
    
    @IBAction func scrubberAction(sender: AnyObject) {
        av_player.currentTime = Double(scrubberOutlet.value) * (av_player.duration)
    }
    
    @IBAction func volumeAction(sender: AnyObject) {
        av_player.volume = volumeOutlet.value
    }
    
    
    func avPlyr_init() {
        
        //nameLabel.text = song_samples[songNum]
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
            //playButtonOutlet.setTitle("Pause", forState: UIControlState.Normal)
            let origImg_play = UIImage(named: "Pause Filled")!
            let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
            playButtonOutlet.tintColor = UIColor.darkGrayColor()
        } else if av_player.playing == false {
            //playButtonOutlet.setTitle("Play", forState: UIControlState.Normal)
            let origImg_play = UIImage(named: "Play Filled")!
            let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
            playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
            playButtonOutlet.tintColor = UIColor.darkGrayColor()
        }
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
    
    func nextSong() {
        
        if shuffle == 0 {
            songNum = (songNum + 1)%song_samples.count
        } else if shuffle == 1 {
            let songNum_og = songNum
            
            while songNum_og == songNum {
                
                let randomNum = arc4random_uniform(UInt32(song_samples.count))
                
                songNum = Int(randomNum)
            }
        }
        
        if av_player.playing == false {
            avPlyr_init()
            av_player.pause()
        } else if av_player.playing == true {
            avPlyr_init()
            av_player.play()
        }
        
        av_player.volume = volumeOutlet.value
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Border around containers
        let containers = [mediaControlContainer,scrubControlContainer]
        for container in containers {
            container.layer.borderWidth = 1
            container.layer.borderColor = UIColor.lightGrayColor().CGColor
        }
        
        avPlyr_init()
        
        //Initiate buttons:
        let origImg_rewind = UIImage(named: "Rewind Filled")!
        let tintedImg_rewind = origImg_rewind.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        backButtonOutlet.setImage(tintedImg_rewind, forState: .Normal)
        backButtonOutlet.tintColor = UIColor.darkGrayColor()
        let origImg_fastf = UIImage(named: "Fast Forward Filled")!
        let tintedImg_fastf = origImg_fastf.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        nextButtonOutlet.setImage(tintedImg_fastf, forState: .Normal)
        nextButtonOutlet.tintColor = UIColor.darkGrayColor()
        let origImg_play = UIImage(named: "Play Filled")!
        let tintedImg_play = origImg_play.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        playButtonOutlet.setImage(tintedImg_play, forState: .Normal)
        playButtonOutlet.tintColor = UIColor.darkGrayColor()
        let origImg_shuffle = UIImage(named: "Shuffle")!
        let tintedImg_shuffle = origImg_shuffle.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        shuffleButtonOutlet.setImage(tintedImg_shuffle, forState: .Normal)
        shuffleButtonOutlet.tintColor = UIColor.blackColor()
        let origImg_loop = UIImage(named: "Repeat")!
        let tintedImg_loop = origImg_loop.imageWithRenderingMode(UIImageRenderingMode.AlwaysTemplate)
        loopButtonOutlet.setImage(tintedImg_loop, forState: .Normal)
        loopButtonOutlet.tintColor = UIColor.darkGrayColor()
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }


}

