
# coding: utf-8

# # Pie charts (2) - Making our first pie chart

# In this lesson we're going to make our first pie chart. This chart will show the breakdown of ethnicity for students at UK universities. We're going to do this using data from the UK's <a href="https://www.hesa.ac.uk/">Higher Education Statistics Agency</a> (HESA).
# 
# We'll also learn how to use the <code>'sort'</code> and <code>'direction'</code> parameters to change the order in which the segments are placed.

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


# ## Getting the data
# I've prepared a small extract of the data available from the HESA website for use in this lesson. 
# 
# We're getting this .csv file in a slightly different way; the .csv file doesn't have a header column, so we're telling pandas that this is the case and specifying a name for the column:

# In[7]:

ethnicity = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKStudentsEthnicity.csv",
                        index_col = 0, header=None, names=['N'])
ethnicity


# ## Making a pie chart
# 
# To make a pie chart with Plotly, we only need to pass three parameters to our trace; <code>'labels'</code>, <code>'values'</code> and <code>'type'</code>.
# 
# - <code>'labels'</code> is a list of the categories that we're plotting
# - <code>'values'</code> is a list of the number of things in that category
# - <code>'type'</code> should be set to <code>'pie'</code> to tell Plotly that we're making a pie chart
# 
# The lists for <code>'labels'</code> and <code>'values'</code> must be the same length.
# 
# Plotly does all the calculations to determine the angle for each slice of the pie; it's that easy!
# 
# Let's make our first trace:

# In[20]:

pieTrace = {'type' : 'pie',
           'labels' : ethnicity.index,
           'values' : ethnicity['N']}

data = [pieTrace]

layout = {'title' : 'Ethnicity of students in the UK'}

fig = {'data' : data, 'layout' : layout}

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (2) - Making our first pie chart\pyo.iplot-0.png") 
 #

# ## Is this a clear and easy-to-understand pie chart?
# You may remember from the next lesson that the (excellent) ONS guidelines recommend that the segments in a pie chart be sorted from largest to smallest. 
# 
# Plotly have included a <code>'sort'</code> parameter in the pie chart trace and by default it is set to <code>True</code>, although it doesn't appear to have sorted our segments in the correct order; I would expect the segment for 'Not known' to be last instead of 'Asian' as is currently the case.
# 
# Let's try setting <code>'sort'</code> to <code>False</code> and see what changes:

# In[21]:

fig['data'][0].update({'sort' : False})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (2) - Making our first pie chart\pyo.iplot-1.png") 
 #

# So this has changed the order in which the segments appear, but not satisfactorily. The segments now appear in the same order that they do in the data.
# 
# Let's change <code>'sort'</code> back to <code>True</code> and look at the <code>'direction'</code> parameter...
# 
# The default <code>direction</code> for how the segments follow each other is <code>'counterclockwise'</code>. Let's set <code>direction</code> to <code>'clockwise'</code> to fix this:

# In[23]:

fig['data'][0].update({'direction' : 'clockwise',
                      'sort' : True})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (2) - Making our first pie chart\pyo.iplot-2.png") 
 #

# That's much better! Let's push this chart to the Plotly cloud:

# In[24]:

py.plot(fig, filename="Ethnicity of UK students", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (2) - Making our first pie chart\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to create our first pie chart, learning that we only need to pass 3 parameters to the trace object; type, labels and values.
# 
# We've also seen that we can change the order in which the segments appear by changing the values for the 'sort' and 'direction' parameters.
# 
# In the next lesson we'll learn how to style and colour the segments in a pie chart>

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
