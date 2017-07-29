
# coding: utf-8

# # Pie charts (5) - Labels, text & hoverinfo

# In this lesson we're going to learn how text is displayed on a Plotly pie chart. When making line and scatter charts, we can choose to set a <code>'text'</code> property for the text which is displayed at the position of the points. We can do a similar thing for pie charts, instead deciding what is displayed next to each segment.

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
# 
# We're going to use a new data source for this lesson. This .csv file contains data on the number of students studying at each level of study for several years. We're going to plot the number of students at each level of study for the most recent year:

# In[12]:

level = pd.read_csv("http://richard-muir.com/data/public/csv/StudentsByLevelAndYear.csv", index_col = 0)
level


# Let's keep only the column we want, and sort the DataFrame by the values in that column. We saw previously that it can be a good idea to sort the data before putting it into the trace object.

# In[13]:

level = level[['2015/16']]
level.sort_values(by='2015/16', ascending = False, inplace = True)
level


# ## Making our chart
# 
# Let's put the data into a pie chart, remembering to set the <code>'direction'</code> to <code>'clockwise'</code>. I'm also going to change the colours from the default.

# In[23]:

fig = {'data' : [{'type' : 'pie',
                  'name' : "Students by level of study",
                 'labels' : level.index,
                 'values' : level['2015/16'],
                 'direction' : 'clockwise',
                 'marker' : {'colors' : ["rgb(183,101,184)", "rgb(236,77,216)", "rgb(176,164,216)", "rgb(255,168,255)"]}}],
      'layout' : {'title' : 'Students by level of study in 2015-16'}}

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (5) - Labels, text & hoverinfo\pyo.iplot-0.png") 
 #

# ## Different text options on pie charts
# 
# As well as hoverinfo, pie charts also have a parameter called <code>'textinfo'</code>. This determines which trace information appears written on the pie chart.
# 
# <code>'textinfo'</code> can take any of the following values, joined with a '+':
# - <code>'label'</code> - displays the label on the segment
# - <code>'text'</code> - displays the text on the segment (this can be set separately to the label)
# - <code>'value'</code> - displays the value passed into the trace
# - <code>'percent'</code> - displayed the computer percentage
# 
# You can see that the default is to only show <code>'percent'</code>. Let's add a <code>'text'</code> parameter to our trace and experiment with different options for the <code>textinfo</code>.
# 
# I'm going to use the <code>'text'</code> parameter to provide shortened versions of the label.

# In[24]:

fig['data'][0].update({'text' : ['Undergrad FT',' Postgrad FT','Undergrad PT','Postgrad PT'],
                      'textinfo' : 'label+text+value+percent'})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (5) - Labels, text & hoverinfo\pyo.iplot-1.png") 
 #

# So this has given us a lot of information on the chart. You can see that Plotly positions the text on the chart in several different ways.
# 
# I'm going to stop displaying the label because I think it's too long. Because we're showing this info on the pie chart, we can also remove the legend.

# In[25]:

fig['data'][0].update({'textinfo' : 'text+value+percent',
                      'showlegend' : False})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (5) - Labels, text & hoverinfo\pyo.iplot-2.png") 
 #

# ## Hoverinfo
# 
# We also have the same options available to us for displaying the hoverinfo (we can also show the name of the trace on hover).
# 
# Let's set the hoverinfo to be the label. This way, if somebody doesn't understand one of the abbreviations they can still read the chart:

# In[26]:

fig['data'][0].update({'hoverinfo' : 'label'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (5) - Labels, text & hoverinfo\pyo.iplot-3.png") 
 #

# Let's push this chart to the Plotly cloud:

# In[27]:

py.plot(fig, filename="Students by level of study in 2015-16", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (5) - Labels, text & hoverinfo\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to change the text that is displayed on the pie chart and on hover. We've also seen that Plotly can position text inside and outside of the pie chart.
# 
# In the next lesson we're going to look at how to style the text on our pie chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
