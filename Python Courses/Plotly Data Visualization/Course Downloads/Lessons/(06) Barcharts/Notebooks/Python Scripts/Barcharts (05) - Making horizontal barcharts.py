
# coding: utf-8

# # Barcharts (5) - Making horizontal barcharts

# So far in this section we've seen how to apply different styling options to a simple bar chart. In this lesson we'll learn how to change our vertical bar chart to a horizontal bar chart. This will give us greater flexibility when designing clear and concise charts. Horizontal bar charts are very useful when we have categories with long label names; the names often overlap when a vertical bar chart is used.

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


# ## Getting the chart
# 
# We'll use the same chart again:

# In[5]:

meteorite = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsPerYear.csv", index_col = 0)
meteorite.head()


# In[6]:

colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count'],
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

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
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                                       'x' : 2003, 
                                       'y' : 3323,
                                       'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (05) - Making horizontal barcharts\pyo.iplot-0.png") 
 #

# ## Creating a horizontal barchart
# 
# Now we can create a horizontal barchart. As with most things in Plotly, this is fairly straightforward.
# 
# The first thing we have to do is set the <code>'orientation'</code> parameter in the trace to <code>'h'</code> to tell Plotly that we want this trace to be for a horizontal barchart. To change the barchart back to vertical, we can set this parameter to <code>'v'</code>.

# In[9]:

colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                      #NEW CODE GOES HERE
                      'orientation' : 'h',
                     'x' : meteorite.index,
                     'y' : meteorite['count'],
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

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
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                                       'x' : 2003, 
                                       'y' : 3323,
                                       'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (05) - Making horizontal barcharts\pyo.iplot-1.png") 
 #

# You can see that this creates the same problem that we saw in the second lesson of this section. We now need to swap the x-values and y-values because Plotly is now expecting the y-values to be the categories, rather than the x-values.
# 
# We'll also need to change the x- and y-coordinates of our "Comet Bradfield" annotation (but not the source), and the x- and y-axis titles:

# In[11]:

colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                      'orientation' : 'h',
                      #SWAP X- AND Y-COORDINATES HERE
                     'x' : meteorite['count'],
                     'y' : meteorite.index,
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

layout = {'title' : "Number of meteorites found per year",
         'xaxis' : {'title' : 'Number of meteorites'},
         'yaxis' : {'title' : 'Year'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                          #SWAP X- AND Y-COORDINATES HERE
                            'x' : 3323, 
                            'y' : 2003,
                            'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (05) - Making horizontal barcharts\pyo.iplot-2.png") 
 #

# So you can see how by making a few small changes to our code, the look of the chart can be changed drastically.
# 
# Let's push this chart to the Plotly cloud:

# In[12]:

py.plot(fig, filename="Number of meteorites found each year (Horizontal)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (05) - Making horizontal barcharts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to create a horizontal bar chart using the <code>'orientation'</code> key in the trace. We've also seen that we have to change the x- and y-values within the trace, as well as for any annotations positioned on the plotting area. Furthermore, we should also remember to change the x- and y-axis values!
# 
# In the next lesson we'll learn how to plot multiple bar traces on the same chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
