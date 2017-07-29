
# coding: utf-8

# # Lineplots (13) - Stacked Area Plots

# In the last lesson we looked at how to use the <code>'fill'</code> option to fill the space between the trace and the axis.
# 
# In this lesson we're going to take this a step further and use this option to create a stacked area plot. A stacked area plot is similar to a multiple line plot, however the spaces between each trace are filled with colour.
# 
# We'll also learn how to prepare our data to allow it to be presented as a stacked area plot - the data for this type of chart must be in a specific format to prevent the chart from being misleading, or simply wrong.

# # Module Imports

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


# ### Getting the data
# 
# We'll now get the data to create a stacked area chart. This is the same dataset that we used in the previous lesson.

# In[3]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# I'll get a list of the column names so I can know what column name to pass to the DataFrame to get the data I want. 
# 
# When I made this .csv from the data at the World Bank, the country code was contained within a separate column - this didn't fit into the shape of the data that I wanted and so I concatenated the country code to the country name with a <code>'|'</code> separator. This way I can extract the country code from the name at some point in the future.

# In[4]:

columnNames = emissions.columns.tolist()
columnNames


# ## Creating stacked area graphs
# 
# Stacked area graphs are great at displaying how the share between different categories and the total of all categories changes over time. One of the most effective and beautiful area charts I've seen is <a href="http://www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE_GRAPHIC.html">this one</a> by the New York Times:

# <img src="https://i.kinja-img.com/gawker-media/image/upload/s--K9GtbazJ--/c_fit,fl_progressive,q_80,w_636/18s3l4g96exgapng.png"/>

# It shows the box office revenues for films from 1986 to 2008, with the height of each section showing the revenue by week and the color showing the total revenue for a single film. 
# 
# I don't think we're quite at the stage to be producing something of this sohpistication, but let's take <a href="https://www.ec.gc.ca/indicateurs-indicators/default.asp?lang=en&n=64B9E95D-1">this</a> example as a starting point and use it to make something much nicer:

# <img src="https://www.ec.gc.ca/indicateurs-indicators/64B9E95D-5B44-42A8-98E2-7FBFED3CD6D2/AirPollutantEmissions_VOC_Source_EN.gif"/>

# This chart shows, for Canada, how the total emissions of volatile organic compounds have changed between 1990 and 2014. We can see that the overall amount has reduced, and that most of this reduction has come from Off-road vehicles.
# 
# We're now going to make a stacked area chart showing how total Co2 emissions have changed for 5 countries. There will be a little bit of data manipulation here; I'll try to keep it to a minimum but it is handy to be able to quickly make a few simple changes to the to try displaying it in a new way.
# 
# Doing the data manipulation here also makes it very clear how to construct this stacked area chart, as it is not quite as simple as just entering the data.
# 
# #### When making a stacked area chart, the values for each additional trace are cumulative. That is, if Country A has 100Kt emissions, and Country B has 50Kt of emissions, the line for Country B must be drawn at 150Kt of emissions.
# 
# The first thing to do is to select the countries we want from the emissions DataFrame. We've also got to select the 'Year' column. I'll create a new DataFrame which contains only these columns using the <code>df.loc[]</code> label-based selection. I want to select all rows, but only those columns in the list.

# In[5]:

ColumnSelection = ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND','Year']

stackedAreaData = emissions.loc[:,(ColumnSelection)]
stackedAreaData.head(5)


# The plan here is to create one trace for each country, and one for the total. The difference between this chart and other we have made so far, is that the y-values of one country need to be the sum of the y-values for that country and for all previous countries.
# 
# For example:
# 
# - In 1960 the trace for 'United Arab Emirates' will have a y-value of 11.001. 
# 
# - The trace for 'United Kingdom' will have a y-value of 11.001 + 584299.78.
# 
# - The trace for 'United States' will have a y-value of 11.001 + 584299.78 + 2890696.100, and so on. It might be easier to think of this as a running total for the emissions of each country.
# 
# I'll set the <code>'fill'</code> option to <code>'tonexty'</code>; this will fill the area from each trace down to the line of the previous one, or to y = zero if it is the first trace. I'll leave the <code>'fillcolour'</code> to the default, as I think the default colours are quite nice.
# 
# As the <code>'tonexty'</code> option for <code>'fill'</code> fills the vertical area between each trace, the <code>'tonextx'</code> option will fill the horizontal area between each trace. We won't use <code>'tonextx'</code> in this course, but if it interests you, then please share any charts you make with it!
# 
# This is quite a tedious way of making the traces this chart, however I think it really makes clear the fact that each trace is the cumulative total of itself and all the previous traces. In the next lesson we'll prepare the data in such a way that we can create the traces using a loop.

# In[6]:

UnitedArabEmirates = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'UAE Co2 Emissions'
                     }

UnitedKingdom = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'UK Co2 Emissions'
                     }

UnitedStates = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'USA Co2 Emissions'
                     }

China = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'] + stackedAreaData['China | CHN'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'China Co2 Emissions'
                     }

India = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'] + stackedAreaData['China | CHN'] 
                             + stackedAreaData['India | IND'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'India Co2 Emissions'
                     }


layout = {'title' : "Co2 emissions in kilotons, 1960-2011",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Co2 Emissions (kt)'}}

data = Data([UnitedArabEmirates, UnitedKingdom, UnitedStates, China, India])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (13) - Stacked Area Plots\pyo.iplot-0.png") 
 #

# This chart clearly shows how the total emissions have more than tripled since 1960, with China accounting for the majority of the increase. The UK and UAE's emissions have remained relatively flat. It's quite difficult to see how the proportions of total emissions for each country have changed though. 
# 
# In the next lesson we'll make a stacked proportional area chart. This will involve slightly more data manipulation, but it's a really effective and useful chart to create.
# 
# I'm pretty happy with this plot; I'll send it to the Plotly cloud:

# In[7]:

py.plot(fig, filename="Co2 Emissions for UK, USA, UAE, India & China 1960 - 2011", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (13) - Stacked Area Plots\py.plot-0.png") 
 #

# ### Stacked Area Charts - What have we learnt?
# 
# In this lesson we've learnt how to organise our data into the format required for a stacked area chart; that is, the quantity presented for each trace should be a cumulative total including all previous traces.
# 
# We've also learnt how to implement to <code>'tonexty'</code> option for <code>'fill'</code> to actually make a stacked area chart.
# 
# In the next lesson, we're going to create a proportional stacked area chart - this will show each country's share of the total emissions as a percentage, and presents a very different view of the data.
# 
# 
# I hope you've enjoyed this lesson!

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
