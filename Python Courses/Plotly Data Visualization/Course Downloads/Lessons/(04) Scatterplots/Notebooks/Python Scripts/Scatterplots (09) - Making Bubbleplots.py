
# coding: utf-8

# # Scatterplots (09) - Making Bubbleplots

# In this lesson we're going to learn how to make a bubbleplot. A bubbleplot is a variation on a scatterplot which allows us to visualise three variables on the same chart; the x- and y-variables are displayed as normal, and the third variable is shown by the size of the scatter markers.
# 
# Perhaps the most famous bubbleplot is that created by Hans Rosling of <a href="http://www.gapminder.org/tools/#_chart-type=bubbles">Gapminder</a>. This plot shows the life expectancy plotted against GDP for many countries. The size of the countries are shown by the size of the bubble, and the region to which they belong is shown by the colour. This plot encodes four different types of information in one plot. We'll learn how to recreate it in the next lesson:
# <img src="https://openlab.citytech.cuny.edu/ganguli-math1372-fall2014/files/2014/11/gapminder.jpg"/>

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


# ## Changing the marker size
# We've already seen how to change the marker size by accessing the <code>'size'</code> property in the <code>'marker'</code> option within the trace. To make a bubbleplot we pass a list of values to this property instead of a fixed number. Each item in the list of values which we pass to the <code>'marker' : {'size' :}</code> option corresponds to the data point at the same index.
# 
# The numbers that we pass to <code>'marker' : 'size'</code> set the marker size in pixels. We also need to set the <code>'sizemode'</code> property to <code>'area'</code> to ensure that the bubbles are sized correctly. <a href="http://themendozaline.org/post/95757674381/this-bubble-chart-is-killing-me">This article</a> explains why, but the basic idea is that using the circle's diameter exaggerates the degree of change between two numbers that area being compared.
# 
# In the below example, the first data point would have a size of 10 pixels, the second a size of 20 pixels, and the third a size of 30 pixels.
# ````python
# trace = {'x' : [1,2,3],
#         'y' : [5,6,7],
#         'marker' : {'size' : [100, 200, 300],
#                     'sizemode' : 'area'}}
# ````
# When setting the marker size to a list of values, we may need to manipulate the <code>'sizeref'</code> property within the <code>'marker'</code> option in the trace. For example, if we were to set the marker size to the population, the marker for London would be 8,173,941 pixels. This is obviously quite large. We can reduce the size of all of the markers whilst keeping the same ratio by using <code>'sizeref'</code>:
# ````python
# trace = {'x' : [1,2,3],
#         'y' : [5,6,7],
#         'marker' : {'size' : [10000, 20000, 30000],
#                     'sizemode' : 'area'
#                     'sizeref' : 10}}
# ````
# Here's what the first example would look like as a chart:

# In[3]:

pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [100, 200, 300],
                   'sizemode' : 'area'}}])


# And the second, without setting the <code>'sizeref'</code>:

# In[4]:

pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [10000, 20000, 30000],
                   'sizemode' : 'area'}}])


# And with the <code>'sizeref'</code> set, the circles are scaled down in size whilst keeping the same ratio:

# In[5]:

pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [10000, 20000, 30000],
                   'sizemode' : 'area',
                   'sizeref' : 10}}])


# ## Getting the data
# We're going to practise making bubbleplots by using data on English regions which is available from Wikipedia. We'll once again use the <code>pd.read_html()</code> function to access this data:

# In[3]:

regionalData= pd.read_html("https://en.wikipedia.org/wiki/Regions_of_England", header=0)


# The DataFrame with the data we want is the second item in the list that is returned:

# In[7]:

regionalData[3]


# Let's remove England from the DataFrame by using the <code>df.loc[]</code> selector:

# In[9]:

regions = regionalData[3][regionalData[3]['Name[29]'] != 'England']
regions


# We'll also create a text column to show the hovertext. The hovertext will display the region's name and area - we'll show the area of the region by the size of the marker, so it's important to display this information clearly in the hovertext.

# In[9]:

regions['text'] = regions.apply(lambda x: "<b>{}</b><br>Area: {} Km<sup>2</sup>".format(x['Name[29]'], 
                                                                                                      x['Area km²']), 
                                               axis = 1)
regions


# ## Plotting the data
# Let's create our scatterplot. On this plot we're going to represent the population on the x-axis, the median earnings on the y-axis, and the area by the size of the bubble.
# 
# We'll create the basic scatterplot first, and then add in the <code>'marker' : {'size' : }</code> property after.
# 
# I'm going to set the hoverinfo to <code>'text+x+y'</code> so that all the information about a data point will be shown on hover.

# In[10]:

regionTrace = {'type' : 'scatter',
              'mode' : 'markers',
              'x' : regions['Population'],
              'y' : regions['Median gross annual earnings (£) 2014[30]'],
              'text' : regions['text'],
              'hoverinfo' : 'text+x+y'}


# In the layout, I'll set the range of the axes dynamically, as well as adding a <code>'tickformat'</code> and <code>'tickprefix'</code> to the y-axis:

# In[11]:

layout = {'title' : 'Population, median earnings and area of English regions',
         'xaxis' : {'title' : 'Population',
                   'range' : [regions['Population'].min() * 0.95, 
                             regions['Population'].max() * 1.05]},
         'yaxis' : {'title' : 'Median earnings',
                   'tickformat' : ',',
                   'tickprefix' : '£',
                   'range' : [regions['Median gross annual earnings (£) 2014[30]'].min() * 0.95, 
                             regions['Median gross annual earnings (£) 2014[30]'].max() * 1.05]}}

fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (09) - Making Bubbleplots\pyo.iplot-0.png") 
 #

# Now, let's add the marker size to the trace and replot the chart:

# In[12]:

regionTrace.update({'marker' : {'size' : regions['Area km²'],
                               'sizemode' : 'area'}})
fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (09) - Making Bubbleplots\pyo.iplot-1.png") 
 #

# It seems as though we'll have to set the <code>'sizeref'</code>:

# In[13]:

regionTrace['marker'].update({'sizeref' : 5 })
fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (09) - Making Bubbleplots\pyo.iplot-2.png") 
 #

# I'm going to increase the range so we can see the full markers:

# In[14]:

fig['layout']['xaxis'].update({'range' : [regions['Population'].min() * 0.75, 
                                         regions['Population'].max() * 1.05]})

fig['layout']['yaxis'].update({'range' : [regions['Median gross annual earnings (£) 2014[30]'].min() * 0.75, 
                                         regions['Median gross annual earnings (£) 2014[30]'].max() * 1.05]})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (09) - Making Bubbleplots\pyo.iplot-3.png") 
 #

# That allows us to see the entire bubble for each region. Let's push this to the Plotly cloud:

# In[15]:

py.plot(fig, filename = "Population, median earnings and area of English regions", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (09) - Making Bubbleplots\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to pass a list of items to the <code>'marker' : {'size':}</code> option to set the size for each data point individually. This allows us to encode a third variable in our scatterplots. We learnt that we should set the <code>'sizemode'</code> to <code>'area'</code> to allow the sizes of the bubbles to be compared effectively.
# 
# We've also seen how to set the <code>'sizeref'</code> to change the size of the markers whilst keeping the ratio of the sizes the same. This is useful when the marker size shows a particularly large or small variable.
# 
# Finally, we've seen that we might have to update the range of the axes in order to accomodate the size of the bubbles.
# 
# In the next lesson we'll recreate one of the plots from Gapminder.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
