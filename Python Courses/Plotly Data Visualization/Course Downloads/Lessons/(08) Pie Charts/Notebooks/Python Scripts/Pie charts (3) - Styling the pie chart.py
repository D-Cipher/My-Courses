
# coding: utf-8

# # Pie charts (3) - Styling the pie chart

# In this lesson we're going to find out how to change the colour and outlines of the segments in our pie chart. This is useful becuase it allows us to style our pie charts to be in keeping with the rest of the charts we make.

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


# ## Getting the chart
# 
# We'll load the chart that we made last lesson:

# In[3]:

ethPie = py.get_figure("rmuir", 263)
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (3) - Styling the pie chart\pyo.iplot-0.png") 
 #

# We can change the colour of the individual segments by passing a list of colours into the trace:

# In[5]:

ethPie['data'][0].update({'marker' : {'colors' : ["rgb(12,192,170)", 
                                                  "rgb(190,252,250)", 
                                                  "rgb(77,194,84)", 
                                                  "rgb(211,238,128)", 
                                                  "rgb(97,167,193)"]}})

pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (3) - Styling the pie chart\pyo.iplot-1.png") 
 #

# We can also change the width and colour of the line that surrounds each segment:

# In[7]:

ethPie['data'][0]['marker'].update({'line' : {'color' : '#333',
                                             'width' : '1'}})
pyo.iplot(ethPie)


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (3) - Styling the pie chart\pyo.iplot-2.png") 
 #

# Changing these parameters is a very easy way of making some big changes to the presentation of the chart. Let's send this to the Plotly cloud:

# In[8]:

py.plot(ethPie, filename="Ethnicity of UK students (styled)", fileopt = "overwrite")


py.image.save_as(ethPie, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (3) - Styling the pie chart\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to change the colour of the individual segments of the pie chart. We've also seen how to set the width and colour of the line that surrounds each segment. 
# 
# In the next lesson we'll find out how to highlight a specific segment by pulling it away from the rest of the chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
