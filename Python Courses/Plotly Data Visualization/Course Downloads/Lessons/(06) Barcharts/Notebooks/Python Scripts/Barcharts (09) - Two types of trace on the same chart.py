
# coding: utf-8

# # Barcharts (9) - Two types of trace on the same chart

# In this lesson we're going to find out how to plot two different traces on the same chart.
# 
# We're going to recreate the stacked proportional bar chart we made in the previous lesson and add some information about the size of the meteorites which were found.

# ## Module Imports

# In[3]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[4]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Creating the chart
# Let's load our stacked proportional bar chart from the Plotly cloud:

# In[5]:

stacked = py.get_figure("rmuir", 241)
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (09) - Two types of trace on the same chart\pyo.iplot-0.png") 
 #

# Let's now load the .csv file which contains the information on the size of the meteorites. We'll use the same approach that we used to get the proportions for the chart above to get the the propportion of total meteorites which weight less than 101 grams.

# In[6]:

sizes = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightPerYear.csv", index_col = 0)
sizes.head()


# We'll now get the column names for the sizes:

# In[7]:

sizeStrings = sizes.columns.tolist()
sizeStrings


# Calculating the total and percentages:

# In[8]:

sizes['total'] = sizes.sum(axis = 1)
for s in sizeStrings:
    sizes["{}_pc".format(s)] = sizes[s] / sizes['total']
    
sizes.head()


# ## Adding the line trace to our chart
# 
# Now let's add a single trace showing the percentage of meteorites found each year that weighed under 101g. We'll make the trace very dark so it stands out from the rest of the chart:

# In[9]:

stacked['data'].append({'type' : 'scatter',
                       'mode' : 'lines+markers',
                       'x' : sizes.index,
                       'y' : sizes['less than 101g_pc'],
                       'marker' : {'color' : '#333'},
                       'name' : 'Meteorite < 101g'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (09) - Two types of trace on the same chart\pyo.iplot-1.png") 
 #

# By plotting a completely different type of trace on our chart we can show some very different information, and when the presentation of the chart is considered, this can be done so clearly, as we have done. You may have seen some charts which have two y-axes, one at each side of the plotting area - it's generally not a great idea to do this as it can be difficult to determine which trace relates to which side of the plotting area. I would always recommend plotting the same type of variable on the y-axis - percentages in this case.
# 
# Let's send this chart to the Plotly cloud.

# In[10]:

py.plot(stacked, filename="Meteorites found by continent and weight", fileopt = "overwrite")


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (09) - Two types of trace on the same chart\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to put two different types of trace on the same plot. We've also seen some of the things we must take into consideration when doing so.
# 
# In the next lesson we'll take this one step further, using the Plotly subplots object that we created at the end of the last section to create our first Dashboard.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
