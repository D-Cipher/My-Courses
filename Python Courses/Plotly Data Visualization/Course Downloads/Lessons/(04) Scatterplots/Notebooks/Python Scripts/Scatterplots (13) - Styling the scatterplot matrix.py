
# coding: utf-8

# # Scatterplots (13) - Styling the scatterplot matrix

# In this lesson we're going to style the scatterplot matrix that we created in the last lesson.
# 
# We're going to learn how to change the dimensions of the chart, set subplot titles and manipulate each of the x- and y-axes of the subplots object. This will allow us to make sure that any mulitple plots that we create using the Plotly subplots function are clear and well-presented.

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


# We're going to import the tools library again:

# In[2]:

from plotly import tools


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the chart  
# We'll copy the code from the previous chart that we created rather than load it from the Plotly cloud because we're going to make the changes from inside the loop which creates the chart:

# In[4]:

iris = pd.read_csv("http://www.richard-muir.com/data/public/csv/irisDataset.csv", index_col = 0)
irisSpeciesUnique = list(iris['Species'].unique())
colours = ['green','blue','orange']
colourLookup = dict(zip(irisSpeciesUnique, colours))

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour},
                                 'name' : species},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\pyo.iplot-0.png") 
 #

# The first thing we'll do is only show one legend item for each trace. We'll do this by creating a <code>'legendgroup'</code> for each species, and setting <code>'showlegend'</code> to <code>True</code> only for the first trace in each group.
# 
# At this point I'm also going to reduce the marker size on the traces:

# In[5]:

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\pyo.iplot-1.png") 
 #

# ## Styling the subplots object
# 
# First of all, we'll set the plots to have shared x- and y-axes. This will make the plot look a lot cleaner and reduce the quantity of lines and numbers inbetween the subplots:

# In[6]:

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True, shared_xaxes = True, shared_yaxes = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\pyo.iplot-2.png") 
 #

# ## Changing the axis titles
# We now need to add titles to the axes to inform the user which dimensions are being compared. We only need to add y-axis titles to the left-most axes and x-axis titles to the bottom-most axes. We can see from the output from the <code>'print_grid'</code> option that the axes we need to select are:
# - x1, x2, x3 & x4
# - y1, y2, y3 & y4
# 
# Let's add this into our loop. We'll update each axis object inside the layout as we reach the correct position in the loop. We'll update the axis object with the axis title and a new range so that all of the traces are displayed on the scame scale:

# In[7]:

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True, shared_xaxes = True, shared_yaxes = True)

for i, column in enumerate(iris.columns[:-1]):
    fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column + " (cm)",
                                              'range' : [0, max(iris[iris.columns[:-1]].max())]})
    
    for j, row in enumerate(iris.columns[:-1]):
        fig['layout']['yaxis{}'.format(j + 1)].update({'title' : row + " (cm)",
                                                  'range' : [0, max(iris[iris.columns[:-1]].max())]})
        
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\pyo.iplot-3.png") 
 #

# The axis titles are looking a bit squashed, let's change the height of the chart to give a bit more space. I'll also take this opportunity to set the chart title and hover behaviour:

# In[8]:

fig['layout'].update({'title' : 'Length and width of sepals and petals for Iris supspecies',
                     'height' : 1000})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\pyo.iplot-4.png") 
 #

# So this chart has come out looking really well. We've added some axis titles and stretched the chart out a bit to give a bit more space. Let's push it to the Plotly cloud:

# In[9]:

py.plot(fig, filename="Iris scatterplot matrix", fileopt = 'overwrite')


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (13) - Styling the scatterplot matrix\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to apply some styling to our scatterplot matrix. First of all we reduced the number of items being shown in the legend and linked the traces together for each Iris species. We saw how to set the subplots to have shared x-and y-axes, and that by doing so (when appropriate!) we can reduce the amount of clutter on the chart.
# 
# We then saw how to access each x- and y-axis object as we cycled through the loop. We used this knowledge to add x- and y-axis titles, as well as setting the ranges to be the same for every axis. Finally, we saw how to change the chart height to spreadh the y-axis labels out and make the chart a bit clearer.
# 
# We'll come back to styling the subplots object in the next section, but in the next lesson we'll learn how to write a function that will generalise the creation of scatterplot matrices.
# 

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
