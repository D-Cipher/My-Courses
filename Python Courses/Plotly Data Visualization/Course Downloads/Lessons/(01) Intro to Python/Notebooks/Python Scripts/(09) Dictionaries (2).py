
# coding: utf-8

# # Dictionaries (2)

# In the last lesson we saw how to create dictionaries and how to access the different items in a dictionary by their key.  We also saw how to add to and update the items in a dictionary using assignment, or the <code>dict.update()</code> method, and how to delete items using the <code>del</code> keyword.
# 
# In this lesson we're going to continue looking at dictionaries. We're going to find out how to get a dictionary's length, access the keys and values from the dictionary, as well as how to access items inside nested dictionaries. 
# 
# This knowledge will come in really handy when we start building charts with Plotly, as we'll be passing the instructions for our chart to Plotly using nested dictionaries.
# 
# ### Getting a dictionary's length
# 
# You can get the number of items in a dictionary by using the <code>len()</code> function in the same way that we could get the length of a string or a list. This counts the number of key/value pairs in the dictionary:

# In[1]:

testScores1 = {'Alice' : 100, 'Bob' : 75, 'Ian' : 25, 'Susan' : 60}

len(testScores1)


# ### Getting a list of keys from a dictionary
# 
# We can get a list of keys in a dictionary by using the <code>dict.keys()</code> method:

# In[2]:

print(testScores1.keys())


# This returns an object that looks a bit like a list, but doesn't behave like one. You can't slice it for example:

# In[3]:

var1 = testScores1.keys()

var1[0]


# You can however turn it into a list by using the <code>list()</code> function, which behaves like the <code>str()</code> or <code>int()</code> functions we learnt about previously. Converting the <code>dict_keys</code> object into a list lets us index and slice it:

# In[4]:

var2 = list(testScores1.keys())

var2[0]


# ### Getting a list of values in a dictionary
# 
# In the same way that we got the dictionary's keys using <code>dict.keys()</code>, we can also get the dictionary's values using the <code>dict.values()</code> function:

# In[5]:

print(testScores1.values())


# Once again, we can't index or slice this object without turning it into a list:

# In[6]:

var3 = testScores1.values()

var3[0]


# In[7]:

var4 = list(testScores1.values())

var4[0]


# ### Getting the keys and values from a dictionary
# 
# As well as getting the keys and values from a dictionary separately, we can also get them together using the <code>dict.items()</code> method. This is especially useful for looping through the items in a dictionary, and we'll look at this in more depth in the loops lesson.
# 
# <code>dict.items()</code> returns a collection of tuples. A tuple is very similar to a list, in that you can index the items in it, however you cannot change their values. 

# In[8]:

print(testScores1.items())


# Once again, we need to convert this <code>dict_items</code> object into a list to be able to index and slice it:

# In[9]:

var5 = list(testScores1.items())

var5[0]


# We can then select the items individually inside the tuple as if we were selecting items in a nested list:

# In[10]:

var5[0][0]


# ### Nested Dictionaries
# 
# Just as we can create nested lists, we can also create nested dictionaries. Here I've created a dictionary which holds the test scores for the students. I've initially populated it with the scores for the first test:

# In[11]:

studentGrades = {'test1' : testScores1}

print(studentGrades)


# Now I can add the scores for the second test:

# In[12]:

testScores2 = {'Ian': 32, 'Susan': 71, 'Bob': 63, 'Alice': 99}

studentGrades.update({'test2' : testScores2})

print(studentGrades)


# We can access the scores for the first test:

# In[13]:

print(studentGrades['test1'])


# We can access the scores for a particular student for the first test in the same way. First of all, we access the <code>'test1'</code> dictionary, then within that we access the value we want by passing the corresponding key. Here I'm getting Ian's score for test 1:

# In[14]:

print(studentGrades['test1']['Ian'])


# ### What have we learnt this lesson?

# In this lesson we've seen how to get the length of a dictionary - the number of items in it. We've also seen how to get a list of the keys and values in the dictionary by using the <code>dict.keys()</code> and <code>dict.values()</code> functions in conjunction with the <code>list()</code> function, as well as how to get a list of tuples of the keys and values using <code>dict.items()</code>. We also learnt that a tuple is very similar to a list, but that you cannot change the items inside.
# 
# Finally, we learnt how to create nested dictionaries and access the items inside them.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
