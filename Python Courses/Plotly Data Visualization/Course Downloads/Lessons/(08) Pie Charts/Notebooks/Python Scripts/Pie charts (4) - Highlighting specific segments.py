
# coding: utf-8

# # Pie charts (4) - Highlighting specific segments

# In this lesson we're going to learn how to pull specific segments out from the main body of the pie chart to highlight them to our readers. 
# 
# This allows us to focus our readers on a specific message in the data, but does carry the risk of making the chart less easy to understand.

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


# ## Moving all the segments
# 
# In the trace object, we can use the parameter <code>'pull'</code> to spread the segments of the pie chart out. 
# 
# By specifying an number we can move all of the segments an equal amount, and by specifying a list of numbers we can choose to move a specific segment or segments that we wish to highlight. 
# 
# Each number must be between 0 and 1 inclusive.
# 
# Let's try this out on the chart we styled in the last lesson:

# In[3]:

ethPie = py.get_figure("rmuir", 265)
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-0.png") 
 #

# Let's move all of the sectors out the maximum amount:

# In[5]:

ethPie['data'][0].update({'pull' : 1})
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-1.png") 
 #

# And maybe a little less. . .

# In[6]:

ethPie['data'][0].update({'pull' : 0.1})
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-2.png") 
 #

# Let's now try moving a specific segment. I'm going to move the segment for Black students out to highlight it:

# In[7]:

ethPie['data'][0].update({'pull' : [0, 0, 0.2, 0, 0]})
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-3.png") 
 #

# Well that doesn't appear to have worked . . .
# 
# If we look at the data in the chart, we can see that the category for black students is in fact the fourth category in the list of values. It looks like Plotly applies the value for the <code>'pull'</code> parameter before sorting the segments based on size.

# In[8]:

ethPie['data'][0]


# ## Finding a workaround for this problem
# 
# We could go into the data and count along the lists of values and labels to find the segment that we want, but that seems like a lot of hard work. Let's pre-sort our data and put it back into the trace object.
# 
# We'll create a <code>dict()</code> by <code>zip()</code>ping together the lists of labels and values and using the python <code>sorted()</code> function to output this dictionary in a sorted fashion. We could also have sorted the data in our DataFrame, but we may not always have that luxury . . .

# In[10]:

labelValues = dict(zip(ethPie['data'][0]['labels'], 
                       ethPie['data'][0]['values']))
labelValues


# In[14]:

newLabels = []
newValues = []
for w in sorted(labelValues, key=labelValues.get, reverse=True):
    label = w
    value = labelValues[w]
    
    newLabels.append(label)
    newValues.append(value)
    
newLabels, newValues


# Let's put this sorted data back into the trace and replot it!

# In[15]:

ethPie['data'][0]['labels'] = newLabels
ethPie['data'][0]['values'] = newValues

pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-4.png") 
 #

# Success! Let's try changing which segment we're pulling:

# In[17]:

ethPie['data'][0].update({'pull' : [0,0,0,0,0.5]})
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\pyo.iplot-5.png") 
 #

# In[18]:

py.plot(ethPie, filename="Ethnicity of UK students (highlight)", fileopt = "overwrite")


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (4) - Highlighting specific segments\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to use the <code>'pull'</code> parameter to move specific segments away from the main pie chart.
# 
# We've learnt that Plotly sorts the segments by size after the pull parameter has been assigned to a particular label, and that it's therefore a good idea to sort the data beforehand. This is not always the case and we also saw how to sort the data contained within our figure object.
# 
# In the next lesson we'll investigate how Plotly displays text labels on pie charts.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
