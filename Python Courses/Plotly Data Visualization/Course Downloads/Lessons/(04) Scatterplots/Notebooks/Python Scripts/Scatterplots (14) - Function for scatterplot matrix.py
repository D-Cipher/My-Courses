
# coding: utf-8

# # Scatterplots (14) - Function for scatterplot matrix

# In this lesson we'll take what we learnt in the previous lessons about making scatterplot matrices, and use this to write a function which we can use to create a scatterplot matrix from any DataFrame.
# 
# This will be quite a hard lesson, so if you do have problems then please ask in the comments.

# ## Module Imports

# In[2]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# We'll import the Plotly tools libaray again:

# In[1]:

from plotly import tools


# This bit of magic here allows us to view the charts inside an iPython Notebook. When coupled with <code>plotly.offline</code>, this allows us to have a very quick iterative process as we develop and tweak the charts.

# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Making the function
# 
# The last time we made a function to generalise the creation of a chart, we passed several variables to that function. We'll do the same for this function, and the variable we'll pass will serve as instructions for how to make the chart. We'll need the following variables in this function.
# 
# - df - The DataFrame which contains the data
# - scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
# - categoricalColumn - the column which contains the categories of data which should be plotted
# - colours - a list of colours equal in length to the number of categories in the categoricalColumn
# - title - the title of the chart
# 
# Once again, we'll test this function at every step and we'll use the iris dataset to make sure that the function outputs what we expect.

# In[6]:

iris = pd.read_csv("http://www.richard-muir.com/data/public/csv/irisDataset.csv", index_col = 0)
iris.head()


# Let's start by passing the variables that we need into the function and thinking about how we'll use the variables to create the scatterplot matrix. We'll also write the docstring for our function.

# In[11]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    """
    This function create a scatterplot matrix and expects the following inputs:
    - df - The DataFrame which contains the data
    - scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
    - categoricalColumn - the column which contains the categories of data which should be plotted
    - colours - a list of colours equal in length to the number of categories in the categoricalColumn
    - title - the title of the chart
    
    This function does not create a scatterplot where the same variable intersects with itself.
    """
    
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')


# We'll need to create the list of categories within the categoricalColumn, and map this to the list of colours to create the colour lookup. 
# 
# We can also get number of rows and columns in the subplots object from the length of the list of scatterColumns, using this information to create the subplots object:

# In[14]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    categories = list(df[categoricalColumn].unique())
    print(categories)
    colourLookup = dict(zip(categories, colours))
    print(colourLookup)
    
    print(len(scatterColumns))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')


# Now we can transpose the code which we wrote in the previous lessons into this function. First of all, we'll make the basic traces, then we can add in later some of the styling options which we learnt in the last lesson:

# In[19]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    for i, column in enumerate(scatterColumns):
        for j, row in enumerate(scatterColumns):
            if column != row:
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category},
                                    col = i + 1,
                                    row = j + 1)
    pyo.iplot(fig)
    return fig


 #    
test = scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
py.image.save_as(test, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-0.png") 


# ## Styling the chart
# 
# Let's now apply the styling options we learnt about in the previous lesson, but in a more generalised way within the function.
# 
# We'll first set the <code>'legendgroup'</code> and <code>'showlegend'</code> options to ensure that only 1 trace of each category is shown on the legend, and that that legend item controls all of the traces within that category:

# In[20]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    for i, column in enumerate(scatterColumns):
        for j, row in enumerate(scatterColumns):
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
    pyo.iplot(fig)
    return fig


 #    
test = scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
py.image.save_as(test, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-1.png") 


# Now let's set the chart title and the axis titles, remembering that only the left-most and bottom-most axes need titles. we can also use this opportunity to set the range for the axes.
# 
# For the range, we need to take the minimum and maximum values of the columns which we're plotting on the scatterplot matrix. It's best to do this outside of the loop in order to make our code more efficient. 
# 
# We're going to take a slightly different approach to calculating the range of the axes to ensure that this function is as generalisable as possible. To get the minimum for the range, we'll subract 10% of the range (the difference between the minimum and maximum value) from the minimum value of the df, likewise for the maximum value:

# In[24]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    diff = max(df[scatterColumns].max()) - min(df[scatterColumns].min())
    
    minimum = min(df[scatterColumns].min()) - (diff * 0.1)
    maximum = max(df[scatterColumns].max()) + (diff * 0.1)
    
    for i, column in enumerate(scatterColumns):
        fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column,
                                                      'range' : [minimum,maximum]})
        
        for j, row in enumerate(scatterColumns):
            fig['layout']['yaxis{}'.format(i + 1)].update({'title' : row,
                                                      'range' : [minimum,maximum]})
            
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
                    
    fig['layout'].update({'title' : title})
    pyo.iplot(fig)
    return fig


 #    
test = scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
py.image.save_as(test, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-2.png") 


# Finally, because we know the scatterplot matrix is going to be a square, we can set the width and height of the chart based on the number of items which we're comparing (ie <code>len(scatterColumns)</code>) multiplied by a sensible number:

# In[28]:

def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    """
    This function create a scatterplot matrix and expects the following inputs:
    - df - The DataFrame which contains the data
    - scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
    - categoricalColumn - the column which contains the categories of data which should be plotted
    - colours - a list of colours equal in length to the number of categories in the categoricalColumn
    - title - the title of the chart
    
    This function does not create a scatterplot where the same variable intersects with itself.
    """
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    diff = max(df[scatterColumns].max()) - min(df[scatterColumns].min())
    
    minimum = min(df[scatterColumns].min()) - (diff * 0.1)
    maximum = max(df[scatterColumns].max()) + (diff * 0.1)
    
    for i, column in enumerate(scatterColumns):
        fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column,
                                                      'range' : [minimum,maximum]})
        
        for j, row in enumerate(scatterColumns):
            fig['layout']['yaxis{}'.format(i + 1)].update({'title' : row,
                                                      'range' : [minimum,maximum]})
            
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
                    
    fig['layout'].update({'title' : title,
                         'height' : len(scatterColumns * 200),
                         'width' : len(scatterColumns * 200)})
    pyo.iplot(fig)
    return fig


 #    return fig
    
irisScatter = scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
py.image.save_as(irisScatter, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-3.png") 


# Let's test this function with fewer columns:

# In[29]:

irisScatter = scatterplotMatrix(iris, 
                  ['Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
py.image.save_as(irisScatter, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-4.png") 


# If we want a scatterplot with no categorical variable we have to trick the function slightly; let's create a new column in the DataFrame which only has one value:

# In[30]:

iris['noCat'] = 'Iris'


# We can now pass this column as the categorical column:

# In[31]:

irisScatter = scatterplotMatrix(iris, 
                  ['Petal length','Petal width'], 
                  'noCat', 
                  ['purple'],
                 'Scatterplot matrix of Iris dataset')

py.image.save_as(irisScatter, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (14) - Function for scatterplot matrix\pyo.iplot-5.png") 

# ### What have we learnt this lesson?

# In this lesson we've taken the code that we've written in previous lessons and generalised it so that it can be contained within a function which will produce a scatterplot matrix regardless of which variables we pass to it (within reason!).
# 
# I hope you've enjoyed this lesson and found it challenging.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
