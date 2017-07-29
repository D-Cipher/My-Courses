
# coding: utf-8

# # Barcharts (10) - Creating our first Dashboard (1)

# In this lesson we're going to create our first dashboard. We're going to take the subplots template object that we created at the end of the last section and populate it with three different charts.
# 
# We're going to include the stacked proportional barchart that shows the number of meteorites by continent as well as two new charts. The first will display a time series line chart of the number of meteorites found in different weight categories each year, and the second will be a scatterplot showing the different weights of the different types of meteorite.

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


# ## Getting our subplots 'skeleton'
# 
# We'll copy the code which we wrote at the end of the last section and use the resulting subplots object as the skeleton into which we'll insert our charts.
# 
# We'll take this opportunity to add the titles to our plots. We pass a list of strings to <code>subplot_titles</code>; each title corresponds to a different subplot, from top left to bottom right.

# In[24]:

fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]],
                   subplot_titles = ["Types of meteorite by weight", 
                                     "Number of meteorites by continent",
                                     "Weight categories of meteorite",
                                    ])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (10) - Creating our first Dashboard (1)\pyo.iplot-0.png") 
 #

# ## Adding a chart to the subplots skeleton
# 
# Let's now retrieve the stacked proportional area plot from the Plotly cloud. We'll need to strip the data from it and append those traces to the subplots object. 
# 
# I think this plot will fit best in the right-most space, but in order to make it fit well, we'll change the orientations of the bars from vertical to horizontal. This also means we need to switch the x- and y-values round:

# In[25]:

stacked = py.get_figure("rmuir", 241)
for d in stacked['data']:
    xVals = d['y']
    yVals = d['x']
    d.update({'orientation' : 'h',
             'x' : xVals,
             'y' : yVals})
    fig.append_trace(d, row = 1, col = 3)
    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (10) - Creating our first Dashboard (1)\pyo.iplot-1.png") 
 #

# ### Styling this chart
# Let's now add the chart and axis titles and some of the other styling options which exist on the main chart.
# 
# Note that by changing <code>'barmode'</code> to <code>'stack'</code>, all of the bar charts on this subplot will be stacked; this is one limitation of using a subplots object to make a dashboard.
# 
# I think we should also increase the height of the chart.

# In[26]:

fig['layout']['xaxis2'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

fig['layout'].update({'barmode' : 'stack',
                      'height' : 1000})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (10) - Creating our first Dashboard (1)\pyo.iplot-2.png") 
 #

# This chart isn't quite finished yet, but we'll return to it in the next lesson.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to take the traces from a chart we've already made and insert them into a subplot. 
# 
# We've also seen how to change some of the layout options for each axis.
# 
# In the next lesson we'll create the other two charts which we'll then insert into this subplot.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
