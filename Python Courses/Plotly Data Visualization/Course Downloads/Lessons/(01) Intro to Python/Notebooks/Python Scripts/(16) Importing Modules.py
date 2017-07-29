
# coding: utf-8

# # Importing Modules

# In this lesson we're going to learn how to import different code libraries and how to use functions from those libraries. This is vital knowledge for this course; Plotly itself is an external code library and there are many different functions which we'll need to use.
# 
# ## How to import a module
# 
# We'll start by importing the Python builtin library called <code>random</code> - this library allows us to create different random numbers. 
# 
# It's as easy as typing <code>import</code>, then the module name into the cell. When the Python interpreter finds an <code>import</code> statement, it searches through a list of directories in which it expects to find modules to be imported.

# In[1]:

import random


# When we try to import a module that doesn't yet exist, we get an <code>ImportError</code>:

# In[2]:

import bananas


# We can test to see that the module has been imported by typing the module name, then a <code> . </code>, then pressing <code>tab</code> to see what functions are available to us from the module. We can scroll through these options using the arrow keys:

# In[3]:

random.


# We're going to use the <code>random.randint</code> function to get a random integer. Remember to press <code>shift + tab</code> after opening the brackets to see what arguments the function takes.

# In[4]:

random.randint(5, 10)


# But imagine that we had to use <code>random.randint()</code> a lot in whatever program we are writing. It would become very time consuming to write <code>random.randint()</code> every time.
# 
# Luckily, we can create a shorthand to reference the <code>random</code> module:

# In[5]:

import random as r


# We can now use <code>random.randint()</code> by typing <code>r.randint()</code>:

# In[6]:

r.randint(5, 10)


# We could go one step further, and import the <code>randint</code> module directly from <code>random</code>. This will let us use <code>randint</code> without having to reference the <code>random</code> module at all:

# In[7]:

from random import randint

randint(5, 10)


# You can also import multiple modules at the same time. In this example, <code>random()</code> creates a random number between 0 and 1:

# In[8]:

from random import randint, random

print(random())


# Finally, we can choose to import all of the functions in a module:

# In[9]:

from random import *


# This option should be used sparingly. Python uses 'namespaces' to keep track of object and function names; if you had created your own function called <code>randint</code>, and then imported the <code>random.randint()</code> function, you might experience some unwanted and unexpected behaviour in your program.

# ## Importing the modules we'll use in the course
# 
# From now on, we'll use the same modules in almost every lesson - we may add a few more modules, or utilise some different functions from these libraries, but we will always use at least these imports.
# 
# <code>plotly.offline</code> allows us to use plotly's <code>plot</code> function to create our charts without pushing them to the Plotly cloud. This is handy when we develop a chart and don't want multiple beta versions being displayed publicly. I've imported this as <code>pyo</code>,
# 
# The <code>plotly.graph_objs</code> library contains many functions which help us to create different kinds of charts; I've decided to import them all throughout the course.
# 
# On the other hand, <code>plotly.plotly</code> makes the chart and pushes it to your plotly account in the cloud. We'll use this when we're happy with the chart we've made. I've imported this as <code>py</code>
# 
# <code>pandas</code> is a great library for data analysis and manipulation. It's very powerful and very complex; a full tutorial on how to use it is far beyond the scope of this course, but there are a few functions that we'll use repeatedly, one of these being a Pandas DataFrame, which I've imported separately as we'll use it that often! We'll learn about Pandas very soon!

# In[10]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# ### What have we learnt this lesson?

# In this lesson we have learnt how to import modules into our program. We have seen how to import the whole module which allows us to access each of the functions within that module and we've also learnt that we can create shorthand 'nickname' for the module when we import it. We've seen how to import a specific function or functions from a module, and that it's possible to import all of the functions in a module, but that this should be done sparingly.
# 
# Finally, we've learnt which modules we'll be using in the course and have imported them for the first time.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
