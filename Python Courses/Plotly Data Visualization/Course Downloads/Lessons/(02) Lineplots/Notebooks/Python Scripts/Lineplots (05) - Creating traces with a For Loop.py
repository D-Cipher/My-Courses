
# coding: utf-8

# # Lineplots (5) - Creating traces with a For Loop

# In the last lesson we saw how to create multiple traces and plot them on the same chart. We did this manually and found that it took quite some time. Fortunately, we can solve this problem!
# 
# In this lesson I'm going to show you how to use a For loop to create multiple traces. We'll then plot these traces on the same chart.
# 
# One benefit of using a For loop to create multiple traces is that you don't have to write as much code as if you did them all by hand. Secondly, you can also write your code in such a way that you can include future updates to the data with only minimal changes to the code. We'll learn how to do this in two different ways.

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


# ### Making our first trace

# Below is the code that we used to create our traces in the previous lesson. With a few changes we can adapt this code to make it suitable to be run in a For loop. We'll make the same chart with two different For loops to give you some different options for when you make your own chart.

# In[5]:

trace_2010 = {'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2010'],
             'name' : '2010',
             'mode' : 'lines'}


# ### Looping through the years of data
# 
# I have set up my data in a way that allows us to loop through it easily. The data for each year has been named in a consistent way - we can use a For loop to loop through the years.
# 
# The first step is to create an empty list to store the traces in:

# In[6]:

traces = []


# Next, I'll create the loop:

# In[7]:

for i in range(2010, 2016):
    print(i)


# You can see how in each iteration of the loop, the variable <code>i</code> takes the value of a different year.
# 
# Now, I'll loop through the years again, but this time I need to append some items to our list of traces. I'll start by just appending the values of <code>i</code>:

# In[8]:

for i in range(2010, 2016):
    traces.append(i)
    
traces


# Now, let's add in the code we used to create the traces in the previous lesson. I've reset the variable <code>traces</code> to be an empty list:

# In[9]:

traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2010'],
             'name' : '2010',
             'mode' : 'lines'})
traces


# So each list in the list of traces contains data for the same year - we have simply copied it. Before you continue, think about what changes we need to make to the code in order to get the data for different years.
#  
#   
#    
# We'll use the value of the variable <code>i</code> to access different columns in the DataFrame and to set a different name for the trace:

# In[10]:

traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
             'mode' : 'lines'})
traces


# Now you can see that each trace holds different data.
# 
# We need to turn the list of traces into a Data object. The variable <code>traces</code> is already a list so we don't need to contain it in square brackets:

# In[11]:

data = Data(traces)


# Let's reuse the layout that we utilised in the previous lesson - we just have to change the title to reflect the data held in the chart.

# In[12]:

layout = {'title' : 'Expense claims by month for 2010 - 2015',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of expense claims'}}


# Now, we'll create the Figure object:

# In[13]:

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (05) - Creating traces with a For Loop\pyo.iplot-0.png") 
 ##py.plot(fig, filename = "Expenses by month in 2012 & 2013")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (05) - Creating traces with a For Loop\py.plot-0.png") 
 #

# Now you can see 6 of the standard colours that Plotly uses. We can also see the relationship between the data much more clearly than if all the traces we on separate charts. It looks like 2010 and 2015 don't follow the same pattern as the other years.

# ### Loop through the column names in a DataFrame

# For cases when the column names don't follow a particular convention, we can instead loop through the column names.

# In[14]:

for col in expenseData.columns.tolist():
    print(col)


# We don't want to plot the <code>month</code> variable as a Y-value, as we're already plotting it as an X-value...

# In[15]:

for col in expenseData.columns.tolist():
    if col != 'month':
        print(col)


# Now, let's adjust the code slightly:

# In[16]:

traces = []
for col in expenseData.columns.tolist():
    if col != 'month':
        traces.append({'type' : 'scatter',
                 'x' : expenseData['month'],
                 'y' : expenseData[col],
                 'name' : col,
                 'mode' : 'lines'})
traces


# We have to refresh the Data and Figure objects, but we can reuse the Layout from the previous chart, only having to slightly change the title.

# In[17]:

layout = {'title' : 'Expense claims by month for 2010-2015',
         'xaxis' : {'title' : 'month'},
         'yaxis' : {'title' : 'Number of expense claims'}}


# In[18]:

data = Data(traces)
fig = Figure(data = data, layout = layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (05) - Creating traces with a For Loop\pyo.iplot-1.png") 
 #

# You can see how the data that has been plotted is identical. The only thing that has changed is that the legend items now have different names (HINT: you can use string slicing to remove this difference).
# 
# These two methods for using a For loop to create traces from a DataFrame are very versatile and powerful; we'll be using them a lot in this course.
# 
# Let's sent this plot to our Plotly account!

# In[19]:

py.plot(fig, filename="MP Expense claims by month 2010-2015", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (05) - Creating traces with a For Loop\py.plot-1.png") 
 #

# ### Using a For loop to plot multiple traces - what have we learnt?

# We've seen how to use a For loop in two different ways to allow us to dynamically create multiple traces.
# 
# We saw that if the columns in our data have a consistent naming convention, then we may be able to loop through a list of numbers and use the loop variable to access the column names.
# 
# For data where the naming convention is not consistent, we can instead loop through a list of the column names, being careful not to plot one of the variables as both an x-variable and a y-variable (month, in this case).
# 
# In the next lesson we'll look at how to style these different traces.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
