
# coding: utf-8

# # Scatterplots (08) - Adding text to charts

# There are two ways of adding text to a Plotly chart. We have already seen how to add text annotations to a chart in the previous lesson, and in the previous section we saw how to add hovertext. In this lesson we'll look at how to repurpose the <code>'text'</code> option in the trace to add text notes to certain points on the chart.
# 
# Adding these notes are a really helpful way of explaining outliers to your readers, especially if you expect that your charts will mainly be viewed in a static medium such as print. In these circumstances creating the hoverlabels will not be sufficient to explain the data.

# ## Module Imports

# In[75]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[76]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# We're going to continue the theme of looking at life expectancy data, but instead of looking at the price of cigarettes, we'll instead plot the relationship between life expectancy at birth and the average healthcare spending per capita in dollars.
# 
# You can get the data from my website:

# In[77]:

healthcare = pd.read_csv("http://www.richard-muir.com/data/public/csv/lifeExpectancy-HealthcareSpending.csv", index_col = 0)
healthcare.head()


# ### Creating the text columns
# We're going to create one column for the hovertext which will show a similar thing for every data point. We're also going to create a column for the text to display on the chart. We don't want to display this text for every data point because the chart would soon look messy, instead let's have a quick look at the data and see which are the outlying points - we can then decide how to assign the text to these data points.
# 
# Here's a very quick chart:

# In[78]:

pyo.iplot([{'type' : 'scatter',
          'mode' : 'markers',
          'x' : healthcare['Spending per capita($)'],
          'y' : healthcare['Life expectancy'],
          'text' : healthcare['Country'],}])


# So looking at this plot, the USA (far right point), and South Africa (bottom-most point) are both clear outliers here and we'll create text fields for those countries. I think it's also a good idea to create a note for India and Indonesia (next 2 bottom-most points), and for Switzerland and Norway (next 2 right-most points).
# 
# It seems that we can select these six countries for a text note by only adding a note if the life expectancy is below 70 years, or if the spending is about \$6000.
# 
# Let's create the hovertext field:

# In[79]:

healthcare['hovertext'] = healthcare.apply(lambda x: 
        "<b>{}</b><br>Life expectancy: {:.0f} years<br>Healthcare spend per capita: ${:,}".format(x['Country'],
                                                                                                x['Life expectancy'],
                                                                                                x['Spending per capita($)']),
                                          axis = 1)

healthcare.head()


# And check it:

# In[80]:

healthcare.loc[0,'hovertext']


# And now we can create the text note field. I'm going to do this by applying a function, rather than using a lambda function inside the <code>apply()</code> method because it's easier to add the log inside a defined function.
# 
# Because of the way the text is positioned on the plot we need to pad the country names with a couple of spaces at the beginning of the string:

# In[81]:

def addTextNote(row):
    if row['Life expectancy'] > 70 and row['Spending per capita($)'] < 6000:
        return ''
    else:
        return "  " + row['Country']


# In[82]:

healthcare['textnote'] = healthcare.apply(addTextNote, axis = 1)
healthcare.head()


# ## Plotting the data
# Now we can create our chart, however we have to create the traces in a slightly different way.
# 
# In order to show the text notes at the data points we must specify <code>'text'</code> in the <code>'mode'</code> option:
# ````python
# trace = {'mode' : 'text+lines+markers'} # for example
# # or:
# trace = {'mode' : 'text'}
# ````
# 
# We therefore need to create two traces; the first will contain the data points and the hoverinfo, whilst the second will only show the text notes. Each trace will therefore have a different column attached to the <code>'text'</code> attribute. We have to create the chart in this way because we can only have one text attribute per trace.
# 
# Let's create the first trace and the layout and then plot the chart. I'll set it to be a nice dark red colour to highlight the importance of health outcomes.
# 
# We'll set <code>'showlegend'</code> to False for this trace because we'll be adding another trace to show the text values, and we don't need to clutter the chart with a legend.

# In[83]:

healthcareTrace = {'type' : 'scatter',
                  'mode' : 'markers',
                  'text' : healthcare['hovertext'],
                  'x' : healthcare['Spending per capita($)'],
                  'y' : healthcare['Life expectancy'],
                  'hoverinfo' : 'text',
                  'showlegend' : False,
                  'marker' : {'color' : '#B22222'}}
data = Data([healthcareTrace])

layout = {'title' : 'Healthcare spending and life expectancy',
          'hovermode' : 'closest',
         'xaxis' : {'title' : 'Healthcare spending per capita',
                   'tickformat' : '$,',
                   'range' : [0, healthcare['Spending per capita($)'].max()*1.05]},
         'yaxis' : {'title' : 'Life expectancy (years)',
                   'range' : [healthcare['Life expectancy'].min()*0.95,
                             healthcare['Life expectancy'].max()*1.05]}}
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (08) - Adding text to charts\pyo.iplot-0.png") 
 #

# Now let's add the second trace which will only contain the text notes for the countries we decided upon earlier.
# 
# We're going to set <code>'mode'</code> to <code>'text'</code> because we don't want to see any data points. We're also going to set <code>'hoverinfo'</code> to <code>'none'</code> to suppress the hover behaviour for this trace, and set <code>'showlegend'</code> to <code>False</code>.
# 
# We also need to add this trace to the beginning of the list, otherwise Plotly will detect the hover over these points, and not the original trace we created:

# In[84]:

fig['data'] = [{'type' : 'scatter',
                  'mode' : 'text',
                  'text' : healthcare['textnote'],
                  'x' : healthcare['Spending per capita($)'],
                  'y' : healthcare['Life expectancy'],
                  'hoverinfo' : 'none',
                   'showlegend' : False}] + fig['data']
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (08) - Adding text to charts\pyo.iplot-1.png") 
 #

# So this looks OK, we just have to make a couple of tweaks to the chart: 
# 
# As you can see, the labels are centred over the data point. We can change the <code>'textposition'</code> option to change where the text is drawn relative to the data point. <code>'textposition'</code> can take the following options:
# - 'top left'
# - 'top center'
# - 'top right'
# - 'middle left'
# - 'middle center'
# - 'middle right'
# - 'bottom left'
# - 'bottom center'
# - 'bottom right'
# 
# We'll set the <code>'textposition'</code> to <code>'middle right'</code> to align the text to the right of the data point (remember, we put the text-only trace at the start of the list of traces!):

# In[85]:

fig['data'][0].update({'textposition' : 'middle right'})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (08) - Adding text to charts\pyo.iplot-2.png") 
 #

# Now we just need to extend the range of the plot to accomodate the label for the United States:

# In[86]:

fig['layout']['xaxis'].update({'range' : [0, healthcare['Spending per capita($)'].max() * 1.15]})
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (08) - Adding text to charts\pyo.iplot-3.png") 
 #

# Let's push this chart to the Plotly cloud!

# In[90]:

py.plot(fig, filename="Life expectancy and healthcare spending", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (08) - Adding text to charts\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to create a trace object which is designed to only show text notes for certain data points.
# 
# We practised using a user-defined function in the <code>df.apply()</code> method to create the column for the textnote in our DataFrame, and saw that it's good practise to pad this text field with a couple of spaces to move the text note slightly away from the data point.
# 
# We also saw that when creating a second trace which only displays text items, we should set this trace to have no hover effect, legend or data points, and we should also prepend this trace to the beginning of the list of traces so that the hoverinfo works for the remaining traces.
# 
# Finally, we saw how to manipulate the <code>'textposition'</code> option to change where the text notes are displayed relative to the data points.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
