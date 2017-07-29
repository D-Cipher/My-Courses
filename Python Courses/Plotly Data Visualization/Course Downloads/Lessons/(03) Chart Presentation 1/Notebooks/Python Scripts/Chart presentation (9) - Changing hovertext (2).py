
# coding: utf-8

# # Chart presentation (9) - Changing hovertext (2)

# In the last lesson we applied what we had previously learnt about hovertext to the stacked quantity area plot which we previously made. In this lesson we're going to do the same for the stacked proportional area plot.

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


# ### Stacked proportional area plot
# 
# Let's get the emissions data again:

# In[4]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# ## Changing the proportional area plot
# 
# Now we can take the concepts that we applied to the stacked quantity area and inject them into the function that we wrote for the stacked proportional area plot. I suggest just copying and pasting this function from your notes from the previous lesson rather than writing it out. 
# 
# I'm going to add another variable <code>hover</code> to the function - this allows us to define which text appears on each hover label.

# In[5]:

def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')

py.image.save_as(test, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (9) - Changing hovertext (2)\pyo.iplot-0.png") 

# First of all we need to merge the cumulative percentage DataFrame with the original. I'll paste this bit of code over in just after we create the cumulative DataFrame. We can also remove the part where we assign the <code>time</code> column to the cumulative sum DataFrame:
# 
# ````python
# stackedAreaData = stackedAreaDF[[time] + PCcols].merge(stackedPCAreaDF[PCcols], 
#                                         left_index = True,
#                                          right_index = True,
#                                         suffixes = ('_o','_c'))
# ````    
# 
# We also need to change the data source and column names that we pass to the trace to reflect the updated names from the merge function:
# ````python
# 'x' : stackedAreaData[time],
# 'y' : stackedAreaData[col + "_c"],
# ````
# 
# I'm not going to plot the chart, but I am going to return the <code>stackedAreaData</code> object to see that it has been made correctly:

# In[6]:

def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes six arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    
    
    ########################################################
    ################## NEW CODE GOES HERE ##################
    ########################################################
    stackedAreaData = stackedAreaDF[[time] + PCcols].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))
    
    for col in PCcols:
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                       ## CHANGE THE COLUMN REFERENCE ##
                      'y' : stackedAreaData[col + "_c"],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    #pyo.iplot(fig)


 #
    
    return stackedAreaData
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
test.head()


# The DataFrame looks as it should.
# 
# Now we can create the text column. We can reuse most of the code from the previous function, but we just need to change the format and column references.
# 
# We need to change the string slice which we take from the <code>col</code> variable within the loop to account for the fact that each col is prefixed with <code>pc_</code>:
# ````python
# stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" . . . 
# ````
# 
# The most important thing to do is to make sure that we are formatiing the raw value for x in the <code>lambda</code> function rather than the rounded, integer-ised version. We need to change the <code>lambda</code> to:
# ````python
# .apply(lambda x: "{:.0%}".format(x))
# ````

# In[7]:

def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    stackedAreaData = stackedAreaDF[PCcols + [time]].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))

    for col in PCcols:
        
        ########################################################
        ################## NEW CODE GOES HERE ##################
        ########################################################        
        stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" + str(hover) + stackedAreaData[col + "_o"].apply(lambda x:
            "{:.0%}".format(x))
        
        
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                      'y' : stackedAreaData[col + "_c"],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    #pyo.iplot(fig)


 #
    
    return stackedAreaData
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
test.head()


# Now let's add the hovertext to the trace and update the <code>'hovermode'</code> and <code>'hoverinfo'</code> options, update the <code>'tickformat'</code>, plot the chart and return the Figure object for later use:

# In[8]:

def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    stackedAreaData = stackedAreaDF[PCcols + [time]].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))

    for col in PCcols:       
        stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" + str(hover) + stackedAreaData[col + "_o"].apply(lambda x:
            "{:.0%}".format(x))
        
        
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                      'y' : stackedAreaData[col + "_c"],
                       'text' : stackedAreaData[col + "_t"],
                       'hoverinfo' : 'text+x',
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle,
                       'tickformat' : '%'},
              'hovermode' : 'closest'}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)


 #
    return fig
    
    
C02Prop = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')

py.image.save_as(C02Prop, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (9) - Changing hovertext (2)\pyo.iplot-1.png") 

# Let's send this to the Plotly cloud:

# In[9]:

py.plot(C02Prop, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = 'overwrite')


py.image.save_as(C02Prop, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (9) - Changing hovertext (2)\py.plot-0.png") 
 #

# ### What have we learnt this lesson?
# In this lesson we updated some code that we'd previously written in order to set the hovertext and tickformat on the stacked proprtional area plot which we had previously made.
# 
# From now on, we'll be incorporating these options into every chart that we make, but if you feel that you need more practise in order to understand the concepts that we've addressed, then I would recommend applying your knowledge about hovertext and tickformats to other charts that we've made.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
