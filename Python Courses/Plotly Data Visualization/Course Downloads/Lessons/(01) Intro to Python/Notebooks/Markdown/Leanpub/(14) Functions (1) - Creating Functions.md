
# Functions (1) - Creating Functions

In this lesson we're going to learn about functions in Python. Functions are an important tool when programming and their use can be very complex. It's not the aim of this course to teach you how to implement functional programming, instead, this lesson will give you a grounding in how functions work and an insight into how we can use them to help us create charts with Plotly.

## What is a function?

A function is a block of code which is used to perform a single action. A function should be reusable, and it should behave predictably. We have already used several built-in functions, such as `print()` and `len()`, but Python also allows you to create user-defined functions.

## How to create a function

The syntax of creating a function is relatively straightforward. We first need to tell Python that we're going to define a function using the `def` keyword; we must then give the function a name followed by some parentheses (` () `) and a colon. Function names have the same restrictions as variable names (can't start with a number, can only contain letters, numbers and underscores). After the function name has been defined, any code within the function is indented by four spaces (or a tab):
`
def <function name>():
    <code to run>
`

In the cell below, I'm defining a function which prints the string `"This is a function"` every time it is called:



		~~~~~~~~
def testFunction():
    print("This is a function")
~~~~~~~~

When we have defined a function, we can call the function as we would call any built-in function that we have already used, remembering to include the parentheses:



		~~~~~~~~
testFunction()
~~~~~~~~

    This is a function
    

## Using arguments in a function

When we use the `len()` function, we have to tell that function which object we want the length of. We are passing that object as an argument to the function:



		~~~~~~~~
len("abcdefg")
~~~~~~~~




    7



We can do the same with user-defined functions. To do so, we create the function as normal, but inside the parentheses we can put argument names. We can put as many as we like, but each must be separated by a comma:

		~~~~~~~~
def <function name>(<arg1>, <arg2>, . . . <argN>):
    <code to run>
~~~~~~~~

We can then reference these arguments inside the function. In the cell below, I've written a function which prints out two items. Notice that I've converted each item to a string using the `str()` function - this ensures that the function behaves predictably - without converting an integer to a string, the code wouldn't run.



		~~~~~~~~
def testFunction2(item1, item2):
    print("The first item is: " + str(item1) + ", the second item is: " + str(item2))
~~~~~~~~

We can then use this function an pass arguments to it:



		~~~~~~~~
testFunction2('abc', 20)
~~~~~~~~

    The first item is: abc, the second item is: 20
    

The function will create a different output if we pass different arguments to it. This is because the arguments which are passed to a function only endure for the duration of that function.



		~~~~~~~~
testFunction2('howdy', 'partner')
~~~~~~~~

    The first item is: howdy, the second item is: partner
    

## Returning objects from a function

Functions are useful when we use them to create or modify an object. Variables which are created inside a function are not available to the rest of the code, unless we return them (or specifically declare them to be <a href="http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them">global variables</a>)

We can return an object created inside a function by using the return keyword; we must assign the output of a function to an object and we cannot write any more code after the return statment.

In the cell below, I create a function which takes returns a list of alternating valus. This function takes three arguments, two of which are the values to alternate, whilst the third is the number of times they must be repeated:



		~~~~~~~~
def alternateList(item1, item2, repeats):
    alternate = [item1, item2]
    altRepeat = alternate * repeats
    return altRepeat
~~~~~~~~

Because the function returns a value we must assign the output that is return to a variable:



		~~~~~~~~
repeated1 = alternateList(5, 50, 3)
~~~~~~~~

There are two variables created inside this function; `alternate` and `altRepeat`. These variables exist only within the function and we cannot access them in open code:



		~~~~~~~~
print(alternate)
~~~~~~~~


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-78ad8beb27cb> in <module>()
    ----> 1 print(alternate)
    

    NameError: name 'alternate' is not defined




		~~~~~~~~
print(altRepeat)
~~~~~~~~


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-0bb979493623> in <module>()
    ----> 1 print(altRepeat)
    

    NameError: name 'altRepeat' is not defined


But because we returned the value of the variable `altRepeat`, creating a new variable with that value, we can now see what the function `alternateList()` has created:



		~~~~~~~~
repeated1
~~~~~~~~




    [5, 50, 5, 50, 5, 50]



We can return two or more variables from a function by separating each variable with a comma. We must assign each to an object:



		~~~~~~~~
def alternateList(item1, item2, repeats):
    alternate = [item1, item2]
    altRepeat = alternate * repeats
    return alternate, altRepeat

pair, rpt = alternateList(77, 99, 5)

print(pair)
~~~~~~~~

    [77, 99]
    



		~~~~~~~~
print(rpt)
~~~~~~~~

    [77, 99, 77, 99, 77, 99, 77, 99, 77, 99]
    
