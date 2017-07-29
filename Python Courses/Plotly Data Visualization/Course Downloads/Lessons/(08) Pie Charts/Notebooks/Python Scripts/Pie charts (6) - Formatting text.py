
# coding: utf-8

# # Pie charts (6) - Formatting text

# In this lesson we're going to learn how to position and style the labels on a pie chart.
# 
# We'll learn how to control whether the labels sit inside or outside of the segments, as well as how to change the font style separately for labels inside and outside.

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


# ## Setting the <code>'textposition'</code>
# 
# The <code>'textposition'</code> parameter determines whether the labels are drawn inside or outside the segments. It can take one of four values:
# 
# - <code>'inside'</code> - all labels are inside the segments
# - <code>'outside'</code> - all labels are outside the segments
# - <code>'none'</code> - no labels are shown
# - <code>'auto'</code> - labels are positioned inside and outside the segment based on their length and the space available inside the segment (we saw this in action in the previous lesson)
# 
# Let's get the chart we made in the last lesson and practise moving the labels:
# 

# In[4]:

level = py.get_figure("rmuir", 269)
pyo.iplot(level)


py.image.save_as(level, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-0.png") 
 #

# Firstly let's set the <code>'textposition'</code> to <code>'none'</code> to remove the labels. You'll notice that it's probably a good idea to reinstate the legend. We're going to move on quickly, so there's not much point in doing this.

# In[5]:

level['data'][0].update({'textposition' : 'none'})
pyo.iplot(level)


py.image.save_as(level, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-1.png") 
 #

# Let's now change <code>'textposition'</code> to <code>'outside'</code>:

# In[6]:

level['data'][0].update({'textposition' : 'outside'})
pyo.iplot(level)


py.image.save_as(level, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-2.png") 
 #

# And finally to <code>'inside'</code> (which replicates the effect of setting it to auto for this chart):

# In[7]:

level['data'][0].update({'textposition' : 'inside'})
pyo.iplot(level)


py.image.save_as(level, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-3.png") 
 #

# ## Styling text inside and outside the segments
# 
# We'll now look at how to style the text differently depending on if it's inside or outside the segments. This is useful because the colours used in your pie chart may be dark, necessitating light text for the labels inside the segment, whilst still requiring the labels outside to be dark in colour.
# 
# Let's practise on the previous pie chart we made showing the ethnicity of UK students:

# In[16]:

eth = py.get_figure("rmuir", 267)
pyo.iplot(eth)


py.image.save_as(eth, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-4.png") 
 #

# We can set the text separately using <code>'outsidetextfont'</code> and <code>'insidetextfont'</code>. Both of these parameters contain a dictionary which allows us to set the font family, colour and size exactly as we have for other types of text.
# 
# Let's make the inside text darker and slightly larger, and the outside text much larger. This will make the chart easier to read, whilst also drawing more attention to the segment which we previously pulled out:

# In[19]:

eth['data'][0].update({'outsidetextfont' : {'size' : 16},
                      'insidetextfont' : {'color' : 'black',
                                         'size' : 13}})
pyo.iplot(eth)


py.image.save_as(eth, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\pyo.iplot-5.png") 
 #

# Let's send this styled chart to the Plotly cloud:

# In[20]:

py.plot(eth, filename="Ethnicity of UK students (text styled)", fileopt="overwrite")


py.image.save_as(eth, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (6) - Formatting text\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learn how to position the text inside or outside of the segments. We've also seen how to sty;e the text differently depending on where it is positioned relative to the pie chart.
# 
# In the next lesson we'll learn how to position pie charts on a sub plots object. They don't have an x- or y-axis so we have to use a slightly different approach than for other types of chart.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
