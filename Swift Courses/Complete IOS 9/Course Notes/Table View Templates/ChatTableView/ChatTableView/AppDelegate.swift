//
//  AppDelegate.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
        // Override point for customization after application launch.
        
        let vlight_grey = UIColor(red: 0.97, green: 0.95, blue: 0.95, alpha: 1.0)
        let col_blkchalk = UIColor(red: 35/255, green: 35/255, blue: 35/255, alpha: 1.0)
        
        //App Skin Customization
        UINavigationBar.appearance().barTintColor = col_blkchalk
        UINavigationBar.appearance().translucent = false
        UINavigationBar.appearance().titleTextAttributes = [NSForegroundColorAttributeName: UIColor.whiteColor()]
        UINavigationBar.appearance().tintColor = UIColor.whiteColor() //Nav bar back button to white
        UIBarButtonItem.appearance().tintColor = UIColor.whiteColor()
        UIApplication.sharedApplication().statusBarStyle = .LightContent //changes the status bar showing carrier, time, battery. Remember: add "View controller-based status bar appearance" to info.plist with Bool "No"
        UITabBar.appearance().barTintColor = vlight_grey
        UITabBar.appearance().tintColor = UIColor.greenColor()
        
        return true
    }

    func applicationWillResignActive(application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
    }

    func applicationDidEnterBackground(application: UIApplication) {
        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
    }

    func applicationWillEnterForeground(application: UIApplication) {
        // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
    }

    func applicationDidBecomeActive(application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillTerminate(application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
    }


}

