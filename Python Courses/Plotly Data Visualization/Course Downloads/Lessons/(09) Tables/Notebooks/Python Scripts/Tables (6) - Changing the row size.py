
# coding: utf-8

# # Tables (6) - Changing the row size

# We saw at the start of this section how important it is to add space to our table. Adding space can stop our readers from becoming overwhelmed by the amount of data and aids in their understanding of the table, but adding too much can make the table difficult to read as the rows and columns seem unconnected.
# 
# We've previously seen how to change the amount of horizontal spacing by adding and removing columns. Here we'll learn how to change the amount of vertical space.

# ## Module Imports

# In[7]:

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
# FigureFactory:

# In[8]:

from plotly.tools import FigureFactory as FF


# In[9]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Increasing the amount of vertical space
# 
# Because we have to specify the amount of vertical spacing when we create the table, we have to remake the table from the previous lesson:

# In[10]:

df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df = df[['Name','Population (2011)', 'Area (km2)']]
df.set_index('Name', drop = True, inplace = True)
df


# When we make the table we can change the <code>height_constant</code> from its default value of 30 to increase or decrease the amount of space in the table.
# 
# Reducing it to 10 gives us a very compact table:

# In[11]:

pyo.iplot(FF.create_table(df, index=True, index_title='Country',height_constant = 10))


py.image.save_as(FF.create_table(df, index=True, index_title='Country',height_constant = 10), r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (6) - Changing the row size\pyo.iplot-0.png") 
 #

# Whilst increasing it to 50 gives us a more spacious table:

# In[12]:

pyo.iplot(FF.create_table(df, index=True, index_title='Country',height_constant = 50))


py.image.save_as(FF.create_table(df, index=True, index_title='Country',height_constant = 50), r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (6) - Changing the row size\pyo.iplot-1.png") 
 #

# It's best for you to decide on the right amount of spacing for your table and tailor that to each specific use case.

# ### What have we learnt this lesson?

# In this lesson we've seen how to change the vertical spacing in our tables by changing the <code>height_constant</code> parameter when we make the table.
# 
# In the next lesson we'll find out how to add hovertext to a table.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
