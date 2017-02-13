//
//  ViewController.swift
//  My First App
//
//  Created by Tingbo Chen on 6/8/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController {

    var av_player: AVAudioPlayer = AVAudioPlayer()
    
    var song_samples = ["Battle at the misty valley", "Path of Loneliness", "Breath of Freedom", "Classical-bwv-bach", "Dawn of a New Era", "High Hopes", "Twilight Poem"]
    
    var trackNum = 0
    var shuffle = 1
    var loop = 0
    
    @IBOutlet var songLabel: UILabel!
    
    @IBOutlet var playButtonOutlet: UIButton!
    
    @IBOutlet var nextButtonOutlet: UIButton!
    
    @IBOutlet var backButtonOutlet: UIButton!
    
    @IBOutlet var scrubberOutlet: UISlider!
    
    @IBOutlet var volumeScrollOutlet: UISlider!
    
    @IBOutlet var loopButtonOutlet: UIButton!
    
    @IBOutlet var shuffleButtonOutlet: UIButton!
    
    @IBOutlet var currentTimeLabel: UILabel!
    
    @IBOutlet var durationLabel: UILabel!
    
    @IBAction func playButtonAction(sender: AnyObject) {
        
        if playButtonOutlet.titleLabel?.text == "Play" {
            
            av_player.play()
            
            playButtonOutlet.setTitle("Pause", forState: .Normal)
            
        } else if playButtonOutlet.titleLabel?.text == "Pause" {
            
            av_player.pause()
            
            playButtonOutlet.setTitle("Play", forState: .Normal)
        }
        
    }
    
    @IBAction func nextButtonAction(sender: AnyObject) {
        nextSong()
    }

    @IBAction func backButtonAction(sender: AnyObject) {
        
        if trackNum == 0 {
            
            trackNum = song_samples.count - 1
        } else {
            
           trackNum = (trackNum - 1) % song_samples.count
        }
        
        if av_player.playing == false {
            
            avPlyr_init(trackNum)
            av_player.pause()
            
        } else if av_player.playing == true {
            
            avPlyr_init(trackNum)
            av_player.play()
        }
        
        av_player.volume = volumeScrollOutlet.value
        
    }
    
    @IBAction func scrubberAction(sender: AnyObject) {
        
        av_player.currentTime = Double(scrubberOutlet.value) * av_player.duration

        
    }

    @IBAction func volumeScrollAction(sender: AnyObject) {
        
        av_player.volume = volumeScrollOutlet.value
        
    }
    
    
    @IBAction func loopButtonAction(sender: AnyObject) {
        
        if loopButtonOutlet.titleLabel?.text == "Loop" {
            
            loopButtonOutlet.setTitle("Unloop", forState: .Normal)
            
            loop = 1
            
        } else if loopButtonOutlet.titleLabel?.text == "Unloop" {
            
            loopButtonOutlet.setTitle("Loop", forState: .Normal)
            
            loop = 0
        }
        
    }

    
    @IBAction func shuffleButtonAction(sender: AnyObject) {
        
        if shuffleButtonOutlet.titleLabel?.text == "Shuffle" {
            
            shuffleButtonOutlet.setTitle("Unshuffle", forState: .Normal)
            
            shuffle = 1
            
        } else if shuffleButtonOutlet.titleLabel?.text == "Unshuffle" {
            
            shuffleButtonOutlet.setTitle("Shuffle", forState: .Normal)
            
            shuffle = 0
        }
        
    }
    
    func avPlyr_init(songNum: Int = 0) {
        
        songLabel.text = song_samples[songNum]
        
        let audioPath = NSBundle.mainBundle().pathForResource(song_samples[songNum], ofType: "mp3")
        
        do {
            try av_player = AVAudioPlayer(contentsOfURL: NSURL(fileURLWithPath: audioPath!))
        } catch {
            print("error")
        }
        
        let timer = NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: Selector("updateScrubSlider"), userInfo: nil, repeats: true)
        
    }
    
    func updateScrubSlider() {
        
        scrubberOutlet.value = Float(av_player.currentTime / av_player.duration)
        
        currentTimeLabel.text = hsmConverter(Int(av_player.currentTime)).1 + ":" + hsmConverter(Int(av_player.currentTime)).2
        
        durationLabel.text = hsmConverter(Int(av_player.duration)).1 + ":" + hsmConverter(Int(av_player.duration)).2
        
        if av_player.currentTime / av_player.duration >= 0.99 {
            
            if loop == 1 {
                av_player.currentTime = 0
                av_player.play()
                
            } else if loop == 0 {
                nextSong()
            }
            
            
            
        }
        
        
    }
    
    func nextSong() {
        
        if shuffle == 0 {
            trackNum = (trackNum + 1) % song_samples.count
            
        } else if shuffle == 1 {
            
            let trackNum_og = trackNum
            
            while trackNum_og == trackNum {
                let randomNum = arc4random_uniform(UInt32(song_samples.count))
                
                trackNum = Int(randomNum)
            }
            
        }
        
        
        if av_player.playing == false {
            avPlyr_init(trackNum)
            av_player.pause()
        } else if av_player.playing == true {
            avPlyr_init(trackNum)
            av_player.play()
        }
        
        av_player.volume = volumeScrollOutlet.value
        
    }
    
    func hsmConverter(seconds: Int) -> (String, String, String) {
        
        let hr = String(seconds / 3600)
        
        let min = String((seconds % 3600) / 60)
        
        let sec = (seconds % 3600) % 60
        
        var sec_formatted = "00"
        
        if sec <= 9 {
            
            sec_formatted = "0" + String(sec)
            
        } else {
            
            sec_formatted = String(sec)
        }
        
        return(hr, min, sec_formatted)
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        avPlyr_init(0)
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

    }


}

