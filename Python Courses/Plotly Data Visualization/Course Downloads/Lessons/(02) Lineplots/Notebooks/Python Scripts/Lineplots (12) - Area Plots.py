
# coding: utf-8

# # Lineplots (12) - Area Plots

# In this lesson I'm going to introduce the <code>'fill'</code> option and how we can use it to create an area plot. An area plot is basically a line chart with the colour filled in between the trace and the axis. 
# 
# Although an area plot shows the same information as a line plot, the way the data is presented means that they are particularly suited to presenting a quantity of data, such as the amount of oil, money or pollution. The fact that the chart is filled in with colour really helps the reader understand that we are representing a quantity, rather than just a number.

# ## What is an area plot?
# 
# This <a href="https://conceptdraw.com/a2540c3/p1/preview/640/pict--area-graph-us-incarceration-timeline-clean-area-graph">example</a> shows the power of an area graph (although I do not love everything about it, particularly the font). The upward trend in total numbers of encarcerated people would be evident from the line alone, but adding in the red fill undernear really helps to convey the shock of the message. Of course, this plot doesn't take population growth into account, but the author's message is still clear.
# 
# This is another occasion when you have to think about the message that you want to send with your chart - an area plot is another tool for you to use.

# <img src="https://conceptdraw.com/a2540c3/p1/preview/640/pict--area-graph-us-incarceration-timeline-clean-area-graph"/>

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


# ### Creating an area plot
# 
# Let's create an area plot which shows how the total Co2 emissions changed for Great Britain between 1960 and 2015.
# 
# I downloaded the data from <a href="http://data.worldbank.org/indicator/EN.ATM.CO2E.PC?page=2">The World Bank</a> and have already fiddled it into a usable format, available <a href="http://richard-muir/com/data/public/csv/TotalCo2EmissionsByCountry.csv">here</a> (click to download). I'm going to load it straight from my website into Pandas as a DataFrame.
# 
# I'm specifying the <code>index_col</code>, because the index is already contained within the .csv and I don't want to repeat it.

# In[4]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# I'll get a list of the column names so I can know what column name to pass to the DataFrame to get the data I want. 
# 
# When I made this .csv from the data at the World Bank, the country code was contained within a separate column - this didn't fit into the shape of the data that I wanted and so I concatenated the country code to the country name with a <code>'|'</code> separator. This way I can extract the country code from the name at some point in the future.

# In[5]:

columnNames = emissions.columns.tolist()
columnNames


# The column for the UK is called <code>'United Kingdom | GBR'</code>.
# 
# I'll now start making the line chart. We'll see what it looks like without adding the area fill and then look at how that changes the presentation of the data.
# 
# First I'll create the trace. I'll put the year on the x-axis and the total emissions on the y-axis:

# In[16]:

UKEmissions = {'type' : 'scatter',
              'x' : emissions['Year'],
              'y' : emissions['United Kingdom | GBR'],
              'mode' : 'lines',
              'name' : 'UK Co2 Emissions'}

layout = {'title' : "Co2 emissions in kilotons for the UK, 1960-2015",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Co2 Emissions (kt)'}}

data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\pyo.iplot-0.png") 
 #

# Let's send this line plot to the Plotly cloud:

# In[7]:

py.plot(fig, filename="UK CO2 emissions in Kt, 1960-2015", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\py.plot-0.png") 
 #

# So this chart shows quite a clear message; despite a few peaks, the total Co2 emissions for the UK has been steadily decreasing from its peak in the 1970's. 
# 
# Let's see what this looks like as an area graph.
# 
# The <code>'fill'</code> option is contained within the trace object. The possible values are:
# <code>
#     "none" - No fill
#     "tozeroy" - Fills to y = 0 (vertical fill)
#     "tozerox" - Fills to x = 0 (horizontal fill)
#     "tonexty" - Fills between traces (vertically, to the trace before or to 0 if there is no previous trace)
#     "tonextx" - Fills between traces (horizontally, to the trace before or to 0 if there is no previous trace)
#     "toself"  - Connects the endpoints of a trace into a closed shape (useful for <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Synthetic_data_2D_KDE.png/500px-Synthetic_data_2D_KDE.png">Kernel Density Plots</a>)
#     "tonext"  - Fills the space between two plots if one completely encloses the other (useful for Kernel Density Plots again)
# </code>
# 
# We won't be looking at Kernel Density Plots in this course and therefore I won't go into any more detail about <code>'toself'</code> and <code>'tonext'</code>.
# 
# First of all, look at the effect of <code>'tozeroy'</code> and <code>'tozerox'</code>. 
# 
# In the next lesson however, we'll use <code>'tonexty'</code> and <code>'tonextx'</code> to make stacked area graphs.

# In[17]:

UKEmissions.update({'fill' : 'tozeroy'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\pyo.iplot-1.png") 
 #

# You can see how the <code>fill</code> option has filled the area between the trace and the x-axis. This has had the effect of completely changing the message of the chart. In the its first incarnation it seemed like very good news; despite a couple of blips, Co2 has fallen dramatically in the last 40 years. However the chart now sends the message that we still have an awful lot of emissions, and whilst they have fallen, the fall is not a large proportion of the total.
# 
# You'll also notice how the colour under the trace is a much lighter shade (it's actually half-transparent) - this is one of the many things that Plotly does to help us out with the design of our charts, and another option which we can change:

# In[18]:

UKEmissions.update({'fillcolor' : 'rgba(89, 100, 212, 0.46)'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\pyo.iplot-2.png") 
 #

# Let's try changing the <code>'fill'</code> option to <code>'tozerox'</code>. The <code>'tozeroy'</code> option filled the chart down to the y=0 line. The <code>'tozerox'</code> option is going to do the same, but to x=0. Let's see how this affects the chart.

# In[19]:

UKEmissions.update({'fill' : 'tozerox'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\pyo.iplot-3.png") 
 #

# This has produced a strange chart. By setting <code>'fill'</code> to <code>'tozerox'</code>, we have asked Plotly to fill in the area back to the year 0. Because the trace doesn't go back that far, Plotly has copied the y-value for the smallest value of year. 
# 
# The only reason this chart looks wrong is because we chose the wrong value for <code>'fill'</code> to fit our data. If you transpose the x- and y-values and keep the same <code>'fill'</code> option then the chart will make sense again.
# 
# Here's the chart with the x- and y-values switched:

# In[20]:

UKEmissions.update({'x' : emissions['United Kingdom | GBR'],
                   'y' : emissions['Year']})
data = Data([UKEmissions])

layout = {'title' : "Co2 emissions in kilotons for the UK, 1960-2015",
         'xaxis' : {'title' : 'Co2 Emissions (kt)'},
         'yaxis' : {'title' : 'Year'}}

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (12) - Area Plots\pyo.iplot-4.png") 
 #

# Whilst this chart now makes sense, it doesn't necessarily display the data well - it's easier for us to understand time on a horizontal scale rather than a vertical, and easier for us to grasp a magnitude on a vertical scale than a horizontal. I much prefer the first version of this area chart and as such I won't push this to my Plotly cloud, but feel free to do it if you wish!

# ### Area charts - what have we learnt?
# 
# In this lesson we've seen how to create an area chart and how to implement the <code>'tozerox'</code> and <code>'tozeroy'</code> options for <code>'fill'</code>.
# 
# We've also found out how to change the <code>'fillcolor'</code> to have finer control over the style of our chart.
# 
# I hope you've enjoyed this lesson!

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
