
# coding: utf-8

# # Pie charts (7) - Using pie charts in a sub-plots object

# In this lesson we're going to learn how to position pie charts in a Plotly subplots object. This will allow us to include pie charts in any dashboard we make; an important goal!
# 
# Pie charts and subplots objects interact differently in Plotly because, unlike a standard bar or line chart, Pie charts have no concept of an x- or y-axis. Plotly therefore does not understand how to map the range of the data in a pie chart, to the domain which it occupies on the dashboard. We therefore  have to specify this domain ourselves.

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


# We're also going to get the make_subplots function:

# In[2]:

from plotly.tools import make_subplots


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Making a subplots object
# 
# Our first step is to make a subplots object so we can understand more about how to set the domain for cells on the subplot:

# In[4]:

sub = make_subplots(rows = 2, cols = 2)
sub


# We can see from outputting the subplots object, that each x- and y-axis has a domain. The domain is in normalised coordinates; it runs from 0 to 1.
# 
# Each axis has a separate domain, and in a 2x2 subplots object, the y-axes have a domain of either <code>[0.0, 0.425]</code> or <code>[0.575, 1.0]</code>, whilst the x-axes have a domain of either <code>[0.0, 0.45]</code> or <code>[0.55, 1.0]</code>.
# 
# Let's add a simple line chart to the subplots object and see how the domain is treated at a trace level:

# In[5]:

sub.append_trace({'type' : 'scatter',
                 'mode' : 'lines+markers',
                 'x' : [1,2,3],
                 'y' : [1,2,3]}, row = 1, col = 1)

pyo.iplot(sub)


py.image.save_as(sub, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-0.png") 
 #

# Let's have a look at the printed subplots object:

# In[6]:

sub


# The domain for a normal (x/y anchored trace) is set by linking the x- and y-axes in the trace to the x- and y-axes in the layout. This is done by the <code>make_subplots()</code> function when we specify <code>row = 1</code> and <code>col = 1</code>.
# 
# We don't have this luxury when adding pie charts to a subplots object. Instead we must specify the domain of the chart directly, and append the trace to the data portion of the subplots object using the Python <code>list.append()</code> function.

# ## Setting the domain for pie traces
# 
# Let's try this out. I'm going to load a pie chart that we've created in this section and append the trace to the data object in the figure:

# In[7]:

eth = py.get_figure("rmuir", 267)
pyo.iplot(eth)


py.image.save_as(eth, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-1.png") 
 #

# Let's now take the data from the <code>eth</code> pie chart and append it to the data in the <code>sub</code> subplots object. In order for this trace to be accepted, we must specify a domain in the form:
# ````python
# 'domain' : {'x' : [min, max],
#             'y' : [min, max]}
# ````
# I'm going to place this trace in the top-right cell of the subplots object, in cell x2/y2. This means that we must specify the domain as:
# ````python
# 'domain' : {'x' : [0.55, 1.0],
#             'y' : [0.575, 1.0]}
# ````

# In[8]:

pieData = eth['data'][0]
pieData.update({'domain' : {'x' : [0.55, 1.0],
                            'y' : [0.575, 1.0]}})
sub['data'].append(pieData)
pyo.iplot(sub)


py.image.save_as(sub, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-2.png") 
 #

# Great! So we've got a pie chart on a subplots object. Excellent! It looks a bit messy though. Let's set the specs of the subplots object to remove the axis objects in the cell where we've positioned the pie chart:

# ## Hiding axis objects in a cell
# 
# There are two ways of hiding the axis for a particular cell in the subplots object. The first is to set the specs of the subplots object to create an empty cell, and the second is to hide all of the visible parts of the axis objects.
# 
# We'll look at both methods.
# 
# ### Creating an empty cell
# 
# We have to set the specs of the subplots object when we create it. If you remember from the bar chart section, we pass a nested list of dictionaries to the <code>specs</code> parameter, and can set a particular cell to <code>'none'</code> to suppress the axis part of that cell.
# 
# Let's now remake our subplots object with specs, and then pass in the data again to populate it.
# 
# We don't have to pass specs for cells we don't want to modify; an empty dictionary will suffice. I'm also only setting the title for the cell that we're going to put the pie chart in.

# In[9]:

fig = make_subplots(rows = 2, cols = 2,
                   specs = [[{}, None],
                            [{}, {}]])
fig


# We can now pass in the pie chart trace that we modified previously:

# In[10]:

fig['data'].append(pieData)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-3.png") 
 #

# Because the cell doesn't exist, we can't put a title on our pie chart directly; we can set this by using annotations, or we can hide the axis object rather than removing it...
# 
# ### Hiding the axis object
# 
# The parameters within the axis object that we have to change in order to make the axis invisible are:
# - <code>'zeroline'</code> - set this to False
# - <code>'showgrid'</code> - set this to False
# - <code>'showticklabels'</code> - set this to False
# - <code>'showline'</code> - set this to False
# 
# Let's remake our figure object and set a title for the cell where we'll put our pie chart:

# In[11]:

fig = make_subplots(rows = 2, cols = 2,
                   subplot_titles = ['', 
                                    "Ethicity of UK Students",
                                    '',
                                    ''])
fig['data'].append(pieData)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-4.png") 
 #

# Now we can amend the layout for the x2 and y2 axes, and also change the domain of the pie chart slightly so that it doesn't overlap the title - we'll move the y-domain down. Note that we could also move the subplot title up, as it is stored as an annotation within the subplots object.

# In[13]:

hideAxis = {'zeroline' : False,
            'showgrid' : False,
            'showticklabels' : False,
            'showline' : False,}
fig['layout']['xaxis2'].update(hideAxis)
fig['layout']['yaxis2'].update(hideAxis)

fig['data'][0].update({'domain' : {'x' : [0.55, 1.0],
                                    'y' : [0.525, 0.95]}})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (7) - Using pie charts in a sub-plots object\pyo.iplot-5.png") 
 #

# You can see that each of these methods have their own positives and drawbacks:
# - By setting the subplot grid cell to be blank, we have to manually insert and position an annotation, but we do get to have more control over where the pie chart is places.
# - By keeping the subplot grid cell as an axis, but suppressing any visible parts of that axis we can easily place a title near our pie chart. This comes at the expense of flexibility and control in where we place our pie chart.
# 

# ### What have we learnt this lesson?

# In this lesson we've learnt how to place a pie chart in a subplots object by setting the domain directly. 
# 
# We've also seen that there are two ways of hiding the axis object in a subplot grid:
# - We can set a particular cell in the subplots object to be empty, but we have to place the title as an annotation.
# - Alternatively we can hide the axis components and use the title option provided for that cell.
# 
# In the next lesson we'll practise placing pie charts in a subplots object and adding title annotations to them. We'll also see how to size the pie charts relative to each other, so that the user can understand the size of the total population that a particular pie chart represents.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
