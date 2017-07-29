
# coding: utf-8

# # Chart presentation (8) - Changing hovertext (1)

# In the last lessons we learnt how to use Pandas' <code>df.apply()</code> in conjunction with a user-defined or a <code>lambda</code> function to create a column in our DataFrame to store the value for the hovertext.
# 
# In this lesson we'll apply what we've learnt to the  stacked quantity C02 emissions area plot, and in the next we'll update the stacked proportional C02 emissions area plot.
# 
# We will get the data and rewrite the code which creates the chart rather than reloading the charts as we need to manipulate the DataFrames from which they were created in order to make the hovertext field.

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


# ### Stacked quantity area plot
# 
# Let's get the emissions data again:

# In[3]:

emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()


# ### Writing a function
# 
# Seeing as we have to rewrite the code for this chart, let's try to do it as programmatically as we can. In lesson 13 of the Lineplot section we used a very long-winded way of making this chart, however in the subsequent lessons we found that we could reduce the amount of code by using the <code>df.cumsum()</code> method. We then further generalised the code by writing a function to create a stacked proportional area plot; we'll use the ideas from that function as a base to write one for a stacked quantity area plot.
# 
# If you'd like a challenge, go ahead and write a function which makes a stacked quantity area plot (you can base this code on the stacked proportional area), alternatively you can code along with me!
# 
# This function will have six arguments (the same five as for creating the stacked proportional area plot), plus one more which will define some of the text that goes in the hovertext field. As before, I'll write the explanation here and only include it in the finished function to save on space. We'll also test the function as we go.

# In[4]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked quantity area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text common to every hoverlabel
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """


# We need to reduce the input DataFrame down to only the columns which we need. You can also reuse this bit of code from the stacked proportional area function:

# In[5]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    return stackedAreaDF
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head()


# We don't need to create a 'Total' column because we're not calculating proportions, but we do need to calculate the cumulative sum of only the country columns:

# In[6]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
        
    return cumulative
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'],  'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head()


# In order to create the hovertext column, we need the original values for the emissions. I'm going to merge the two DataFrames by their index. Because they both have the same number of rows, this is not a problem - each row in one DataFrame will map correctly to its counterpart in the other.
# 
# I also need to create a suffix for the column names for each DataFrame - because both have the same names, we need to know how to refer to the correct column:
# 

# In[7]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulativeAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
        
    return cumulativeAndOrig
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'],  'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head()


# Now we can use the Pandas' <code>df.apply(lambda x : x)</code> construction that we learnt in the previous lesson to create a text column for each country. This will also use the <code>hover</code> variable that we pass to the function:

# In[8]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
    
    for col in cols:
        cumulAndOrig[col + '_t'] = "<b>" + str(col)[:-6] + "</b><br>" + str(hover) + cumulAndOrig[col + "_o"].apply(lambda x:
            "{:,}Kt".format(int(round(x, 0))))
        
    return cumulAndOrig
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head(1)


# Now we can create our traces inside the same loop which creates the text, then create our Data, Layout and Figure objects before plotting the chart! I'm also going to return the Figure object so we can send it to the Plotly cloud:

# In[9]:

def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    """
    A function which manipulates the data into the correct format to produce a stacked quantity area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
    traces = []
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
    
    for col in cols:
        cumulAndOrig[col + '_t'] = "<b>" + str(col)[:-6]  + "</b><br>" + str(hover) + cumulAndOrig[col + "_o"].apply(lambda x:
            "{:,}Kt".format(int(round(x, 0))))
        
        traces.append({'type' : 'scatter',
                      'x' : cumulAndOrig[time],
                      'y' : cumulAndOrig[col + "_c"],
                       'text' : cumulAndOrig[col + "_t"],
                       'hoverinfo' : 'text+x',
                      'name' : col[:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
        
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle,
                       'ticksuffix' : ' Kt'},
             'hovermode' : 'closest'}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)
    return fig


 #    return fig
    
    
C02Quant = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
py.image.save_as(C02Quant, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (8) - Changing hovertext (1)\pyo.iplot-0.png") 


# Let's push this chart to the Plotly cloud:

# In[10]:

py.plot(C02Quant, "C02 Emissions for UAE, USA, UK, India & China 1960 - 2011", fileopt = 'overwrite')


py.image.save_as(C02Quant, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(03) Chart Presentation 1\Notebooks\images\Chart presentation (8) - Changing hovertext (1)\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we updated some code that we'd previously written in order to set the hovertext and tickformat on the stacked quantity area plot which we previously made.
# 
# In the next lesson we'll apply this to the stacked proportional area plot.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
