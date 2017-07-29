
# coding: utf-8

# # Barcharts (2) - Making our first barchart

# In this lesson we're going to make our first barchart. We're going to make a really simple chart which we will then use to learn about the different styling options available to us.
# 
# For the majority of this section we're going to focus on a single dataset; the <a href="https://data.nasa.gov/view/ak9y-cwf9">NASA Meteorite Landings</a> dataset. This is a very rich dataset which will allow us to make some diverse and interesting bar charts.

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


# ## Getting the data
# 
# The data is available from my website; I've done some pre-processing and summarising to make it as easy as possible to plot. You could also download it yourself from https://data.nasa.gov/view/ak9y-cwf9, and have a play around with it - it's a really rich and interesting dataset!
# 
# I've restricted the source data to only the years 1970 - 2012.

# In[4]:

meteorite = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsPerYear.csv", index_col = 0)
meteorite.head()


# ## Making a barchart
# 
# In the same way that we make a scatter trace by specifying <code>{'type' : 'scatter'}</code>, we can make a bar trace by specifying <code>{'type' : 'bar'}</code>.
# 
# For this barchart, we'll set the x-values as the year (the index in meteorite DataFrame), and the y-values as the number of meteorites found in that year:

# In[5]:

numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count']}

pyo.iplot([numberOfMeteorites])


py.image.save_as([numberOfMeteorites], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (02) - making our first barchart\pyo.iplot-0.png") 
 #

# #### What happens if we don't set our x- and y-values correctly; will the chart still plot? 
# 
# Yes, it will, however for a vertical bar chart, Plotly expects each vlaue to be of a distinct category. As you can see from the chart below, Plotly has treated each distinct value of <code>'count'</code> as a separate category. If your bar charts don't come out as you expect, try switching your x- and y-values first - a simple mistake can make your chart look very strange indeed!

# In[10]:

pyo.iplot([ {'type' : 'bar',
                     'y' : meteorite.index,
                     'x' : meteorite['count']}])


# Let's add a source and titles to our chart:

# In[8]:

layout = {'title' : "Number of meteorites found per year",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Number of meteorites'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (02) - making our first barchart\pyo.iplot-1.png") 
 #

# Let's send our first barchart to the Plotly cloud:

# In[9]:

py.plot(fig, filename="Number of meteorites found each year", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (02) - making our first barchart\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to make a simple barchart. We've seen that it's as easy setting <code>'type' : 'bar'</code> in our trace, remembering to set the x- and y-values correctly.
# 
# In the next lesson we'll learn about some of the new styling options available to us now we can create a bar chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
