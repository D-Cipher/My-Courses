
# coding: utf-8

# # Variable Types - Lists (1)

# In the last few lessons we have looked at four types of variable; integers, floats, strings and boolean. These are all what I like to call 'simple' variable types; each of them is comprised of only one object.
# 
# Python allows for many different types of what I call 'complex' variable types; these are variables which contain 1 or more separate objects. In this course we will only look at lists and dictionaries as these are the primary data structures which Plotly uses to create charts. In the next couple of lessons we'll learn about lists.
# 
# 
# ## What is a list?
# 
# A list, whilst being an object in its own right, is also a container for other objects.
# 
# A list can contain any number of elements (you are limited by your computer's memory), and can contain elements of any type, even other lists.
# 
# A list is comprised of different items, separated by commas, between two square brackets.
# 
# This is a list of numbers:

# In[1]:

list1 = [0, 1, 2, 3, 4]


# This is a list of strings:

# In[2]:

list2 = ['a', 'b', 'c', 'd', 'e']


# And this is a list of lists:

# In[3]:

list3 = [list1, list2]

print(list3)


# ## Mathematical Operators and Common Functions/Methods

# We can do addition on lists:

# In[4]:

list4 = list1 + list2

print(list4)


# And we can also do multiplication:

# In[5]:

print(list1 * 4)


# We can get the number of items in a list by using the <code>len()</code> function:

# In[6]:

print(len(list1))


# Many of the same functions that work on strings also work on lists because they are both 'sequences'; bear in mind that some functions will only work on lists, and others only on strings.
# 
# We can check which functions can be applied to an object by typing the object's name, followed by a <code> . </code> and then pressing <code>tab</code>:

# In[7]:

list1.  #put the cursor on the right of the dot and press tab


# ## Indexing and Slicing Lists

# In a previous lesson we learnt how to select different items within a string by using the index of that item:

# In[8]:

string1 = 'abcdefg'

print(string1[4])


# And we also learnt how to take slices of a string by passing two indices separated by a colon (remember that the slice starts from the first index and stops just before the second):

# In[9]:

print(string1[2:5])


# The same method that we use to index and slice strings can be directly applied to lists. Here, I'm taking a particular item from list 1:

# In[10]:

print(list1[0])


# And a different item from list 2. Notice how taking a single item returns just that item:

# In[11]:

print(list2[3])


# We can also change a value in a list by accessing it by the index:

# In[12]:

list2[3] = 'zzzz'

print(list2)


# We can also take a slice from a list; this returns a list of items:

# In[13]:

print(list1[2:5])


# To change all of the items in a slice, you must set them equal to a new list of the same length as the slice:

# In[14]:

list1[2:5] = [10,10,10]

print(list1)


# ### What have we learnt this lesson?

# So that concludes this lesson, in which we have learnt how to create lists and that a list can hold any number of items of different types - even other lists!
# 
# We learnt that we can add and multiply lists and also how to find the length of a list, discovering that there are many functions which work on lists and string, but also finding a way to know which function will work on which type of object.
# 
# Finally, we learnt how to index and slice lists, and that this works in an identical way to string indexing and slicing. And we also found out how to assign a different value to an item in a list.
# 
# In the next lesson, we'll learn how to add and delete items in a list, as well as how to create nested lists and access the items in those lists.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
