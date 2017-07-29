
# coding: utf-8

# # Scatterplots (12) Making a scatterplot matrix

# In this lesson we're going to revisit the Iris dataset and create a scatterplot matrix to see the relationships between the different sepal and petal widths and lengths.
# 
# We're going to apply what we learnt in the previous lesson about the <code>make_subplots()</code> function to this task of making a scatterplot matrix, using a loop to determine at which point on the grid the traces will be placed.

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


# We're going to import the <code>tools</code> library again:

# In[2]:

from plotly import tools


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# We're going to load the Iris dataset which we used at the beginning of this section:

# In[4]:

iris = pd.read_csv("http://www.richard-muir.com/data/public/csv/irisDataset.csv", index_col = 0)
iris.head()


# We need to get a list of the unique values in the Species column; this will help us to plot only the observations for each species.

# In[5]:

irisSpeciesUnique = list(iris['Species'].unique())
irisSpeciesUnique


# We'll now take this list of species and map it to a list of colours to create a lookup dictionary to assign the same colour to each species name. We'll usew this dictionary to choose the rows for each species in the DataFrame and assign that species a specific colour.
# 
# The <code>zip</code> function is used here to combine the list of colours with the list of Iris species. We then turn the resulting object into a <code>dict</code> which has the species as keys and the colours as values.

# In[6]:

colours = ['green','blue','orange']
colourLookup = dict(zip(irisSpeciesUnique, colours))
colourLookup


# ## Creating the subplots object
# 
# Our scatterplot matrix will plot each of Sepal Length, Sepal Width, Petal Length and Petal Width against every other variable.
# 
# Because we have four variables to plot against each other we need to create a 4x4 grid. Each variable will have be plotted at one row location and one column location. I'm setting <code>print_grid</code> to <code>True</code> to help with the development process - we can turn this off when we've finished.

# In[7]:

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)


# ## Appending each trace to a space on the grid
# 
# We're going to write a nested loop which will give each trace a position on the grid.
# 
# The outermost loop will cycle through the variables to be plotted on the columns. The next loop will cycle through these same variables, but will track the row position. The innermost loop will cycle through the different species of Iris, appending three traces to that particular (row, column) coordinate.
# 
# Let's write a dummy loop to take care of the behaviour of the outer two loops as these are the most difficult. The output should look like this:
# ````python
# (1,1)
# (1,2)
# (1,3)
# (1,4)
# (2,1) etc.
# ````
# Let's do the outer loop first:

# In[8]:

for column in range(1, 5):
    print(column)


# Now the inner loop:

# In[9]:

for column in range(1, 5):
    for row in range(1, 5):
        print(column, row)


# Let's test this with a list of columns from the DataFrame. I'm not including the last column, Species, as we won't be plotting the data in this column:

# In[10]:

for column in iris.columns[:-1]:
    print(column)


# In[11]:

for column in iris.columns[:-1]:
    for row in iris.columns[:-1]:
        print(column," , ", row)


# We don't want to plot a variable against itself, so we'll exclude cases where <code>column == row</code>. I'll also use the <code>enumerate()</code> function to generate the numbers which will position the trace on the subplots object (remembering to add 1 to each number because the subplots are indexed from 1):

# In[12]:

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column == row:
            print("")
        else:
            print(column," , ", row, " | ", (i + 1, j + 1))


# We can now create our traces by creating one more loop within the two we have just created.
# 
# In this innermost loop we'll cycle through the items in the lookup dictionary we created earlier, assigning each species the same colour from the lookup we created earlier.
# 
# We'll use the <code>df.loc[]</code> indexer to choose the rows which relate to each sub-species.
# 
# One point to remember is that if you make a mistake and run the loop more than once, you may have to reset your subplots object (<code>fig</code> in this case) otherwise you'll just append even more traces to the object!

# In[13]:

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour},
                                 'name' : species},
                                col = i + 1, row = j + 1)


# Let's have a look at the plot:

# In[14]:

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (12) Making a scatterplot matrix\pyo.iplot-0.png") 
 #

# So I'm really happy with that. As a first attempt at making a scatterplot matrix it's turned out really well. Let's push it to the Plotly cloud as a record of what we achieved with eleven lines of code and we'll polish it up a bit in the next lesson!

# In[15]:

py.plot(fig, filename = "Iris dataset scatterplot matrix (1)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (12) Making a scatterplot matrix\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've come a long way! In the previous lesson we learnt how to attribute traces to different areas on the subplots grid. In this lesson we've taken that knowledge and used it to dynamically build a relatively complex scatterplot matrix of 4 variables, each with three categories!
# 
# We built the scatterplot matrix step-by-step by nesting one loop inside another, using the enumerate function to provide the numeric variables which keep track of where in the subplots grid that trace will be positioned.
# 
# Finally, we learnt how to use the <code>zip()</code> and <code>dict()</code> functions together to create a lookup dictionary from two lists.
# 
# In the nest lesson we'll polish the chart, adding subplot titles and changing the dimensions of the chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
