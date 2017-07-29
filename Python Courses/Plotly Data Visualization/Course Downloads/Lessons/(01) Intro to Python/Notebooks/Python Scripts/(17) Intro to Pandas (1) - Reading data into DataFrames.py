
# coding: utf-8

# # Intro to Pandas (1) - Reading data into DataFrames

# In the coming lessons we're going to take a brief look at the most common data analysis library in Python - Pandas. 
# 
# Pandas is a free and open-source library which let's us manipulate data structures in an easy and intuitive way. Pandas stores data in a way which means that we can pass the data straight from Pandas to Plotly with no problems - the two libraries work really well together.
# 
# Pandas is a huge module with loads of different features; some of which we'll use in this course and many of which we won't. The function which we'll use most of all is <code>DataFrame()</code>. A Pandas DataFrame stores tabular data, like an Excel spreadsheet, however in Pandas you can't access and edit the cells directly - you instead need to manipulate the data programmatically.
# 
# In this lesson I'll introduce you to the basic functionality which we'll need to create charts in Plotly:
# - How to read data in to a Pandas DataFrame
# 
# In future lessons we'll see:
# - How to access data from a Pandas DataFrame
# - How to manipulate data inside a Pandas DataFrame

# ## Module Imports

# #### Standard Modules
# 
# In a previous lesson we learnt which modules we'll be using in this course. From now on, we'll import these same modules at the start of every lesson. Here's a recap of what the modules do:
# 
# - <code>plotly.offline</code> allows us to use plotly's <code>plot</code> function to create your charts without pushing them to the cloud. This is handy when you're developing a chart and don't want multiple beta versions being displayed publicly.
# 
# - On the other hand, <code>plotly.plotly</code> makes the chart and pushes it to your plotly account in the cloud. We'll use this when we're happy with the chart we've made.
# 
# - <code>pandas</code> is a great library for data analysis and manipulation. It's very powerful and very complex; a full tutorial on how to use it is far beyond the scope of this course, but there are a few functions that we'll use repeatedly, one of these being a pandas DataFrame.

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


# You can see in the cell above that we imported the <code>pandas</code> module as <code>'pd'</code>. We can a list of the different functions available to us by typing <code>pd.</code> and pressing <code>tab</code>:

# In[2]:

pd.


# ### Reading data in to a Pandas DataFrame
# 
# Before we can pass data to Plotly, we must first obtain it! 
# 
# As part of this course, I've provided loads of different datasets which you can download from my website. All of these datasets are available in the .csv format. We can use pandas to download the .csv data directly from the website and put it straight into a DataFrame.
# 
# Pandas can also read in data in many different formats (.xls or .json for example), but as the aim of this course is to teach you how to create charts with Plotly, obtaining the data is a secondary concern - as such we'll just use data in a .csv format.
# 
# To read a .csv file into a Pandas DataFrame, we need to use the <code>pd.read_csv()</code> function. When you've opened the brackets, press <code>shift + tab</code> to see the different arguments which you can pass to the <code>read_csv()</code> function, and then run the cell.

# In[3]:

pd.read_csv()


# So, despite that the <code>read_csv()</code> function has loads of different options, the error message above tells us that we only need 1 argument to make it run, the <code>filepath_or_buffer</code> - this is the location of the .csv file, either on your local machine or on the internet.
# 
# Let's read in a .csv file. This file contains observations of the Bank of England base rate from 2/1/1975 to 23/6/16.
# 
# To access the file from where it is hosted on my website, we need to pass the URL as the argument to <code>pd.read_csv()</code>.

# In[4]:

pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")


# We can also read a .csv file from your local machine.
# 
# If the .csv is in the same folder as the Jupyter Notebook, this is really easy!

# In[5]:

pd.read_csv("BoEBaseRate.csv")


# If the .csv file is in a different location on your machine this is slightly more difficult...

# In[6]:

pd.read_csv("C:\Users\Rytch\Desktop\BoEBaseRate.csv")


# Passing the filepath directly to <code>pd.read_csv()</code> triggers a Unicode error. 
# 
# What is happening here is that the Python interpreter sees the single backslash (<code> \ </code>) as an escape character (which we learnt about in Strings (1)), and knows to pass over the escape character and instead treat the following character as text. 
# 
# We can solve this in different ways:
# 
# - Escape the escape character - replace every single backslash with a double backslash:

# In[7]:

pd.read_csv("C:\\Users\\Rytch\\Desktop\\BoEBaseRate.csv")


# - Tell Python to expect a raw string - prefix the string with an <code> r </code>

# In[8]:

pd.read_csv(r"C:\Users\Rytch\Desktop\BoEBaseRate.csv")


# It doesn't matter which you use, but I tend to use the second option to allow me to copy and paste the filepath without having to change anything.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to read data into a Pandas DataFrame. We've seen how to get the data from a .csv file hosted on the internet and a .csv file on your local machine. We've also learnt how escape characters can make it slightly more difficult to get data from your local machine, but that we can use two different options to read the data in successfully.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
