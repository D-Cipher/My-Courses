
# coding: utf-8

# # Intro to Pandas (4) - Changing the DataFrame

# In the last lesson we saw how to create new columns in a DataFrame.
# 
# In this lesson we'll learn how to change the DataFrame itself; how to rename and drop columns, as well as how to set the index.

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


# ## Making Changes to a DataFrame
# 
# First of all, I'm going to read some data into a DataFrame:

# In[2]:

baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData.head()


# We can rename columns in a DataFrame by using the <code>df.rename()</code> function. To this function, we must pass a dictionary where the key is the old column name, and the value is the new column name.
# 
# We can choose to rename the columns in the DataFrame <code>inplace</code> - this modifies the original object. Here I'm changing the column names to be lowercase:

# In[3]:

baseRateData.rename(columns = {'VALUE' : 'value', 'DATE' : 'date'}, inplace=True)

baseRateData.head()


# If you're creating a new object from the DataFrame, you don't need to do it rename the columns <code>inplace</code>:

# In[4]:

baseRateData_r = baseRateData.rename(columns = {'value' : 'Value', 'date' : 'Date'})

baseRateData_r.head()


# We can also change the index of the DataFrame, this is helpful to do when we want to merge a DataFrame, or to use the index to select locations.
# 
# Here I'm changing the index to be the Date column using the <code>df.set_index()</code> method. I'm doing this <code>inplace</code> because I don't want to create a new object.

# In[5]:

baseRateData_r.set_index(baseRateData_r['Date'], inplace=True)

baseRateData_r.head()


# We can also drop columns by using the <code>df.drop()</code> method. 
# 
# Because we have the information about the Date contained in the index I'm now going to drop the Date column to save memory. I have to tell Pandas to drop a column by using <code>axis = 1</code> (<code>axis = 0</code> tells Pandas to drop a row).
# 
# Once again I don't want to create a new object, so I'll drop this column <code>inplace</code>:

# In[6]:

baseRateData_r.drop(['Date'], axis = 1, inplace = True)

baseRateData_r.head()


# ### What have we learnt this lesson?

# In this lesson we've seen how to make changes to the DataFrame itself; learning how to rename and drop columns, how to set the index and how to do this inplace or by creating a new object. 
# 
# In the next lesson we'll see how to access rows and columns by their label and position, and to use this positional selection to make changes to the data in the DataFrame.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
