
# coding: utf-8

# # Chart Presentation (1) - Styling the legend

# In this third section on chart presentation we'll mainly focus on how to style the legend. We'll see how to colour and position the legend, as well as how to change how the items within it are postioned. Finally, we'll also learn how to change the background colour of our plotting area.
# 
# In this lesson we're going to learn how to apply some styling options to the legend. We're going to see how to set a border for the legend and find out how to change the thickness and color of the border. We'll also look at how the set a background colour for the legend.

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


# ## Styling the legend border
# 
# Putting a border around your legend is a great way to visually separate it from your chart. In Plotly we can control the thickness and colour of the legend border. 
# 
# Let's grab our stacked bar chart showing meteorite landings per continent and the percentage of meteorites under 101 grams in mass; we'll use this to practise on in this section.

# In[6]:

stacked = py.get_figure("rmuir", 251)
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\pyo.iplot-0.png") 
 #

# The legend styling options are contained within the layout. We're going to use the <code>bordercolor</code> and <code>borderwidth</code> keys to style the legend's border.
# 
# Let's set the borderwidth to 5 to see how that affects the legend:

# In[7]:

stacked['layout'].update({'legend' : {'borderwidth' : 5}})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\pyo.iplot-1.png") 
 #

# So that's a bit thick, let's reduce it slighlty:

# In[11]:

stacked['layout'].update({'legend' : {'borderwidth' : 2}})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\pyo.iplot-2.png") 
 #

# We can now change the colour the legend border. I'm going to try something a little lighter:

# In[22]:

stacked['layout']['legend'].update({'bordercolor' : '#e0e0e0'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\pyo.iplot-3.png") 
 #

# ## Changing the background colour for the legend
# 
# By changing the background colour of the legend we can force it to stand out even more from the chart. I'm going to set the background colour to be slightly lighter than the border:

# In[23]:

stacked['layout']['legend'].update({'bgcolor' : '#ededed'})
pyo.iplot(stacked)


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\pyo.iplot-4.png") 
 #

# By slightly changing background and border colour of the legend we have distinguished it from the rest of the chart. This can be useful if the legend is key to your readers understanding the chart.
# 
# I'm going to push this chart to the Plotly cloud:

# In[24]:

py.plot(stacked, filename="Meteorites by continent and weight (styled legend)", fileopt="overwrite")


py.image.save_as(stacked, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart Presentation (1) - Styling the legend\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to set the border thickness and colour, as well as the background colour of the legend.
# 
# In the next lesson we'll see again how to set the tracegroupgap, as well as how to set the traceorder.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
