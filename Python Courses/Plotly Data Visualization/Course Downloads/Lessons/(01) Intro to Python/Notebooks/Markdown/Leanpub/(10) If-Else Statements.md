
# If-Else Statements

In this lesson we're going to move away from variable types and data structures and instead look at conditional programming. We'll see how to make decisions using the `if`, `elif` and `else` statements.

This is one of the most powerful constructs we can use when programming and it's especially helpful when making different charts. For example, we might want to set a bar on a barchart to be a different colour if it shows a value above a certain threshhold. We would use an `if` statement to achieve this.

## How do If statements work?

The `if` statement in Python is constructed as follows:

`
if <condition>:
    <code to run>
~~~~~~~~

The condition must be an expression which evaluates to a boolean (True or False) value. If the condition evaluates to True, then the code below is run. In Python, we must indent the code to run with four spaces (or a tab). Any code that is not indented after the statement is run anyway.

In the example below, we're checking if a is greater than three, and if it is we return a string confirming this:



a = 5

if a > 3:
    print("a is greater than 3")
print("This code runs anyway")
~~~~~~~~

    a is greater than 3
    This code runs anyway
    

When a is not greater than three, nothing happens in the `if` statemnt because there is no code to run (notice that the code outside of the `if` statement still runs):



		~~~~~~~~
a = 2

if a > 3:
    print("a is greater than 3")
print("This code runs anyway")
~~~~~~~~

    This code runs anyway
    

### Adding an Else Statement

If we want to run some code when the condition evaluates to `False`, we need to add an `else` statement. The code that comes after this statement must be indented by four spaces (or a tab). The syntax is as follows:
~~~~~~~~
if <condition>:
    <code to run>
else:
    <code which runs when if condition is False>
~~~~~~~~

The code after the `else` statement only runs when the `if` statement evaluates to `False`:



		~~~~~~~~
a = 2

if a > 3:
    print("a is greater than 3")
else:
    print("a is less than 3")
    
print("This code runs anyway")
~~~~~~~~

    a is less than 3
    This code runs anyway
    

### Adding other conditions

We can also introduce more conditions using the `elif` statement (else if). These conditions work in the same way as the `if`statement; the code after each is only run if the condition evaluates to `True`. The syntax is as follows:
~~~~~~~~
if <condition>:
    <code to run>
elif <other condition>:
    <different code to run>
elif <another condition>:
    <another piece of code>
else:
    <code which runs when all other conditions are False>
~~~~~~~~

You might have noticed an error with the code in the cell above; what happens when a is 3? The statement `"a is less than 3"` is clearly not true here! 

We can use an `elif` statement to add another condition:



		~~~~~~~~
a = 3

if a > 3:
    print("a is greater than 3")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is less than 3")
    
print("This code runs anyway")
~~~~~~~~

    a is equal to 3
    This code runs anyway
    

We can add as many `elif` statements as we wish:



		~~~~~~~~
a = 2

if a > 3:
    print("a is greater than 3")
elif a == 3:
    print("a is equal to 3")
elif a == 2:
    print("a is equal to 2")
else:
    print("a is less than 2")
    
print("This code runs anyway")
~~~~~~~~

    a is equal to 2
    This code runs anyway
    

### Nested If Statements

We can place an If-Else statement as the code to run inside an if statement. The code to run in the nested if statement must be indented by 8 spaces (or two tabs). The syntax is as follows:

~~~~~~~~
if <condition>:
    if <condition>:
        <code to run>
    else:
        <code to run if the nested if statement is False>
else:
    <code to run if the first if statement is False>
~~~~~~~~

Creating nested if statements allows us to create complex decision trees and to tailor our code to deal with many different situations.

In the cell below, we first check if a is greater than 3, if this condition is True, we then invoke the nested if statment and check if a is then subsequently greater than 4; if not, we know that it must be equal to 4, and this is captured in the Else part of the nested If statement.



		~~~~~~~~
a = 6

if a > 3:
    if a > 4:
        print("a is greater than 4")
    else:
        print("a is equal to 4")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is less than 3")
    
print("This code runs anyway")
~~~~~~~~

    a is greater than 4
    This code runs anyway
    
