//
//  Message+CoreDataProperties.swift
//  Chat with CoreData
//
//  Created by Tingbo Chen on 4/5/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//
//  Choose "Create NSManagedObject Subclass…" from the Core Data editor menu
//  to delete and recreate this implementation file for your updated model.
//

import Foundation
import CoreData

extension Message {

    @NSManaged var text: String?
    @NSManaged var incoming: NSNumber?
    @NSManaged var timestamp: NSDate?

}
