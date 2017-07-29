
# coding: utf-8

# # Tables (4) - Changing the colours in a table

# In this lesson we're going to learn how to change the colours in our table. This is useful because it allows us to style our table to fit the theme of other charts we produce.

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
# Not forgetting the FigureFactory!

# In[2]:

from plotly.tools import FigureFactory as FF


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting a table to practise on
# 
# Let's get the chart we created in the last lesson:

# In[4]:

table = py.get_figure("rmuir", 313)
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (4) - Changing the colours in our table\pyo.iplot-0.png") 
 #

# ## How are the colours set on this table?
# 
# We learnt previously that a Plotly table is actually made from a heatmap. There are certain parameters in the Plotly heatmap that control what colour a particular section is.
# 
# We don't need to learn how to make a heatmap to change these, but let's look at the data part of our table and find out how the colour is specified: 

# In[5]:

table['data']


# You can see that the data items have a <code>'colorscale'</code> specifed, and that this colorscale is a list of three lists. The first list links together a colour with the value 0, the second links a colour to the value 0.5, and the third links a colour to the value 1.

# In[6]:

table['data'][0]['colorscale']


# Now, when we look at the <code>'z'</code> parameter within the data, you will notice that this is a list of lists, each populated by one of three numbers: 0, 0.5 and 1.
# 
# Each list within the <code>'z'</code> parameter relates to a row on the table. The first list in the <code>'z'</code> parameter is populated entirely by zeroes. The cells in the top row therefore all have the colour <code>'#00083e'</code>.
# 
# The second list in the <code>'z'</code> parameter has a 0, which relates to the first column, followed by five 0.5 values. This means that the first cell in the second row (the index cell) is dark in colour (<code>'#00083e'</code>), whilst the other cells in that row are coloured a light grey (<code>'#ededee'</code>).

# In[7]:

table['data'][0]['z']


# ## Controlling the colours in a table
# 
# We can control the colours in the table by changing the colours in the <code>'colorscale'</code> parameter. 
# 
# The text in our table has already had the colours set. The text in the header and index is white, whilst the text in the rows is dark. I chose these colours so that they will allow the text to contrast against the background colour.
# 
# Let's now change the <code>'colorscale'</code> parameter, remembering that 0 should be a dark colour and 0.5 and 1 specify the colours to be used alternately in the rows:

# In[8]:

table['data'][0]['colorscale'] = [[0, "#2f4b4e"],
                                 [0.5, "#86e6ca"],
                                 [1, "#ffffff"]]
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (4) - Changing the colours in our table\pyo.iplot-1.png") 
 #

# Let's try a different colour scheme:

# In[9]:

table['data'][0]['colorscale'] = [[0, "#a73830"],
                                  [0.5, "#fbcab9"],
                                 [1, "#ffffff"]]
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (4) - Changing the colours in our table\pyo.iplot-2.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learn how to change the colour of our tables by changing the <code>'colorscale'</code> parameter. 
# 
# We've seen that we should specify a dark colour for the header and index columns (0 in the colorscale parameter), and then by setting values for 0.5 and 1 we can set the colours to be used alternately in the row banding.
# 
# In the next lesson we'll find out how to format the text that appears inside the table.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
