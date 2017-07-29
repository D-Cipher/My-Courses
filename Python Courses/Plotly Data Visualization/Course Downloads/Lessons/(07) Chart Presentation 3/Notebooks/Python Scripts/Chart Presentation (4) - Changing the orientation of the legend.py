
# coding: utf-8

# # Chart Presentation (4) - Changing the orientation of the legend

# In this lesson we're going to find out how to change the orientation of the legend from vertical to horizontal. This can be useful when you have legend items with long names, and limited horizontal space in which to place the chart. Placing the legend items above or below the chart can give you more options when styling your chart to make it clear to your user.

# ## Module Imports

# In[2]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Changing the orientation of the legend

# We can change the orientation of the legend by setting the <code>'orientation'</code> parameter to either <code>'h'</code>, for a horizontally-oriented legend, or <code>'v'</code> for a vertically-oriented legend. The default setting is <code>'v'</code>.
# 
# Let's get the chart that we made in the previous lesson to practise on:

# In[9]:

stacked = py.get_figure("rmuir", 259)
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (4) - Changing the orientation of the legend\pyo.iplot-0.png") 
 #

# Let's now change the orientation of the legend to horizontal. You can see how Plotly has retained the legend grouping when moving the legend to horizontal:

# In[11]:

stacked['layout']['legend'].update({'orientation' : 'h'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (4) - Changing the orientation of the legend\pyo.iplot-1.png") 
 #

# I'll now remove the grouping using <code>'traceorder'</code>. This shows the legend items in a long line:

# In[12]:

stacked['layout']['legend'].update({'traceorder' : 'normal'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (4) - Changing the orientation of the legend\pyo.iplot-2.png") 
 #

# This legend isn't positioned very well, let's improve this! I used trial and error to find the best position for it:

# In[13]:

stacked['layout']['legend'].update({'y' : 1.125})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (4) - Changing the orientation of the legend\pyo.iplot-3.png") 
 #

# Part of the legend item for the line trace is now chopped off. We need to increase the width of the chart to account for this:

# In[17]:

stacked['layout'].update({'width' : 1050})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (4) - Changing the orientation of the legend\pyo.iplot-4.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to change the orientation of the legend from vertical to horizontal by changing the <code>'orientation'</code> to <code>'v'</code> or <code>'h'</code> respectively.
# 
# We've also seen that we may want to reposition the legend after changing the orientation.
# 
# In the final lesson in this section we'll learn how to change the background colour of the plotting area.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
