
# coding: utf-8

# # Chart presentation (5) - Setting hovertext

# In the last lesson we saw how to set specific ticklabels on the axis. 
# 
# In this lesson we'll find out how to set the hovertext and control what is displayed when a user hovers over a point on the chart.
# 
# Hovertext is one of the best features about Plotly; it's this functionality which sets it apart from static charts. Without hovertext, a user who noticed an interesting data point would have to consult a table to find the values of that data point, or read through the description of the chart to see if there is an explanation for it. With hovertext, you can provide this information directly to the user when they hover their mouse pointer over a particular data point. Creating hoverinfo which is clear and intuitive is therefore really important when creating charts with Plotly.

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


# ## Setting and controlling hovertext
# 
# There are three elements that we can manipulate to control what is displayed when a user moves their mouse over a particular data point.
# 
# The first is the <code>'text'</code> element contained within each trace object. This allows you to choose exactly what words and numbers are displayed when a user moves their mouse over a point. This attribute expects a list of values the same length as the x- and y-values. In the example below, each point of data would have one of the letters a-e attributed to it:
# 
# ````python
# trace = {'x' : [1,2,3,4,5],
#         'y' : [1,2,3,4,5],
#         'text' : ['a','b','c','d','e'],
#         'type' : 'scatter'}
# ````        
# 
# The second element which controls the hovertext is also contained within the trace. The <code>'hoverinfo'</code> element  determines which information appears when the user moves their mouse over a data point. It differs from the <code>'text'</code> attribute in that it doesn't allow you to choose the exact number and letters which are displayed, merely a more high-level view. This attribute expects a string:
# ````python
# trace = {'hoverinfo' : <'x', 'y', 'z', 'text', 'name' (or any joined with a '+'), 'all', 'none'>}
# ````
# 
# The potential values for <code>'hoverinfo'</code> have the following effects:
# - <code>'x'</code> : shows the x-values of the data over the x-axis
# - <code>'y'</code> : shows the y-values of the data at the point of hover
# - <code>'z'</code> : shows the z-values of the data at the point of hover (3d charts only)
# - <code>'text'</code> : shows the information contained in the <code>'text'</code> attribute at the point of hover
# - <code>'name'</code> : shows the name of the trace
# - <code>'all'</code> : shows all the information (except the name)
# - <code>'none'</code> : shows nothing
# 
# You can select multiple hover options by concatenating them together with a '+':
# - <code>'text+x'</code> : shows the information contained in the <code>'text'</code> attribute and the x-values
# 
# We'll investigate these different options using some dummy data before discussing the third element which controls hover info.

# In[3]:

trace = {'type' : 'scatter',
        'mode' : 'lines',
        'x' : [1,2,3,4,5,6,7,8,9],
        'y' : [4,9,6,7,5,8,1,3,2],
        'text' : ['a','b','c','d','e','f','g','h','i','j'],
        'name' : 'Testing Trace'}
pyo.iplot([trace])


py.image.save_as([trace], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (5) - Setting hovertext\pyo.iplot-0.png") 
 #

# You can see that the default behaviour is for Plotly to show the x-value at the x-axis, and the y-value and text attribute at the hoverpoint. We can get this functionality by setting the <code>'hoverinfo'</code> to <code>'text+x+y'</code>.
# 
# I'll use a function to update the hoverinfo each time:

# In[4]:

def updateHoverInfo(info):
    trace.update({'hoverinfo' : info})
    pyo.iplot([trace])


py.image.save_as([trace], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (5) - Setting hovertext\pyo.iplot-1.png") 
 #    
updateHoverInfo('text+x+y')


# Let's try some different values for <code>'hoverinfo'</code>. This shows only the x-values:

# In[5]:

updateHoverInfo('x')


# This shows only the y-values:

# In[6]:

updateHoverInfo('y')


# This shows only the name of the trace:

# In[7]:

updateHoverInfo('name')


# And this shows only the text attribute:

# In[8]:

updateHoverInfo('text')


# And this shows nothing:

# In[14]:

updateHoverInfo('none')


# This shows everything apart from the trace name:

# In[10]:

updateHoverInfo('all')


# ## Changing how the hovertext is displayed
# 
# The third element which controls the hovertext is contained within the layout. The <code>'hovermode'</code> attribute controls which hover info the user sees depending on the location of their mouse pointer relative to the points. It also changes which value is displayed on the axis and which is displayed near the mouse pointer.
# ````python
# layout = {'hovermode' : <'x', 'y', 'closest' or False>}
# ````
# 
# This attribute expects a string which can take one of three values:
# - <code>'x'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's x-position, x-value is displayed on the axis
# - <code>'y'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's y-position, y-value is displayed on the axis
# - <code>'closest'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's x- and y-positions
# - <code>'False'</code> : No hoverinfo
# 
# Let's create a layout and a Figure object and learn how changing the <code>'hovermode'</code> affects our chart:

# In[11]:

layout = {'hovermode' : 'x'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (5) - Setting hovertext\pyo.iplot-2.png") 
 #

# The hoverinformation that is shown hasn't changed, but you can see that where it is shown depends on the location of the mouse pointer relative to the x-axis. Let's set <code>'hovermode'</code> to <code>'y'</code>:

# In[12]:

layout = {'hovermode' : 'y'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (5) - Setting hovertext\pyo.iplot-3.png") 
 #

# You can see that the information shown now depends on the y-position of the cursor. The y-value is now shown next to the axis, rather than the left.
# 
# Finally, let's set <code>'hovermode'</code> to <code>'closest'</code>:

# In[13]:

layout = {'hovermode' : 'closest'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (5) - Setting hovertext\pyo.iplot-4.png") 
 #

# This now only shows the hover information when the mouse moves near a point. Furthermore, the hoverinfo which is shown is all contained near the data point.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to manipulate the <code>'text'</code>, <code>'hoverinfo'</code> and <code>'hovermode'</code> attributes to control what is displayed on hover and where.
# 
# In the next lesson we'll learn how to create a custom text field in a Pandas DataFrame, and to format this field using HTML tags to affect how it is displayed in Plotly.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
