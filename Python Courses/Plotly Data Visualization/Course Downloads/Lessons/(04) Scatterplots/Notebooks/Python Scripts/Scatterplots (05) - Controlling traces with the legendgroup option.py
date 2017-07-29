
# coding: utf-8

# # Scatterplots (05) - Controlling traces with the legendgroup option

# In this lesson we're going to learn how to control the show/hide behaviour of multiple traces at the same time by using the <code>'legendgroup'</code> option within the trace object.
# 
# We're going to plot data on life expectancy at age 60 against the dollar price of the most popular brand of cigarettes. The dataset contains data for 182 countries, each belonging to one of six regions. Each country has an observation on the life expectancy for males and females.
# 
# This will be quite a complex chart, but by grouping the observations for Sex by colour, and allowing the user to select which region(s) they can view, we can make this data easier to understand.

# ## Module Imports

# In[221]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[222]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting and preparing the data
# We'll get the data as a .csv file from my website:

# In[236]:

lifeExpectancy = pd.read_csv("http://www.richard-muir.com/data/public/csv/LifeExpectancyCigarettePrices.csv", index_col = 0)
lifeExpectancy.head()


# Let's create a text column:

# In[224]:

lifeExpectancy['text'] = lifeExpectancy.apply(lambda x: 
    "<b>{}</b><br>Life expectancy for {}s at 60: {} years<br>Price of cigarettes: ${:.2f}".format(x['Country'], 
                                                                                  x['Sex'],
                                                                                x['Years'],
                                                                                 float(x['Most sold cigarette brand (US$)'])), axis = 1)


# And check that it has worked as expected:

# In[225]:

lifeExpectancy.loc[0, 'text']


# We need to get a list of the unique values of the Region column so that we can loop through these to create the traces:

# In[226]:

regions = list(lifeExpectancy['Region'].unique())
regions


# We need to do the same for the values in the Sex column

# In[227]:

sexes = list(lifeExpectancy['Sex'].unique())
sexes


# We can now use this to build our region-to-symbol and sex-to-colour lookup:

# In[228]:

markerLookup = {'Eastern Mediterranean' : {'symbol' : 'circle'},
                     'Europe' :           {'symbol' : 'square'},
                     'Africa' :           {'symbol' : 'diamond'},
                     'Americas' :         {'symbol' : 'triangle-up'},
                     'Western Pacific' :  {'symbol' : 'cross'},
                     'South-East Asia' :  {'symbol' : 'x'},
                'Male' : {'color' : '#663399'}, 
                'Female' :{'color' : '#FF6347'}}


# ## Plotting the data

# For this chart we're going to create a trace for each of the Regions and for each of 'Male' and 'Female'. This will result in our chart having a total of 12 legend items! We'll then use <code>'legendgroup'</code> to control how these traces are displayed in the legend, and make the chart a lot clearer.
# 
# Let's now make the traces for our chart. We're going to do this in a nested loop; the outer loop will cycle through the list of sexes, whilst the inner loop will cycle through the regions; we'll create a trace for each combination. 
# 
# We'll plot the Life expectancy from age 60 on the y-axis, as it is the dependent variable; in this case I'm hypothesising that as the price of cigarettes increases, the life expectancy from age 60 will also increase.
# 
# We'll set the x-values, y-values and text for each trace by using the <code>df.loc[]</code> indexer in the same way as in the previous lesson, however rather than only using a condition on one column, we're going to select only the rows which fulfill two conditions on two columns. Namely that the values for Region and Sex match those which we are plotting for this trace. Notice that each condition is contained within parentheses:
# ````python
# lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years']
# ````
# 
# We're also going to use the colour lookup we created earlier to style each trace, and I'm setting the name of the trace by inserting the values of <code>region</code> and <code>sex</code> into a string using the <code>str.format()</code> method:

# In[229]:

traces = []

for sex in sexes:
    for reg in regions:
        traces.append({'type' : 'scatter',
                      'mode' : 'markers',
                      'x' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),
                                               'Most sold cigarette brand (US$)'],
                        'y' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years'],
                       'text' : lifeExpectancy.loc [(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),'text'],
                       'hoverinfo' : 'text',
                       'marker' : {'color' : markerLookup[sex]['color'],
                                   'symbol' : markerLookup[reg]['symbol'],
                                  'opacity' : 0.7},
                      'name' : "{}, {}".format(reg, sex)})


# Let's create the layout, Figure and plot the chart.
# 
# I'm setting the range for each axis (with the price of cigarettes going down to 0), the hovermode to 'closest', and a tickformat for the y-axis:

# In[230]:

layout = {'title' : 'Life expectancy against price of most popular brand of cigarettes (2011)',
         'xaxis' : {'title' : 'Price of most popular brand of cigarettes',
                    'range' : [0, 
                               lifeExpectancy['Most sold cigarette brand (US$)'].max() * 1.05],
                   'tickformat' : "${:}"},
         'yaxis' : {'title' : 'Life expectancy at age 60 (years)',
                    'range' : [lifeExpectancy['Years'].min()*0.9, 
                              lifeExpectancy['Years'].max()*1.05],},
         'hovermode' : 'closest'}


# In[231]:

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (05) - Controlling traces with the legendgroup option\pyo.iplot-0.png") 
 #

# So this chart seems to show that as the price of cigarettes increases, the life expectancy at age 60 also increases. We've got a pretty clear split between the life expectancies of males and females which is clear from the colour of the markers, but it's difficult to discern the differences within regions - you have to click on many different legend items to reduce the number of regions which are shown.
# 
# Let's use <code>'legendgroup'</code> to change this:

# ## Using <code>'legendgroup'</code>
# 
# The <code>'legendgroup'</code> option allows us to group traces together so that they are shown and hidden by clicking any of the legend items in that group. A <code>'legendgroup'</code> must be a string:
# ````python
# trace = {'legendgroup' : <string>}
# ````
# 
# We're going to set the <code>'legendgroup'</code> to be equal to the current <code>region</code>; each <code>'legendgroup'</code> will therefore contain two traces; one for males and one for females.

# In[232]:

traces = []

for sex in sexes:
    for reg in regions:
        traces.append({'type' : 'scatter',
                      'mode' : 'markers',
                      'x' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),
                                               'Most sold cigarette brand (US$)'],
                        'y' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years'],
                       'text' : lifeExpectancy.loc [(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),'text'],
                       
                       'legendgroup' : reg,                 
                       
                       'hoverinfo' : 'text',
                       'marker' : {'color' : markerLookup[sex]['color'],
                                   'symbol' : markerLookup[reg]['symbol'],
                                  'opacity' : 0.7},
                      'name' : "{}, {}".format(reg, sex)})


# Let's refresh the Figure object and plot the data:

# In[233]:

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (05) - Controlling traces with the legendgroup option\pyo.iplot-1.png") 
 #

# So this is a great improvement on the legend - although the number of legend items hasn't changed, they are grouped in such a way that it is intuitive for the reader to use. The legend items are now connected; should the user want to only view the data for a single region, they don't have to remove every single trace:
# 
# Let's push this chart to the Plotly cloud:

# In[234]:

py.plot(fig, filename="Life expectancy and cigarette prices", fileopt = 'overwrite')


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (05) - Controlling traces with the legendgroup option\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've had a little more practise at creating a lookup to set the marker colour and symbol.
# 
# We've also practised using the <code>df.loc[]</code> indexer to select specific observations from a DataFrame, but using multiple conditions enclosed by parentheses.
# 
# We've also seen how to use <code>'legendgroup'</code> to group the traces together on the legend.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
