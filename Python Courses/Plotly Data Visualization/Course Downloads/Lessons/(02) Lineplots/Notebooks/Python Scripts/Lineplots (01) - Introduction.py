
# coding: utf-8

# # Lineplots (1) - Introduction

# In this lesson we'll find out how to make a simple lineplot in Plotly. We're going to start at the very basics, but as we progress through the lessons in this section, we'll add more options to our code and more functionality to our chart. 
# 
# First of all we'll learn about the concept of a 'trace'. We'll make a chart with one trace and in doing so learn how to set the values of the x- and y-variables.

# ## Module Imports

# These library imports will remain the same for most of the lessons in this course; we may add a few more libaries or different modules from existing libraries later on in the course.
# 
# <code>plotly.offline</code> allows us to use Plotly's <code>plot</code> function to create your charts without pushing them to the cloud. This is handy when you're developing a chart and don't want multiple beta versions being displayed publicly.
# 
# On the other hand, <code>plotly.plotly</code> makes the chart and pushes it to your Plotly account in the cloud. We'll use this when we're happy with the chart we've made.
# 
# <code>pandas</code> is a great library for data analysis and manipulation. It's very powerful and very complex; a full tutorial on how to use it is far beyond the scope of this course, but there are a few functions that we'll use repeatedly, one of these being a Pandas DataFrame.

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


# This bit of magic here allows us to view the charts inside an iPython Notebook. When coupled with <code>plotly.offline</code>, this allows us to have a very quick iterative process as we develop and tweak the charts.

# In[2]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# # The structure of a chart

# In order to create a chart in Plotly, we must pass our instructions to it in a certain structure.
# 
# The <code>plotly.plot()</code> function expects to recieve a Figure object.
# 
# This Figure object is comprised of two parts; a Layout and the Data. These parts are kept separate in Plotly - we can style a chart without affecting the data within it.
# 
# The Layout object contains information about the size of the chart, the title, the axis title, the font and many other aspects.
# 
# The Data object is comprised of a list of traces. A trace is one of the key concepts when using Plotly. There is no absolute definition to what a trace is or can be however I describe a trace as a collection of data points which you want to share a set of traits. 
# 
# For example, you may want to display the stock prices over time for several companies on the same line chart; obviously you would want each line to have a separate colour! You would therefore need to make a separate trace for each company.
# 
# At a high level, the structure of the chart could be represented like this:
# ````
# Figure = {'layout' : {<information about the chart's layout>},
#            'data' : [{trace1}, {trace2}, {trace3}]
#            }
# ````

# ### Making the trace

# We'll now make our first trace.
# 
# A Plotly chart is made of a series of instructions which Plotly interprets and uses to decide how to display the chart. We're going to give these instructions to Plotly in the form of a dictionary.
# 
# A dictionary is comprised of key/value pairs, separated by commas and enclosed in curly brackets. Each key and value is separated by a colon:
# ````python
# dict1 = {'key1' : 'value1', 'key2' : 10}
# ````

# The first instruction which we'll give to Plotly tells it what type of data this trace will display; we're going to make a scatterplot. 
# 
# You might be wondering why this lesson is called 'Lineplot (1)' when we're actually making a scatterplot. This is because Plotly treats all scatterplots, lineplots, bubbleplots and textplots as being a type of scatterplot - all we have to do is vary the instruction which we give to Plotly to determine which chart to create.

# In[3]:

trace1 = {'type' : 'scatter'}


# The second instruction tells Plotly the x-values of the chart.
# 
# Plotly expects this to be a list of numbers and it will interpret the list from left to right. This simple example has the numbers in ascending order, but this does not necessarily have to be the case.

# In[4]:

trace1 = {'type' : 'scatter',
        'x' : [0,1,2,3,4,5,6,7,8,9]}


# The third instruction tells Plotly what the y-values of the chart are; these are interpreted in the same way as the x-values, from left to right.

# In[5]:

trace1 = {'type' : 'scatter',
        'x' : [0,1,2,3,4,5,6,7,8,9],
        'y' : [0,1,2,3,4,5,6,7,8,9]}


# Next, we should give a name to our trace. This isn't essential however it is good practise, especially when we start to incorporate more traces into our charts.

# In[6]:

trace1 = {'type' : 'scatter',
        'x' : [0,1,2,3,4,5,6,7,8,9],
        'y' : [0,1,2,3,4,5,6,7,8,9],
        'name' : 'trace1'}


# Finally, we'll tell Plotly to only display the lines on the chart - we don't want it to show any scatter points.

# In[7]:

trace1 = {'type' : 'scatter',
        'x' : [0,1,2,3,4,5,6,7,8,9],
        'y' : [0,1,2,3,4,5,6,7,8,9],
        'name' : 'trace1',
        'mode' : 'lines'}


# The next thing to do is to create the Data object. Plotly expects to receive the traces as a list. the <code>Data()</code> function was imported from the <code>plotly.graph_objs</code> library.

# In[8]:

data = Data([trace1])


# ### Setting the layout

# As I previously mentioned, the data and the presentation of the data are kept separate. In the cell below I'll set some of the layout options.
# 
# I'll set the chart title first, and then the axis titles. The axes each have their own set of parameters that can be changed. For now, we'll only specify the title for each axis:

# In[9]:

layout = {'title' : "My first plotly line chart",
         'xaxis' : {'title' : 'X Values'},
         'yaxis' : {'title' : 'Y Values'}}


# ### Creating the figure object and plotting it

# Although the data and layout are kept separate, at some point we need to combine them in order to display the chart as intended.This is where the Figure object comes in. 
# 
# The Figure object takes the sets of instructions that we specified for the data and the layout, aggregating them togther. The Figure object is created by the <code>Figure()</code> function which we imported from the <code>plotly.graph_objs</code> library.

# In[10]:

fig = Figure(data = data, layout = layout)


# Finally, we'll plot the figure object in offline mode.
# 
# When you're happy with the chart, uncomment the <code>py.plot(...)</code> line to push your first chart to the Plotly cloud! Here we can also specify a filename. This is the name which appears on the plotly cloud when we push the finished chart up. 

# In[11]:

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (01) - Introduction\pyo.iplot-0.png") 
 #
# Uncomment this to push the chart to the cloud:
#py.plot(fig, filename="My first line chart")`

py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (01) - Introduction\py.plot-1.png") 
 #


# You can see clearly how each of the options we specified in the chart have determined how it looks. The chart and axis titles are exactly as expected, and we can see how the x- and y-values relate to the list of values we passed to trace1.
# 
# There's also some behaviour that we didn't ask for! You'll notice that if you hold your mouse over the line a number appears. Because our x- and y-values are identical, we can't yet tell what the default option is (although it looks like the y-values appear on the line, and the x-values by the x-axis), but you can go to <a href="https://plot.ly/python/reference/">the plotly website</a> to find out what the defaults are for any option.
# 
# Alternatively, we could update the chart and see if we can make any changes which will allow us to find this out without using the reference . . . 
# 
# We'll look at how to change this hover behaviour in later lessons.

# ### What have we learnt in this lesson?

# We've learnt how to create a Plotly trace, fill it with data and name it. We've also learnt that we must pass the trace(s) to Plotly in a list - this becomes the Data object.
# 
# We've seen how to set the chart and axis titles in a Layout object, and that the Data and Layout objects are combined into a Figure.
# 
# We've also seen that the default option for the <code>hovertext</code> shows the x-values on the x-axis, and the y-values next to the chart.
# 
# I hope you've enjoyed making your first chart with Plotly, and I hope you'll join me to learn some more!

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
