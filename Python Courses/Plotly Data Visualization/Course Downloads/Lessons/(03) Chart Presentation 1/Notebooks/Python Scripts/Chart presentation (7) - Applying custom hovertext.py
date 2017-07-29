
# coding: utf-8

# # Chart presentation (7) - Applying custom hovertext

# In the last lesson we found out how to create a custom text field in a Pandas DataFrame using the <code>apply()</code> and <code>lambda</code> functions.
# 
# In this lesson we'll plot a chart which will show this custom hovertext field.

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


# ### Getting the data
# 
# We'll load the house price and ranks dataset from my website and use the code we wrote in the previous lesson to create the text column for each region.

# In[6]:

housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/RegionalHousePricesAndRanksJan16.csv")

regions = ['South West','South East','London', 
           'East of England','West Midlands','East Midlands',
           'Yorkshire and The Humber','North West','North East']

for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(round(x, 0)))) + "<br><i>Rank of average price: " + housePrices[r + "_rank"].apply(lambda x: 
                                                                                                             str(int(x))) + "</i>"
housePrices.head(1)


# ### Plotting the data
# 
# Now, let's create our plot of the changes in the average house price:

# In[93]:

traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (7) - Applying custom hovertext\pyo.iplot-0.png") 
 #

# So you can see that the default hovertext makes things a little clearer, but it's not quite there. The average price is the full floating point number, when we really don't need that much precision, and the trace name isn't particularly clear. Let's add the  text field that we created and see how this changes the chart:

# In[94]:

traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"]})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (7) - Applying custom hovertext\pyo.iplot-1.png") 
 #

# So that's a little better; we have the information that we placed in the text field - the region name, formatted average price and the rank, but Plotly is still showing the default hover information. Let's change the <code>'hoverinfo'</code> option to on show the <code>'text'</code> and the x-values:

# In[80]:

traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"],
                  'hoverinfo' : 'text+x'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (7) - Applying custom hovertext\pyo.iplot-2.png") 
 #

# Much better! But still not there yet.
# 
# When we hover over the chart, we only ever see the information for the first five traces, as the hoverinfo fills all the available space. Let's change <code>'hovermode'</code> in the layout object to <code>'closest'</code> and see if that improves things:

# In[83]:

traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"],
                  'hoverinfo' : 'text+x'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'},
         'hovermode' : 'closest'}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (7) - Applying custom hovertext\pyo.iplot-3.png") 
 #

# I think that's done it! Let's push this chart to the Plotly cloud:

# In[84]:

py.plot(fig, "Average UK houses prices by region (1995 - 2016)")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (7) - Applying custom hovertext\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've created a chart which uses a custom hovertext field. We've seen the effect of incorporating the &lt;b&gt;...&lt;/b&gt; tags to create bold text, the &lt;i&gt;...&lt;/i&gt; for italicised text, and the &lt;br&gt; tag to insert a line break, and how Plotly interprets these tags.
# 
# We've also reviewed how to control what information is displayed on hover, using the <code>'hoverinfo'</code> and <code>'hovermode'</code> in the trace and layout objects respectively.
# 
# In the next lesson we'll practise what we've learnt about creating custom hovertext fields to the C02 emissions charts that we previously made.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
