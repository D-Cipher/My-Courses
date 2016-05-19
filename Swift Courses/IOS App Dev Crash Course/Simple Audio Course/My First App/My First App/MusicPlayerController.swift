//
//  ViewController.swift
//  My First App
//
//  Created by Tingbo Chen on 5/4/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import AVFoundation

class MusicPlayerController: UIViewController {
    
    var av_player: AVAudioPlayer = AVAudioPlayer()
    
    var song_samples = ["Battle at the misty valley", "Twilight Poem", "Classical-bwv-bach"]
    
    var songNum = 0
    var shuffle = 1
    var loop = 0
    
    @IBOutlet var nameLabel: UILabel!
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
            
            playButtonOutlet.setTitle("Pause", forState: UIControlState.Normal)
            
            //print(av_player.duration)
            
        } else if av_player.playing == true {
            av_player.pause()
            
            playButtonOutlet.setTitle("Play", forState: UIControlState.Normal)
            
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
        if shuffleButtonOutlet.titleLabel?.text == "Shuffle" {
            
            shuffleButtonOutlet.setTitle("Unshuffle", forState: UIControlState.Normal)
            
            shuffle = 1
            
         } else if shuffleButtonOutlet.titleLabel?.text == "Unshuffle" {
            
            shuffleButtonOutlet.setTitle("Shuffle", forState: UIControlState.Normal)
            
            shuffle = 0
            
         }
    }
    
    @IBAction func loopButtonAction(sender: AnyObject) {
        //print("loop")
        if loopButtonOutlet.titleLabel?.text == "Loop" {
            loopButtonOutlet.setTitle("Unloop", forState: UIControlState.Normal)
            loop = 1
        } else if loopButtonOutlet.titleLabel?.text == "Unloop" {
            loopButtonOutlet.setTitle("Loop", forState: UIControlState.Normal)
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
        
        nameLabel.text = song_samples[songNum]
        
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
            playButtonOutlet.setTitle("Pause", forState: UIControlState.Normal)
        } else if av_player.playing == false {
            playButtonOutlet.setTitle("Play", forState: UIControlState.Normal)
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
        
        avPlyr_init()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

}
