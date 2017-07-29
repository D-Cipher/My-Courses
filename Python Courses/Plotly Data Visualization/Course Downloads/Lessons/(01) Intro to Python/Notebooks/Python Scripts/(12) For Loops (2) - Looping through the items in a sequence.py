
# coding: utf-8

# # For Loops (2) - Looping through the items in a sequence

# In the last lesson we introduced the concept of a For loop and learnt how we can use them to repeat a section of code.  We learnt how to write a For loop that repeats a piece of code a specific number of times using the <code>range()</code> function, and saw that we have to create a variable to keep track of our position in the loop (conventionally called <code>i</code>). We also found out how to implement if-else statements within our loop to change which code is run inside the loop.
# 
# As well as writing a loop which runs a specific number of times, we can also create a loop which acts upon each item in a sequence. In this lesson we'll learn how to implement this functionality and find out how to use this knowledge to help us make charts with Plotly.
# 
# ## Looping through each item in a sequence
# 
# Being able to access each item in turn in a sequence is a really useful ability and one which we'll use often in this course. The syntax is very similar to that which we use to loop through the numbers in a range:
# ```` python
# for <variable name> in <sequence>:
#     <code to run>
# ````
# 
# The difference here is that the variable which keeps track of our position in the loop does not increment by 1 each time the loop is run. Instead, the variable takes the value of each item in the sequence in turn:

# In[1]:

list1 = ['a', 'b', 'c', 'd', 'e']

for item in list1:
    print(item)


# It's not important what we call this variable:

# In[2]:

for banana in list1:
    print(banana)


# But it's probably a good idea to call the variable something meaningful:

# In[3]:

data = [20, 50, 10, 67]

for d in data:
    print(d)


# ## Using these loops
# 
# We can use these loops in conjunction with other concepts we have already learnt. For example, imagine that you had a list of proportions stored as decimals, but that you needed to create a new list to store them as whole numbers.
# 
# We can use <code>list.append()</code> with a for loop to create this new list. First, we have to create an empty list to which we'll append the percentages:

# In[4]:

proportions = [0.3, 0.45, 0.99, 0.23, 0.46]

percentages = []


# Next, we'll loop through each item in proportions, multiply it by 100 and append it to percentages:

# In[5]:

for prop in proportions:
    percentages.append(prop * 100)
    
print(percentages)


# ## Using for loops with dictionaries
# 
# We've seen how to loop through each item in a list. We will also make great use of the ability to loop through the keys and values in a dictionary.
# 
# If you remember from the dictionaries lessons, we can get the keys and values in a dictionary by using <code>dict.items()</code>. We can use this in conjunction with a for loop to manipulate each item in a dictionary. This is something which we'll use often; we'll often have data for several years stored in a dictionary; looping through these items will let us plot the data really easily.
# 
# In the cell below, I've created a simple data structure which we'll access using a for loop. Imagine that this data contains sales figures for the 4 quarters in a year:

# In[6]:

data = {2009 : [10,20,30,40],
       2010 : [15,30,45,60],
       2011 : [7,14,21,28],
       2012 : [5,10,15,20]}


# We can loop through the keys by using <code>dict.keys()</code>:

# In[7]:

for k in data.keys():
    print(k)


# And we can loop through the values (which are lists):

# In[8]:

for v in data.values():
    print(v)


# We can loop through them both together:

# In[9]:

for k, v in data.items():
    print(k, v)


# Having the data available to compare each year is really handy, but it might also be helpful to store them as one long list so we can plot the data and see trends over time. 
# 
# First, we'll make a new list to store all of the data items:

# In[10]:

allYears = []


# And then we'll loop through the dictionary and concatenate each year's data to the <code>allYears</code> list:

# In[11]:

for v in data.values():
    allYears = allYears + v
    
print(allYears)


# ### What have we learnt this lesson?

# In this lesson we've seen how to access each item in a sequence. We've learnt that the variable that keeps track of our position in the loop stores each value in the sequence in turn. We've seen how to apply this knowledge to loop through a dictionary of data and concatenate data for several years into one long list.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
