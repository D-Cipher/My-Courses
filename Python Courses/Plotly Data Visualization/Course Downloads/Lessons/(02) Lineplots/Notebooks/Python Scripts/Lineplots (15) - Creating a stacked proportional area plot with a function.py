
# coding: utf-8

# # Lineplots (15) - Creating a stacked proportional area plot with a function
# 
# In the last lesson we saw how to prepare the data to allow us to easily make a stacked proportional area plot. 
# 
# In this lesson we're going to wrap the code we wrote in a function which will allow us to choose which countries are displayed in what order on the chart.
# 
# This will be the most difficult piece of code we'll have written so far - it's meant to be challenging. If you don't understand or get stuck along the way, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>.

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


# We'll also import the <code>random</code> library which we'll use at the end of this lesson to help us test our function.

# In[2]:

import random


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# I'll get the data in the same way as the previous lesson:

# In[4]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# ### Writing the function
# 
# The function we're going to write will not only plot the chart, but will also do all of the data manipulation and calculation. The function will take 5 arguments:
# - a DataFrame
# - the column name of the time element in the data as a string
# - a list of columns which contain the variables we want to include in the chart (the columns must be present in the DataFrame)
# - The title of the chart
# - The y-axis title (the x-axis title will be the time element of the DataFrame)
# 
# At each stage of making this function we're going to return an object that will allow us to check if the code we've written works as expected.
# 
# Before we begin writing the function, it's important to write a docstring, especially for a large function such as this. Writing a docstring means that when you come back to use the function, you don't have to figure out what each variable does and what type of variable you need to pass to the function. I'll write this now, and then include it in the finished version to save on space.

# In[5]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame as a string
    cols - the name of the columns in the DataFrame which you want to include in the area plot as list
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """


# The first step in the function is to create a DataFrame which contains only the columns that we want to keep. 
# 
# In this section, I'm going to include Andorra to make sure that the <code>fillna()</code> function has worked. In the rest of the lesson I'm going to test the function as we go by using the same countries as in the previous lesson. This will assure me that the function is right! 

# In[6]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    return stackedAreaDF
   
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND', 'Andorra | AND'],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()


# The next step is to create the <code>'Total'</code> column:

# In[7]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    return stackedAreaDF
    
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()


# Now we'll calculate the percentage for each country using the <code>'Total'</code> column. I also want to create a list of all the column names which hold percentages. I'll use that hlist to help me calculate the cumulative sum.

# In[8]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):
    PCcols = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)

    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
    
    return stackedAreaDF
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()


# We'll now create a new DataFrame which will be the cumulative sum of the percentages for the countries of interest. We'll also need to concatenate the time element variable:

# In[9]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):
    PCcols = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    
    
    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]
    
    
    return stackedPCAreaDF
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()


# Now we'll create the traces in the same way as we did in the previous lesson:

# In[10]:

def createStackedPropArea(df, time, cols, title, yaxisTitle):  
    
    PCcols = []
    traces = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    stackedAreaDF.fillna(0, inplace=True)

    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]

    for col in PCcols:
        traces.append({'type' : 'scatter',
                     'x' : stackedPCAreaDF[time],
                     'y' : stackedPCAreaDF[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    return traces
  
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test


# Finally, we'll create the Data, Layout and Figure objects and plot the chart. We're not going to return anything this time, as we'll be able to see the plot and diagnose any problems:

# In[11]:

def createStackedPropArea(df, time, cols, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
    PCcols = []
    traces = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]

    for col in PCcols:
        traces.append({'type' : 'scatter',
                      'x' : stackedPCAreaDF[time],
                      'y' : stackedPCAreaDF[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)
    return fig

 #    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')

py.image.save_as(test, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (15) - Creating a stacked proportional area plot with a function\pyo.iplot-0.png") 


# OK, so that looks like it worked! Let's try passing the countries in a different order:

# In[12]:

test2 = createStackedPropArea(emissions, 'Year', ['China | CHN', 
                                          'United States | USA', 
                                          'India | IND',
                                          'United Arab Emirates | ARE',
                                          'United Kingdom | GBR', 
                                          ],
                      "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')

py.image.save_as(test2, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (15) - Creating a stacked proportional area plot with a function\pyo.iplot-1.png") 

# Finally, we'll try passing a totally new list of countries. I'll pick these at random using the <code>random.choice()</code> function from the <code>random</code> library, but feel free to have a look at the list of countries and choose some interesting comparisons!

# In[13]:

countries = []
for i in range(10):
    countries.append(random.choice(emissions.columns.tolist()))
countries


# In[14]:

test3 = createStackedPropArea(emissions, 'Year', countries,  "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
py.image.save_as(test3, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (15) - Creating a stacked proportional area plot with a function\pyo.iplot-2.png") 

# ### Creating a stacked proportional area plot with a function - What have we learnt?
# 
# In this lesson we've learnt how to take code that we've previously written and wrap it in a function, making it more generalisable and reusable. We've written a function that we can use to create a stacked proportional area plot from any suitable input DataFrame, learning how to build a function step by step, checking the output each time.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
