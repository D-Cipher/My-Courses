import UIKit

let stripped_number = "12312312342"

if stripped_number.characters.count == 10 {
    let stringts: NSMutableString = NSMutableString(string: stripped_number)
    stringts.insertString("-", atIndex: 3)
    stringts.insertString("-", atIndex: 7)
    let formatted_phoneNum = String(stringts)
    print(formatted_phoneNum)
} else {
    let formatted_phoneNum = "number"
    print(formatted_phoneNum)
}

