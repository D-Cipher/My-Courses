
# coding: utf-8

# # Functions (1) - Creating Functions

# In this lesson we're going to learn about functions in Python. Functions are an important tool when programming and their use can be very complex. It's not the aim of this course to teach you how to implement functional programming, instead, this lesson will give you a grounding in how functions work and an insight into how we can use them to help us create charts with Plotly.
# 
# ## What is a function?
# 
# A function is a block of code which is used to perform a single action. A function should be reusable, and it should behave predictably. We have already used several built-in functions, such as <code>print()</code> and <code>len()</code>, but Python also allows you to create user-defined functions.
# 
# ## How to create a function
# 
# The syntax of creating a function is relatively straightforward. We first need to tell Python that we're going to define a function using the <code>def</code> keyword; we must then give the function a name followed by some parentheses (<code> () </code>) and a colon. Function names have the same restrictions as variable names (can't start with a number, can only contain letters, numbers and underscores). After the function name has been defined, any code within the function is indented by four spaces (or a tab):
# ````python
# def <function name>():
#     <code to run>
# ````
# 
# In the cell below, I'm defining a function which prints the string <code>"This is a function"</code> every time it is called:

# In[10]:

def testFunction():
    print("This is a function")


# When we have defined a function, we can call the function as we would call any built-in function that we have already used, remembering to include the parentheses:

# In[11]:

testFunction()


# ## Using arguments in a function
# 
# When we use the <code>len()</code> function, we have to tell that function which object we want the length of. We are passing that object as an argument to the function:

# In[12]:

len("abcdefg")


# We can do the same with user-defined functions. To do so, we create the function as normal, but inside the parentheses we can put argument names. We can put as many as we like, but each must be separated by a comma:
# ````python
# def <function name>(<arg1>, <arg2>, . . . <argN>):
#     <code to run>
# ````
# 
# We can then reference these arguments inside the function. In the cell below, I've written a function which prints out two items. Notice that I've converted each item to a string using the <code>str()</code> function - this ensures that the function behaves predictably - without converting an integer to a string, the code wouldn't run.

# In[13]:

def testFunction2(item1, item2):
    print("The first item is: " + str(item1) + ", the second item is: " + str(item2))


# We can then use this function an pass arguments to it:

# In[14]:

testFunction2('abc', 20)


# The function will create a different output if we pass different arguments to it. This is because the arguments which are passed to a function only endure for the duration of that function.

# In[15]:

testFunction2('howdy', 'partner')


# ## Returning objects from a function
# 
# Functions are useful when we use them to create or modify an object. Variables which are created inside a function are not available to the rest of the code, unless we return them (or specifically declare them to be <a href="http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them">global variables</a>)
# 
# We can return an object created inside a function by using the return keyword; we must assign the output of a function to an object and we cannot write any more code after the return statment.
# 
# In the cell below, I create a function which takes returns a list of alternating valus. This function takes three arguments, two of which are the values to alternate, whilst the third is the number of times they must be repeated:

# In[16]:

def alternateList(item1, item2, repeats):
    alternate = [item1, item2]
    altRepeat = alternate * repeats
    return altRepeat


# Because the function returns a value we must assign the output that is return to a variable:

# In[17]:

repeated1 = alternateList(5, 50, 3)


# There are two variables created inside this function; <code>alternate</code> and <code>altRepeat</code>. These variables exist only within the function and we cannot access them in open code:

# In[18]:

print(alternate)


# In[19]:

print(altRepeat)


# But because we returned the value of the variable <code>altRepeat</code>, creating a new variable with that value, we can now see what the function <code>alternateList()</code> has created:

# In[20]:

repeated1


# We can return two or more variables from a function by separating each variable with a comma. We must assign each to an object:

# In[21]:

def alternateList(item1, item2, repeats):
    alternate = [item1, item2]
    altRepeat = alternate * repeats
    return alternate, altRepeat

pair, rpt = alternateList(77, 99, 5)

print(pair)


# In[22]:

print(rpt)


# ### What have we learnt this lesson?

# In this lesson we've learnt how to define a function using the <code>def</code> keyword, and how to pass arguments to the function. We've seen that these arguments only hold their value within the function, and that we can use a return statement to return one or more values from within the function.
# 
# In the next lesson we'll look at how we can use functions to help us make our charts.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
