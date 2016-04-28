/*
* Copyright (c) 2015 Razeware LLC
* https://www.raywenderlich.com/122148/firebase-tutorial-real-time-chat
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
*/

import UIKit
import Firebase

class LoginViewController: UIViewController {
  
  // MARK: Properties
  var ref: Firebase!
  
  override func viewDidLoad() {
    super.viewDidLoad()
    ref = Firebase(url: "https://crackling-inferno-3276.firebaseio.com")
  }

  @IBAction func loginDidTouch(sender: AnyObject) {
    ref.authAnonymouslyWithCompletionBlock { (error, authData) in
      if error != nil { print(error.description); return }
      self.performSegueWithIdentifier("LoginToChat", sender: nil)
    }
  }
  
  override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
    super.prepareForSegue(segue, sender: sender)
    let navVc = segue.destinationViewController as! UINavigationController
    let chatVc = navVc.viewControllers.first as! ChatViewController
    chatVc.senderId = ref.authData.uid
    chatVc.senderDisplayName = ""
  }
  
}

