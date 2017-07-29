
# coding: utf-8

# # Chart presentation (2) -  Setting the tickformat

# In the last lesson we learnt how to use the <code>plotly.get_figure()</code> function to retrieve a chart from the Plotly cloud and the <code>plotly.plot()</code> function with <code>fileopt = 'overwrite')</code> to push it back to the Plotly cloud and overwrite the original.
# 
# In this lesson we'll use this knowledge to update the format which we apply to the ticklabels.
# 
# Applying a format to a number does not change the value of that number, merely how it's displayed. We'll learn how to format a number as a currency and a percentage with differing levels of decimal precision. We'll also learn how apply datetime formats to the ticklabels.

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


# ## Getting a chart:
# 
# We'll get the same chart as in the last lesson; there's still a few tweaks that we need to make to it before it's ready to be published:

# In[4]:

stocks = py.get_figure("https://plot.ly/~rmuir/162/stock-closing-prices-for-apple-in-2012/")


# Let's just confirm that we've got the right chart:

# In[5]:

pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-0.png") 
 #

# First of all let's format the ticks on the y-axis to show the dollar amount rather than just a number. We can then remove the dollar sign from the axis label.

# ## Changing the tickformat
# 
# Now we'll change the <code>'tickformat'</code> for the y-axis. We can specify the <a href="https://docs.python.org/3/library/string.html#format-string-syntax">Python</a> or <a href="https://github.com/d3/d3-format/blob/master/README.md#format">D3</a> number formats.
# 
# The string formatting language can be quite dense and difficult to interpret, but there are some great resources which can really help you. <a href="https://mkaz.tech/python-string-format.html">Marcus Kazmierczak</a> has some nice examples for the Python number formats, and <a href="http://bl.ocks.org/zanarmstrong/05c1e95bf7aa16c4768e">this</a> bl.ock by Zan has some examples in D3.
# 
# This said, there are some occasions when you won't be able to format the ticks exactly as you wish - I've had difficulty applying a '£' format for example. We'll learn how to work around this problem in the next lesson.
# 
# The <code>'tickformat'</code> option is contained within each of the x- and y-axis objects within the layout:
# ````python
# layout = {'xaxis' : {'tickformat' : <format string>},
#           'yaxis' : {'tickformat' : <format string>}}
# ````
# To change the tick format, we can pass different format string as the value for this option.
# 
# Here are some common string format values we can pass:
# - Percentage with 2 decimal places: <code>".2%"</code>
# - Percentage with 0 decimal places: <code>".0%"</code>
# - Currency with 2 decimal places: <code>"&#36;.2f"</code>
# - Currency with 0 decimal places: <code>"&#36;.0"</code>
# - Currency with 0 decimal places and thousand separator: <code>"&#36;,"</code>
# 
# Let's apply each of these to the chart to see what happens:

# Here, applying the 2 decimal place percentage format has mulitplied the number by 100, and added a decimal point, two 0s and a percentage (%) sign to the number. This isn't what we need for this chart, but we will update the stacked area charts with a similar format later in the lesson.

# In[7]:

stocks['layout']['yaxis'].update({'tickformat' : '.2%'})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-1.png") 
 #

# This is the same format but without the decimal places:

# In[8]:

stocks['layout']['yaxis'].update({'tickformat' : '.0%'})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-2.png") 
 #

# This format gives us the dollar amount and two decimal places:

# In[13]:

stocks['layout']['yaxis'].update({'tickformat' : '$.2f'})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-3.png") 
 #

# This gives us the dollar amount with 0 decimal places:

# In[14]:

stocks['layout']['yaxis'].update({'tickformat' : '$.0'})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-4.png") 
 #

# And this format gives us the dollar amount, but with a ',' separating each thousand. I've had to update the range on this chart to show this in action:

# In[15]:

stocks['layout']['yaxis'].update({'range' : [0, 1500], 'tickformat' : '$,'})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-5.png") 
 #

# Let's change the tickformat to something sensible and update the y-axis title then update our chart.

# In[16]:

stocks['layout'].update({'yaxis' : {'range' : [0, max(stocks['data'][0]['y']) * 1.05],
                                    'title' : 'Closing Price', 'tickformat' : "$.0"}})
pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-6.png") 
 #

# ## Datetime
# 
# Datetime formats work in the same way as number formats; they themselves a form of number format.
# 
# Plotly has a builtin datetime formatter which chooses what it thinks are is the most suitable datetime format to use based on your data. Obviously we can change that! Let's find out how . . .
# 
# A datetime object is made of two parts; a date and a time. Plotly does not recognise a time without a date. 
# 
# - A date object:  31/12/95 - 31st December 1995
# - A time object:  12:35:59.99 - Almost 12:36pm (This is not valid on its own)
# - A datetime object:  31/12/95 12:35:59.99 - Almost 12:36pm on 31st December 1995
# 
# 
# ### Common date formats:
# 
# Here we'll implement a few different date formats to give you some easy ones to work with. You can see the <a href="https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">Python documentation</a> to find out how to build your own datetime formats.
# 
# - UK date: <code>"%d/%m/%y"</code>
# - UK date with 4 digit year:  <code>"%d/%m/%Y"</code>
# - American date with hyphens: <code>"%m-%d-%Y"</code>
# - Abbreviated weekday and month names: <code>"%a %d %b %Y"</code>
# - Unabbreviated weekday and month names: <code>"%A %d %B %Y"</code>
# 
# ### Common time formats:
# 
# We don't have any time data stored in this chart, but the datetime objects have a default time of 00:00:00.00:
# - 24 hour clock with microseconds: <code>"%H:%M:%S.%f"</code>
# - 12 hour clock: <code>"%H%p %M:%S"</code>
# 
# If you have date and time data that you need to display, you can combined these formats:
# - American date with hyphens and 24 hour clock: <code>"%m-%d-%Y %H:%M:%S"</code>
# 
# Let's try a few of these out. I'm going to write a function to make this a little easier:

# In[39]:

def updateDT(dt):
    stocks['layout'].update({'xaxis' : {'tickformat' : dt}})
    pyo.iplot(stocks)


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-7.png") 
 #

# UK date with a two digit year:

# In[40]:

updateDT("%d/%m/%y")


# American date with hyphens:

# In[41]:

updateDT("%m-%d-%Y")


# Abbreviated weekday and month names:

# In[42]:

updateDT("%a %d %b %Y")


# I think that after all of that, I actually prefer the default datetime format for this use case! It seems that adding the day of the month gives a bit too much accuracy for the level of data we're showing:

# In[45]:

updateDT("%b %Y")


# Let's push this fully updated chart to the cloud. Don't forget to overwrite it and remember to spell the filename correctly!

# In[46]:

py.plot(stocks, filename="Stock closing prices for Apple in 2012 (Savitzy-Golay Smoothing)", fileopt = 'overwrite')


py.image.save_as(stocks, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\py.plot-0.png") 
 #

# ### Review and practice
# 
# It's time for you to practise what we've learnt; get the stacked proportional area plots that we previously created and set the y-axis format to a percentage format.

# In[51]:

stackedArea = py.get_figure('rmuir', 168)
stackedArea


# In[52]:

stackedArea['layout']['yaxis'].update({'tickformat' : ".0%", 'title' : 'Percentage of C02 Emissions'})
stackedArea['layout'].update({'title' : 'C02 Emissions, 1960 - 2011'})
pyo.iplot(stackedArea)


py.image.save_as(stackedArea, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\pyo.iplot-8.png") 
 #

# In[54]:

py.plot(stackedArea, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = 'overwrite')


py.image.save_as(stackedArea, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (2) -  Setting the tickformat\py.plot-1.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to apply different number and date formats to the axis ticklabels. This allows us to change how the values are displayed; as percentages, currencies or different datetime formats.
# 
# In the next lesson we'll find out how to specify a ticksuffix and tickprefix for each tick value which will allow us to apply formats that don't exist in the Python or D3 format library, such as a currency format containing a '£'.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
