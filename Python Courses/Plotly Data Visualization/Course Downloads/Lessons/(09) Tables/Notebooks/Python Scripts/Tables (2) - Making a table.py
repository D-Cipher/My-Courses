
# coding: utf-8

# # Tables (2) - Making a table

# In this lesson we're going to learn how make a table in Plotly.
# 
# We'll learn how to make one from a list and a Pandas DataFrame.

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


# #### New Modules:
# 
# In order to make a table in Plotly, we have to use a different library called the <code>'FigureFactory'</code>. This is an in-development part of the Plotly codebase and is liable to change without notice.
# 
# The <code>'FigureFactory'</code> gives options for creating many different types of chart . . . I suggest trying a few of them out if you're curious!

# In[2]:

from plotly.tools import FigureFactory as FF


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Making a table from a list
# 
# We can use the <code>FigureFactory.create_table()</code> function to create a table. This function actually uses the Heatmap chart type (which we won't cover in this course) to create a table, and we'll use different aspects of the Heatmap chart to make stylistic changes to our tables.
# 
# It's very simple to create a table from a list, provided that the list is in the correct format.
# 
# The list must be comprised of several sublists. Each sublist will be a row in the table, and the first sublist will be the column titles.
# 
# Let's try this out and create a table showing the population and area of the different countries in the United Kingdom. I sourced this data from <a href = "https://en.wikipedia.org/wiki/Population_of_the_countries_of_the_United_Kingdom">Wikipedia</a>.
# 
# Here's our table data with the row for the column headings and space for the data:

# In[4]:

tableData = [['Country','Population','Area (km2)'],
             [],
             [],
             [],
             []]


# Here's the table data with the values completed:

# In[5]:

tableData = [['Country','Population','Area (km2)'],
             ['England',53865800, 130395],
             ['Scotland',5327700, 78772],
             ['Wales',3082400,20779],
             ['Northern Ireland', 1829700, 13843]]


# We can now pass this into the <code>FF.create_table()</code> function and create an object to plot:

# In[6]:

UKCountries = FF.create_table(tableData)
pyo.iplot(UKCountries)


py.image.save_as(UKCountries, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (2) - Making a table\pyo.iplot-0.png") 
 #

# You can see that Plotly follows many of the recommendations for designing clear tables. The header row is a different colour, the row colours alternate, and the font allows for comparisons between the numbers.
# 
# There are still improvements to make which we will look at later in this section.
# 
# #### The structure of a table object
# 
# Let's have a look at the structure of our table object.
# 
# You can see that the data displayed in the table is not contained within the data element of the figure. The data element actually contains the instructions for colouring the rows and header.
# 
# The data displayed in the table is stored as annotations which are positioned by the <code>FF.create_table()</code> function. We will use this knowledge later to allow us to style the data in the table.

# In[7]:

UKCountries


# ## Making a table from a DataFrame
# 
# Let's get the same data that we used earlier, but rather than writing it out in a dictionary, we'll get it as a csv:

# In[8]:

df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df


# We can now pass this DataFrame directly into the <code>create_table()</code> function:

# In[9]:

UKCountryInfo = FF.create_table(df)
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (2) - Making a table\pyo.iplot-1.png") 
 #

# So you can see that the entire DataFrame gets translated into a Plotly table, but it looks a bit cramped. We could increase the size of the table to include all the information, but for now, let's reduce the number of columns. We'll take the column for 2011 because we'll use data from another source for 2011 in a later lesson in this section.

# In[10]:

df = df[['Name','Population (2011)', 'Area (km2)']]
UKCountryInfo = FF.create_table(df)
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (2) - Making a table\pyo.iplot-2.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to create a table from a list or a DataFrame using the <code>FigureFactory.create_table()</code> function.
# 
# We've seen that the <code>create_table()</code> function actually uses the Plotly heatmap as a base for the table, and that the information in the table rows is actually stored as annotations.
# 
# In the next lesson we'll learn how to add an index column to the table.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
