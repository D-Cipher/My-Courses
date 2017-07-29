
# coding: utf-8

# # Barcharts (7) - Creating stacked barcharts

# In this lesson we're going to learn how to use the Plotly <code>'barmode'</code> option in the layout to switch between stacked and grouped bar charts.
# 
# Using stacked and grouped bar charts allows us to compare the same data in different ways. Grouped bar charts allow us to compare quantities between different sub-categories, whilst stacked bar charts allow us to make comparisons between the sub-categories as part of the whole category.

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


# ## Creating the chart
# We're going to use the first chart that we created in a previous lesson as a base. We'll take this opportunity to tone down the colours a little bit!

# In[4]:

meteorites = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoritesByContinent.csv", index_col = 0)
meteorites.head()


# In[5]:

continents = list(meteorites['continent'].unique())
continents


# In[6]:

traces = []
for c in continents:
    traces.append({'type' : 'bar',
                  'name' : c,
                  'x' : meteorites.loc[meteorites['continent'] == c, 'year'],
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count'],
                  'opacity' : 0.7})
    
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


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (07) - Creating stacked barcharts\pyo.iplot-0.png") 
 #

# ## Changing the <code>'barmode'</code>
# 
# The <code>'barmode'</code> option is contained within the layout and can take one of two options:
# - <code>'stack'</code> - makes a stacked bar chart
# - <code>'group'</code> - the default, makes a grouped bar chart (as above)
# 
# Let's change the <code>'barmode'</code> to <code>'stacked'</code> for this chart:

# In[7]:

fig['layout'].update({'barmode' : 'stack'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (07) - Creating stacked barcharts\pyo.iplot-1.png") 
 #

# You can see that making such a small change in the layout has had drastic effects on how this chart is displayed. The bars are now stacked on top of each other. 
# 
# There are pros and cons to using a stacked bar chart. One advantage is that by stacking the bars, we can easily see how the total number of meteorites changes each year, whilst still getting some idea (but not an exact comparison) of the distribution between the continents. When the bars are grouped however, it becomes much easier to compare the numbers per continent, but nearly impossible to ascertain the total number of meteorites found each year.
# 
# It's conventional to order the traces in a stacked bar chart by placing the category with the largest amount at the bottom. We'll re-order our list of continents to achieve this, with Antartica being first in our list of traces:

# In[8]:

continents = ['Antarctica',
              'Asia',
              'Africa',
              'South America',
              'North America',
              'Australia',
              'Europe',]


# In[9]:

traces = []
for c in continents:
    traces.append({'type' : 'bar',
                  'name' : c,
                  'x' : meteorites.loc[meteorites['continent'] == c, 'year'],
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count'],
                  'opacity' : 0.7})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
          'barmode' : 'stack',
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


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (07) - Creating stacked barcharts\pyo.iplot-2.png") 
 #

# In[10]:

py.plot(fig, filename="Meteorites found by continent (2000 - 2012, stacked bar)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (07) - Creating stacked barcharts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to create a stacked or grouped bar chart by setting the <code>'barmode'</code> to <code>'stack'</code> or <code>'group'</code> respectively.
# 
# In the next lesson we'll learn how to create stacked proportional bar charts.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
