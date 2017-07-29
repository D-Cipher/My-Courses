
# coding: utf-8

# # Lineplots (14) - Stacked proportional area plots

# In the last lesson, we saw how to make a stacked area plot using the <code>'tonexty'</code> option for the <code>'fill'</code> option. This allowed us to compare the change in total emissions, as well as the change in each individual country's emissions over a period of time.
# 
# In this lesson we're going to create a stacked area plot which shows the percentage of total emissions that each country produced. The code for the chart will be almost identical to the previous lesson; the novelty in this lesson will be learning how to do a little data manipulation to get the data into percentages of total emissions, rather than just the raw figures. 
# 
# We'll also prepare the data in a way that allows us to create the traces using a loop, rather than the long-form way we learnt in the previous lesson, and in doing so we'll learn how to use the <code>pandas.cumsum()</code> function to get a cumulative sum over several traces.

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


# ## Getting the data
# 
# I'll get the data in the same way as the previous lesson:

# In[3]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# ### Preparing the data
# 
# The next step is to select from the DataFrame the columns which we want to include in our chart. I'm going to include the same five countries as in the previous lesson - I suggest you do the same so you can check your code is working properly. 
# 
# To make life a little easier in the future, I'm going to select the columns in two stages. First of all I'm going to get a list of the countries that will be included in the chart. This list will serve two purposes:
# - Select the countries that we want to include
# - Provide a list of country columns which we can use to create the row totals (we don't want to add the year column to the total)
# Then, I also need to pass the <code>'Year'</code> column to the selection to make sure that's included in the new DataFrame:

# In[4]:

sumColumnSelection = ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',]

stackedAreaData = emissions.loc[:,(['Year'] + sumColumnSelection)]
stackedAreaData.head()


# The next step is to calculate the row totals for each year; we'll need these in order to calculate each country's share of the total emissions each year. We'll do this with the <code>df.sum()</code> method and the list of countries that we've just created.

# In[5]:

stackedAreaData['Total'] = stackedAreaData[sumColumnSelection].sum(axis = 1)
stackedAreaData.head()


# Now, I'll calculate each country's percentage of total emissions for the year. I'll write a loop to go through the columns to make this easier:

# In[6]:

for country in sumColumnSelection:
    stackedAreaData["pc_"+str(country)] = stackedAreaData[country] / stackedAreaData['Total']
    
stackedAreaData.head()


# We can now use the <code>pandas.DataFrame.cumsum()</code> method to get a cumulative row total of the percentages. This will allow us to create the traces much more easily. 
# 
# First of all I'll make a new list of the percentage columns:

# In[7]:

sumColumnSelectionPC = ['pc_United Arab Emirates | ARE','pc_United Kingdom | GBR', 
                   'pc_United States | USA','pc_China | CHN', 'pc_India | IND',]


# Now, I'll use that list to only select the percentage columns for cumulative summing. I'm also going to create a new object:

# In[8]:

PCAreaData = stackedAreaData[sumColumnSelectionPC].cumsum(axis=1)
PCAreaData.head()


# We can check if this worked by using a calculator on a couple of rows. However it does seem likely that it worked because the cumulative total for India is 1 in every case.
# 
# Next we need to add the <code>'Year'</code> column to the DataFrame - we'll take this straight from the <code>stackedAreaData</code> DataFrame.

# In[9]:

PCAreaData['Year'] = stackedAreaData['Year']

PCAreaData.head()


# ### Plotting the chart
# 
# Now, we can loop through the columns in the DataFrame and create our traces. 
# 
# I'm using a string slice to remove the <code>'pc_'</code> and the country code from the column name to create a meaningful name for the trace.

# In[10]:

traces = []

for col in PCAreaData.columns.tolist():
    if col != 'Year':
        traces.append({'type' : 'scatter',
                      'x' : PCAreaData['Year'],
                      'y' : PCAreaData[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
traces


# Let's create the Data, Layout and Figure objects and plot the chart!

# In[11]:

data = Data(traces)
layout = {'title' : "Proportion of Co2 Emissions, 1960-2011",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Proprtion of Co2 Emissions'}}
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (14) - Stacked proportional area plots\pyo.iplot-0.png") 
 #

# This chart, whilst showing the same data as the previous chart, paints a very different picture. We can see that the United Arab Emirates' proportion of total emissions has risen slightly, the UK's had fallen to about a third of the 1960 levels by 2010. America's share of total emissions has dropped even more dramatically, whilst China and India's share of emissions has rise, with China's share rising much more dramatically.
# 
# When taken in conjunction with the previous chart, which showed how the total emissions has rises, both of these charts present a very powerful message.
# 
# On a more critical note, this chart isn't quite there yet. The hoverinfo shows the cumulative sum of emissions, rather than each country's individual emissions and it would also be nice to display the proportions as percentages. We will return to both of these in a future lesson, but for now I'm really happy with this chart; let's push it to the Plotly cloud!

# In[12]:

py.plot(fig, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (14) - Stacked proportional area plots\py.plot-0.png") 
 #

# ### Stacked proportional area plots - what have we learnt?
# 
# This class focussed more on data manipulation that on actually charting. We saw that with a few simple functions and methods, we can make our life much easier!
# 
# We learnt how to use label-based indexing to select certain columns from a DataFrame. We used the <code>df.sum(axis = 1)</code> method to get a total for each row in the DataFrame to allow us to calculate the percentage of total.
# 
# We calculated the percentage of total emissions for each country in a list using a loop, and then used <code>df.cumsum(axis=1)</code> to give us a cumulative total over the columns.
# 
# Finally, we plotted this data using a For loop, specifying <code>'fill' : 'tonexty'</code> in the trace.
# 
# In the next lesson we're going to wrap all of this in a function which will let us create a stacked area plot for as many countries as we wish.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
