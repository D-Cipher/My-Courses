//
//  ChatCell.swift
//  ChatTableView
//
//  Created by Tingbo Chen on 4/2/16.
//  Copyright © 2016 Tingbo Chen. All rights reserved.
//

import UIKit

class ChatCell: UITableViewCell {
    
    let messageLabel: UILabel = UILabel()
    private let bubbleImageView = UIImageView()
    
    private var outgoingConstraints: [NSLayoutConstraint]!
    private var incomingConstraints: [NSLayoutConstraint]!
    
    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        bubbleImageView.translatesAutoresizingMaskIntoConstraints = false
        contentView.addSubview(bubbleImageView)
        bubbleImageView.addSubview(messageLabel)
        
        
        //Set Constraints
        messageLabel.centerXAnchor.constraintEqualToAnchor(bubbleImageView.centerXAnchor).active = true
        messageLabel.centerYAnchor.constraintEqualToAnchor(bubbleImageView.centerYAnchor).active = true
        
        bubbleImageView.widthAnchor.constraintEqualToAnchor(messageLabel.widthAnchor, constant: 40).active = true
        bubbleImageView.heightAnchor.constraintEqualToAnchor(messageLabel.heightAnchor, constant: 20).active = true
        
        outgoingConstraints = [
            bubbleImageView.trailingAnchor.constraintEqualToAnchor(contentView.trailingAnchor, constant: -25),
            bubbleImageView.leadingAnchor.constraintGreaterThanOrEqualToAnchor(contentView.leadingAnchor, constant: 70)
        ]
        
        incomingConstraints = [
            bubbleImageView.leadingAnchor.constraintEqualToAnchor(contentView.leadingAnchor, constant: 25),
            bubbleImageView.trailingAnchor.constraintLessThanOrEqualToAnchor(contentView.trailingAnchor, constant: -70)
        ]
        
        bubbleImageView.topAnchor.constraintEqualToAnchor(contentView.topAnchor, constant: 10).active = true
        bubbleImageView.bottomAnchor.constraintEqualToAnchor(contentView.bottomAnchor, constant: -10).active = true
        
        messageLabel.textAlignment = .Center
        messageLabel.numberOfLines = 0
        
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func incoming(incoming: Bool) {
        if incoming == true {
            NSLayoutConstraint.deactivateConstraints(outgoingConstraints) //Note: deactivate before activate
            NSLayoutConstraint.activateConstraints(incomingConstraints)
            
            bubbleImageView.image = makeBubble().incoming
            
        } else if incoming == false {
            NSLayoutConstraint.deactivateConstraints(incomingConstraints) //Note: deactivate before activate
            NSLayoutConstraint.activateConstraints(outgoingConstraints)
            
            bubbleImageView.image = makeBubble().outgoing
        }
    }
    
    //Make Chat Bubbles
    func makeBubble() -> (incoming: UIImage, outgoing: UIImage) {
        
        let image = UIImage(named: "MessageBubble")!
        let flippedImage = UIImage(CGImage: image.CGImage!, scale: image.scale, orientation: UIImageOrientation.UpMirrored)
        
        let insetsOutgoing  = UIEdgeInsets(top: 17, left: 21, bottom: 17.5, right: 26.5)
        let insetsIncoming = UIEdgeInsets(top: 17, left: 26.5, bottom: 17.5, right: 21)
        
        let outgoing = coloredImage(image, red: 0/255, green: 122/255, blue: 255/255, alpha: 1).resizableImageWithCapInsets(insetsOutgoing)
        let incoming = coloredImage(flippedImage, red: 229/255, green: 229/255, blue: 229/255, alpha: 1).resizableImageWithCapInsets(insetsIncoming)
        
        return (incoming, outgoing)
    }
    func coloredImage(image: UIImage, red:CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> UIImage! {
        
        let rect = CGRect(origin: CGPointZero, size: image.size)
        UIGraphicsBeginImageContextWithOptions(image.size, false, image.scale)
        
        let context = UIGraphicsGetCurrentContext()
        image.drawInRect(rect)
        
        CGContextSetRGBFillColor(context, red, green, blue, alpha)
        CGContextSetBlendMode(context,CGBlendMode.SourceAtop)
        CGContextFillRect(context, rect)
        
        let result = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return result
    }
    
}


