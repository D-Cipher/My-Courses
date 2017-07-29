
# coding: utf-8

# # Lineplots (2) - Plotting Different Data

# In the last lesson we learnt how to make a simple line chart in Plotly. We learnt about the concept of a trace and discovered what structure Plotly expects the instructions to be in when it makes a chart.
# 
# In this lesson we're going to use the <code>dict.update()</code> method to plot different data in our chart.

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

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Creating a chart
# 
# We're going to use the same chart as last time.

# In[3]:

trace1 = {'type' : 'scatter',
        'x' : [0,1,2,3,4,5,6,7,8,9],
        'y' : [0,1,2,3,4,5,6,7,8,9],
        'name' : 'trace1',
        'mode' : 'lines'}


# Creating the Data object as a list of traces (one in this case):

# In[4]:

data = Data([trace1])


# ### Setting the layout

# In[5]:

layout = {'title' : "My first plotly line chart",
         'xaxis' : {'title' : 'X Values'},
         'yaxis' : {'title' : 'Y Values'}}


# ### Creating the figure object and plotting it

# Combining the Data and Layout objects into a Figure object:

# In[6]:

fig = Figure(data = data, layout = layout)


# Plotting the chart:

# In[7]:

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (02) - Plotting Different Data\pyo.iplot-0.png") 
 #
# Uncomment this to push the chart to the cloud:


# ## Updating the chart

# When we're developing a chart it can be helpful to update some of the instructions without having to rewrite everything, or to amend our previous code. Furthermore, we may want to create some slightly different versions of the same chart.
# 
# This is where Python's native <code>dict.update()</code> function comes in handy. You can pass a new dictionary to this function and it will overwrite any values in the old dictionary that are present in the new version, and add any that are only present in the new version.
# 
# To remove an option, you can use the <code>del</code> keyword, this removes the key/value pair from the dictionary.
# 
# To practise this, we'll update the data in the chart, remove the y-axis title and also change the title of our chart. 
# 
# This is trace1 before updating:

# In[8]:

trace1


# Here, I'm creating a variable which I'll pass to the update method:

# In[9]:

updatedY = {'y' : [0,3,7,2,6,9,1,4,5,8]}


# Now I can pass it to the update method:

# In[10]:

trace1.update(updatedY)

trace1


# Now, let's look at the chart with the updated Y-values. We have to recreate the Data and Figure objects because we have changed the trace:

# In[11]:

data = Data([trace1])
fig = Figure(data = data, layout = layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (02) - Plotting Different Data\pyo.iplot-1.png") 
 #

# You can see how by changing the y-values, we suddenly have a much more interesting chart.
# 
# Let's now change the chart title. This is the layout before updating:

# In[12]:

layout


# Here I'm updating the layout directly, rather than creating a variable and passing it to the update method:

# In[13]:

layout.update({'title' : 'My second Plotly line chart'})


# Let's have a look at the new chart. We only have to update the Figure object this time because we haven't changed any data:

# In[14]:

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (02) - Plotting Different Data\pyo.iplot-2.png") 
 #

# Finally, let's remove the Y-axis label using the <code>del</code> keyword.
# 
# The Y-axis is a sub-dictionary within the layout. The Y-axis title is contained within this dictionary so we first need to access the <code>'yaxis'</code> key:

# In[15]:

layout['yaxis']


# Next we need to tell the <code>del</code> keyword to only delete the <code>'title'</code> key from the <code>'yaxis'</code> dictionary:

# In[16]:

del layout['yaxis']['title']


# The layout after updating:

# In[17]:

layout


# Now, let's refresh the chart again by recreating the Figure object and plotting it:

# In[18]:

fig = Figure(data = data, layout = layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (02) - Plotting Different Data\pyo.iplot-3.png") 
 #

# You can see now how the Y-axis title has disappeared.

# ### What have we learnt in this lesson?

# In this lesson we've seen how to use the <code>dict.update()</code> and <code>del</code> keywords to make changes to our chart after creating it. We've seen how to change the data within the chart and how to affect the layout. We've also discovered that we must refresh the Data, Layout and Figure objects after making any changes.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
