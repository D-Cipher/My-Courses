
# coding: utf-8

# # Lineplots (8) - Changing marker symbols

# In the last lesson we saw how to change the solidity of the line; showing a dashed or dotted line rather than a solid one.
# 
# In this lesson we'll see how to add different marker symbols to our traces. We'll also get a sneak preview of how to manipulate the properties of the <code>'marker'</code> option, but we'll cover this in more depth in the Scatterplots lessons.

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


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-0.png") 
 #

# ## Changing Marker Symbols
# 
# In the <a href="https://plot.ly/python/reference/">Plotly docs</a>, there is a list of the different marker symbol codes you can choose, and a very helpful plotly user has kindly made a <a href="https://plot.ly/~neda/1032/hover-over-the-marker-points-to-see-their-names/">chart which shows these symbols</a>, although it doesn't display particularly well.
# 
# I'm going to pick a couple of different marker symbols to demonstrate the concept, but please experiment and find ones which work for you!
# 
# We've already accessed the <code>'marker'</code> sub-dictionary to change the colour of our trace. To change the marker symbol, all we have to do is add a <code>'symbol'</code> key to this dictionary:
# 
# ````python
# trace = {'type' : 'scatter',
#         'marker' : {'symbol' : <Marker symbol string/Variable>}
# ````
# 
# We also need to tell Plotly that we want to use markers in addition to lines by changing the value for <code>'mode'</code> from <code>'lines'</code> to <code>'lines+markers'</code>:
# ````python
# trace = {'type' : 'scatter',
#         'mode' : 'lines+markers'}
# ````
# 
# We have a choice of two options for how to set the marker symbol; there are 44 (at the time of writing) basic options available, and most of the marker symbols can be made to be shown <code>'open'</code>, with a <code>'dot'</code> or both: <code>'dot-open'</code>. This makes for over 100 different marker options
# 
# First of all, we can use a symbol name. Here I'll use a brief list of 6 different marker symbols; one for each trace.

# In[9]:

markerSymbols = ['circle','square','diamond','x','triangle-up','cross']


# In[10]:

traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'marker' : {'symbol' : markerSymbols[i]},
             'name' : yr,
             'mode' : 'lines+markers'})
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-1.png") 
 #

# Next, we can plot these symbols as with the additional <code>'open'</code> option:

# In[11]:

markerSymbolsOpen = ['circle-open','square-open','diamond-open','x-open','triangle-up-open','cross-open']
traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'marker' : {'symbol' : markerSymbolsOpen[i]},
             'name' : yr,
             'mode' : 'lines+markers'})
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-2.png") 
 #

# I'm going to push this chart to the Plotly cloud. There's still a few more charts to make in this lesson, but they are really for demonstration.

# In[12]:

py.plot(fig, filename = "MP number of expense claims 2010-2015 (Marker symbols)", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\py.plot-0.png") 
 #

# The <code>'dot'</code> option only works on scatterplots where there is no line to obscure the dot in the centre. 
# 
# I'll turn the <code>'line'</code> option off for now, and set but we'll look properly at Scatterplots in a later lesson.
# 
# I also need to change the <code>marker size</code> and the <code>marker line width</code> properties in order to be able to see the difference, but rest assured that we'll cover these in depth in a later lesson.

# In[13]:

markerSymbolsDot = ['circle-dot','square-dot','diamond-dot','x-dot','triangle-up-dot','cross-dot']
traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'marker' : {'symbol' : markerSymbolsDot[i], 'size' : 10, 'line' : {'width' : 1}},
             'name' : yr,
             'mode' : 'markers'})
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-3.png") 
 #

# Finally, we can combine the <code>'open'</code> and <code>'dot'</code> options. These must be specified in that order.

# In[14]:

markerSymbolsOpenDot = ['circle-open-dot','square-open-dot','diamond-open-dot','x-open-dot','triangle-up-open-dot','cross-open-dot']
traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'marker' : {'symbol' : markerSymbolsOpenDot[i], 'size' : 10, 'line' : {'width' : 1}},
             'name' : yr,
             'mode' : 'markers'})
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-4.png") 
 #

# As an alternative to specifying the name of the marker, you can also specify the number; each of the 44 markers is enumerated.
# 
# You can add 100 to the number to specify that the marker should be <code>'open'</code>, add 200 to specify <code>'dot'</code>, and add 300 to specify <code>'open-dot'</code>. Remember that this won't necessarily work on every option - in the case of the last trace, this hasn't worked and the marker has been replaced with the standard <code>'O'</code>:

# In[15]:

markerSymbolsNum = [1,101,201,301,25,225]
traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'marker' : {'symbol' : markerSymbolsNum[i], 'size' : 10, 'line' : {'width' : 1}},
             'name' : yr,
             'mode' : 'markers'})
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (08) - Changing marker symbols\pyo.iplot-5.png") 
 #

# ### Changing marker symbols - what have we learnt?
# 
# We've seen that Plotly has loads of available marker symbols that we can use to distinguish traces from each other. 
# 
# We've found out how to specify the marker symbol by passing a string or a number to the <code>'marker' 'symbol'</code> option.
# 
# We've learnt that for most symbols, we can specify that the symbol is presented without colour (<code>'open'</code> or <code>+100</code>), with a dot in the centre (<code>'dot'</code> or <code>+200</code>), or both (<code>'open-dot'</code> or <code>+300</code>).
# 
# We've also seen that in order to be able to see the impact of these options, we have to change the <code>'marker' 'size'</code> and <code>'marker' 'line' 'width'</code>, but that we will learn more about these options in a later lesson.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
