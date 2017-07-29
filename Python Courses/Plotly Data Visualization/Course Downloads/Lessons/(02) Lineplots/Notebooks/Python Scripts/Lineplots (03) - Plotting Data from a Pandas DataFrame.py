
# coding: utf-8

# # Lineplots (3) - Plotting Data from a Pandas DataFrame

# In the last lesson we saw how to change the data and layout of our chart with the <code>dict.update()</code> method. 
# 
# In this lesson we're going to plot data from a Pandas DataFrame which we've created from a .csv file.
# 
# In the previous lessons we used dummy data to introduce a line plot. I'm going to keep the use of dummy data to an absolute minimum in this course; when you apply what you've learnt in these lessons you'll be using real data, so why not learn with it too! 

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


# ## Reading a .csv and making a DataFrame

# We're going to use the <code>read_csv()</code> function to read in some data from a .csv file and display it as a DataFrame.
# 
# I'm going to get the data straight from my website, but if you'd like to download the data to your computer, click <a href="http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv">here</a>. When the data is downloaded, simply pass the folder location and filename to <code>pd.read_csv()</code>, rather than the web address.

# In[3]:

expenseData = pd.read_csv("http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv")


# Let's have a quick look at the data. The .csv hold information on the number of expense claims submitted each month by British MPs between 2010 and 2015.

# In[4]:

expenseData.head(5)


# Let's see some summary statistics:

# In[5]:

expenseData.describe()


# ## Plotting the Data
# 
# So, let's make a lineplot which shows these expenses.
# 
# First of all, we need to tell Plotly that we're going to make a scatterplot, but that we only want to see the lines. I'm also going to name the trace:

# In[6]:

trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1'}


# Next, we need to pass the data from the DataFrame to Plotly. Because we're plotting a time series, I'll put the time element on the horizontal axis (X-axis) as this is the convention.
# 
# In this case, the time element is contained within the <code>'month'</code> column in <code>expenseData</code>. It looks like this (the numbers on the left-hand side are the index):

# In[7]:

expenseData['month']


# Let's pass this to our trace:

# In[8]:

trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1',
         'x' : expenseData['month']}


# Now, let's pass the Y-values. I'm going to plot the number of expense claims in 2010.
# 
# The number of expense claims in 2010 is held in the <code>'NumberOfClaims2010'</code> column in <code>expenseData</code>. It looks like this:

# In[9]:

expenseData['NumberOfClaims2010']


# Let's add this to the trace:

# In[10]:

trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1',
         'x' : expenseData['month'],
         'y' : expenseData['NumberOfClaims2010']}


# OK, so now we need to create a Data object as a list of traces. We only have one trace:

# In[11]:

data = Data([trace1])


# Now it's time to create the layout. I'm setting the chart title and the axis titles:

# In[12]:

layout = {'title' : 'Expenses by month in 2010',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of Claims'}}


# Finally, I'll create the Figure object and plot the chart:

# In[13]:

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (03) - Plotting Data from a Pandas DataFrame\pyo.iplot-0.png") 
 ##py.plot(fig, filename = "Something in 2012")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (03) - Plotting Data from a Pandas DataFrame\py.plot-0.png") 
 #

# OK, so we have our first trace; you can see that the quantity of expense claims changes every month, but is it like that every year? 
# 
# Let's make a new chart with the expense claims for 2011.
# 
# I'm going to copy the code that we used to create trace1, and make a few changes so that we can reuse it for trace2.
# 
# I'm going to change the name of the trace and change the column in the DataFrame from which we get the data:

# In[14]:

trace2 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace2',
         'x' : expenseData['month'],
         'y' : expenseData['NumberOfClaims2011']}


# Now I'm going to create a new Data object because I don't want to affect the one which we used to create our first chart:

# In[15]:

data2 = Data([trace2])


# Next I'm going to create a new layout and change the title. We have to create a new layout object because we don't want to affect the original.

# In[16]:

layout2 = {'title' : 'Expenses by month in 2011',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of Claims'}}


# Finally, I need to create a new Figure object:

# In[17]:

fig2 = Figure(data = data2, layout = layout2)

pyo.iplot(fig2)


py.image.save_as(fig2, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (03) - Plotting Data from a Pandas DataFrame\pyo.iplot-1.png") 
 #

# ### Creating and styling charts with multiple traces - what have we learnt?

# So we've seen how to create different charts from the same DataFrame - if you feel that you need more practise in doing this, you can try to create some more charts using the other columns in the DataFrame.
# 
# This said, it's difficult to compare the data for each year when they are all on different charts. In the next lesson we'll see how to create a chart with multiple traces.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
