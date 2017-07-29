
# coding: utf-8

# # Intro to Pandas (5) - Accessing and Changing Specific Observations

# In the last lesson we saw how to rename and drop columns, and to set the index in a DataFrame.
# 
# In this lesson we'll learn about positional and label-based selection and how to use this to make changes to specific observations.

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


# ## Positional and Label-based Selection
# 
# First of all, I'm going to read some data into a DataFrame. I also need to make another DataFrame which has a label-based index rather than a positional index.

# In[2]:

baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData_r = baseRateData.rename(columns = {'VALUE' : 'Value', 'DATE' : 'Date'})
baseRateData_r.set_index(baseRateData_r['Date'], inplace=True)
baseRateData_r.drop(['Date'], axis = 1, inplace = True)


# Let's have a look at these DataFrames:

# In[3]:

baseRateData.head()


# In[4]:

baseRateData_r.head()


# #### Selecting observations in a DataFrame
# 
# We can select observations from a DataFrame by using <code>df.loc</code> and <code>df.iloc</code>.
# 
# - <code>df.loc</code> selects the observations by their index label
# - <code>df.iloc</code> selects the observations by their position
# 
# Here, I'm using <code>df.loc</code> to select the first 10 rows from <code>baseRateData</code>. Note that <code>df.loc</code> doesn't work like a list slice in Python; rather than stopping before the specified number, we include that observation:

# In[5]:

baseRateData.loc[:9]


# If I try to use <code>df.loc</code> on <code>baseRateData_r</code>, this won't work because we have changed the index label:

# In[6]:

baseRateData_r.loc[:9]


# Instead I have to pass the row index label which I want:

# In[7]:

baseRateData_r.loc[:'15/01/1975']


# But <code>df.iloc</code> works the same on both DataFrames because in <code>baseRateData</code>, the index is equal to the position - <code>df.iloc</code> works on the ordinal position of the rows.
# 
# Confusingly, <code>df.iloc</code> works in the same way as list and string slicing, stopping just before the specified position:

# In[8]:

baseRateData.iloc[:9]


# In[9]:

baseRateData_r.iloc[:9]


# For both <code>df.loc</code> and <code>df.iloc</code>, we can take a slice from the middle of the DataFrame:

# In[10]:

baseRateData_r.loc['06/01/1975':'13/01/1975']


# In[11]:

baseRateData.iloc[4:6]


# We can also combine the column names with <code>df.loc</code> and <code>df.iloc</code> to get 2D slices of a DataFrame.
# 
# Remember that <code>df.loc</code> works on the labels:

# In[12]:

baseRateData.loc[5:13, 'DATE']


# But <code>df.iloc</code> operates on the index; the columns are numerically indexed (in the same way as the rows):

# In[13]:

baseRateData.iloc[5:13, 0]


# ### Changing Data in a DataFrame
# 
# So now we can select individual rows and columns in a DataFrame by the index label or position. We can use this knowledge to make changes to specific observations within the DataFrame.
# 
# Imagine that we were told that the first twenty rows of our data were incorrect; they should have been 1.15 instead of 11.5. Let's make some changes!
# 
# First of all, I'm using <code>df.loc</code> to select the first 20 rows by label and only the 'VALUE' column. It's just a simple matter of setting the value which we want these observations to take:

# In[14]:

baseRateData.loc[:19, 'VALUE'] = 1.15

baseRateData.head(25)


# We can also do it with <code>df.iloc</code>. Remember that the slicing is slightly different...
# 
# I'll change it instead to 2.15 so we can prove it works:

# In[15]:

baseRateData.iloc[:20, 0] = 2.15

baseRateData.head(25)


# ### What have we learnt this lesson?

# In this lesson we've seen how to access rows and columns by their label and position, and to use this positional selection to make changes to the data in the DataFrame.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
