
# coding: utf-8

# # Scatterplots (11) - Plotly sub-plots

# Plotly's sub-plots allow us to plot several different charts on the same figure. Over the next few lessons we'll learn how to utilise this feature to create a scatterplot matrix showing the relationships between several different variables. 
# 
# The example below shows a scatterplot where several different variables are plotted against each other. Where the same variable would be plotted against itself, a histogram of that variable's observations is shown:
# 
# <img src="http://176.32.230.52/richard-muir.com/blog/wp-content/uploads/2015/09/correlations1.png"/>
# 
# By the end of the next few lessons you'll be able to create your own scatterplot matrix.
# 
# In this lesson we're going to learn how to place charts on the Plotly sub-plot object. Later we'll learn how to place those charts procedurally using a loop to generate a scatterplot matrix. We'll then write a function to which will allow us to pass any DataFrame which contains appropriate variables, and make a scatterplot matrix of those variables.

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


# We're going to import the <code>tools</code> library which contains the <code>make_subplots()</code> function which will be the main focus of this lesson. We'll also import the <code>random</code> library to help is create some dummy data to plot:

# In[2]:

from plotly import tools
import random


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## The Plotly <code>make_subplots()</code> function
# 
# The Plotly <code>make_subplots()</code> function allows us to create a grid of plots. Each plot is numbered with an (x,y) coordinate, starting at (1,1) in the top-left corner. Note that the grid created by the <code>make_subplots()</code> function is not zero-indexed!
# 
# The <code>make_subplots()</code> function can take the following arguments (amongst others):
# - <code>rows</code> - how many rows of charts are in the subplot
# - <code>cols</code> - how many columns of charts are in the subplot
# - <code>print_grid</code> - whether or not to print a string representation of the grid (this helps when developing the subplot
# - <code>shared_xaxes</code> - whether or not the plots share an x-axis
# - <code>shared_yaxes</code> - whether or not the plots share a y-axis
# - <code>subplot_titles</code> - A list of the titles for each subplot. These are distributed from top-left to bottom-right.
# 
# We'll learn about all of these options as we develop our understanding of the <code>make_subplots()</code> function.
# 
# ## Making subplots
# In order to utilise the <code>make_subplots()</code> functionality, we have to create a subplots object, and then assign a chart to each location in the grid of available spaces.
# 
# Let's make our first subplots object with 2 rows and 2 columns. We also want to set <code>print_grid</code> to <code>True</code> so we can see where each plot will go:

# In[4]:

plots = tools.make_subplots(cols = 2, rows = 2, print_grid = True)


# We can see the shape that our 2 by 2 chart will take. We can also see that Plotly has set up the beginnings of the subplots chart. 
# 
# There is space for us to add the traces to the chart, as well as separate x- and y-axis objects for each subplot. The <code>'domain'</code> information tells us the space that the axis covers on the chart. You can style each of these axes individually, setting the axis titles and range for example, just as we have done with previous charts. 

# In[5]:

plots


# ## Adding charts to the subplots object
# We'll now add a trace to the subplots object. We'll use some dummy data for this so we can focus on learning how to manipulate the subplots object, rather than how to manipulate the individual charts.
# 
# To add a trace to the subplot object, we use the <code>append_trace()</code> method of the subplot object, specifying the row and column location where we'll put the trace.
# 
# The <code>append_trace()</code> method takes 3 arguments:
# - <code>trace</code> - the trace object we're adding to the subplots
# - <code>row</code> - the row reference (enumerated from 1)
# - <code>col</code> - the column reference (also enumerated from 1)
# 
# We're going to append the traces one at a time to the subplots object, plotting it each time to see how it changes. Each trace will be comprised of 10 random x- and y-values which we'll make using the <code>random.random()</code> function:

# In[6]:

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace1'},
                    row = 1, col = 1)

pyo.iplot(plots)


py.image.save_as(plots, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (11) - Plotly sub-plots\pyo.iplot-0.png") 
 #

# Let's add another trace to a different sub-plot:

# In[7]:

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace2'},
                    row = 1, col = 2)
pyo.iplot(plots)


py.image.save_as(plots, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (11) - Plotly sub-plots\pyo.iplot-1.png") 
 #

# We can now fill in the final two spaces:

# In[8]:

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace3'},
                    row = 2, col = 1)

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace4'},
                    row = 2, col = 2)
pyo.iplot(plots)


py.image.save_as(plots, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (11) - Plotly sub-plots\pyo.iplot-2.png") 
 #

# We can also add more than 1 trace to a grid space. Here I'm adding trace5 to the top-left space in the subplots:

# In[9]:

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace5'},
                    row = 1, col = 1)
pyo.iplot(plots)


py.image.save_as(plots, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (11) - Plotly sub-plots\pyo.iplot-3.png") 
 #

# We'll see in a later section how to manipulate some of the styling options for the subplots object itself, but the remainder of the lessons in this section will focus on getting the data into the subplots object and making the subsequent chart clear and informative.

# ### What have we learnt this lesson?

# In this lesson we've learnt what a scatterplot matrix is and have set ourselves the challenge of creating one using the Plotly <code>make_subplots()</code> function.
# 
# We've seen how to create a Plotly subplots object how to add traces to it using the <code>append_trace()</code> method. We've seen that the subplots object takes the form of a grid of charts, and that each trace must be attributed to a space on the grid of plots.
# 
# We've seen that each plot in the subplots object has its own x- and y-axes (by default) which can be styled independently, and that these axes and the grid references are indexed from 1 rather than from 0 as with lists and strings.
# 
# We've also seen that there are other options which we can use to style the subplots object, and we'll cover these in a later section.
# 
# In the next lesson we'll learn how to create a scatterplot matrix procedurally using a loop.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
