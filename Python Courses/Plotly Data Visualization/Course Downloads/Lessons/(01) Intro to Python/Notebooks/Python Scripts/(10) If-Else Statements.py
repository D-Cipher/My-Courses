
# coding: utf-8

# # If-Else Statements

# In this lesson we're going to move away from variable types and data structures and instead look at conditional programming. We'll see how to make decisions using the <code>if</code>, <code>elif</code> and <code>else</code> statements.
# 
# This is one of the most powerful constructs we can use when programming and it's especially helpful when making different charts. For example, we might want to set a bar on a barchart to be a different colour if it shows a value above a certain threshhold. We would use an <code>if</code> statement to achieve this.
# 
# ## How do If statements work?
# 
# The <code>if</code> statement in Python is constructed as follows:
# 
# ````
# if <condition>:
#     <code to run>
# ````
# 
# The condition must be an expression which evaluates to a boolean (True or False) value. If the condition evaluates to True, then the code below is run. In Python, we must indent the code to run with four spaces (or a tab). Any code that is not indented after the statement is run anyway.
# 
# In the example below, we're checking if a is greater than three, and if it is we return a string confirming this:

# In[1]:

a = 5

if a > 3:
    print("a is greater than 3")
print("This code runs anyway")


# When a is not greater than three, nothing happens in the <code>if</code> statemnt because there is no code to run (notice that the code outside of the <code>if</code> statement still runs):

# In[2]:

a = 2

if a > 3:
    print("a is greater than 3")
print("This code runs anyway")


# ### Adding an Else Statement
# 
# If we want to run some code when the condition evaluates to <code>False</code>, we need to add an <code>else</code> statement. The code that comes after this statement must be indented by four spaces (or a tab). The syntax is as follows:
# ````
# if <condition>:
#     <code to run>
# else:
#     <code which runs when if condition is False>
# ````
# 
# The code after the <code>else</code> statement only runs when the <code>if</code> statement evaluates to <code>False</code>:

# In[3]:

a = 2

if a > 3:
    print("a is greater than 3")
else:
    print("a is less than 3")
    
print("This code runs anyway")


# ### Adding other conditions
# 
# We can also introduce more conditions using the <code>elif</code> statement (else if). These conditions work in the same way as the <code>if</code>statement; the code after each is only run if the condition evaluates to <code>True</code>. The syntax is as follows:
# ````
# if <condition>:
#     <code to run>
# elif <other condition>:
#     <different code to run>
# elif <another condition>:
#     <another piece of code>
# else:
#     <code which runs when all other conditions are False>
# ````
# 
# You might have noticed an error with the code in the cell above; what happens when a is 3? The statement <code>"a is less than 3"</code> is clearly not true here! 
# 
# We can use an <code>elif</code> statement to add another condition:

# In[4]:

a = 3

if a > 3:
    print("a is greater than 3")
elif a == 3:
    print("a is equal to 3")
else:
    print("a is less than 3")
    
print("This code runs anyway")


# We can add as many <code>elif</code> statements as we wish:

# In[5]:

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


# ### Nested If Statements
# 
# We can place an If-Else statement as the code to run inside an if statement. The code to run in the nested if statement must be indented by 8 spaces (or two tabs). The syntax is as follows:
# 
# ````
# if <condition>:
#     if <condition>:
#         <code to run>
#     else:
#         <code to run if the nested if statement is False>
# else:
#     <code to run if the first if statement is False>
# ````
# 
# Creating nested if statements allows us to create complex decision trees and to tailor our code to deal with many different situations.
# 
# In the cell below, we first check if a is greater than 3, if this condition is True, we then invoke the nested if statment and check if a is then subsequently greater than 4; if not, we know that it must be equal to 4, and this is captured in the Else part of the nested If statement.

# In[6]:

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


# ### What have we learnt this lesson?

# In this lesson we've learnt how to run code based on a condition. We learnt the syntax of the if-else statement, finding that we must put a colon after every statement and indent the code following it by four spaces (or a tab).
# 
# We've seen that we can selectively run a piece of code  by using an <code>if</code> statement. We also learnt how to run some code when the <code>if</code> statement evaluates to <code>False</code> by using an <code>else</code> statemnt. FInally, we saw that we can add many other conditions between the <code>if</code> and <code>else</code> statements by creating <code>elif</code> statements.
# 
# Finally, we learnt how to create nested if statements which allow us to create complex decision trees and to tailor our code to handle many different situations.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
