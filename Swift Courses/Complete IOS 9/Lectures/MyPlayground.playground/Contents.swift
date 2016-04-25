import Foundation
import UIKit

func test(firstName: String) -> String {
    
    let first_char = firstName.characters.first
    var first_str = ""
    
    if first_char != nil {
        first_str = String(first_char!)
    } else {
        first_str = ""
    }
    
    let alphaNameTest = NSPredicate(format: "SELF MATCHES %@", "^([a-zA-Z])")
    
    let result = alphaNameTest.evaluateWithObject(first_str)
    
    guard result == true else {
        let symbol_str = "#"
        
        return symbol_str
    }
    
    let letter = firstName.characters.first
    
    let letter_str = String(letter!)
    
    return letter_str
}

test("Yan Yan")
