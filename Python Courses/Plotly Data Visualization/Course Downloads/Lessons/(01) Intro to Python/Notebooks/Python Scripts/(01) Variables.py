
# coding: utf-8

# #  Variables
# 
# In Python there are many different types of data. In this lesson we'll learn about how we can assign values to variables.
# 
# ## What is a variable?
# 
# As the name implies, a variable is something which can change. It is the name we give to a piece of memory used by a computer program. We can think of it as being a container into which we can put different types of data.
# 
# You can assign a value to a variable by using the <code>=</code> sign; you should think of this as meaning 'is set to', rather than 'is equal to'. The variable name goes on the left-hand side, and the value assigned to the variable goes on the right-hand side. 
# 
# In the cell below I have assigned the value <code>5</code> to the variable named <code>counter</code>.

# In[1]:

counter = 5


# In a Jupyter Notebook we can look at the value of a variable by using the <code>print()</code> function:

# In[2]:

print(counter)


# A variable name in Python must begin with an uppercase or lowercase letter or an underscore:
# ````python
# - _variable1
# - variable2
# - Variable2
# ````
# 
# The variable name may only contain letters, numbers and underscores:
# ````python
# - this_is_a_variable_name
# - this_1_2
# - this_i$'nt
# ````
# 
# Variable names are case sensitive; the following two variables are different:
# ````python
# - this_is_a_variable
# - This_Is_A_Variable
# ````
# 
# Finally, you may not use Python keywords as variable names. You can see a list of examples by running the code in the cell below. Don't worry about what it means for now; we'll come to it later.

# In[3]:

import keyword
keyword.kwlist


# You can assign multiple values to multiple variables by using a comma to separate the values and the variables:

# In[4]:

var1, var2, var3 = 5,6,7


# Let's look at the values of these variables:

# In[5]:

print(var1, var2, var3)


# You can also assign a the value of a variable to another variable:

# In[6]:

numberOfPies = 10

numberOfPlates = numberOfPies

print(numberOfPlates)


# When you assign the value of a variable to another variable, you can change the original value without changing the new variable:

# In[7]:

x = 2
y = x
print(x, y)


# In[8]:

x = 5
print(x, y)


# ## What have we learnt in this lesson?
# In this lesson we've learnt what a variable is, what constitutes a valid variable name and how to assign values to variables.
# 
# We've also seen how to assign multiple values to multiple variables and to set a variable to the value of another variable.
# 
# Thanks for watching!

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
