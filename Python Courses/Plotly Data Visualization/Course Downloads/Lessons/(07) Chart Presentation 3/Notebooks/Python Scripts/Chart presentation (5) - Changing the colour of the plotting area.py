
# coding: utf-8

# # Chart presentation (5) - Changing the colour of the plotting area

# In this lesson we're going to learn how to change the colour of the plotting area. This is especially useful for if you need to align the presentation of your charts with a specific theme or brand.

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


# ## Options for changing the colour.
# 
# There are two colours we can change; the <code>'paper_bgcolor'</code> and the <code>'plot_bgcolor'</code>. 
# 
# <code>'paper_bgcolor'</code> changes the colour of the area around the plotting area, whilst <code>'plot_bgcolor'</code> changes the colour of the background of the plotting area. Just to keep things interesting, let's test this on a different chart to the one that we've been using.

# In[4]:

lifeExp = py.get_figure('rmuir', 225)
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart presentation (5) - Changing the colour of the plotting area\pyo.iplot-0.png") 
 #

# Let's change the <code>'paper_bgcolor'</code> first. I'm going to change it to an off-white colour:

# In[5]:

lifeExp['layout'].update({'paper_bgcolor' : '#faebd7'})
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart presentation (5) - Changing the colour of the plotting area\pyo.iplot-1.png") 
 #

# You can see how this changes the colour for everything but the plotting area. We can now change the colour within the plotting area:

# In[6]:

lifeExp['layout'].update({'plot_bgcolor' : '#faebd7'})
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart presentation (5) - Changing the colour of the plotting area\pyo.iplot-2.png") 
 #

# You can see that by changing the background colour of the chart, it would be very easy to make it fit seamlessly into a theme on a website or in a report.
# 
# I'm going to send this to the Plotly cloud:

# In[7]:

py.plot(lifeExp, filename="Life expectancy and GDP per capita (coloured background)", fileopt='overwrite')


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(07) Chart Presentation 3\Notebooks\images\Chart presentation (5) - Changing the colour of the plotting area\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to use the <code>'paper_bgcolor'</code> and <code>'plot_bgcolor'</code> options to change the colour of any charts we make.
# 
# In the next section we'll learn how to make some pie charts.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
