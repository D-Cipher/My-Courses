
# coding: utf-8

# # Pie charts (9) - Donut charts

# In this lesson we're going to learn how to make a special kind of pie chart called a donut chart.
# 
# A donut chart is like a pie chart, except the centre of the pie has been removed to leave a space, causing it to look like a donut.
# 
# There is a lot of controversy over whether or not we should use donut charts; many people believe they are even harder to understand than a pie chart because you can't see where the segments meet in the middle. Regardless, I believe that it's better to know how to create something and then have the option not to, rather than not knowing. 
# 
# I've also seen some donut charts which I though were particularly effective, especially from a design point of view.
# 
# Donut charts can be used when the information that we need to convey is very simple and the differences between the categories are stark. They can be used when seeing the general trend in the data is more important than knowing the exact figures.
# 
# Donut charts are most useful when you need to display contextual information about your data, and that contextual information must be inextricably linked to that bit of data - by using a donut chart, you can put the information in the hole. You don't need to link it to a single chart with a line, a figure reference or a footnote; the contextual info becomes part of the data.

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


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# We're going to use the same data as in the previous lesson. In this lesson we'll make a single donut chart and learn how to change the size of the hole. We'll also practise placing text effectively within the hole.

# In[10]:

outcomes = pd.read_csv("http://richard-muir.com/data/public/csv/StudentOutcomes201415BySubjectArea.csv", index_col = 0)
outcomes


# ## Making a pie chart
# We'll take the data for a single subject and make a pie chart:

# In[15]:

fig = {'data' : [{'type' : 'pie',
          'labels' : outcomes.columns.tolist(),
          'values' : outcomes.loc['Medicine & dentistry'],
          'name' : 'Medicine & dentistry',
          'direction' : 'clockwise'}],
       'layout' : {'title' : 'Outcomes for medicine and dentistry students'}}

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-0.png") 
 #

# ## Turning a pie chart into a donut chart
# 
# To make a donut chart, we simply set a value between 0 and 1 for the <code>'hole'</code> parameter. The default is 0. Let's try a large value:

# In[16]:

fig['data'][0].update({'hole' : 0.9})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-1.png") 
 #

# That's not particularly clear. Let's use a slightly smaller value:

# In[17]:

fig['data'][0].update({'hole' : 0.5})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-2.png") 
 #

# ## Providing contextual info with an annotation
# 
# As I mentioned in the introduction, donut charts are most useful when you need to link some contextual info to your data. Let's add some information about Medicine and Dentistry students in the form of an annotation and place it in the hole.
# 
# Adding an annotation in this way requires some trial and error; you will certainly need to play with the text size, the line breaks, the wording and the size of the donut hole in order for the information to fit and to look good.
# 
# Let's have a go!
# 
# We need to set the <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code> because there is no idea of x- and y-coordinates on a pie chart.
# 
# Let's start by positioning the annotation dead centre:

# In[18]:

info = "Medicine & Dentistry students are more likely to be employed than students from any other subject area"

fig['layout'].update({'annotations' : [{'text' : info,
                                       'xref' : 'paper',
                                       'yref' : 'paper',
                                       'x' : 0.5,
                                       'y' : 0.5,
                                       'showarrow' : False}]})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-3.png") 
 #

# Let's add some line breaks into the text, and make the font slightly bigger and bold.
# 
# It's worth saying that it took me a while to get the line breaks right here! When you're making your own chart, don't be put off if it takes a few minutes!

# In[39]:

info = "<b>Medicine &<br>Dentistry students<br>are more likely to<br>be employed than<br>students from any<br>other subject<br>area</b>"

fig['layout'].update({'annotations' : [{'text' : info,
                                       'xref' : 'paper',
                                       'yref' : 'paper',
                                       'x' : 0.5,
                                       'y' : 0.5,
                                       'showarrow' : False,
                                       'font' : {'size' : 16}}]})

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-4.png") 
 #

# Finally, let's increase the size of the hole to accomodate the text:

# In[40]:

fig['data'][0].update({'hole' : 0.55})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\pyo.iplot-5.png") 
 #

# I'm happy with this! Let's send it to the Plotly cloud:

# In[41]:

py.plot(fig, filename="Outcomes for Medicine & Dentistry students (donut chart)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(08) Pie Charts\Notebooks\images\Pie charts (9) - Donut charts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to make a donut chart. We've seen that they are only useful in very specific situations, and that they can be enhanced by including contextual information as an annotation within the hole.
# 
# I hope you've enjoyed this section. In the next we will learn how to create tables; a useful, but often overlooked component of data presentation and visualisation.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
