
# coding: utf-8

# # Chart Presentation (2) - Setting the tracegroupgap and traceorder

# In this lesson we're going to look at different ways of displaying the traces in the legend. In the final lesson of the previous section we saw how to set a <code>legendgroup</code> for our traces, and that we can increase the space between the different legend groups. In this lesson we're going to look at different values for tracegroupgap, and we're also going to find out how to change the order of the traces in the legend by changing the <code>traceorder</code> parameter.

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


# ## Applying a tracegroup to the data items
# 
# Let's get the chart we styled in the previous legend. We'll need to loop through the data items and set a <code>legendgroup</code> to each depending on if the trace is a bar or a scatter type. I've plotted the chart before the changes to <code>legendgroup</code> so you can compare them:

# In[3]:

stacked = py.get_figure("rmuir", 255)
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-0.png") 
 #
for d in stacked['data']:
    if d['type'] == 'bar':
        d.update({'legendgroup' : 'continent'})
    else:
        d.update({'legendgroup' : 'weight'})


# Now, when we plot the chart after the changes, you can see that there is now some space between the bar traces and the line trace in the legend. The order of the traces has also changed.

# In[4]:

pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-1.png") 
 #

# ## Changing the <code>tracegroupgap</code>
# 
# In the last section we set <code>tracegroupgap</code> to a large number in order to move the traces near the correct part of our dashboard. Here we'll supply a much smaller number with the aim of distinguishing better between the traces:

# In[5]:

stacked['layout']['legend'].update({'tracegroupgap' : 20})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-2.png") 
 #

# ## Changing the <code>traceorder</code>
# 
# The <code>traceorder</code> parameter accepts any of the following inputs. These inputs can also be combined with a <code>'+'</code> symbol:
# 
# - <code>'reversed'</code> - reverses the order of the traces
# - <code>'normal'</code> - puts the traces in the same order as the input data
# - <code>'grouped'</code> - displays the items in groups if a <code>'legendgroup'</code> is provided
# 
# Let's see how these work in practise.
# 
# We can remove the grouping by setting <code>traceorder</code> to <code>'normal'</code>:

# 
# The <code>traceorder</code> parameter accepts any of the following inputs. These inputs can also be combined with a <code>'+'</code> symbol:
# 
# - <code>'reversed'</code> - reverses the order of the traces
# - <code>'normal'</code> - puts the traces in the same order as the input data
# - <code>'grouped'</code> - displays the items in groups if a <code>'legendgroup'</code> is providedstacked['layout']['legend'].update({'traceorder' : 'normal'})
# pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-3.png") 
 #
# We can reverse the order by setting <code>traceorder</code> to <code>'reversed'</code>:

# In[6]:

stacked['layout']['legend'].update({'traceorder' : 'reversed'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-4.png") 
 #

# We can reinstate the tracegrouping by setting <code>traceorder</code> to <code>'grouped'</code>. Note that at the time of writing, one cannot set the traceorder to be <code>'reversed+grouped'</code> (well you can, but it doesn't work).

# In[7]:

stacked['layout']['legend'].update({'traceorder' : 'grouped'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\pyo.iplot-5.png") 
 #

# In[8]:

py.plot(stacked, filename="Meteorites by continent and weight (styled legend)", fileopt="overwrite")


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (2) - Setting the tracegroupgap and traceorder\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learn how to change the <code>tracegroupgap</code> and <code>traceorder</code> to change how the legend items are displayed.
# 
# In the next lesson we'll change the position of the legend.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
