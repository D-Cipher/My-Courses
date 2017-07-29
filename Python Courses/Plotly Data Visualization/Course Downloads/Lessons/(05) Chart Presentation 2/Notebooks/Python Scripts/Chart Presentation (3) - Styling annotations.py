
# coding: utf-8

# # Chart Presentation (3) - Positioning annotation text

# In this lesson we'll learn about some further styling options for annotations.
# 
# We'll learn how to position the annotation text on the chart with greater precision by using the <code>'textangle'</code>, <code>'xanchor'</code> and <code>'yanchor'</code> options.

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


# ## Using <code>'xanchor'</code> and <code>'yanchor'</code> to position annotations

# We can use the <code>'xanchor'</code> and <code>'yanchor'</code> options to position annotations relative to the point at which they were placed, binding the x (or y) position to the top/bottom/left/right/middle/center of the annotation.
# 
# - <code>'xanchor'</code> positions the annotation horizontally and can take the following values:
#     - <code>'left'</code> - the left-most part of the annotation lines up with the specified position (moves the annotation right)
#     - <code>'center'</code> - the horizontal centre of the annotation lines up with the specified position
#     - <code>'right'</code> - the right-most part of the annotation lines up with the specified position (moves the annotation left)
#     - <code>'auto'</code> - works like 'center' when positioning annotations on according to a data point
#   
#   
# - <code>'yanchor'</code> positions the annotation vertically and can take the following values:
#     - <code>'top'</code> - the top-most part of the annotation lines up with the specified position (moves the annotation down)
#     - <code>'middle'</code> - the vertical centre of the annotation lines up with the specified position
#     - <code>'bottom'</code> - the bottom-most part of the annotation lines up with the specified position (moves the annotation up)
#     - <code></code>'auto' - works like 'middle' when positioning annotations on according to a data point
# 
# Let's see this in action.
# 
# We're going to make a trace with a single point which will also act as the annotation's anchor point; we will then find out how to move the annotation relative to this point by using the <code>'xanchor'</code> and <code>'yanchor'</code> options.

# In[8]:

trace = [{'type' : 'scatter',
         'x' : [5],
         'y' : [5],}]
layout = {'annotations' : [{'text' : 'Testing',
                          'xref' : 'x',
                          'yref' : 'y',
                           'x' : 5,
                           'y' : 5,
                           'showarrow' : False,
                           'font' : {'size' : 16}}]}
fig = {'data' : trace, 'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-0.png") 
 #

# Let's try varying the <code>'xanchor'</code> and <code>'yanchor'</code> values:

# In[10]:

fig['layout']['annotations'][0].update({'xanchor' : 'left'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-1.png") 
 #

# In[11]:

fig['layout']['annotations'][0].update({'yanchor' : 'bottom'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-2.png") 
 #

# In[12]:

fig['layout']['annotations'][0].update({'xanchor' : 'right'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-3.png") 
 #

# You can see how these two options give us a grid of 9 spaces where we can place the text around the the central point.
# 
# ## Using <code>'textangle'</code>
# 
# We can specify the <code>'textangle'</code> to change the angle at which the text is drawn in relation to the horizontal (0). <code>'textangle'</code> must be an integer:

# In[13]:

fig['layout']['annotations'][0].update({'textangle' : 45})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-4.png") 
 #

# In[14]:

fig['layout']['annotations'][0].update({'textangle' : 90})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (3) - Styling annotations\pyo.iplot-5.png") 
 #

# You can see how this rotates the text around the anchor point, taking into account the xanchor and yanchor options.

# ### What have we learnt this lesson?

# In this lesson we've seen how to have finer control over where the annotations are positioned on the chart. We've used the <code>'xanchor'</code>, <code>'yanchor'</code> and <code>'textangle'</code> options to move the annotation relative to its anchor point.
# 
# In the next lesson we'll learn how to position annotations outside the chart area.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
