
# coding: utf-8

# # Chart Presentation (4) - Creating ticklabels

# In the last lesson we saw how to use the <code>'tickprefix'</code> and <code>'ticksuffix'</code> parameters to modify the existing ticklabels. We also saw that we can gain some control over the number of ticks by specifying a value for <code>'nticks'</code>.
# 
# In this lesson we'll find out how to set the text and position of our own ticklabels using the <code>'tickmode'</code>, <code>'tickvals'</code> and <code>'ticktext'</code> parameters.

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


# ## Getting a chart to modify:
# 
# We'll import the MPs expense claims chart and set the tickvalues individually:

# In[6]:

expenses = py.get_figure('rmuir', 148)
pyo.iplot(expenses)


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\pyo.iplot-0.png") 
 #

# ## Setting the tickvalues
# 
# In order to set the tickvalues, we need to manipulate three different parameters within the axis object. First of all, we need to set <code>'tickmode'</code> to <code>'array'</code> to tell Plotly to expect a list of ticks.
# 
# Next, we need to set the <code>'tickvals'</code> to be a list of numbers where each tick will be displayed.
# 
# Finally, we specify the <code>'ticktext'</code> to place at each of the <code>'tickvals'</code>:
# ````python
# layout = {'xaxis' : {'tickmode' :  'array',
#                        'tickvals' : <list of values>,
#                        'ticktext' : <list of values>}}
# ````
# 
# The values that we specify in <code>'tickvals'</code> must be contained within the data that relates to the axis. For example, we couldn't have <code>'tickvals' : [5, 10]</code> when the axis is categorical, for example <code>'x' : ['UK','USA']</code>.
# 
# Both lists of <code>'ticktext'</code> and <code>'tickvals'</code> must have the same length otherwise your text will not display properly.
# 
# Let's specify some practise tickvalues:

# In[10]:

expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [3, 6, 9], 'ticktext' : ['three',' six','nine']})
pyo.iplot(expenses)


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\pyo.iplot-1.png") 
 #

# You can see how the <code>'ticktext'</code> and <code>'tickvals'</code> have been placed on the x-axis.

# In[11]:

expenses['layout']['xaxis'].update({'tickmode' : 'array', 
                                    'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['three',' six','nine']})
pyo.iplot(expenses)


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\pyo.iplot-2.png") 
 #

# You can see that whilst we have specified 12 values for the position of the ticklabels, we have only specified 3 values for the <code>'ticktext'</code>. Plotly will use each value of <code>'ticktext'</code> once and then revert to using the <code>'tickvals'</code> when they have run out.
# 
# 
# Let's specify the values to be something more relevant, the month names for example:

# In[12]:

expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']})
pyo.iplot(expenses)


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\pyo.iplot-3.png") 
 #

# Great, that seems to have worked. But we can acheive the same outcome by using a date format. Let's try something a little more complex.
# 
# We'll use the <code>'ticktext'</code> to add some contextual information to the tick labels. For example, the number of expense claims is so low in August because the MPs go on a summer recess. 
# 
# Let's encode this information into the <code>'ticktext'</code>:

# In[13]:

expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug<br>(Summer Recess)','Sep','Oct','Nov','Dec']})
pyo.iplot(expenses)


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\pyo.iplot-4.png") 
 #

# Great, that helps to clarify one of the main trends in the chart. Let's push it back to the Plotly cloud:

# In[15]:

py.plot(expenses, filename="MP Expense claims by month 2010-2015", fileopt = "overwrite")


py.image.save_as(expenses, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart Presentation (4) - Creating ticklabels\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to specify the exact text that we want to show at a specific position on an axis. This allows us to explain different elements in a chart, or to override Plotly's default functionality when it doesn't fit our expectation of what the data should look like.
# 
# In the next lesson we'll learn how to manipulate the hovertext options.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
