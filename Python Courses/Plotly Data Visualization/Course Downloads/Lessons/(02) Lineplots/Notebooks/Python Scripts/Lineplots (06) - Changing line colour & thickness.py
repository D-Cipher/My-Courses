
# coding: utf-8

# # Lineplots (6) - Changing line colour & thickness

# In the last lesson we saw how to use a For loop to create multiple traces on the same chart. In the coming lessons we're going to learn how to change the style of the traces in our lineplot.
# 
# In this lesson we'll learn how to change the colour and thickness of the line.
# 
# Understanding how colour and shape affect people's perception of the relationships between different data is vital to creating effective charts and I urge you to go beyond the concepts introduced in these lessons. 
# 
# There are many great articles available to help us understand how people perceive colour. <a href = "https://www.perceptualedge.com/articles/b-eye/choosing_colors.pdf">Maureen Stone</a> speaks about how to use colour to group and distinguish different data elements, <a href="https://blog.graphiq.com/finding-the-right-color-palettes-for-data-visualizations-fcd4e707a283#.4ivp20cjv">Samantha Zhang</a> has a more practical article on how to actually choose the colours for your visualisation, and <a href="http://lisacharlotterost.github.io/2016/04/22/Colors-for-DataVis/">Lisa Charlotte Rost</a> provides information on many different resources which you can use to help you incorporate colour into your data visualisations.
# 
# These resources are really helpful, but you will learn the most by experimenting with your own charts and by casting a critical eye over your own and others' visualisations.

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
# As a quick revision session we'll plot the data for the different years using a For loop:

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
         'yaxis' : {'title' : 'Number of Expense Claims'}}


# In[8]:

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (06) - Changing line colour & thickness\pyo.iplot-0.png") 
 #

# ## Changing the colour of a trace

# So whilst it's very helpful that Plotly automatically changes the colour for additional traces, there will doubtless be times when you want to specify the colours yourself; perhaps you need to produce a chart that fits your company's brand theme, or maybe you just love purple and yellow as a colour combination! It's also hard to guarantee that the colours you use will be suitable for black and white printing or for colourblind people (HINT: <a href="http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3">ColorBrewer</a> or <a href="http://vrl.cs.brown.edu/color">Colorgorical</a> really help when choosing colours with this in mind).

# Plotly understands the standard <a href = "http://www.w3schools.com/colors/colors_names.asp">CSS colour names</a>, <a href="http://www.hexcolortool.com/">HEX codes</a> or <a href="http://www.css3.info/preview/rgba/">rgba</a> codes. I'll use a combination of the CSS Colour Names and rgba in this course. The CSS colour names are really easy and intuitive to use and are helpful for quick examples, whilst using rgba allows us to set the opacity of a colour, as well as providing very fine control over the shade and hue.
# 
# To change the colour of a trace we need to add a <code>'marker'</code> key to the trace. The value associated with the <code>'marker'</code> key will be a dictionary which can contain a <code>'color'</code> key:
# 
# ````python
# trace = {'type' : 'scatter',
#         'marker' : {'color' : <CSS Color Name/HEX Code/RGB code/RGBA code/Variable>}
# ````
# 
# Keeping in mind some of the principles of using colour in data visualisation, I'm going to assume that the reader is most interested in the most recent data. I'll therefore colour the trace for 2015 in Red, and all the other traces in Grey.
# 
# We can do this in two ways, first of all by using conditional programming in the For loop. Here, the value of the variable <code>colour</code> changes with each iteration of the loop.

# In[9]:

traces = []
for i in range(2010, 2016):
    if i == 2015:
        colour = 'Red'
    else:
        colour = 'Grey'
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
                   'marker' : {'color' : colour},
             'mode' : 'lines'})


# I'll refresh the Data and Figure objects to see the effect on the chart:

# In[10]:

data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (06) - Changing line colour & thickness\pyo.iplot-1.png") 
 #

# Alternatively, we can define a function to return the colour which we want. I've changed the colour to Blue to show the difference here.

# In[11]:

def chooseColour(yr):
    if yr == 2015:
        return 'Blue'
    else:
        return 'Grey'


# We can now pass the value of <code>i</code> to this function in each iteration of the loop. The function will then return the specified colour as the value which corresponds to the <code>'color'</code> key in the <code>'marker'</code> dictionary:

# In[12]:

traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
                   'marker' : {'color' : chooseColour(i)},
             'mode' : 'lines'})


# Refresh the Data and Figure objects:

# In[13]:

data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (06) - Changing line colour & thickness\pyo.iplot-2.png") 
 #

# It's also possible to change the width of the line. To do this we need to create another key in the trace, but for the <code>'line'</code> option rather than the <code>'marker'</code>:
# ````python
# trace = {'type' : 'scatter',
#         'line' : {'width' : <Float/Integer/Variable>}
# ````
# 
# We can change the width of the line using the same technique as we did when we changed the colour; either by creating a variable within the loop, or by setting the value of width to the output of a function. I'll just do the first method, but feel free to practise with the other method as well.
# 
# I'm going to continue the theme of highlighting the most recent data, setting the trace for 2015 to be thicker than the other traces.

# In[14]:

traces = []
for i in range(2010, 2016):
    if i == 2015:
        width = 2
        colour = 'Red'
    else:
        width = 1
        colour = 'Grey'
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
                   'line' : {'width' : width},
                   'marker' : {'color' : colour},
             'mode' : 'lines'})


# Refresh the Data and Figure objects:

# In[15]:

data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (06) - Changing line colour & thickness\pyo.iplot-3.png") 
 #

# Let's add this file to our Plotly account:

# In[16]:

py.plot(fig, filename="MP Expense claims by month 2010-2015 (Coloured)", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (06) - Changing line colour & thickness\py.plot-0.png") 
 #

# ### Changing line colour and thickness - what have we learnt so far?

# At the start of the lesson we saw that colour is a complex yet important aspect of visualising data. It can be used to group and distinguish different elements.
# 
# We've seen that we can change the colour of a trace by accessing the <code>'color'</code> property in the <code>'marker'</code> sub-dictionary in the trace. Plotly understands several different ways of representing colour; CSS Colour Codes, HEX Code, RGB and RGBA.
# 
# We can change the thickness of the line by accessing the <code>'width'</code> property in the <code>'line'</code> sub-dictionary in the trace. Plotly expects an integer or float value here.
# 
# Finally, we've learnt how to set the line thickness and colour of a trace dynamically within a For loop. We've seen how to do this by creating a variable which holds a different value depending on where in the loop we are, or by using a function to define the value that we want this property to have.
# 
# By changing the colour and line thickness of different data, we can help to make our charts more easily understood, especially in situations where they are printed in black and white, or when they are interpreted by someone with a visual impairment or colourblindness.
# 
# In the next lesson, we'll go a couple of steps further in distinguishing between different data. We'll learn how to change the solidity of the line and add marker symbols which will allow the user to discern even more easily between different data.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
