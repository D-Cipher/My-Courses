
# coding: utf-8

# # Chart Presentation (3) - Positioning the legend

# In this lesson we're going to learn how to position the legend. The legend can be positioned in the same way that we position annotations - by setting an x- and y-position.

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


# ## Changing the x- and y-values for the legend position
# 
# The legend is always positioned using normalised coordinates; that is, we don't position the legend relative to any data items, instead positioning it relative to the chart. 
# 
# The x- and y-values for the normalised coordinates can be between -2 and 3, with the coordinate (0, 0) positioning the legend at the bottom-left corner of the chart.
# 
# Let's load a chart and practise moving the legend:

# In[3]:

stacked = py.get_figure("rmuir", 255)
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (3) - Positioning the legend\pyo.iplot-0.png") 
 #

# We'll first change the x-values for the legend position. By setting the x-value to the maximum (3), we move the legend far away from the chart, squashing the chart up. This doesn't look great.

# In[4]:

stacked['layout']['legend'].update({'x' : 3})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (3) - Positioning the legend\pyo.iplot-1.png") 
 #

# By setting the x-value to the minimum (-2), the same happens, but the legend moves to the left instead.

# In[5]:

stacked['layout']['legend'].update({'x' : -2})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (3) - Positioning the legend\pyo.iplot-2.png") 
 #

# By setting the x-value to 0, we line the legend up with the y-axis (where x = 0). Note that the legend obscures the chart when it is placed over it. This might work for a scatterplot where there are no points plotted in the top-left corner, but it doesn't work here.

# In[6]:

stacked['layout']['legend'].update({'x' : 0})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (3) - Positioning the legend\pyo.iplot-3.png") 
 #

# Let's move the legend down by changing the y-value to position the legend underneath the chart:

# In[7]:

stacked['layout']['legend'].update({'y' : -1})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (3) - Positioning the legend\pyo.iplot-4.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to change the position of the legend by setting the x- and y- position.
# 
# In the next lesson we'll find out how to change the orientation of the legend from vertical to horizontal.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
