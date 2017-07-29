
# coding: utf-8

# # Barcharts (6) - Plotting multiple bar traces

# In this lesson we're going to make a slightly more complex barchart which shows multiple categories.
# 
# We're going to plot the number of meteorites by continent since the year 2000, and by doing so we'll get some experience of how Plotly creates a bar chart with multiple traces.

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


# ## Getting the data
# We're going to use a different dataset for this chart. The data comes from the same source as the previous chart, however I have disaggregated the total number of meteorites found and split them by which continent they were found on. The total number of meteorites does not correspond to the previous dataset because there were many instances where the latitude and longitude of the found meteorite could not be translated by the Google Maps API.

# In[20]:

meteorites = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoritesByContinent.csv", index_col = 0)
meteorites.head()


# ## Plotting the data
# 
# We'll now create a bar trace for each continent. We'll do this by getting a list of the unique values in the 'continent' column, then looping through this list, selecting only the rows which belong the that particular continent.

# In[21]:

continents = list(meteorites['continent'].unique())
continents


# In[22]:

traces = []
for c in continents:
    traces.append({'type' : 'bar',
                  'name' : c,
                  'x' : meteorites.loc[meteorites['continent'] == c, 'year'],
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count']})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
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
fig = {'data' : traces, 'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (06) - Plotting multiple bar traces\pyo.iplot-0.png") 
 #

# So that gives us this striking chart. The standard Plotly colours are very bright! 
# 
# Plotly's default option when working with bar charts is to create a grouped bar chart. We'll find out how to change this to a stacked or overlaid bar chart in the next lessons.
# 
# You can see that there are distinct groups of bars for each Year, with the bars in each group corresponding to a particular continent.
# 
# Let's try looking at this data another way, grouping the number of meteorites by continent rather than year. We'll also tone down those colours a little bit!

# In[23]:

years = list(meteorites['year'].unique())
years


# In[24]:

traces = []
for y in years:
    traces.append({'type' : 'bar',
                  'name' : y,
                   # CHANGE TO SPLIT BY YEAR
                  'x' : meteorites.loc[meteorites['year'] == y, 'continent'],
                  'y' : meteorites.loc[meteorites['year'] == y, 'count'],
                  'opacity' : 0.7})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
         'xaxis' : {'title' : 'Continent'},
         'yaxis' : {'title' : 'Number of meteorites'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : traces, 'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (06) - Plotting multiple bar traces\pyo.iplot-1.png") 
 #

# Changing the grouping like this gives us another perspective on the data; it shifts the focus to the differences between each year for each continent. Let's send this chart to the Plotly cloud:

# In[25]:

py.plot(fig, filename="Meteorites found by continent (2000 - 2012)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (06) - Plotting multiple bar traces\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to create a barchart with multiple traces. We've seen how we can change the focus of the chart by switching which categories are represented on the x-axis and which are represented by the different traces.
# 
# In the next lesson we'll use this chart to practise creating stacked bar charts, in addition to the default of 'grouped'.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
