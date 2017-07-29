
# coding: utf-8

# # Tables (7) - Adding hovertext

# At the start of this section we learnt that the <code>create_table()</code> function actually uses the Plotly heatmap to create a table. We also learnt that we can use some of the instructions for creating a heatmap to modify our table.
# 
# In this lesson we're going to learn how to add hovertext to a table by passing data through the <code>create_table()</code> function into the heatmap.
# 
# Adding hovertext to a table may seem a little redundant because the table itself is made of text, however we can consider the hovertext in this case as a kind of sophisticated annotation. In the section on bar charts we added an annotation which we though explained the large number of meteorites in a a particular year. In this lesson we'll add some hovertext that fills a similar role.

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


# In[2]:

from plotly.tools import FigureFactory as FF


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## How does hovertext work on a heatmap/table?
# 
# We can add hovertext by amending the figure which is returned by the create_table function.
# 
# First, let's look at how hovertext is displayed on a table. Let's get our table object and tell it to display <code>'hoverinfo' : 'all'</code>:

# In[4]:

table = py.get_figure("rmuir", 309)
table['data'][0].update({'hoverinfo' : 'all'})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (7) - Adding hovertext\pyo.iplot-0.png") 
 #

# This is quite unhelpful. The standard hoverinfo doesn't convey any interesting or helpful information.
# 
# In order to make the hoverinfo relevant, we have to include some text to display.
# 
# A heatmap expects the <code>'text'</code> parameter to be of the same shape as the <code>'z'</code> parameter, with each item in the text corresponding to an item in <code>'z'</code>.
# 
# Let's see what shape our text item must take:

# In[5]:

table['data'][0]['z']


# We therefore have to add a specific text item to be displayed over each cell in the table. 

# ## Adding a text parameter
# 
# As a useful piece of contextual information, let's add the population of the capital city of each country.
# 
# This information will be attached to the third item in every row (but the first).
# 
# Let's add some holding text to make sure we have got the right place. We will pass in an empty string for the items for which we don't want text displayed, and tell Plotly to only display text on hover:

# In[6]:

text = [['','','','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],]

table['data'][0].update({'text' : text,
                        'hoverinfo' : 'text'})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (7) - Adding hovertext\pyo.iplot-1.png") 
 #

# Now let's add the info:

# In[7]:

text = [['','','','','',''],
       ['','','<b>London</b><br>Population: 8,630,100','','',''],
       ['','','<b>Edinburgh</b><br>Population: 492,680','','',''],
       ['','','<b>Cardiff</b><br>Population: 346,100','','',''],
       ['','','<b>Belfast</b><br>Population: 333,870','','',''],]

table['data'][0].update({'text' : text})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (7) - Adding hovertext\pyo.iplot-2.png") 
 #

# I'm really happy with how that's turned out! Let's push this to the Plotly cloud:

# In[8]:

py.plot(table, filename="Population of UK Countries (hoverinfo)", fileopt="overwrite")


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (7) - Adding hovertext\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to add hovertext to our tables, and that to do so we must pass in a list of hovertext of the same shape as the <code>'z'</code> parameter of the table. each item in this nested list corresponds to a cell in the table.
# 
# In the next lesson we'll learn how to add a table to a subplots object to enable us to include tables in a dashboard.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
