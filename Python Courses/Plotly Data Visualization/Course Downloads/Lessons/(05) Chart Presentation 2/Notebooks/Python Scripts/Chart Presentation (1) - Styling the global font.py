
# coding: utf-8

# # Chart Presentation (1) - Styling the global font

# In this lesson we're going to learn how to apply styling options to text displayed in Plotly. Text can be displayed on the chart as a datapoint, on the chart as an annotation, in the legend, as a ticklabel, or as an axis or chart title.
# 
# In this lesson we'll learn how to set the global font on the chart, learning about the styling options and how this affects each type of chart text.

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


# In[2]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Styling text

# By setting the global font we can style the font colour, font family and font size. In each case, the styling options are contained in a dictionary within the layout:
# ````python
# {'font' : {'color' : <HTML colour representation>,
#             'family' : <HTML font family (only some available)>,
#             'size' : <integer >= 1>}}
# ````
# 
# The most restrictive of these options in the <code>'family'</code> option. Plotly has a number of fonts installed on their server, including:
# - Arial
# - Balto
# - Courier New
# - Droid Sans
# - Droid Serif
# - Droid Sans Mono
# - Times New Roman
# 
# However in practise these fonts don't often work on every machine. For this reason, I suggest sticking to Arial, Courier New or Times New Roman.
# 
# Let's now look at how the styling options affect text on a chart by creating a dummy chart with each of the types of text, and trying out some different styling options:

# ### Making the chart
# 
# Here's our dummy chart which contains each type of text: text as a data point, annotation text, ticklabels, axis titles, chart title and a legend:

# In[3]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
         'xaxis' : {'title' : 'Who likes fruit?'},
         'yaxis' : {'title' : 'Who likes cheese?'},
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (1) - Styling the global font\pyo.iplot-0.png") 
 #

# Let's now set the global <code>'font'</code> within the <code>'layout'</code>. I'm going to start by setting the <code>'color'</code> to a dark grey, and the <code>'family'</code> to a Serif font.
# 
# The default font <code>'size'</code> is <code>12</code>, and each separate text item inherirts its size from this number:

# In[4]:

textStyling = {'color' : '#333',
              'family' : 'Times New Roman',
              'size' : 12}

fig['layout']['font'] = textStyling

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (1) - Styling the global font\pyo.iplot-1.png") 
 #

# I'm going to try a slightly darker colour, and a more modern font family:

# In[5]:

textStyling = {'color' : '#292929',
              'family' : 'Arial',
              'size' : 12}

fig['layout']['font'] = textStyling

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (1) - Styling the global font\pyo.iplot-2.png") 
 #

# Let's try changing the global <code>'font'</code> <code>'size'</code> to see the effect this has on the chart:

# In[6]:

textStyling = {'color' : '#333',
              'family' : 'Droid Serif, Raleway,Times New Roman',
              'size' : 20}

fig['layout']['font'] = textStyling

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (1) - Styling the global font\pyo.iplot-3.png") 
 #

# You can see that each different text option has changed size relative to the global font size.

# ### What have we learnt this lesson?

# In this lesson we've found out how to set the global font styling options. We've seen that we can set the font family (although it's generally a good idea to stick with common fonts) and the colour, and that these styles apply to each text item.
# 
# We've also seen that we can change the global font size, but that this size serves as a starting point for the sizes of the other text items.
# 
# In the next lesson we'll find out how to control the individual font styles for each type of text.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
