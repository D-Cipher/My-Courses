
# coding: utf-8

# # Pie charts (8) - Relative sizing of pie charts

# In this lesson we're going to practise placing pie charts in a plotly subplot. We're also going to employ the <code>'scalegroup'</code> parameter to size these linked pie charts by their totals, relative to each other.

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

from plotly.tools import make_subplots


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# We're going to again use publically available data from HESA. This data shows, for each subject area, how many students who graduated in 2014-15 are in work, further study or are unemployed.
# 
# We'll choose a four different subject areas to compare using pie charts:

# In[4]:

outcomes = pd.read_csv("http://richard-muir.com/data/public/csv/StudentOutcomes201415BySubjectArea.csv", index_col = 0)
outcomes.head(10)


# ## Making the subplots object
# 
# We're going to make a subplots object with four cells, one for each subject which we're going to compare. We'll also set the width and height to make the figure a square.
# 
# Finally, we'll add a dummy data item so we can see the plotting area and make sure that we have removed all the visible legend components.

# In[5]:

fig = make_subplots(rows = 2, cols = 2,
                   subplot_titles = ["Medicine & Dentistry",
                                   "Biological Sciences",
                                   "Computer Science",
                                   "Engineering & Technology"])

fig['layout'].update({'height' : 900, 'width' : 900})

fig['data'].append({'type' : 'scatter'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (8) - Relative sizing of pie charts\pyo.iplot-0.png") 
 #

# Let's now remove the axis components by looping through the items in the layout, and for each axis object, applying the hideAxis parameters that we created in the previous lesson.

# In[6]:

hideAxis = {'zeroline' : False,
            'showgrid' : False,
            'showticklabels' : False,
            'showline' : False}

for key, axis in fig['layout'].items():
    if 'axis' in key:
        axis.update(hideAxis)
        
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (8) - Relative sizing of pie charts\pyo.iplot-1.png") 
 #

# The final thing to do before we start putting the pie charts in the subplots object is to get the domains of the axes. We need to create a lookup between the subject area and the domain.
# 
# To do this, we need to order the list of subjects to match their order on the subplots object; "Medicine & Dentistry" first in the list, and "Engineering & technology" last:

# In[7]:

subjects = ['Medicine & dentistry','Biological sciences','Computer science','Engineering & technology']

for key, axis in fig['layout'].items():
    if 'axis' in key:
        print(key, axis['domain'])


# Using the helpful plot grid format, we can now assign each x- and y-axis domain to a subject, and create a lookup dictionary between the subject and that domain:
# ````
# This is the format of your plot grid:
# [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
# [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
# ````
# 
# Remember that lists and 0-indexed, but the axis objects start from 1!

# In[8]:

subjLookup = {}
for i, sub in enumerate(subjects):
    axisPos = i + 1
    subjLookup[sub] = {'x' : fig['layout']['xaxis{}'.format(axisPos)]['domain'],
                       'y' : fig['layout']['yaxis{}'.format(axisPos)]['domain']}
    
subjLookup


# ## Making the pie charts
# 
# Let's now select the data for each subject area of interest and make a pie trace for each one.
# 
# We'll use the lookup to set the domain for this pie trace, and then append that trace to the list of data items in the fig:

# In[9]:

for s in subjects:
    fig['data'].append({'type' : 'pie',
                       'labels' : outcomes.columns.tolist(),
                       'values' : outcomes.loc[s],
                      'domain' : subjLookup[s],
                       'direction' : 'clockwise',
                       'name' : s})
    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (8) - Relative sizing of pie charts\pyo.iplot-2.png") 
 #

# So there's some overlap between the labels on the pie charts and the subplot titles. The easiest way of fixing this is to move the titles up, but before we do this, let's scale the pie charts relative to each other.
# 
# The total number of students in each subject area is different, so we expect the pie charts to be different sizes. This may fix our problem!

# ## Linking the pie charts together
# 
# It's super easy to link the pie charts together! All we have to do is set a value for the <code>'scalegroup'</code> parameter, much as we would for a <code>'legendgroup'</code>.
# 
# Let's delete the traces from our figure, and re-add them with a <code>'scalegroup'</code> of <code>'subjects'</code>. We'll also suppress the pie chart name from the hoverinfo, as this doesn't add any information.

# In[10]:

fig['data'] = []

for s in subjects:
    fig['data'].append({'type' : 'pie',
                       'labels' : outcomes.columns.tolist(),
                       'values' : outcomes.loc[s],
                      'domain' : subjLookup[s],
                       'direction' : 'clockwise',
                       'scalegroup' : 'subjects',
                       'name' : s,
                       'hoverinfo' : 'label+value+percent'})
    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (8) - Relative sizing of pie charts\pyo.iplot-3.png") 
 #

# We've got this chart looking really good! Let's send it to the Plotly cloud:

# In[11]:

py.plot(fig, filename="Student outcomes by subject area", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (8) - Relative sizing of pie charts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've practised adding pie charts to a subplots object.
# 
# We've seen how to take the information that Plotly gives us about the domain of each axis, and apply it to each pie trace using a lookup dictionary.
# 
# We've also learnt how to use the <code>'scalegroup'</code> parameter to set the size of the pie charts relative to each other.
# 
# In the next lesson we'll learn how to create a donut chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
