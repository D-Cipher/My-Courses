
# coding: utf-8

# # Barcharts (11) - Creating our first Dashboard (2)

# In this lesson we're going to finish adding the data to this dashboard. We'll get the traces we need to create the final two charts and add these traces to the subplots object.

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


# We'll use the Plotly sub-plots module:

# In[2]:

from plotly.tools import make_subplots


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the chart from the previous lesson
# 
# Below is all the code we wrote in the last lesson to make this chart:

# In[4]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]],
                   subplot_titles = ["Types of meteorite by weight", 
                                     "Number of meteorites by continent",
                                     "Weight categories of meteorite",
                                    ])

stacked = py.get_figure("rmuir", 241)
for d in stacked['data']:
    xVals = d['y']
    yVals = d['x']
    d.update({'orientation' : 'h',
             'x' : xVals,
             'y' : yVals})
    fig.append_trace(d, row = 1, col = 3)
    
fig['layout']['xaxis2'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

fig['layout'].update({'barmode' : 'stack',
                      'height' : 1000})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (11) - Creating our first Dashboard (2)\pyo.iplot-0.png") 
 #

# ## How many meteorites were found each year in each weight category?
# 
# Let's add the traces for the number of meteorites in each weight category which were found each year. We'll get this data from my website:

# In[5]:

sizes = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightPerYear.csv", index_col = 0)
sizes.head()


# Let's take our code from a previous lesson to calculate the proportion for each weight category:

# In[6]:

sizeStrings = sizes.columns.tolist()

sizes['total'] = sizes.sum(axis = 1)
for s in sizeStrings:
    sizes["{}_pc".format(s)] = sizes[s] / sizes['total']
    
sizes.head()


# Now we'll add a trace for each of the weight categories and append these traces to the bottom-most cell.
# 
# Because we're using proportions, we also need to set the tickformat and hoverformat:

# In[7]:

for s in sizeStrings:
    fig.append_trace({'type' : 'scatter',
                     'mode' : 'markers+lines',
                     'x' : sizes.index,
                     'y' : sizes["{}_pc".format(s)],
                     'name' : s},
                    row = 3, col = 1)
    
fig['layout']['yaxis3'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (11) - Creating our first Dashboard (2)\pyo.iplot-1.png") 
 #

# You'll notice that Plotly keeps cycling through its default list of colours as we add each additional trace. We'll set the colours ourselves later to avoid this behaviour.
# 
# ### Adding the size and type of meteorites
# 
# We'll now get the final data for this chart as a .csv from my website. This .csv file contains information on the type of and weight of each meteorite.

# In[8]:

typeWeight = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightAndType.csv", index_col = 0)
typeWeight.head()


# Let's now make a scatter trace showing the type of meteorite against the weight for that meteorite. We'll show the type on the xaxis and weight on the yaxis. We'll append this trace with row = 1 and col = 1.
# 
# We won't show a legend for this chart because there will only be one trace.

# In[9]:

fig.append_trace({'type' : 'scatter',
             'mode' : "markers",
             'x' : typeWeight['wideClass'],
             'y' : typeWeight['mass (g)'],
                'showlegend' : False},
                row = 1, col = 1)

fig['layout']['yaxis1'].update({'title' : 'Weight (g)'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (11) - Creating our first Dashboard (2)\pyo.iplot-2.png") 
 #

# So there's our first (almost) finished Dashboard. I say almost finished because we still have some work to do to style the chart. We should change the colours so the dashboard itself looks coherent, set the hover behaviour so that it's optimal for all the charts and find a way to break up the legend items so it's clear they relate to different charts.

# ### What have we learnt this lesson?

# In this lesson we've practised adding traces to our subplot object and have made our first Dashboard.
# 
# In the next lesson we'll style this dashboard to make it really clear to our readers.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
