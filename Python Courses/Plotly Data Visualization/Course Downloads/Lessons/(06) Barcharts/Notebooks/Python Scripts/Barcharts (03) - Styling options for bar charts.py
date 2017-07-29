
# coding: utf-8

# # Barcharts (3) - Styling options for bar charts

# In the last lesson we created our very first bar chart. In this lesson we're going to learn about some of the different styling options available to us.

# ## Module Imports

# In[10]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[11]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the chart
# 
# We'll create the chart from scratch rather than load it from the Plotly cloud; it's a good idea to practise new concepts as much as possible!

# In[12]:

meteorite = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsPerYear.csv", index_col = 0)
meteorite.head()


# In[13]:

numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count']}

layout = {'title' : "Number of meteorites found per year",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Number of meteorites'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (03) - Styling options for bar charts\pyo.iplot-0.png") 
 #

# ## Changing the colour of the bars
# 
# We can change the colour of the bars in a bar chart in the same way as we change the colour of a scatterplot or lineplot.
# 
# Within the trace object, we access the <code>'color'</code> property within <code>'marker'</code> sub-dictionary, setting this colour as normal (CSS colour, HEX codes etc.):

# In[14]:

fig['data'][0].update({'marker' : {'color' : 'lightblue'}})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (03) - Styling options for bar charts\pyo.iplot-1.png") 
 #

# ## Styling the bars
# We can also change different styling options for the bars. I'm going to add a grey outline to each bar:

# In[15]:

fig['data'][0]['marker'].update({'line' : {'color' : '#333',
                                          'width' : 2}})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (03) - Styling options for bar charts\pyo.iplot-2.png") 
 #

# Finally, we can also change the opacity of the bars:

# In[24]:

fig['data'][0].update({'opacity' : 0.5})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (03) - Styling options for bar charts\pyo.iplot-3.png") 
 #

# Let's send this updated and stylish barchart to the Plotly cloud:

# In[23]:

py.plot(fig, filename="Number of meteorites found each year", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (03) - Styling options for bar charts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to apply some different styling options to our barchart. We've seen how to set the colour and opacity, as well as how to add an outline to the bar itself.
# 
# In the next lesson we'll look at how to set the colour for individual bars.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
