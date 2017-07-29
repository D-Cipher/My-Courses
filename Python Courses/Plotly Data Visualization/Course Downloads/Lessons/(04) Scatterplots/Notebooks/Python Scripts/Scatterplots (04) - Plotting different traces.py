
# coding: utf-8

# # Scatterplots (04) - Plotting different traces

# In this lesson we're going to plot the famous <a href="https://en.wikipedia.org/wiki/Iris_flower_data_set">Iris flower dataset</a> which is often used as a test case for machine learning models. This dataset contains 50 samples from each of 3 species of the Iris flower (<i>setosa, virginica</i> and <i>versicolor</i>), and each flower had four measurements taken from it; the length and the width of the <a href="https://en.wikipedia.org/wiki/Sepal">sepals</a> and the <a href="https://en.wikipedia.org/wiki/Petal">petals</a>.
# 
# We're going to create a scatterplot from this dataset, and in doing so apply the marker styling options that we learnt in the previous lesson. 
# 
# We're also going to find out how to use Pandas to get a dataset straight from table in a webpage - this is a really useful tool which will allow you access many different data sources. 
# 
# Finally, we'll learn how to use the Python functions <code>dict()</code> and <code>zip()</code> to create a lookup dictionary which we'll use to style the marker symbols and colours for each species.

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
# 
# We're going to use the Pandas <code>read_html()</code> function to get the Iris dataset from Wikipedia. This function takes a url as an argument, and returns a list of objects from the webpage which could contain data. This particular functionality relies on a few different Python libraries (lxml, html5lilb and BeautifulSoup4), all of which are included in the Anaconda distribution which we downloaded. However if you're having trouble using this function for whatever reason, you can download the .csv from my website by passing this url: http://www.richard-muir.com/data/public/csv/irisDataset.csv to the <code>pd.read_csv()</code> function.
# 
# We're going to set <code>header = 0</code> to make sure that the table headings are set as the column titles:

# In[21]:

url = "https://en.wikipedia.org/wiki/Iris_flower_data_set"
returnObject = pd.read_html(url, header=0)


# <code>pd.read_html()</code> returns a list. Let's have a look at the first item in that list:

# In[22]:

returnObject[0]  #it works!


# I'll now create a new object called <code>iris</code> and set it to the output of <code>pd.read_html()</code>:

# In[23]:

iris = returnObject[0]


# ### Preparing the data for plotting 
# Because we have the three different data traces contained within the same DataFrame, we need to find a way of splitting them so we can plot them separately in Plotly. 
# 
# I'm going to use <code>pd.Series.unique()</code> to get the unique items in the Species column:

# In[24]:

irisSpeciesUnique = list(iris['Species'].unique())
irisSpeciesUnique


# Those strange characters ("\xa0") have snuck in as a consequence of reading the HTML and converting the output to a string. We don't have to worry about them affecting the way the chart is displayed because Plotly also displays HTML.

# ### Plotting the data
# We can now use the <code>irisSpecies</code> list to select each species in turn from the DataFrame by using <code>df.loc[]</code>. We're going to create the traces directly from this loop, only plotting the Sepal length and Sepal width for each species.
# 
# The x-values are set using this code which tells pandas to select only the rows where the Species column is equal to the current value of sp in the loop, and then to take only the 'Sepal length' column:
# ````python
# iris.loc[iris['Species'] == species,'Sepal length']
# ````
# 
# The y-values are set in the same way, but we only want the 'Sepal width' column:

# In[29]:

traces = []
for sp in irisSpeciesUnique:
    traces.append({'type' : 'scatter',
                  'mode' : 'markers',
                  'x' : iris.loc[iris['Species'] == sp,'Sepal length'],
                  'y' : iris.loc[iris['Species'] == sp,'Sepal width'],
                  'name' : sp})


# Now I'll create the layout and Figure object and plot the data. 
# 
# I want to set the range for each axis so that the chart doesn't resize when we show and hide the different traces:

# In[30]:

layout = {'title' : "Sepal length and width for Iris setosa, versicolor and virginica",
         'xaxis' : {'title' : 'Sepal length (cm)',
                   'range' : [iris['Sepal length'].min() * 0.95, iris['Sepal length'].max() * 1.05]},
         'yaxis' : {'title' : 'Sepal width (cm)',
                   'range' : [iris['Sepal width'].min() * 0.95, iris['Sepal width'].max() * 1.05]}}

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (04) - Plotting different traces\pyo.iplot-0.png") 
 #

# So that plot has come out looking OK. It's great that Plotly's default colour system looks so good! 
# 
# It's now time to apply our own styling to the traces. First we need to create a lookup dictionary which contains the marker symbol information which we want to attach to each trace.
# 
# We'll first create a list of dictionaries which contain the marker symbols and colours:

# In[34]:

symbolsAndColours = [{'color' : "#663399", 'symbol' : 'circle'},
                    {'color' : '#FF6347', 'symbol' : 'square'}, 
                    {'color' : '#2E8B57', 'symbol' : 'diamond'}]


# We'll now take our list of species and <code>zip()</code> the two lists together, then turn the resulting output into a dictionary. You can see how <code>zip()</code> combines the two lists into one object:

# In[37]:

markerSymbolInfo = dict(zip(irisSpeciesUnique, symbolsAndColours))
markerSymbolInfo


# We can now copy our previous loop and add in the marker styling options. It is only the colour and symbol which will change for each species.
# 
# For each trace I will set the marker size to 8, the opacity to 0.7 and the marker line to width = 1.25 and color = black.

# In[39]:

traces = []
for sp in irisSpeciesUnique:
    traces.append({'type' : 'scatter',
                  'mode' : 'markers',
                  'x' : iris.loc[iris['Species'] == sp,'Sepal length'],
                  'y' : iris.loc[iris['Species'] == sp,'Sepal width'],
                  'name' : sp,
                  
                  'marker' : {'color' : markerSymbolInfo[sp]['color'],
                             'symbol' : markerSymbolInfo[sp]['symbol'],
                             'size' : 8,
                             'opacity' : 0.7,
                             'line' : {'width' : 1.25,
                                      'color' : 'black'}}})


# Let's refresh the Figure object and replot the chart:

# In[40]:

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (04) - Plotting different traces\pyo.iplot-1.png") 
 #

# In my opinion this is a great improvement on the chart. By changing the marker opacity we have made clear that there is some overplotting within the species groups (look at the darker purple dots), and by changing the marker symbol we have made clear that there is overplotting between the species groups.
# 
# Let's send this chart to the Plotly cloud:

# In[13]:

py.plot(fig, filename="Iris dataset", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (04) - Plotting different traces\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to get tabular data from a webpage by using the <code>pd.read_html()</code> function, and we've seen how we might have to manipulate the data that is returned.
# 
# We've learnt how to restrict the data items in a DataFrame to only those rows and columns which satisfy certain criteria, and how to implement this knowledge when creating a chart with many traces from the same DataFrame.
# 
# We've also seen how to create a lookup dictionary to allow us to style the marker colour and symbol for each trace. This is a very useful concept which we'll use again in the course. We'll also revisit the Iris dataset.
# 
# In the next lesson we'll again find out how to plot multiple scatter traces on the same plot, but we'll also learn how to control which traces are hidden and shown by setting the <code>legendgroup</code> option.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
