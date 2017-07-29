
# coding: utf-8

# # Tables (8) - Adding tables to a dashboard

# In this lesson we'll find out how to add tables to a dashboard. This is different to how we've included other charts together in a dashboard because we must initialise the figure by creating the table, and then add other charts to it.

# ## Module Imports

# In[3]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[4]:

from plotly.tools import FigureFactory as FF


# In[5]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting a table
# 
# Let's get the table we made in the previous lesson:

# In[6]:

table = py.get_figure("rmuir", 311)
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-0.png") 
 #

# ## Making a bar chart

# Let's now create a bar chart showing some information about the regions compared with the countries. We'll get the information on countries from the csv, but we'll exclude England because we'll be including information about each English region:

# In[10]:

countryDf = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
countryDf = countryDf[countryDf['Name'].isin(['Scotland','Wales','Northern Ireland'])][['Name','Population (2011)']]
countryDf


# And the data on the regions:

# In[11]:

regionsDf = pd.read_csv('http://richard-muir.com/data/public/csv/UKPopulationByRegion.csv', index_col = 0)
regionsDf


# And now let's concatenate them together, set the Population column to numeric, sort the values by Population and reset the index:

# In[12]:

df = pd.concat([countryDf, regionsDf])
df['Population (2011)'] = pd.to_numeric(df['Population (2011)'])
df = df.sort_values(by = 'Population (2011)', ascending = False).reset_index(drop = True)
df


# We can now make a bar trace. I'm going to change the standard colour as well:

# In[13]:

bar = {'type' : 'bar',
      'x' : df['Name'],
      'y' : df['Population (2011)'],
      'marker' : {'color' : '#596dee'}}
pyo.iplot([bar])


py.image.save_as([bar], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-1.png") 
 #

# ## Adding the bar trace to our table

# We can now add the bar trace to our figure containing the table. We're going to plot this bar chart above the table.
# 
# We have to do this in a few steps:
# 
# 1. Add an axis anchor to our bar trace and add the bar trace to the data
# 2. Create new axes to hold the bar chart and set the domain of all the axes
# 3. Anchor the new axes together
# 4. Update the height
# 
# We're going to plot the table after every step to see how it changes:

# ### Adding an axis anchor and adding the bar trace to the table figure
# Because we're adding this chart to a what will be a subplots object we have to specify which axes it will be attached to. Normally the subplots.append_trace() function does this for us.
# 
# We're going to add the bar trace to x2 and y2:

# In[14]:

bar.update({'xaxis' : 'x2',
           'yaxis' : 'y2'})
table['data'].extend([bar])
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-2.png") 
 #

# ### Create new axes and set the domain
# 
# We're adding the bar traces to the y2axis, and we want the bar chart to sit above the table. We therefore need to set the domain of the y1axis and the y2axis to they occupy separate vertical space:

# In[15]:

table['layout']['yaxis'].update({'domain' : [0, 0.3]})
table['layout']['yaxis2'].update({'domain' : [0.5, 1]})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-3.png") 
 #

# ### Anchoring the new axes together
# 
# We need to anchor the new axes together so they know which space to reference:

# In[16]:

table['layout']['yaxis2'].update({'anchor' : 'x2'})
table['layout']['xaxis2'].update({'anchor' : 'y2'})

pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-4.png") 
 #

# ### Updating the height
# 
# Let's now update the height to spread apart the table and chart:

# In[17]:

table['layout'].update({'height' : 500})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-5.png") 
 #

# Let's now increase the left and right margins so we can see the yaxis range and the Northern Ireland label respectively and add a title.
# 
# We'll also need to increase the width to hold the row labels in the table (specifically Northern Ireland)

# In[18]:

table['layout'].update({'margin' : {'r' : 60, 'l' : 20, 't' : 40}})
table['layout'].update({'title' : 'Size of English Regions',
                       'width' : 900})
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\pyo.iplot-6.png") 
 #

# In[ ]:

py.plot(table, filename="Population of English Regions (table & barchart)", fileopt = "overwrite")


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (8) - Adding tables to a dashboard\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to plot tables and charts together. This has been the most complicated way of plotting two different styles of chart together; it was relatively easy to plot bar, scatter and line traces together because they all share the idea of an axis. Plotting pie charts with other types of charts was slightly more difficult as we had to specify the domain, whilst plotting charts and tables together is yet more difficult again becuase we have to manually specify the domain <i>and</i> anchor the axes together.
# 
# We also saw that we have to start with a table, and then add other charts to it, rather than the other way round. This means that when we're making a dashboard we should plan ahead and decide from the beginning if we're going to include a table or not.
# 
# I hope you've enjoyed this section. In the next and final section we'll pull together everything that we've learnt and start creating some dashboards!

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
