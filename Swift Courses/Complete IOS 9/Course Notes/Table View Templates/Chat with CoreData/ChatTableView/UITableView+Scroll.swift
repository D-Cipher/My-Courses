//
//  UITableView+Scroll.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/3/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import Foundation
import UIKit

extension UITableView {
    func scrollToBottom(animation: Bool) {
        
        if self.numberOfSections > 1 {
            
            let lastSection = self.numberOfSections - 1
            
            self.scrollToRowAtIndexPath(NSIndexPath(forRow: self.numberOfRowsInSection(lastSection)-1, inSection: lastSection), atScrollPosition: .Bottom, animated: animation) //Scrolls to the bottom of table
            
        } else if numberOfRowsInSection(0) > 0 && self.numberOfSections == 1 {
            
            self.scrollToRowAtIndexPath(NSIndexPath(forRow: self.numberOfRowsInSection(0)-1, inSection: 0), atScrollPosition: .Bottom, animated: animation) //Scrolls to the bottom of table
        
        }
    }
}
