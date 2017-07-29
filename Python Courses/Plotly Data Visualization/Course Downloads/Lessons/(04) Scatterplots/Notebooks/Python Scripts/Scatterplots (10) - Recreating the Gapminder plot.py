
# coding: utf-8

# # Scatterplot (10) - Recreating the Gapminder plot

# In this lesson we're going to recreate Hans Rosling's famous <a href="https://www.gapminder.org/data/">Gapminder</a> bubbleplot.
# 
# We'll practise how to use the <code>'marker' : {'size' : }</code> and <code>'sizeref'</code> options to change the size of the bubbles and we'll also learn how to set the <code>'sizemin'</code> property to set the minimum size of the bubbles on the plot to help us account for the large difference in sizes between the countries; the smallest country has just 104,000 people, whilst the largest has 1.3 billion.

# ## Module Imports

# In[1]:

#plotly.offline doesn't push your charts to the cloud
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
# I've sourced the data we need from the <a href="https://www.gapminder.org/data/">Gapminder</a> data page and done some pre-processing to merge the various data files together. We'll download it as a .csv file from my website.
# 
# The GDP per capita is in US$ at <a href="https://en.wikipedia.org/wiki/Purchasing_power_parity">purchasing power parity</a>

# In[3]:

LifePopGDP = pd.read_csv("http://www.richard-muir.com/data/public/csv/GapminderData.csv", index_col = 0)
LifePopGDP.head()


# Let's create a column to hold the hovertext. We'll put the country name in bold, the life expectancy as an integer, and the GDP per capita and Population as integers with a comma as a thousand separator.

# In[4]:

LifePopGDP['text'] = LifePopGDP.apply(lambda x: 
        "<b>{}</b><br>Life Expectancy: {:.0f} years<br>GDP/Capita: ${:,.0f}<br>Population: {:,.0f}".format(x['Country'], 
                                                                                                 x['Life Expectancy'],
                                                                                                x['GDP per Capita'],
                                                                                                x['Population']),
                                     axis = 1)
LifePopGDP.head()


# And check that it's worked properly:

# In[5]:

LifePopGDP.loc[0, 'text']


# ## Creating the chart
# 
# The chart we'll create will have a data point for each country. The y-value will be the life expectancy in years. The x-value will be the GDP per capita. The bubbles will be sized for the population, but we'll have to specify the <code>'sizeref'</code>  to be <code>500,000</code> because the numbers are so large. Each country's data point will be coloured depending on which continent it belongs to.
# 
# We'll first of all need a list of continents which we'll use to create a trace for each continent:

# In[6]:

continents = LifePopGDP['Continent'].unique()
continents


# Now let's loop through this list of continents, selecting the rows where the value for Continent matches the current continent in the loop, and selecting the column which relates to the x-variable, y-variable or size variable. We'll do this using the <code>df.loc[]</code> indexer:

# In[7]:

traces = []
for c in continents:
    traces.append({'type' : 'scatter',
                   'mode' : 'markers',
                   'name' : c,
                   'hoverinfo' : 'text',
                  'x' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'GDP per Capita'],
                  'y' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Life Expectancy'],
                  'text' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'text'],
                  'marker' : {'size' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Population'],
                             'sizeref' : 500000,
                             'sizemode' : 'area'}})


# Let's plot these traces to get an idea of how the chart looks before we start to style it:

# In[8]:

pyo.iplot(traces)


py.image.save_as(traces, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (10) - Recreating the Gapminder plot\pyo.iplot-0.png") 
 #

# So we can see straight away that because we've had to set <code>'sizeref'</code> to 500,000, the smaller countries are practically invisible on the plot. Let's update each trace with a <code>'sizemin'</code> value in the <code>'marker'</code> dictionary to set the minimum possible size for each marker point:

# In[9]:

traces = []
for c in continents:
    traces.append({'type' : 'scatter',
                   'mode' : 'markers',
                   'name' : c,
                   'hoverinfo' : 'text',
                  'x' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'GDP per Capita'],
                  'y' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Life Expectancy'],
                  'text' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'text'],
                  'marker' : {'size' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Population'],
                             'sizeref' : 500000,
                              'sizemode' : 'area',
                             'sizemin' : 2.5}})
pyo.iplot(traces)


py.image.save_as(traces, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (10) - Recreating the Gapminder plot\pyo.iplot-1.png") 
 #

# Now let's tweak the layout to finish styling the chart. We'll set the axis titles as normal and I'm also going to set the range  of each axis in the normal way, being aware that we'll have to expand this number to accomodate the large population bubbles for India and China.
# 
# Finally, we'll set the <code>'hovermode'</code> to <code>'closest'</code>:

# In[10]:

layout = {'title' : 'Life Expectancy and GDP per capita',
         'xaxis' : {'title' : 'GDP per capita at PPP ($)',
                   'range' : [LifePopGDP['GDP per Capita'].min() * 0.95, 
                              LifePopGDP['GDP per Capita'].max() * 1.05]},
         'yaxis' : {'title' : 'Life expectancy (years)',
                   'range' : [LifePopGDP['Life Expectancy'].min() * 0.95, 
                              LifePopGDP['Life Expectancy'].max() * 1.05]},
         'hovermode' : 'closest'}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (10) - Recreating the Gapminder plot\pyo.iplot-2.png") 
 #

# Let's update the x-axis range. We'll do this in a slighlty different way because we need to extend the range below 0. Rather than reducing the minimum amount by 5%, we'll instead reduce the minimum amount by 5% of the total range of the data:

# In[13]:

difference = LifePopGDP['GDP per Capita'].max() - LifePopGDP['GDP per Capita'].min()
fig['layout']['xaxis'].update({'range' : [LifePopGDP['GDP per Capita'].min() - (difference * 0.05), 
                                          LifePopGDP['GDP per Capita'].max() * 1.05]})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (10) - Recreating the Gapminder plot\pyo.iplot-3.png") 
 #

# Let's send this chart to the Plotly cloud:

# In[14]:

py.plot(fig, filename="Life Expectancy and GDP per Capita", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (10) - Recreating the Gapminder plot\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've reviewed how to make a Bubbleplot by setting the <code>'marker'</code> <code>'size'</code> option to a list of values. We've used data from Gapminder to recreate their famous 'Health and Wealth of Nations' chart, and in doing so have also discovered how to use the <code>'sizemin'</code> marker property to account for large disparities in the data values which are being represented in the size of the bubbles.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
