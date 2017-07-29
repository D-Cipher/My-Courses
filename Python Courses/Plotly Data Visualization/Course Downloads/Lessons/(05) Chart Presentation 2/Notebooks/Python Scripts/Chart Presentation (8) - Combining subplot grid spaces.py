
# coding: utf-8

# # Chart Presentation 2 (8) - Combining subplot grid spaces

# In this lesson we're going to learn how to use the <code>'colspan'</code> and <code>'rowspan'</code> options to create a complex subplots object.
# 
# We're going to take a 3x3 grid of plots and combine some of them together to fit only three charts into the same space. The plot grid will start out looking like this:
# ````python
# +-----+-----+-----+
# |     |     |     |
# |     |     |     |
# +-----------------+
# |     |     |     |
# |     |     |     |
# +-----------------+
# |     |     |     |
# |     |     |     |
# +-----+-----+-----+
# 
# ````
# And finish looking like this:
# ````python
# +-----+-----+-----+
# |           |     |
# |           |     |
# +           +     +
# |           |     |
# |           |     |
# +-----------------+
# |                 |
# |                 |
# +-----+-----+-----+
# 
# ````
# We'll create this as a skeleton subplots object, and I'll leave it to you to populate it with data - please post the results in the comments section!

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
# We'll import the Plotly subplots module again:

# In[2]:

from plotly.tools import make_subplots


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Making the subplots object
# We'll make a subplots object with three rows and 3 columns, append a dummy trace to it and plot it as before:

# In[4]:

fig = make_subplots(rows = 3, cols = 3)
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (8) - Combining subplot grid spaces\pyo.iplot-0.png") 
 #

# ## Combining columns and rows
# We can use the special keyword argument <code>'specs'</code> to specify how the rows and columns are combined.
# 
# The <code>'specs'</code> parameter acts like a set of instructions which determine the behaviour of each 'cell' in the subplots grid.
# 
# The <code>'specs'</code> parameter is made of a list of lists. The indices of the outer list correspond to the rows in the subplots object, whilst the indices of the inner list correspond to columns. The instructions passed to the <code>'specs'</code> parameter must match the shape of the subplots object.
# 
# Each item in the list of lists of specs therefore corresponds to a single subplot grid space. 
# 
# The <code>'specs'</code> parameter that we will use for this subplots object will be shaped as so:
# ````python
# specs = [[{}, {}, {}],
#          [{}, {}, {}],
#          [{}, {}, {}]]
# ````
# 
# The spaces in the <code>'specs'</code> parameter will therefore correspond to the following grid spaces:
# ````python
# specs = [[{1, 1}, {1, 2}, {1, 3}],
#          [{2, 1}, {2, 2}, {2, 3}],
#          [{3, 1}, {3, 2}, {3, 3}]]
# ````
# 
# Let's add the list of specs to our subplot object:
# 

# In[5]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {}],
                            [{}, {}, {}],
                            [{}, {}, {}]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (8) - Combining subplot grid spaces\pyo.iplot-1.png") 
 #

# ## Manipulating <code>'colspan'</code> and <code>'rowspan'</code>
# 
# Each item in the list of lists of specs corresponds to a single subplot grid space. Each item can be a dictionary or <code>None</code>.
# 
# By putting <code>None</code> at that list index, we are telling Plotly that we do no wish to make any changes to that particular space. A dictionary allows us to change certain parameters.
# 
# There are several different parameters for the specs, however we will only focus on <code>'rowspan'</code> and <code>'colspan'</code> as these are sufficient for our aims.
# 
# Let's make the bottom-left cell on our grid. This will have a <code>colspan</code> of 3. We'll start the <code>colspan</code> in the bottom-left corner and therefore need to set the spec of the cell which will be overwritten (the cell immediately to the right) to <code>None</code>:

# In[6]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {}],
                            [{}, {}, {}],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (8) - Combining subplot grid spaces\pyo.iplot-2.png") 
 #

# We can now create the right-most cell, which will have a <code>rowspan</code> of two, starting in the top-right corner. The cell directly below it will therefore have a <code>None</code> value:

# In[7]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {'rowspan' : 2}],
                            [{}, {}, None],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (8) - Combining subplot grid spaces\pyo.iplot-3.png") 
 #

# Finally we can create the top-left plotting area which will have both a <code>'rowspan'</code> and <code>'colspan'</code> of 2. We'll therefore set the remaining cells to <code>None</code>:

# In[8]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (8) - Combining subplot grid spaces\pyo.iplot-4.png") 
 #

# Great, that's our plotting area finished! It's now up to you to fill this template with some beautiful charts! Post your examples in the comments section.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to use the <code>'rowspan'</code> and <code>'colspan'</code> options within the <code>specs</code> parameter to combine grid spaces on the subplots object.
# 
# We've seen that in order to successfully combine columns or rows, we need to set the <code>specs</code> of the cells which will be overwritten to 0. We've also learnt that the specs object must be of the same dimensions as the subplots object, with each index of the outer list corresponding to a row, and each index of the inner lists corresponding to a column.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
