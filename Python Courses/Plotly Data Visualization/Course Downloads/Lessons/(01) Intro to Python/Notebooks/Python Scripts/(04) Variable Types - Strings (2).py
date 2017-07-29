
# coding: utf-8

# #  Variable Types - Strings (2)
# 
# In the last class we learnt how to create strings, how to convert between string, integers and floats using the <code>str()</code>, <code>int()</code> and <code>float()</code> functions respectively. We also learnt that we can add and multiply strings, but that we cannot divide or subtract them. 
# 
# In this lesson we're going to learn how to index and slice strings, as well as how to implement some common functions on them.
# 
# ## Indexing and Slicing Strings
# 
# Each character in a string has a numeric position, starting from 0. We can access the character at this position by using square brackets:

# In[1]:

testString = "Hi there, this is a string"

testString[0]


# In[2]:

testString[1]


# We can access the last string with <code>[-1]</code>, and the next-last with <code>[-2]</code> and so on:

# In[3]:

testString[-1]


# In[4]:

testString[-2]


# We can take slices of a string using <code>[0:5]</code>. A string slice includes the first number and stops just before the second:

# In[5]:

testString2 = '0123456789'

testString2[0:5]


# We can take a slice starting from the beginning of the string by leaving the first index blank:

# In[6]:

testString2[:5]


# We can slice to the end by leaving the last index blank:

# In[7]:

testString[5:]


# We can also use variables instead of the numbers in a string slice:

# In[8]:

x = 3
y = 6

testString2[x:y]


# ### String functions and methods
# 
# There are many different functions which we can use with strings. We'll take a look at the most useful.
# 
# #### Get the length of a string
# 
# We can find the length of a string by using the <code>len()</code> function:

# In[9]:

testString = "Hi there, this is a string"

print(len(testString))


# #### Find out if a word or character is in a string
# 
# We can see if a string contains another string:

# In[10]:

testString = "Hi there, this is a string"

print('string' in testString)


# In[11]:

print('badger' in testString)


# In[12]:

print('badger' not in testString)


# We can find the position of a string within another string using the <code>str.find()</code> function.
# 
# This function returns the index of the first letter of the substring within the string, or -1 if the string is not found:

# In[13]:

testString.find('string')


# In[14]:

testString[20:26]


# In[15]:

testString.find('badger')


# ## What have we learnt in this lesson?
# In this lesson we've learnt more about strings in Python. We've seen  how to index and slice strings, as well as how to find the length of a string and how to find the position of a substring within the main string.
# 
# The next lesson is about Boolean, or True and False values. Thanks for watching.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
