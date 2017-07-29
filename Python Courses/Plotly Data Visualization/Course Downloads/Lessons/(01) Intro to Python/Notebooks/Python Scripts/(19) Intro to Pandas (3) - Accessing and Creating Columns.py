
# coding: utf-8

# # Intro to Pandas (3) - Accessing and Creating Columns

# In the last lesson we saw how to implement some useful functions and methods to help us describe a DataFrame. 
# 
# In this lesson we'll learn how to access data in a DataFrame. We'll also learn how to create new columns from existing columns and from a list. These skills are essential to be able to plot data with Plotly as we'll often want to plot the data in different ways - being able to do some basic data manipulation will be really helpful. 
# 
# The content in the next few lessons is by no means an exhaustive list of what you can do with Pandas, and we will introduce some more functionality as we progress with the course, but the material presented here is enough to get us started.

# ## Module Imports

# In[1]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# ## Accessing columns in a DataFrame
# 
# First of all, I'm going to read some data into a DataFrame:

# In[2]:

baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData.head()


# We access the data held in each column in the same way that we would access a dictionary's values by the key. This is the most common aspect of a DataFrame which we'll use in this course. 

# In[3]:

baseRateData['VALUE']


# We can also access these values by using a <code> . </code>. Which option to use is not important, I prefer using the dictionary-like option because it's familiar to me, and the syntax highlighting makes it obvious that I'm accessing a column rather than a method.

# In[4]:

baseRateData.VALUE


# We can get the minimum, maximum and mean values for a particular column:

# In[5]:

baseRateData['VALUE'].max()


# In[6]:

baseRateData['VALUE'].min()


# In[7]:

baseRateData['VALUE'].mean()


# ## Creating New Columns in a DataFrame
# 
# We can create new columns in a DataFrame in the same way that we create new keys and values in a Dictionary.
# 
# Here, I'm creating a new column which stores the base rate data as a proportion rather than a percentage:

# In[8]:

baseRateData['VALUE_PROP'] = baseRateData['VALUE'] / 100

baseRateData.head()


# We can also create a new column from a list. 
# 
# Imagine that we wanted to set the colour of the data point depending on the value of the base rate, for example if the base rate drops below 5, we could colour this green, otherwise it would be coloured red.
# 
# In the cell below, I'm looping through each value in the VALUE column, and appending a new item to the list <code>colours</code> depending on the value of VALUE:

# In[9]:

colours = []

for row in baseRateData['VALUE']:
    if row < 5:
        colours.append('Green')
    else:
        colours.append('Red')


# I can now create a new column directly from the list:

# In[10]:

baseRateData['COLOUR'] = colours


# Let's check that this has worked by looking at the top and bottom five rows:

# In[11]:

baseRateData.head()


# In[12]:

baseRateData.tail()


# ### What have we learnt this lesson?

# In this lesson we've learnt how to get the data from a column in a DataFrame, and that this data exists in a format which can be passed straight to Plotly. We've also learnt how to create new columns by applying a mathematical operation directly to an existing column, as well as creating a new column from a list.
# 
# In the next lesson we'll see how to make changes to the DataFrame itself; learning how to rename and drop columns and how to set the index.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
