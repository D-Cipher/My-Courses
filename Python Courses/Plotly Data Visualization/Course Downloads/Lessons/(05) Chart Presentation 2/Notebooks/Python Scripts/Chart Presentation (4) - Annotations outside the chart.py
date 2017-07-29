
# coding: utf-8

# # Chart Presentation (4) - Annotations outside the chart

# In this lesson we'll learn about some further styling options for annotations.
# 
# We'll learn how to set the position of annotations using normalised coordinates which correspond to the area which contains the chart (the 'paper') rather than by using the coordinates of a data point on the chart. 
# 
# This allows us to consistently position annotations in a specific area of the chart without having to make any reference to the data. 
# 
# This is especially useful when making a chart that will be updated with different data - you may want an annotation at a specific point on the chart, but when making reference to the data, this specific point will move. Using normalised coordinates prevents this from happening.

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


# ## Normalised paper coordinates
# 
# Whereas we can position annotations relative to the data, it's often helpful to position them relative to the chart itself. To do this, we must set <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code>. This allows us to use normalised coordinates to refer to points on and around the chart.
# 
# With <code>'xref'</code> and <code>'yref'</code> set to <code>'paper'</code>, a value of 0 for  <code>'x'</code> would set the point of the annotation to be the left-hand side of the plotting area (on the y-axis), whereas a value of 1 would set the annotation at the right-hand side of the plotting area.
# 
# It follows that a value of 0 for <code>'y'</code> would position the annotation at the botton of the plotting area, and a value of 1 would position it at the top.
# 
# Let's see this in action.
# 
# We're going to create a dummy trace and four annotations; each will be placed at one corner of the plotting area. The default values for text-anchor will position the annotations at the left and right of the anchor point. We must also set a specific range:

# In[3]:

trace = [{'type' : 'scatter'}]
layout = {'annotations' : [{'text' : 'x = 0, y = 0',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'x = 1, y = 0',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'x = 0, y = 1',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : 1,
                           'showarrow' : False},
                          {'text' : 'x = 1, y = 1',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 1,
                           'showarrow' : False}],
         'xaxis' : {'range' : [0, 10]},
         'yaxis' : {'range' : [0, 10]}}
fig = Figure(data = trace, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (4) - Annotations outside the chart\pyo.iplot-0.png") 
 #

# Now let's try changing the range to something very different to make sure that the annotations stay in the same point:

# In[4]:

fig['layout']['xaxis']['range'] = [50, 200]
fig['layout']['yaxis']['range'] = [0, 0.5]
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (4) - Annotations outside the chart\pyo.iplot-1.png") 
 #

# ## Placing annotations outside of the plotting area
# 
# We can set the x- and y-coordinates to a negative number to place annotations to the left of (or below) the plotting area. We could also set the x- and y-coordinates to a number >1 to place annotations or to the right of (or above) the plotting area.
# 
# Let's test this out:

# In[5]:

fig['layout']['annotations'] = [{'text' : 'Left of the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : -1,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'Right of the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 2,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'Below the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : -1,
                           'showarrow' : False},
                          {'text' : 'Above the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 2,
                           'showarrow' : False}]
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (4) - Annotations outside the chart\pyo.iplot-2.png") 
 #

# So we can see from this chart how to place annotations outside of the plotting area, however the visible area of the chart doesn't change to reflect this. We need to adjust the margins to increase the amount of chart area outside of the plotting area which is shown.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to place annotations consistently on the chart, in a way that is not influenced by what data the chart holds. 
# 
# We've also seen how to place annotations outside of the chart, although this has presented a further problem; namely that we can't see the entirety of the annotation!
# 
# In the next lesson we'll learn how to increase the margins of the chart, showing more chart outside of the plotting area. This will enable us to see these annotations.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
