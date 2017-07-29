
# coding: utf-8

# # Variable Types - Lists (2)

# In the last lesson we learnt that a list can hold any number of  variables and that these variables can be of any type, even other lists. We also saw that we can index and slice lists in the same way that we can with strings.
# 
# In this lesson we'll learn how to add items to a list using the <code>list.append()</code> function, how to delete an item from a list by its index using the <code>del</code> keyword, and how to create and access nested lists.

# ## Adding items to a list
# 
# When Plotly interprets data, it expects each particular piece (or trace) of data to be an item in a list, for example Plotly would expect the x-values and y-values of a chart to be in two separate lists, and there are many occasions where we would want to create the dynamically.
# 
# To do this, we use the <code>list.append()</code> function.
# 
# First, we start with an empty list which will eventually contain our x-values:

# In[1]:

xVals = []

print(xVals)


# Then, we might decide that we want to add some observations to our list of x-values. To do this, we can use <code>list.append()</code> to add them one by one (we'll learn a faster way to do this in a future lesson):

# In[2]:

xVals.append(2)

print(xVals)

xVals.append(4)

print(xVals)

xVals.append(6)

print(xVals)

xVals.append(8)

print(xVals)

xVals.append(10)

print(xVals)


# ## Deleting items from a list
# 
# After creating our list of x-values, we might then want to delete items from that list. To do this, we use the <code>del</code> keyword in conjunction with the list index to select the item which we want to remove.
# 
# Here I'm taking a copy of the x-vals because I want to use this list later on in this lesson:

# In[3]:

xValsDel = xVals


# If we wanted to delete the first (or zeroeth) item in the list we would use the <code>del</code> keyword, and select the item at index 0:

# In[4]:

print("Before:", xValsDel)

del xValsDel[0]

print("After:", xValsDel)


# We might also want to delete the last item in the list. We can select the last item by choosing the item at index -1:

# In[5]:

print("Before:", xValsDel)

del xValsDel[-1]

print("After:", xValsDel)


# ## Creating and accessing nested lists
# 
# So, now we've created our x-values and y-values and seen how to delete items from them as we wish, we'll now learn how to create a nested list and how to access the items in that list.
# 
# First, I'll create a list which contains our x-values and y-values:

# In[8]:

yVals = [1,2,3]
allData = [xVals, yVals]
print(allData)


# We can then access the item in the zeroeth position by using index 0:

# In[9]:

print(allData[0])


# We can then access the items inside the list at index 0 in allData by adding another square bracket:

# In[10]:

print(allData[0][1])


# We can continue this process indefinitely, with nested lists inside nested lists. This list is three levels deep:

# In[11]:

allData2 = [allData, allData]
allData2


# We can access the list at index 0:

# In[12]:

allData2[0]


# We can access the nested list at index 1:

# In[13]:

allData2[0][1]


# And we can access the item at index 2 in that list:

# In[14]:

allData2[0][1][2]


# ### What have we learnt this lesson?

# So that concludes this lesson, in which we have learnt how to add items to a list using the <code>list.append()</code> function, as well as how to delete items from a list by using the <code>del</code> keyword and selecting the item by index.
# 
# Finally, we learnt how to create nested lists and how to access the objects at different levels within the nested list.
# 
# The next lesson will look at dictionaries.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
