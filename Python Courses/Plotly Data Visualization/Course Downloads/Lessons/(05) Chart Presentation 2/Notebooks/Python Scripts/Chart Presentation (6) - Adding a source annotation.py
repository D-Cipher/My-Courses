
# coding: utf-8

# # Chart Presentation (6) - Adding a source annotation

# In this lesson we'll put into practise what we've learnt so far about creating and positioning annotations and increasing the margins of our charts to add a source annotation to some charts that we've previously created. 
# 
# Citing and referencing your sources is a vital part of producing any data visualisation as it's important for people to be able to replicate your work.

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


# ## Getting the charts

# We're going to add source annotations to two charts that we've previously produced; the Gapminder plot, and the plot which shows Life Expectancy against cigarette prices.

# In[3]:

gapMinder = py.get_figure("rmuir", 225)
lifeExp = py.get_figure("rmuir", 223)


# ### Setting the source for the Gapminder plot
# 
# Let's add the source as an annotation to the Gapminder plot, remembering to set the <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code> to allow us to position this annotation outside of the plotting area.
# 
# I'm going to position this annotation at the bottom-right of the chart, in italics, and in a small, light grey font.

# In[4]:

gapMinder['layout'].update({'annotations' : [{'text' : "<i>Source: https://www.gapminder.org/data/</i>",
                                             'xref' : 'paper',
                                             'yref' : 'paper',
                                             'x' : 0,
                                             'y' : -0.4,
                                             'font' : {'size' : 12,
                                                      'color' : 'grey'},
                                              'xanchor' : 'left',
                                             'showarrow' : False}]})
pyo.iplot(gapMinder)


py.image.save_as(gapMinder, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (6) - Adding a source annotation\pyo.iplot-0.png") 
 #

# ## Changing the source for the Life Expectancy plot
# 
# I sourced the data for this plot from the WHO. Let's add this to the chart, keeping the same parameters for the annotation:

# In[5]:

lifeExp['layout'].update({'annotations' : [{'text' : "<i>Source: The World Health Organisation (WHO)</i>",
                                             'xref' : 'paper',
                                             'yref' : 'paper',
                                             'x' : 0,
                                             'y' : -0.4,
                                             'font' : {'size' : 12,
                                                      'color' : 'grey'},
                                              'xanchor' : 'left',
                                             'showarrow' : False}]})
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (6) - Adding a source annotation\pyo.iplot-1.png") 
 #

# Let's increase the height and bottom margin of the chart so we can see the source:

# In[6]:

lifeExp['layout'].update({'height' : 500,
                         'margin' : {'b' : 130}})
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (6) - Adding a source annotation\pyo.iplot-2.png") 
 #

# Great, these two plots are looking much better. Let's send them to the PLotly cloud:

# In[7]:

py.plot(gapMinder, filename="Life expectancy and GPD per capita", fileopt="overwrite")


py.image.save_as(gapMinder, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (6) - Adding a source annotation\py.plot-0.png") 
 #
py.plot(lifeExp, filename="Life expectancy against cost of cigarettes (Male & Female regressions)", fileopt="overwrite")


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (6) - Adding a source annotation\py.plot-1.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've practise adding, positioning and styling annotations. We've also practise modifying the chart margins and size to allow the annotations to be seen.
# 
# From now on we'll use this knowledge in almost every lesson to add a source to every chart that we create.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
