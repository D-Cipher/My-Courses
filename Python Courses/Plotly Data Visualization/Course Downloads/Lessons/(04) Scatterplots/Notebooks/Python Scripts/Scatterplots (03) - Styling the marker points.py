
# coding: utf-8

# # Scatterplots (03) - Styling the marker points

# In this lesson we're going to learn how to apply different styling options to  the marker points. We've already briefly touched upon this in the lineplots section, however in this lesson we'll take a more in-depth look at the styling options available.
# 
# In the lineplots section, the aim of utilising the marker styling options was to enable us to distinguish between the different data points, however this lesson will focus more on the stylistic aspect of manipulating the marker symbols - let's make them look GOOD!
# 
# We'll quickly review the available marker symbol shapes, then find out how to change their size, opacity, colour and outline.

# ## Module Imports

# In[48]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[49]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting a chart
# We'll use the same chart that we made in the previous lesson:

# In[50]:

revEmp = py.get_figure("rmuir", 200)
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-0.png") 
 #

# ### Changing the marker symbols
# Let's quickly review how to change the marker symbol on this scatterplot. Through the use of different marker symbols we can allow the reader to discern between two different categories on the same plot. These categories are often distinguished through the use of colour, but using different marker symbols accounts for those times when the colour is not sufficient (black and white printing, colour-blindness etc).
# 
# You can find a list of the available symbols <a href="https://plot.ly/python/reference/#scatter-marker-symbol">here</a>.
# 
# To change the marker symbol we need to change the <code>'symbol'</code> option within the <code>'marker'</code> dictionary. 
# ````python
# trace = {'marker' : {'symbol' : <symbol string or numer>}}
# ````
# Marker symbols are represented by a string or a number, and there are four different stying options available (although not every marker symbol has all available styling options):
# - solid (default)
# - open
# - dot
# - open-dot
# 
# 
# 
# Let's try out a few of these marker symbols and see how they look on the chart:

# In[51]:

revEmp['data'][0].update({'marker' : {'symbol' : 'square'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-1.png") 
 #

# In[52]:

revEmp['data'][0].update({'marker' : {'symbol' : 'square-open'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-2.png") 
 #

# In[53]:

revEmp['data'][0].update({'marker' : {'symbol' : 'triangle-left'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-3.png") 
 #

# I'll change the marker symbols on this chart back to 'circle', but you can explore your own options for the marker symbols to create your own style for your charts.

# In[54]:

revEmp['data'][0].update({'marker' : {'symbol' : 'circle'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-4.png") 
 #

# ### Changing marker size, opacity and colour
# 
# Plotly allows us to control different aspects of the marker style. We can change the size, opacity and colour by manipulating different options within the marker dictionary:
# ````python
# trace = {'marker' : {'opacity' : <number between 0 and 1 inclusive>,
#                      'size' : <number >= 0>,
#                      'color' : <a colour name, hex, rgb or rgba value>}}
# ````                     

# #### Marker size
# 
# Let's see how we can change the marker size. I've increased the size to 8 (the default is 6) because I'd like the styling of the points to be clear. There's some overplotting here, but we can make this obvious by changing the opacity of the marker point

# In[55]:

revEmp['data'][0].update({'marker' : {'size' : '8'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-5.png") 
 #

# #### Marker opacity
# 
# We'll now change the marker opacity; the markers are currently totally opaque, but I find that adding a slight opacity to the marker symbols can greatly enhance the look of a chart:

# In[56]:

revEmp['data'][0].update({'marker' : {'opacity' : '0.7'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-6.png") 
 #

# #### Changing the colour
# 
# I'm going to change the colour to something a little different to the standard Plotly blue:

# In[57]:

revEmp['data'][0].update({'marker' : {'color' : '#6A5ACD'}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-7.png") 
 #

# ## Changing the marker line
# 
# Every marker can have an outline, and Plotly allows us very fine control over the appearance of this line. We're only going to look at the line width and colour. Because we've set our points to be slightly transparent, adding a dark outline to them will really make them stand out. I chose the width of this line after some trial and error, but feel free to spend some time developing your own style.

# In[58]:

revEmp['data'][0].update({'marker' : {'line' : {'width' : 1.25, 'color' : 'black'}}})
pyo.iplot(revEmp)


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\pyo.iplot-8.png") 
 #

# I'm going to push this chart to the Plotly cloud:

# In[59]:

py.plot(revEmp, filename="Revenue by number of employees (styled)", fileopt = "overwrite")


py.image.save_as(revEmp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (03) - Styling the marker points\py.plot-0.png") 
 #

# ### What have we learnt this lesson?
# 
# In this lesson we've reviewed how to change the marker symbol, and which options for styling the symbol are available. We've also found out how to change the marker colour, size and opacity, as well as how to style the line that surrounds the marker.
# 
# In the next lesson we're going to plot a scatterplot with different categories, using what we've just learnt to style the dots in these categories so they can be easily distinguished.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
