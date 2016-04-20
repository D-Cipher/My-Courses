import UIKit

func validate(value: String) -> Bool {
    
    let PHONE_REGEX = "^\\d{3}\\d{3}\\d{4}$"
    
    var phoneTest = NSPredicate(format: "SELF MATCHES %@", PHONE_REGEX)
    
    var result =  phoneTest.evaluateWithObject(value)
    
    return result
    
}

validate("3148073944")
