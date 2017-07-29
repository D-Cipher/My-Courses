
# coding: utf-8

# # Chart presentation (3) - Modifying tickvalues

# In the last lesson we saw how to apply different tickformats to the ticks on the x- and y-axes.
# 
# In this lesson we'll learn how to modify the standard tickvalues by adding a tick prefix or suffix. We'll also learn how to specify the number of ticks that Plotly shows.

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


# ## Getting a chart to modify:
# 
# We'll use the stacked area chart showing total emissions for 5 countries to practise setting the tickprefix, ticksuffix and number of ticks:

# In[46]:

C02 = py.get_figure('rmuir', 156)
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-0.png") 
 #

# ## Modifying the tick values
# 
# We can change how the tick values are displayed by adding a tick suffix or prefix.
# Both of these options are contained within in the x- and y-axis objects:
# ````python
# layout = {'xaxis' : {'ticksuffix' :  <string>}}
# ````
# 
# Let's add a tick suffix of <code>'Kt'</code> to the ticks on the y-axis:

# In[35]:

C02['layout']['yaxis'].update({'ticksuffix' : ' Kt'})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-1.png") 
 #

# We can also add a tick prefix if we wish. I'm removing the title so that it doesn't overlap with the longer ticks:

# In[37]:

C02['layout']['yaxis'].update({'tickprefix' : 'C02: ', 'title' : ''})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-2.png") 
 #

# I'm not a fan of the tick prefix in this case, however it is useful when plotting currencies which aren't available as a tickformat. I'll remove the tick prefix and reinstate the title before we continue:

# In[38]:

C02['layout']['yaxis'].update({'tickprefix' : '', 'title' : 'C02 Emissions'})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-3.png") 
 #

# Let's make a chart to practise using the <code>'tickprefix'</code> parameter.
# 
# We'll plot a line which shows the average house prices in England in £. There is no currency format which displays '£', but we can use a tick prefix to achieve this:

# In[26]:

housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKAvgHousePrices.csv")
housePrices.head()


# In[30]:

EnglandAvgPrices = {'type' : 'scatter',
                   'x' : housePrices['Date'],
                   'y' : housePrices['England']}

data = Data([EnglandAvgPrices])
layout = {'title' : 'Average house prices in England 1995 - 2016',
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-4.png") 
 #

# Let's set the tickformat on the yaxis to have a thousand separator of a ' , ':

# In[31]:

fig['layout']['yaxis'].update({'tickformat' : ','})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-5.png") 
 #

# We can now change the tick prefix to show a '£':

# In[32]:

fig['layout']['yaxis'].update({'tickprefix' : '£'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-6.png") 
 #

# Let's send this chart to the Plotly cloud:

# In[33]:

py.plot(fig, filename="Average House Prices in England 1995-2016")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\py.plot-0.png") 
 #

# ## Changing the number of ticks
# 
# We'll use the C02 emissions plot from earlier to practise changing the number of ticks.
# 
# First of all, let's increase the number of tick along the x-axis. We can do this by setting the <code>'tickmode'</code> to <code>'auto'</code> and specifying the number of ticks with the <code>'nticks'</code> parameter. Both of these options are contained within in the axis object:
# ````python
# layout = {'xaxis' : {'tickmode' : 'auto', 'nticks' : <integer>}}
# ````
# 
# Let's try doubling the number of ticks to show a tick every 5 years:

# In[39]:

C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 12})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-7.png") 
 #

# We can also make the ticks more sparse:

# In[40]:

C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 3})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-8.png") 
 #

# But note that Plotly views the value for<code>'nticks'</code> as being the maximum number of ticks; it may not actually draw the requested number of ticks:

# In[41]:

C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 5})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-9.png") 
 #

# Let's set the <code>'nticks'</code> parameter to 12 and update the chart in the Plotly cloud:

# In[42]:

C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 12})
pyo.iplot(C02)


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\pyo.iplot-10.png") 
 #

# In[43]:

py.plot(C02, filename="C02 Emissions for UAE, USA, UK, India & China 1960 - 2015", fileopt = 'overwrite')


py.image.save_as(C02, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (3) - Modifying tickvalues\py.plot-1.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to use the <code>'tickprefix'</code> and <code>'ticksuffix'</code> options to expand our options for how to display the ticklabels. Using <code>'tickprefix'</code> and <code>'ticksuffix'</code> in conjunction with <code>'tickformat'</code> allows us to effectively create formats which Plotly doesn't recognise, such as a £ currency format.
# 
# We've also seen how to change the number of ticks that Plotly shows, but that this number is only a maximum; Plotly will choose the actual amount of ticks to be below this number and spaced depending on the data in the chart.
# 
# In the next lesson we'll find out how to specify the exact text and position for each tick value which will give us a lot more freedom and opportunity to design the chart that we envisage.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
