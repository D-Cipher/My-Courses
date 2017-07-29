
# coding: utf-8

# # Chart Presentation (7) - Changing subplot options

# We'll now move away from annotations for a couple of lessons and instead learn some different ways we can control the Plotly sub-plots figure.
# 
# In this lesson we'll see how to change the horizontal and vertical spacing between the different plots within the subplots object.

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
# We'll import the <code>subplots</code> library:

# In[2]:

from plotly.tools import make_subplots


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Making a subplots object
# 
# We're going to make a dummy subplots object which we'll use to demonstrate changing the horizontal and vertical spacing:

# In[4]:

testFig = make_subplots(rows = 2, cols = 2)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-0.png") 
 #

# ## Changing the horizontal spacing
# 
# The easiest way of changing the horizontal and vertical spacing of the subplots object is by using the <code>horizontal_spacing</code> and <code>vertical_spacing</code> options. Each of these options requires a float between 0 and 1:

# In[5]:

testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-1.png") 
 #

# You can see that setting <code>horizontal_spacing</code> to 0 moves the subplots next to each other on the horizontal axis. Likewise, setting it to 1 moves them further apart:

# In[6]:

testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0.95)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-2.png") 
 #

# We probably wouldn't want to ever make a plot like this, but you can now see the range of values available. Let's return it to the default of 0.2:

# In[7]:

testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0.2)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-3.png") 
 #

# ## Changing the vertical spacing
# Let's now change the vertical spacing between the different charts on the subplots object. 
# 
# We'll first set it to the minimum value of 0:

# In[8]:

testFig = make_subplots(rows = 2, cols = 2,
                       vertical_spacing = 0)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-4.png") 
 #

# This has the expected effect of moving the plots closer together in the vertical dimension.
# 
# Increasing this to a value near the maximum produces the following result:

# In[9]:

testFig = make_subplots(rows = 2, cols = 2,
                       vertical_spacing = 0.95)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)


py.image.save_as(testFig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (7) - Changing subplot options\pyo.iplot-5.png") 
 #

# So once agains, we're unlikely to ever make a plot that looks like this, but this should give you some idea of the magnitude of the effect you expect from manipulating the <code>vertical_spacing</code> option.

# ### What have we learnt this lesson?

# In this lesson we've seen how to style our subplots object by moving the charts closer together and further apart in the horizontal and vertical dimensions.
# 
# In the next lesson we'll find out how to combine different grid spaces on the subplot object. This will enable us to produce complex subplots which can show data in subtley different ways.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
