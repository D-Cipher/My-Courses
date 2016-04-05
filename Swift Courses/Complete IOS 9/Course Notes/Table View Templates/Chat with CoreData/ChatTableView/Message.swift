//
//  Message.swift
//  Chat with CoreData
//
//  Created by Tingbo Chen on 4/5/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import Foundation
import CoreData


class Message: NSManagedObject {
    
    var isIncoming: Bool {
        get {
            guard let incoming = incoming else {return false}
            return incoming.boolValue
        }
        set(incoming) {
            self.incoming = incoming
            
        }
        
    }

}
