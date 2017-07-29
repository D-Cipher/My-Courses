
# coding: utf-8

# # Chart Presentation (2) - Styling annotations, text, ticklabels & titles

# In this lesson we're going to learn more about how to apply styling options to text displayed in Plotly. In the previous lesson we learnt how to use the global font to affect every piece of text on our chart, however in this lesson we'll learn how to set the style for each individually.

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


# ## Styling text

# We use the same set of options to style titles, text, ticklabels, annotations and legend text individually as we do to set the global font, however the font style option is contained in different areas of our set of chart instructions:
# ````python
# {'font/tickfont/titlefont/textfont' : {'color' : <HTML colour representation>,
#             'family' : <HTML font family (only some available)>,
#             'size' : <integer >= 1>}}
# ````
# Let's find out how to set the style individually for each text item. I'll leave you to develop your own style; for now we'll only change the colour of the text as a proof of concept.

# ### Making the chart
# 
# Here's our dummy chart from the last lesson:

# In[3]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
         'xaxis' : {'title' : 'Who likes fruit?'},
         'yaxis' : {'title' : 'Who likes cheese?'},
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-0.png") 
 #

# ## Changing the font of text contained in the trace
# 
# We can change the style of the font for each trace individually by using the <code>'textfont'</code> option within each trace:

# In[4]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
           #new code goes here
           'textfont' : {'color' : 'green'},
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
          #new code goes here
           'textfont' : {'color' : 'yellow'},
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
         'xaxis' : {'title' : 'Who likes fruit?'},
         'yaxis' : {'title' : 'Who likes cheese?'},
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-1.png") 
 #

# ## Changing the title font
# 
# We can set a different <code>'titlefont'</code> for each of the axis titles, as well as for the chart title:

# In[5]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
           'textfont' : {'color' : 'green'},
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
           'textfont' : {'color' : 'yellow'},
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
          #new code goes here
          'titlefont' : {'color' : 'purple'},
         'xaxis' : {'title' : 'Who likes fruit?',
                   #new code goes here
                  'titlefont' : {'color' : 'red'},
                   },
         'yaxis' : {'title' : 'Who likes cheese?',
                    #new code goes here
                  'titlefont' : {'color' : 'blue'},
                   },
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-2.png") 
 #

# ## Changing the ticklabel font
# 
# We can change the font for the ticklabels on each axis by using the <code>'tickfont'</code> option within each axis object:

# In[6]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
           'textfont' : {'color' : 'green'},
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
           'textfont' : {'color' : 'yellow'},
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
          'titlefont' : {'color' : 'purple'},
         'xaxis' : {'title' : 'Who likes fruit?',
                  'titlefont' : {'color' : 'red',},
                   #new code goes here
                   'tickfont' : {'color' : 'goldenrod'},
                   },
         'yaxis' : {'title' : 'Who likes cheese?',
                  'titlefont' : {'color' : 'blue'},
                    #new code goes here
                   'tickfont' : {'color' : 'orange'},
                   },
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-3.png") 
 #

# ## Changing the annotation font
# 
# Much like the traces, the font for each annotation can be set individually:

# In[7]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
           'textfont' : {'color' : 'green'},
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
           'textfont' : {'color' : 'yellow'},
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
          'titlefont' : {'color' : 'purple'},
         'xaxis' : {'title' : 'Who likes fruit?',
                  'titlefont' : {'color' : 'red',},
                   'tickfont' : {'color' : 'goldenrod'},
                   },
         'yaxis' : {'title' : 'Who likes cheese?',
                  'titlefont' : {'color' : 'blue'},
                   'tickfont' : {'color' : 'orange'},
                   },
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                           #new code goes here
                           'font' : {'color' : 'magenta'},
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-4.png") 
 #

# ## Legend font
# 
# Finally, we can change the font for the legend items with the <code>'font'</code> option:

# In[8]:

traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
           'textfont' : {'color' : 'green'},
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
           'textfont' : {'color' : 'yellow'},
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
          'titlefont' : {'color' : 'purple'},
         'xaxis' : {'title' : 'Who likes fruit?',
                  'titlefont' : {'color' : 'red',},
                   'tickfont' : {'color' : 'goldenrod'},
                   },
         'yaxis' : {'title' : 'Who likes cheese?',
                  'titlefont' : {'color' : 'blue'},
                   'tickfont' : {'color' : 'orange'},
                   },
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                           'font' : {'color' : 'magenta'},
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}],
         #new code goes here
         'legend' : {'font' : {'color' : 'brown'}}}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(05) Chart Presentation 2\Notebooks\images\Chart Presentation (2) - Styling annotations, text, ticklabels & titles\pyo.iplot-5.png") 
 #

# So in each of these examples we have only changed the colour of the font; remember that you can also control the size and font family of the text as well. Obviously we would never publish a chart such as this; it has instead been used to demonstrate the finer control over the different text items in our chart.

# ### What have we learnt this lesson?

# In this lesson we've learnt how to set the font style individually for each possible text items on the chart.
# 
# We've seen that the font dictionary we create goes under a different key, depending on if we intend it to change the titlefont, ticklables or text, but that the dictionary we pass is of the same structure as that for the global font.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
