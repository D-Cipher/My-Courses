
# coding: utf-8

# # Barcharts (8) - Stacked proportional bar charts

# In this lesson we'll learn how to create a special type of stacked bar chart; a stacked proportional bar chart. This is similar in concept to the stacked area chart that we learnt how to make in the Lineplot section.

# ## Module Imports

# In[36]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[37]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# We're going to get the same dataset that we used for the previous chart. We'll need to do some reshaping and data manipulation in order to calculate the the proportions.

# In[38]:

meteorites = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoritesByContinent.csv", index_col = 0)
meteorites.head()


# Firstly we need a list of the unique continents, which we'll use to calculate the proportions:

# In[39]:

continents = list(meteorites['continent'].unique())
continents


# The first step is to pivot the DataFrame. We want a DataFrame which shows for each year, the number of meteorites found in each continent.
# 
# I'll use <code>df.pivot()</code>, setting <code>index='year'</code>, <code>columns='continent'</code> and <code>values='count'</code>. This means that each of the unique values in the 'year' column will become a row and each of the unique values in the 'continent' column will become a column. The intersection of each row and column will then be filled with the value held in the 'count' column.

# In[40]:

meteorites = meteorites.pivot(index='year',columns = 'continent', values='count')
meteorites.head()


# We now need to replace the <code>NaN</code> values with a 0:

# In[41]:

meteorites.fillna(value = 0, inplace = True)
meteorites.head()


# Then use the <code>df.sum()</code> method to get the total for each row:

# In[42]:

meteorites['total'] = meteorites.sum(axis = 1)
meteorites.head()


# We can now loop through our list of continents, calculating the proportion of meteorites each year that fell in each continent:

# In[43]:

for c in continents:
    meteorites["{}_pc".format(c)] = meteorites[c] / meteorites['total']
    
meteorites.head()


# We'll now order the traces in order to show the trace with the largest proprtion at the bottom. I'll do this heuristically by calculating the sum of the proportions and ordering the traces based on that sum.
# 
# We'll use the <code>sorted()</code> function in conjunction with the <code>lambda</code> function to sort the list by the values of the dictionary. I'll set <code>reverse=True</code> to sort by descending values:

# In[44]:

pcContinents = [c + "_pc" for c in continents]

sortKeys = dict(meteorites[pcContinents].sum())

pcContinents = sorted(pcContinents, key=lambda k: sortKeys[k], reverse=True)
pcContinents


# ## Making the chart
# We can now pass the percentages into the bar chart traces, modifying the loop slightly to take into account the changed data structure:

# In[45]:

traces = []

for c in pcContinents:
    traces.append({'type' : 'bar',
                  'name' : c[:-3],
                  'x' : meteorites.index,
                  'y' : meteorites[c],
                  'opacity' : 0.7})

pyo.iplot(traces)


py.image.save_as(traces, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (08) - Stacked proportional bar charts\pyo.iplot-0.png") 
 #

# ## Stacking the bars and polishing the chart
# 
# Let's now add the layout:

# In[46]:

layout = {'title' : "Proportion of meteorites found by continent, 2000 - 2012",
          'barmode' : 'stack',
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Proportion of meteorites',
                   'tickformat' : '%',
                   'hoverformat' : '%',},
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


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (08) - Stacked proportional bar charts\pyo.iplot-1.png") 
 #

# Thus completes our stacked proportional bar chart. There seems to be a lot of variability in where meteorites are found in the world, however the majority are found in Antartica abd Asia, with very few being found in Australia.
# 
# Let's send this chart to the Plotly cloud.

# In[47]:

py.plot(fig, filename="Meteorites found by continent (2000 - 2012, stacked bar)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (08) - Stacked proportional bar charts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to create a stacked proportional bar chart. In doing so we've learnt how to use the Pandas <code>df.pivot()</code> function to change the shape of our data.
# 
# In the next lesson we'll see how we can include two different types of traces on the same chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
