## Section 1a: Getting Started, Variables

### Overview of Programming

Programming, specifically high-level programming, is using language that is more like human language which is then translated to machine language through an interpreter or compiler for the computer to understand. (example: Python)

Commenting -> In python, # means comment.

Block Commenting -> Python actually does not have this, but... """.

### Basic Variables
Variable -> A store of information, a piece of data we want the computer to hold on to.

Three basic types: String, Int, Float, Bool,

Strings:
```
phoneNumber = '323-232-2131'

countryCode = '+1'

countryName = 'United States'
```

Integers and Floats:
```
chocolateBars = 100

gummyWorms = 200

totalCandy = chocolateBars + gummyWorms

print(totalCandy)

grams = 20.0

testType = type(candyGrams)
```

Basic Math:
```
gramsHalf = grams / 2

gramsDoubled = grams * 2

gummyWorms = gummyWorms + 1

gummyWorms += 1

number = 7
mod2 = number % 2
print(mod2)
```

Basic Conversions:
```
phoneNumber = countryCode + '-' + phoneNumber

totalChocolates = 'There are ' + str(chocolateBars) + ' chocolates.'

print(float(chocolateBars))
print(int(grams))
```

Booleans:
```
favoriteSong = True #Will become useful with conditionals.
```

Declaring Variable Type:
```
Note: Python variables are weakly typed meaning the variable type does not need to be declared. Other languages like C you must declare the type (so called strongly typed)
```

*Practice Excercise:*
```
"""
Practice Problem: Tax Machine calculates the tax on an item. Create a variable "price" as an Int and a "tax rate" as a Float and multiply them together and convert the result into a String that reads:
The tax is: (answer)
"""

price = 20
tax_rate = .05
prefix = "The tax is: "
tax = float(price)*tax_rate
answer = prefix + "$" + str(totalPrice)
print(answer)
```
