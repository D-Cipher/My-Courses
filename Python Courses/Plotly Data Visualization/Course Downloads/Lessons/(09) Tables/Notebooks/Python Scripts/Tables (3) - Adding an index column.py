
# coding: utf-8

# # Tables (3) - Adding an index column

# In this lesson we're going to learn how to add an index column to the left of our table. Using an index column can help people to find data more easily in the table.
# 
# Which column to include as an index column is a matter of preference, but it's a good idea to set the index column so that the data contained in that row describes the item named in the column.
# 
# For example, in a table of countries by population, you would probably choose the Country as the index column, rather than the population. Likewise, in a table displaying stock prices, you might put the date or the company as the index column, rather than the closing price.

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
# Let's import the FigureFactory again:

# In[2]:

from plotly.tools import FigureFactory as FF


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Setting an index column
# 
# Throughout this course we have generally used DataFrames to store the data for our charts. A Pandas DataFrame already has an index and we can leverage this property to create an index in a Plotly table.
# 
# In order to set the index column in a DataFrame as the index column in a Plotly table, we specify <code>index = True</code> when calling the <code>create_table()</code> function.
# 
# Let's get some data and try this out. This is the same data we used in the previous lesson:

# In[5]:

df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)

df = df[['Name','Population (2011)', 'Area (km2)']]
df


# Let's now plot this with <code>index = True</code> and see what the index column looks like:

# In[6]:

UKCountryInfo = FF.create_table(df, index='True')
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\pyo.iplot-0.png") 
 #

# So we definitely have an index column; it's the same colour as the column titles, but this index column doesn't really add much to the table. Let's try changing the index column in the Pandas DataFrame.
# 
# We'll use the <code>DataFrame.set_index()</code> function to do this. We need to tell this function which column to use as the index. We also want to drop that column from the table, and do all of this in place:

# In[7]:

df.set_index('Name', drop=True, inplace = True)
df


# Let's try creating a Plotly table from this DataFrame:

# In[8]:

UKCountryInfo = FF.create_table(df, index=True)
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\pyo.iplot-1.png") 
 #

# ## Adding a title to the index column
# 
# We can also specify a title for the index column by specifying an <code>index_title = ''</code> in the function call. A title on the index is not necessary in every table (certainly not in this example), but is definitely useful to know:

# In[9]:

UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\pyo.iplot-2.png") 
 #

# Explain option 2

# ## Changing the size of the index column
# 
# You might notice that, especially in a table with as few columns as this one, the index column dominates the table somewhat. Whilst we have no direct way of setting the width of the columns, we can trick Plotly into reducing the width of all of this columns together by passing in some empty columns.
# 
# Let's add in three empty columns to our DataFrame; one between the index and the Population column, and another between Population and Area, and a final one after Area.
# 
# We'll set the column names to be spaces; 1 space, 2 spaces and 3 spaces respectively to ensure that all the columns have different names. The data held in each column will be an empty string:

# In[10]:

df[" "] = ""
df["  "] = ""
df["   "] = ""
df


# Let's now reorder the columns:

# In[11]:

df = df[[' ', 'Population (2011)', '  ', 'Area (km2)', '   ']]
df


# And plot our new table:

# In[12]:

UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\pyo.iplot-3.png") 
 #

# And sent it to the Plotly cloud:

# In[13]:

py.plot(UKCountryInfo, filename='UK Country Population Info', fileopt = 'Overwrite')


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\py.plot-0.png") 
 #

# ## Changing the size of the columns by changing the size of the table
# 
# As well as adding more columns to the table in order to spread out the existing columns and reduce the size of the index, we can also change the width of the table itself.
# 
# Adding new columns is useful when the table must fill a particular space, however if the table is standalone, or does not have to fill a particular width, we can reduce the width to reduce the size of all the columns.

# In[16]:

df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df = df[['Name','Population (2011)', 'Area (km2)']]
df.set_index('Name', drop=True, inplace = True)

UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
UKCountryInfo['layout'].update({'width' : 500})
pyo.iplot(UKCountryInfo)


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\pyo.iplot-4.png") 
 #

# In[17]:

py.plot(UKCountryInfo, filename='UK Country Population Info (Small)', fileopt = 'Overwrite')


py.image.save_as(UKCountryInfo, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (3) - Adding an index column\py.plot-1.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to add an index column to our Plotly table. 
# 
# We've seen that the Plotly table takes the index straight from the Pandas DataFrame, and that we can set a specific column in the DataFrame to be the index using the <code>df.set_index()</code> function. We can also specify a title for the index column.
# 
# Finally, we've seen how to trick Plotly into making a smaller index column by creating some empty columns in our DataFrame to reduce the size of all the columns together.
# 
# In the next lesson we'll see how to set the colour for the rows, the index column and the column headers.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
