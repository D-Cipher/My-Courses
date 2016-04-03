//
//  ViewController.swift
//  Table View with Code
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    private let tableView = UITableView()
    
    private var messages = [Message]()
    
    private let cellIdentifier = "Cell"

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Add dummy data
        for i in 0...10 {
            let m = Message()
            m.text = String(i)
            messages.append(m)
        }
        
        //Create Table
        tableView.registerClass(UITableViewCell.self, forCellReuseIdentifier: cellIdentifier)
        tableView.dataSource = self
        tableView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(tableView)
        
        //Set tableView constraints
        let tableViewConstraints: [NSLayoutConstraint] = [
            
            tableView.topAnchor.constraintEqualToAnchor(view.topAnchor),
            tableView.leadingAnchor.constraintEqualToAnchor(view.leadingAnchor),
            tableView.trailingAnchor.constraintEqualToAnchor(view.trailingAnchor),
            tableView.bottomAnchor.constraintEqualToAnchor(view.bottomAnchor)
        
        ]
        
        NSLayoutConstraint.activateConstraints(tableViewConstraints)
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


extension ViewController: UITableViewDataSource {
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return messages.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentifier, forIndexPath:  indexPath)
        let message = messages[indexPath.row]
        cell.textLabel?.text = message.text
        return cell
    }
    
}
