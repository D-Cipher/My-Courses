
#  Variable Types - Strings (2)

In the last class we learnt how to create strings, how to convert between string, integers and floats using the `str()`, `int()` and `float()` functions respectively. We also learnt that we can add and multiply strings, but that we cannot divide or subtract them. 

In this lesson we're going to learn how to index and slice strings, as well as how to implement some common functions on them.

## Indexing and Slicing Strings

Each character in a string has a numeric position, starting from 0. We can access the character at this position by using square brackets:



testString = "Hi there, this is a string"

testString[0]





    'H'





		~~~~~~~~
testString[1]
~~~~~~~~




    'i'



We can access the last string with `[-1]`, and the next-last with `[-2]` and so on:



		~~~~~~~~
testString[-1]
~~~~~~~~




    'g'





		~~~~~~~~
testString[-2]
~~~~~~~~




    'n'



We can take slices of a string using `[0:5]`. A string slice includes the first number and stops just before the second:



		~~~~~~~~
testString2 = '0123456789'

testString2[0:5]
~~~~~~~~




    '01234'



We can take a slice starting from the beginning of the string by leaving the first index blank:



		~~~~~~~~
testString2[:5]
~~~~~~~~




    '01234'



We can slice to the end by leaving the last index blank:



		~~~~~~~~
testString[5:]
~~~~~~~~




    'ere, this is a string'



We can also use variables instead of the numbers in a string slice:



		~~~~~~~~
x = 3
y = 6

testString2[x:y]
~~~~~~~~




    '345'



### String functions and methods

There are many different functions which we can use with strings. We'll take a look at the most useful.

#### Get the length of a string

We can find the length of a string by using the `len()` function:



		~~~~~~~~
testString = "Hi there, this is a string"

print(len(testString))
~~~~~~~~

    26
    

#### Find out if a word or character is in a string

We can see if a string contains another string:



		~~~~~~~~
testString = "Hi there, this is a string"

print('string' in testString)
~~~~~~~~

    True
    



		~~~~~~~~
print('badger' in testString)
~~~~~~~~

    False
    



		~~~~~~~~
print('badger' not in testString)
~~~~~~~~

    True
    

We can find the position of a string within another string using the `str.find()` function.

This function returns the index of the first letter of the substring within the string, or -1 if the string is not found:



		~~~~~~~~
testString.find('string')
~~~~~~~~




    20





		~~~~~~~~
testString[20:26]
~~~~~~~~




    'string'





		~~~~~~~~
testString.find('badger')
~~~~~~~~




    -1



## What have we learnt in this lesson?
In this lesson we've learnt more about strings in Python. We've seen  how to index and slice strings, as well as how to find the length of a string and how to find the position of a substring within the main string.

The next lesson is about Boolean, or True and False values. Thanks for watching.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>