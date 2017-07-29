
# coding: utf-8

# # Intro to Pandas (2) - Useful DataFrame Functions

# In the last lesson we saw how to read data into a Pandas DataFrame from a .csv file on the internet or on your local machine and we also saw how to account for escape characters when reading a .csv file from a different folder in your local machine.
# 
# In this lesson we're going to look at some useful DataFrame functions and methods. Whilst we won't use these directly to plot data, utilising these will make your life a lot easier!

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


# ## Using DataFrames

# Before we can learn about some useful DataFrame functions, we first need to create one. This time I'm going to assign the DataFrame to an object, rather than just display it.
# 
# We can see the DataFrame by typing the object name on its own line:

# In[2]:

baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData


# This DataFrame is really long, and it's a pain to keep scrolling up to see the column names. We can use <code>df.head(x)</code> to see the top x rows (df is the conventional abbreviation for DataFrame, which I'll use throughout the course). 
# 
# The default number of rows is 5. Note that this doesn't change the DataFrame, merely how it is displayed on the screen.

# In[3]:

baseRateData.head(10)


# In[4]:

baseRateData.head()


# We can also see the bottom x rows using <code>df.tail(x)</code>. Once again, the default is 5.

# In[5]:

baseRateData.tail(5)


# That's much more manageable!
# 
# Before we start looking at more useful functions, let's take a quick tour of a DataFrame.
# 
# You can see that this DataFrame has 10,486 rows (remember, Python is zero-indexed!) and 3 columns. The left-most column (in bold) is called the index. The index of the DataFrame doesn't necessarily hold any data; instead it allows us to access the data by its location.
# 
# We can also see the column names of the DataFrame. Used in conjunction with the index, we can reference an exact cell within the DataFrame.
# 
# We can get some more information about the DataFrame by using the <code>df.info()</code> method.

# In[6]:

baseRateData.info()


# This tells us that we are inspecting a DataFrame and that the DataFrame has 10,486 rows (indexed from 0-10,485), and 2 data columns (the index doesn't hold data). It also gives us some information about the type of data stored in each column, as well as the approximate amount of RAM used to hold it.
# 
# We can get some statistical information on numeric columns by using the <code>df.describe()</code> method:

# In[7]:

baseRateData.describe()


# This has given us some summary statistics for the <code>VALUE</code> column, for example we can see that the average base rate for the time period is 7.14%. This is useful to allow you to get an idea of the shape of your data - if it does not look as you expect after plotting it, something may have gone wrong along the way!

# Finally, we can get the column names in a DataFrame and store it in a list. This is helpful when we want to plot different data columns on the same chart - we can loop through the column names.

# In[8]:

baseRateData.columns.tolist()


# ### What have we learnt this lesson?

# In this lesson we've seen how to restrict the amount of rows that are shown when we view the DataFrame using <code>df.head()</code> and <code>df.tail()</code>. We've also learnt how to describe the DataFrame object, as well as how to obtain some summary statistics.
# 
# In the next lesson we'll see how to select and access data from a DataFrame.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
