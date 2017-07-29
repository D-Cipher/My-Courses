
# coding: utf-8

# # Functions (2) - Using Functions

# In the last lesson we saw how to create a function using the <code>def</code> keyword. We found out how to pass arguments to a function and how to use these arguments within the function. Finally, we learnt how to return one or many objects from the function, and that we need to assign the output of the function to a variable (or variables).
# 
# In this lesson we're going to practise writing functions. We'll write a few practise functions to help us review what we learnt in the last lesson, before  writing a function that we'll actually be able to use when making our charts.
# 
# ## Review - Writing some simple functions
# 
# We'll use this as a opportunity to practise what you've learnt about functions, the exercises below use concepts which you have already learnt in this course.
# 
# ### 1
# Your first challenge is to write a function which takes one string and one number (n). The function should return a string that is n copies of the string:
# 
# ````
# stringMultiply('hi', 5) --> 'hihihihihi'
# stringMultiply('one', 2) --> 'oneone'
# ````

# ### 2
# Write a function which takes two strings and returns the longer of the two strings. If the strings are the same length return one string which is both strings concatenated together:
# 
# ````
# stringCompare('hi', 'hiya') --> 'hiya'
# stringCompare('hi', 'ab') --> 'hiab'
# ````

# ### 3
# Write a function which takes one string and one number (n) as inputs. The function should return a string which is the concatenation of the first n characters and the last n characters of the string. If the length of the string is less than n, the function should return "I'm sorry Dave, I can't do that.".
# 
# ````
# stringFirstLast('purple', 2) --> 'pule'
# stringFirstLast('hi', 2) --> 'hihi'
# stringFirstLast('hi', 3) --> "I'm sorry Dave, I can't do that."
# ````

# ## Answers
# 
# These answers do not show the only way of solving the problem, as with everything in programming, there are several solutions!
# 
# ### 1

# In[1]:

def stringMultiply(stringIn, number):
    return stringIn * number

test1 = stringMultiply('hi', 5)
test2 = stringMultiply('one', 2)

print(test1, test2)


# ### 2

# In[2]:

def stringCompare(string1, string2):
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return string1 + string2
    
test3 = stringCompare('hi', 'hiya')
test4 = stringCompare('hi', 'ab') 

print(test3, test4)


# In[3]:

def stringFirstLast(stringIn, number):
    if number > len(stringIn):
        return "I'm sorry Dave, I can't do that."
    else:
        return stringIn[:number] + stringIn[-number:]

test5 = stringFirstLast('purple', 2)
test6 = stringFirstLast('hi', 2) 
test7 = stringFirstLast('hi', 3) 

print(test5, test6, test7)


# ## Using functions to help us create awesome visualisations
# 
# So hopefully you're feeling well-practised and ready to apply what we've learnt!
# 
# In this lesson we'll explore a couple of different use cases for functions which we'll apply later in the course.
# 
# ### Using functions to set the colour of a data item
# 
# Colour is an incredibly important aspect of any visualisation. We can use colour to group different data together, or to set them apart. In this example, we'll write a function which will set the colour of a data item depending on it's value. This function is directly applicable to code which we'll write; you can set the colours in Plotly by using the colour names (as well as in many other ways too!).
# 
# Have a go at writing the function yourself according to the specification below. If you get stuck, have a peek at the answer! Remember, there's always more than one solution, so don't take my version as the only way. If you code something and it works; great!
# 
# ##### Write  a function that takes two numbers as inputs. The first number is the value of the data item, and the second is the threshold at which we want the colour of that data item to change. The function should return 'Blue' if the first number is less than or equal to the second, and 'Red' otherwise.
# 
# ````
# chooseColour(50, 60) --> 'Blue'
# chooseColour(50, 40) --> 'Red'
# ````

# In[4]:

def chooseColour(value, threshold):
    if value <= threshold:
        return 'Blue'
    else:
        return 'Red'
    
test1 = chooseColour(50,60)
test2 = chooseColour(50,40)

print(test1, test2)


# ### What have we learnt this lesson?

# In this lesson we've reviewed how to write functions. We did three practise functions to solidify the knowledge from the last lesson, and we also created two helper functions which we'll be able to reuse throughout the course.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
