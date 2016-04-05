//
//  CDHelper.swift
//  CoreDataStack
//
//  Created by Matthew Parker on 8/14/15.
//  Copyright © 2015 BitFountain. All rights reserved.
//

import Foundation
import CoreData

class CDHelper {
    
    static let sharedInstance = CDHelper()
    
    
    lazy var storesDirectory: NSURL = {
        
        //An NSFileManager object lets you examine the contents of the file system and make changes to it. A file manager object is usually your first interaction with the file system. You use it to locate, create, copy, and move files and directories. You also use it to get information about a file or directory or change some of its attributes.
        //Returns the shared file manager object for the process.
        //This method always returns the same file manager object. If you plan to use a delegate with the file manager to receive notifications about the completion of file-based operations, you should create a new instance of NSFileManager (using the init method) rather than using the shared object.

        let fm = NSFileManager.defaultManager()
        
        //Returns an array of URLs for the specified common directory in the requested domains.
        // NSSearchPathDirectory: These constants specify the location of a variety of directories by the URLsForDirectory:inDomains: and URLForDirectory:inDomain:appropriateForURL:create:error: NSFileManager methods.
        // DocumentDirectory
        
        // NSSearchPathDomainMask: Search path domain constants specifying base locations for the NSSearchPathDirectory type. These constants are used by the URLsForDirectory:inDomains: and URLForDirectory:inDomain:appropriateForURL:create:error: NSFileManager methods.
        // user’s home directory = .DocumentDirectory
        
        let urls = fm.URLsForDirectory(.DocumentDirectory, inDomains: .UserDomainMask)
        return urls[urls.count-1] as NSURL
        }()
    
    //Returns a new URL made by appending a path component to the original URL.
    lazy var localStoreURL: NSURL = {
        let url = self.storesDirectory.URLByAppendingPathComponent("Chat with CoreData.sqlite")
        return url
        }()
    
    //1 An NSURL object represents a URL that can potentially contain the location of a resource on a remote server, the path of a local file on disk, or even an arbitrary piece of encoded data.
    
    lazy var modelURL: NSURL = {
        
        //An NSBundle object represents a location in the file system that groups code and resources that can be used in a program. NSBundle objects locate program resources, dynamically load and unload executable code, and assist in localization. You build a bundle in Xcode using one of these project types: Application, Framework, plug-ins. Availability
        // mainBundle - Returns the NSBundle object that corresponds to the directory where the current application executable is located.
        //This method allocates and initializes a bundle object if one doesn’t already exist. The new object corresponds to the directory where the application executable is located. Be sure to check the return value to make sure you have a valid bundle. This method may return a valid bundle object even for unbundled applications.

        let bundle = NSBundle.mainBundle()
        
        //Returns the file URL for the resource identified by the specified name and file extension.
        
        if let url = bundle.URLForResource("Model", withExtension: "momd") {
            return url
        }
        print("CRITICAL - Managed Object Model file not found")
        
        abort()
        }()
    
    //2 An NSManagedObjectModel object describes a schema—a collection of entities (data models) that you use in your application.
    lazy var model: NSManagedObjectModel = {
        return NSManagedObjectModel(contentsOfURL:self.modelURL)!
        }()
    
    //Instances of NSPersistentStoreCoordinator associate persistent stores (by type) with a model (or more accurately, a configuration of a model) and serve to mediate between the persistent store or stores and the managed object context or contexts. Instances of NSManagedObjectContext use a coordinator to save object graphs to persistent storage and to retrieve model information. A context without a coordinator is not fully functional as it cannot access a model except through a coordinator. The coordinator is designed to present a façade to the managed object contexts such that a group of persistent stores appears as an aggregate store. A managed object context can then create an object graph based on the union of all the data stores the coordinator covers.
    
    lazy var coordinator: NSPersistentStoreCoordinator = {
        
        //The NSPersistentStoreCoordinator is the true maestro of Core Data. The NSPersistentStoreCoordinator is responsible for persisting, loading, and caching data. Think of the NSPersistentStoreCoordinator as the heart of Core Data. Having said this, we do very little work with the NSPersistentStoreCoordinator directly. We work with it upon initialization, but we almost never touch it again over the life of the application.
        
        let coordinator = NSPersistentStoreCoordinator(managedObjectModel: self.model)
        
        
        //Adds a new persistent store of a specified type at a given location, and returns the new store.
        //The SQLite database store type.
        
        do {
            try coordinator.addPersistentStoreWithType(NSSQLiteStoreType, configuration: nil, URL: self.localStoreURL, options: nil)
        } catch {
            print("Could not add the peristent store")
            abort()
        }
        
        return coordinator
        }()
}