
# coding: utf-8

# # Lineplots (07) - Making dashed and dotted lines

# In the last lesson we saw how to change the colour and thickness of the lines in our plot. 
# 
# In this lesson we'll learn how to displayed a dashed or dotted line instead of a solid line. In the next lesson we'll find out how to set the marker symbol for each trace. Changing these two properties in addition to manipulating the colour and line width gives us the ability to distinguish between a large number of different data items.

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

# We'll get the data from the same source as the previous lesson.

# In[3]:

expenseData = pd.read_csv("http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv")


# In[4]:

expenseData.head(5)


# ## Plotting the data
# 
# We'll plot the data for the different years using a For loop:

# In[5]:

traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
             'mode' : 'lines'})


# In[6]:

data = Data(traces)


# In[7]:

layout = {'title' : 'Number of expenses by month for 2010 - 2015',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Yaxis title1'}}


# In[8]:

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (07) - Making dashed and dotted lines\pyo.iplot-0.png") 
 #

# ## Changing the solidity of a line

# We can change the solidity of a line by using the <code>'dash'</code> option in the <code>'line'</code> dictionary in the trace:
# ````python
# trace = {'type' : 'scatter',
#         'line' : {'dash' : <Dash string/Dash length in pixels/Variable>}
# ````
# 
# Some valid dash strings are:
# - <code>'solid'</code>
# - <code>'dash'</code>
# - <code>'dot'</code>
# - <code>'dashdot'</code>
# 
# Here's what the dash strings look like. 
# 
# I'm using a list of dash strings to contain the possible values.
# 
# I'm using the enumerate function and floor division to give me the number of the index to pass to the list. The <code>enumerate()</code> creates a variable which holds the value of each item's index in the list in addition to the variable which holds the actual value of the variable. This value starts at 0 for the first item and increments by one for each subsequent item.

# In[9]:

dashes = ['dash', 'dot', 'dashdot']

for i, yr in enumerate(range(2010, 2016)):
    print(i, yr)


# In[10]:

for i, yr in enumerate(range(2010, 2016)):
    print(dashes[(i//2)])


# Now I'll apply this to our loop which creates the traces:

# In[11]:

traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'line' : {'dash' : dashes[i//2]},
             'name' : yr,
             'mode' : 'lines'})


# Refreshing the Data and Figure objects to see the effect on the chart:

# In[12]:

data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (07) - Making dashed and dotted lines\pyo.iplot-1.png") 
 #

# Let's push this chart to the cloud. It's not quite production-ready, but it's good to record our progress!

# In[13]:

py.plot(fig, filename = "MP expenses by month 2010-2015 (Line solidity)", filopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (07) - Making dashed and dotted lines\py.plot-0.png") 
 #

# ### Changing line solidity - what have we learnt?
# 
# We've seen how to manipulate the value of the <code>'dash'</code> key in the <code>'line'</code> dictionary to change the solidity of the line. We can use a string such as <code>'dashdot'</code> or set the dash length to be an integer number of pixels. We also utilised the <code>enumerate()</code> function to help us choose an item from a list by index and value.
# 
# In the next lesson we'll find out how to specify that Plotly shows the marker in addition to the line. We'll also see how to change the marker symbol.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
