
# coding: utf-8

# # Chart presentation (1) - Changing the range

# Welcome to the first lesson in this Chart Presentation section. In this section we'll learn how to change the range of the axes of our charts, define and format the ticklabels and control the hover behaviour.
# 
# So far in the course we have focused on getting the data into our charts and making sure that it's legible, clear and that each data item is distinguishable from the others. We've looked at how to change the colour of a trace, the line thickness and the marker symbols, however there are other aspects of a chart which also need to be changed to ensure that the chart is the best it can possibly be.
# 
# In this lesson we're going to learn how to load a chart from the Plotly cloud, update the range of the axes for the chart, and overwrite the file stored in your user account.

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


# ## Retrieving a chart from your plotly account
# 
# Before we can begin to polish our charts, we must first retrieve them.
# 
# We can use the <code>plotly.get_figure()</code> function to get the Figure object which relates to your chart.
# 
# We can retrieve the chart in two ways:
# - pass the plotly url of the chart (you can get this by clicking 'Share' on the chart and getting the shareable link
# - pass the file owner and the unique file id separately
# 
# Here's how we get it the first way:

# In[3]:

stocks = py.get_figure("https://plot.ly/~rmuir/162/stock-closing-prices-for-apple-in-2012/")


# And the second:

# In[4]:

stocks = py.get_figure('rmuir', 162)
stocks


# We can now pass this object to the <code>po.iplot()</code> function to confirm that it's the correct chart:

# In[5]:

pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (1) - Changing the range\pyo.iplot-0.png") 
 #

# Great, that looks to be exactly as we left it!
# 
# It's now time to update the range of the y-axis on this chart; I'd like this axis to extend down to 0 to show the stock price change relative to 0.

# ## Changing the range

# So far, most of the work we have done has revolved around making changes to the traces; we have only manipulated the layout to change the chart and axis titles. The layout option allows us to control how the chart is displayed and there are many options to explore. For now, let's just update the axes objects to change the range.
# 
# Each of <code>'xaxis'</code> and <code>'yaxis'</code> within the layout object have their own <code>'range'</code> attribute which we can change. We set the range for each axis as a list of two numbers (float or integer). These number correspond to the minimum and maximum values respectively:
# 
# ````python
# layout = {'xaxis' : {'range' : [<min>, <max>]},
#           'yaxis' : {'range' : [<min>, <max>]}
#           }
# ````
# 
# Let's update the range in this chart:

# In[6]:

stocks['layout']['yaxis'].update({'range' : [0, 1000]})

pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (1) - Changing the range\pyo.iplot-1.png") 
 #

# So that is quite different, we can see how the stock price has moved relative to 0, but there is a lot of empty space above the line. I'm going to use the Python <code>max()</code> function to find the maximum y-value in the chart and update the range accordingly:

# In[7]:

maximum = max(stocks['data'][0]['y'])
maximum


# I can now pass this value to the range, but it's a good idea to add about 5% to the maximum range value to give a little space at the top. Similarly, I'd also subtract about 5% from the minimum range value if we wanted the range to fit the chart exactly.

# In[8]:

stocks['layout']['yaxis'].update({'range' : [0, maximum * 1.05]})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (1) - Changing the range\pyo.iplot-2.png") 
 #

# Let's push this updated chart to the cloud.
# 
# When overwriting a chart it's important to specify the same name that you saved the chart as. You can get this name by clicking on the share icon in your Plotly cloud. I'm not aware of a way of getting the plot name programmatically. You should specify fileopt = 'overwrite' to overwrite your chart and you should also check the the unique identifier for your overwritten chart is the same as the one which you loaded.

# In[9]:

py.plot(stocks, filename="Stock closing prices for Apple in 2012 (Savitzy-Golay Smoothing)", fileopt = 'overwrite')


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (1) - Changing the range\py.plot-0.png") 
 #

# You can also set the range when building the chart by taking the maximum and minimum of the data when creating the chart. The pandas <code>df.max()</code> and <code>df.min()</code> methods make this really easy:

# In[10]:

df = pd.read_csv("http://richard-muir.com/data/public/csv/BoEBaseRate.csv")
df.head()


# This gets the maximum value for each column in the DataFrame. Note that the maximum value for the DATE column is the maximum value when the dates are compared as strings, rather than being the largest (most recent) date value.

# In[11]:

df.max()


# We can convert this string to a date using <code>pd.to_datetime()</code>:

# In[12]:

df['strDate'] = pd.to_datetime(df['DATE'])
df.head()


# Now we can get the maximum value:

# In[13]:

df.max()


# This gets the maximum value for a single column in the DataFrame:

# In[14]:

df['VALUE'].max()


# And the same for <code>df.min()</code>. Once again we have the smallest string value for DATE, rather than the earliest date.

# In[15]:

df.min()


# In[16]:

df['VALUE'].min()


# ### What have we learnt this lesson?

# In this lesson we've learnt how to get a chart from the Plotly cloud, update the range of the x-axis and overwrite the original chart. 
# 
# We've seen how to use the Python <code>max()</code> and <code>min()</code> functions to get the maximum and minimum values in a list or array, and the Pandas <code>df.max()</code> and <code>df.min()</code> methods to get the maximum and minimum values in a DataFrame.
# 
# We've also learnt that it's good practise to set the range to be slightly wider than the range between the minimum and maximum values; I generally increase (or decrease) the value by 5%.
# 
# In the next lesson we'll find out how to specify different formats for the tick values on the axes.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
