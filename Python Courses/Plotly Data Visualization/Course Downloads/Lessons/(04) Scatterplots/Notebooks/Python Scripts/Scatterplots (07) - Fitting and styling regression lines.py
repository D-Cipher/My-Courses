
# coding: utf-8

# # Scatterplots (07) - Fitting and styling regression lines

# In this lesson we're going to fit and display a regression line and equation to the data for males and females separately. This is a great opportunity to practise this skill, and it also results in a very striking chart.
# 
# We'll also learn how apply some styling to the text annotations, changing their colours to that each can be attributed to the correct data source.
# 
# We're going to get the DataFrame, then calculate the regressions and create the regression traces and annotations within a loop. We'll then get the original chart from the Plotly cloud and add these new traces and annotations to it.

# ## Module Imports

# In[176]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# #### New Modules:
# 
# We're going to use the <code>stats</code> module from the <code>scipy</code> library again:

# In[177]:

from scipy.stats import linregress


# In[178]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# We'll get the data and use it to calculate the regressions for the males and females separately:

# In[179]:

lifeExpectancy = pd.read_csv("http://www.richard-muir.com/data/public/csv/LifeExpectancyCigarettePrices.csv", index_col = 0)


# In[180]:

lifeExpectancy


# We'll get a list which contains the unique values for the Sex column and adapt the markerLookup dictionary to contain the colours which correspond to each sex. We'll use this to style the regression lines and equations.

# In[181]:

sexes = list(lifeExpectancy['Sex'].unique())
markerLookup = {'Male' : {'color' : '#663399'}, 
                'Female' :{'color' : '#FF6347'}}


# ### Fitting the regressions
# We'll now fit the regression equation to the data for males and females separately. I'll store the results of the regression in a dictionary, with separate keys for Males and Females.
# 
# We'll calculate the x- and y-values of the regression line in the same way as in the previous lesson, I'm going to store the coordinates of the regression line so we can plot them easily:

# In[182]:

regressions = {}
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]


# ### Creating the traces
# Now, within the same loop I can create the traces for the regression lines which we can then add to the chart. I'm setting the colours of these traces using the <code>markerLookup</code> dictionary:

# In[183]:

regressions = {}
traces = []
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]
    
    traces.append({'type' : 'scatter',
                  'mode' : 'lines',
                  'x' : regressions[sex]['x-values'],
                  'y' : regressions[sex]['y-values'],
                   'marker' : {'color' : markerLookup[sex]['color']},
                   'showlegend' : False })   
    


# ### Creating the annotations
# Finally I can create the annotations within the loop. I'm going to loosely set the x- and y-coordinates and then fine-tune them when we have positioned them on the chart.
# 
# I also need to set the colour of the annotation text. This parameter is within the <code>'font'</code> dictionary:

# In[184]:

regressions = {}
traces = []
annotations = []
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]
    
    traces.append({'type' : 'scatter',
                  'mode' : 'lines',
                  'x' : regressions[sex]['x-values'],
                  'y' : regressions[sex]['y-values'],
                   'marker' : {'color' : markerLookup[sex]['color']},
                   'showlegend' : False }) 
    
    annotations.append({'text' : "<b>{}s: y = {:.2f}x + {:.2f}<br>R<sup>2</sup> = {:.2f}</b>".format(sex,slope, intercept, r_value**2),
                       'xref' : 'x',
                       'yref' : 'y',
                        'x' : 10,
                        'y' : 28,
                        'showarrow' : False,
                       'font' : {'color' : markerLookup[sex]['color']}})


# Let's have a look at the objects we've created:

# In[185]:

regressions


# In[186]:

traces


# In[187]:

annotations


# Both annotations have the same x- and y-coordinates. I'll change one so we can tell them apart:

# In[188]:

annotations[0]['y'] = 20


# ## Modifying the original chart
# I'll use the <code>py.get_figure()</code> function to get the original chart:

# In[189]:

lifeExp = py.get_figure('rmuir',206)
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (07) - Fitting and styling regression lines\pyo.iplot-0.png") 
 #

# Now I can add the traces to the Data object within the Figure:

# In[190]:

lifeExp['data'] = lifeExp['data'] + traces
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (07) - Fitting and styling regression lines\pyo.iplot-1.png") 
 #

# And now the annotations can be added to the layout:

# In[191]:

lifeExp['layout']['annotations'] = annotations
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (07) - Fitting and styling regression lines\pyo.iplot-2.png") 
 #

# I'll move the annotation for females left and up a bit:

# In[192]:

lifeExp['layout']['annotations'][1]['x'] = 8
lifeExp['layout']['annotations'][1]['y'] = 29
pyo.iplot(lifeExp)


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (07) - Fitting and styling regression lines\pyo.iplot-3.png") 
 #

# So this chart looks pretty good to me! We have a different regression line for males and females, with the text annotations and lines styled to be consistent with the data points. You can clearly see the difference in the life expectancies for males and females; not only do females tend to live longer in all countries, but as the price of cigarettes increases their life expectancy at age 60 increases more than for males.
# 
# Let's send this to the Plotly cloud:

# In[193]:

py.plot(lifeExp, filename="Life expectancy against cost of cigarettes (Male & female regressions)", fileopt = "overwrite")


py.image.save_as(lifeExp, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (07) - Fitting and styling regression lines\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've reviewed everything we learnt in the previous lesson. We've plotted separate regression lines and equations for males and females and we've also learnt how to change the colour of the annotations.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
