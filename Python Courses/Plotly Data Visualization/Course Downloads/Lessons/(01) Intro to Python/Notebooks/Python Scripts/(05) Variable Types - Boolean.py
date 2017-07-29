
# coding: utf-8

# # Variable Types - Boolean

# In the last lesson we learnt how to index and slice strings. We also learnt how to use some common string functions such as the <code>len()</code> function.
# 
# In this lesson, we'll learn about Boolean values. Boolean values evaluate to either True or False and are commonly used for comparisons of equality and inequality, as well as controlling the flow of a program.

# ## Boolean Values

# Boolean values evaluate to True or False. You can see how Jupyter highlights these keywords:

# In[1]:

boolTrue = True
boolFalse = False


# Integers, floats and strings can be evaluated to a boolean value by using the <code>bool()</code> function.
# 
# All non-zero numbers evaluate to <code>True</code> whilst 0 evaluates to <code>False</code>:

# In[2]:

bool(0)


# In[3]:

bool(0.00000000001)


# In[4]:

bool(10)


# All non-empty strings evaluate to <code>True</code>, whilst an empty string evaluates to <code>False</code>:

# In[5]:

bool("hi")


# In[6]:

bool(' ')


# In[7]:

bool('')


# ## And, Or and Not
# 
# You can also create more complex boolean expressions by using <code>and</code>, <code>or</code> and <code>not</code> to compare multiple expressions.
# 
# <code>and</code> only returns <code>True</code> if all the boolean expressions evaluate to <code>True</code>:

# In[8]:

print(True and True)


# In[9]:

print(True and False)


# In[10]:

print(True and True and True and True and False)


# <code>or</code> returns <code>True</code> if at least one expression evalutes to <code>True</code>:

# In[11]:

print(True or False)


# In[12]:

print(False or False)


# In[13]:

print(False or False or False or False or True)


# <code>not</code> inverts the boolean expression; <code>True</code> becomes <code>False</code> and vice versa:

# In[14]:

print(not True)


# In[15]:

print(not False)


# In[16]:

print(not(True and True))


# You can use brackets to create complex expressions. What do you think this evaluates to?

# In[17]:

print(not (True or False) and not(False and True))


# ## Logical comparisons
# 
# We've just seen the basics of boolean values, however comparing <code>True</code> and <code>False</code> isn't particularly useful. The power of boolean values lies in how we can use them to compare values.
# 
# In Python, we can test for equality by using the <code>==</code> symbol; this test for equality returns a boolean value:

# In[18]:

5 == 5


# In[19]:

5 == 10


# We can also test for inequality using <code>!=</code>; this also returns a boolean value:

# In[20]:

1 != 2


# In[21]:

1 != 1


# <code>==</code> and <code>!=</code> both work on strings:

# In[22]:

'hi' == 'hi'


# In[23]:

'hi' != 'ho'


# We can test if a number is greater than another number using <code>></code>:

# In[24]:

5 > 4


# In[25]:

5 > 10


# We can test if a number is greater than or equal to another number by using <code>>=</code>

# In[26]:

5 >= 4


# In[27]:

5 >= 5


# In[28]:

5 >= 6


# We can also test if a number is less than another number by using <code>&lt;</code>:

# In[29]:

5 < 4


# In[30]:

10 < 100


# An we can test if a number is less than or equal to another number by using <code>&lt;=</code>:

# In[31]:

5 <= 7


# In[32]:

5 <= 5


# In[33]:

5 <= 4


# We can also do these comparisons on strings. Python compares the first two items in the string and if they differ, this determines the outcome of the comparison. If they're the same, the next two items are compared:

# In[34]:

'a' < 'b'


# In[35]:

'hi' < 'ho'


# In[36]:

'z' < 'x'


# ### Combining comparisons with And, Or and Not

# We now know how to create complex comparisons of strings and numbers. For the following examples, try to figure out what the answer will be before you run the cell.

# In[37]:

1 != 3 and 2 == 5


# In[38]:

"test" != "testing" and 5 == 5


# In[39]:

"one" == 1


# In[40]:

not (True and False)


# In[41]:

not (4 == 4 and 0 != 10)


# ### What have we learnt this lesson?

# In this class we've learnt about Boolean values and how to use them for comparisons of equality and inequality, as well as how to make complex comparisons. We also briefly touched upon using Boolean values to control the flow of a program. We'll return to this in a later lesson.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
