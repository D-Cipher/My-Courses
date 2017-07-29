
# coding: utf-8

# #  Variable Types - Strings (1)
# 
# In the last class we learnt about <code>integers</code> and <code>floats</code> in Python. We also learnt how to do different mathematical operations, some of which you may not have come across before, such as the modulus function.
# 
# In this lesson we're going to learn about <code>strings</code>. A string is another name for a variable which contains text, rather than numbers. We're going to learn how to create string variables, how to convert between string, integer and float, and finally how to use mathematical operators on strings.
# 
# ### Strings
# 
# A string is several characters enclosed by single or double quotation marks:

# In[1]:

'This is a string'


# In[2]:

"This is also a string"


# Strings which contain a single quotation mark must be enclosed by double quotation marks:

# In[3]:

'This doesn't work'


# In[4]:

"It didn't work, anyway"


# Likewise, strings which contain a double quotation mark must be enclosed by single quotation marks:

# In[5]:

'He said "I never wanted that to happen"'


# Strings which contain both types of quotation mark must be enclosed by 3 single quotation marks:

# In[6]:

'''He said "I didn't want that to happen"'''


# You can see that Python has converted our triple quotation marks into just single quotation marks, and included a <code>\</code>. This is called an 'escape character'; Python uses this to decide whether or not to process the following character as text string or as code. 
# 
# In this case, the escape character tells Python to process the apostrophe as a text string.

# ## Converting between strings, integers and floats
# 
# As with integers and floats, we can convert strings into other data types. This is slightly more complex than converting between integers and floats.
# 
# Some strings can be converted into integers and floats:

# In[7]:

string1 = "5"

testVarInt1 = int(string1)

print(testVarInt1)


# In[8]:

testVarFloat1 = float(string1)

print(testVarFloat1)


# And others can't, even though they look like they can:

# In[9]:

string2 = "5.0"

testVarInt2 = int(string2)

print(testVarInt2)


# In[10]:

testVarFloat2 = int(string2)

print(testVarFloat2)


# And some can't, and definitely shouldn't:

# In[11]:

string3 = 'Hello World!'

print(int(string3))


# We can also convert integers and floats into strings using the <code>str()</code> function:

# In[12]:

int1 = 5

string4 = str(int1)

print(type(string4))


# In[13]:

float1 = 6.77779

string5 = str(float1)

print(type(string5))


# ## Mathematical operators and strings
# 
# We can also use mathematical operators on strings. This might seem counterintuitive at first...

# In[14]:

string1 = "This is a test"

string2 = string1 + '. ' + string1

print(string2)


# In[15]:

string3 = 'Hi'
string4 = 'Ho'

print((string3 + string4 + ', ') * 2 + "it's off to work we go.")


# But not all of the mathematical operators make sense:

# In[16]:

print(string3 - 5)


# In[17]:

print(string3 ** 5)


# In[18]:

print(string3 / 5)


# ## What have we learnt in this lesson?
# In this lesson we've learnt about strings in Python. We've seen how to create strings and when to use single quotes and double quotes and we've learnt a little bit about escape characters. 
# 
# We've also learnt how to change between strings, integers and floats, but that this doesn't always work. We've seen how to apply mathematical operators to strings, but that this is only possible with addition and multiplication.
# 
# In the next lesson we'll learn how to index and slice strings, as well as how to implement some common functions, such as the <code>len()</code> function.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
