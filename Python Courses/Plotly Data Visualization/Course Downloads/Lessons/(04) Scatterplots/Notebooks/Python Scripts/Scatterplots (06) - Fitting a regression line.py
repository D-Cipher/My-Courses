
# coding: utf-8

# # Scatterplots (06) - Fitting a regression line
# In this lesson we're going to learn how to fit a regression line to the life expectancy data. We'll use the <code>stats</code> module from the <code>scipy</code> library to calculate the regression equation.
# 
# We'll then plot the resulting line as a separate trace and add the equation onto our chart as an annotation.

# ## Module Imports

# In[98]:

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
# We're going to use the <code>stats</code> module from the <code>scipy</code> library to calculate the regression equation:

# In[99]:

from scipy import stats


# In[100]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the chart
# We'll create the chart from scratch rather than loading it from the Plotly cloud because we'll need to do the regression calculations on the raw data:

# In[101]:

lifeExpectancy = pd.read_csv("http://www.richard-muir.com/data/public/csv/LifeExpectancyCigarettePrices.csv", index_col = 0)
lifeExpectancy['text'] = lifeExpectancy.apply(lambda x: 
    "<b>{}</b><br>Life expectancy for {}s at 60: {} years<br>Price of cigarettes: ${:.2f}".format(x['Country'], 
                                                                                  x['Sex'],
                                                                                x['Years'],
                                                                                 float(x['Most sold cigarette brand (US$)'])), axis = 1)


# In[102]:

regions = list(lifeExpectancy['Region'].unique())
sexes = list(lifeExpectancy['Sex'].unique())
markerLookup = {'Eastern Mediterranean' : {'symbol' : 'circle'},
                     'Europe' :           {'symbol' : 'square'},
                     'Africa' :           {'symbol' : 'diamond'},
                     'Americas' :         {'symbol' : 'triangle-up'},
                     'Western Pacific' :  {'symbol' : 'cross'},
                     'South-East Asia' :  {'symbol' : 'x'},
                'Male' : {'color' : '#663399'}, 
                'Female' :{'color' : '#FF6347'}}


# In[103]:

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
                      'name' : "{} {}s".format(reg, sex)})


# In[104]:

layout = {'title' : 'Life expectancy against price of most popular brand of cigarettes (2011)',
         'xaxis' : {'title' : 'Price of most popular brand of cigarettes',
                    'range' : [0, 
                               lifeExpectancy['Most sold cigarette brand (US$)'].max() * 1.05],
                   'tickformat' : "${:}"},
         'yaxis' : {'title' : 'Life expectancy at age 60 (years)',
                    'range' : [lifeExpectancy['Years'].min()*0.9, 
                              lifeExpectancy['Years'].max()*1.05],},
         'hovermode' : 'closest'}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (06) - Fitting a regression line\pyo.iplot-0.png") 
 #

# ## Calculating the regression equation
# Now we can use the <code>stats.linregress()</code> function to calculate the regression equation. We're going to touch upon some statistics here, but I'll keep it light and brief; this is a data visualisation course after all! Still, it's important to know what you're dealing with when plotting a regression line.
# 
# <code>stats.linregress()</code> takes two arguments; an x-value and a y-value. It returns 5 variables:
# - slope: the gradient of the regression line
# - intercept: where the line crosses the y-axis
# - r_value: the correlation coefficient of the regression. R^2 is often used to explain how much variation in the y-values is explained by the model.
# - p_value: a statistical measure of whether or not the line is significantly different from 0. Generally speaking, this should be under 0.05 to be considered significant, however statistics is a broad subject and the p-value is not necessarily the best measure for this.
# - std_err: the standard error is an estimate of the standard deviation; ie how much the data varies.
# 
# For the time being we only need to worry about the slope and the intercept, as these are the variables we'll be plotting.
# 
# Let's use this to calculate the regression equation which we can then use to plot the regression line:

# In[105]:

slope, intercept, r_value, p_value, std_err = stats.linregress(lifeExpectancy['Most sold cigarette brand (US$)'],
                                                              lifeExpectancy['Years'])


# Let's see the values for slope and intercept:

# In[106]:

slope, intercept


# What this means is that the regression line crosses the y-axis at 17.20 years (this is the life expectancy at age 60 when the price of cigarettes is \$0), and then for every increase of \$1 in the price of cigarettes, life expectancy at age 60 increases by 0.84 years. 
# 
# Obviously the price of cigarettes does not explain every change in life expectancy, and we can evaluate this regression equation by looking at the R^2, p_value and std_err:

# In[107]:

r_value**2, p_value, std_err


# This model only explains 31% of the variation in the y-values (R^2 = 0.31). The p-value is very small, and therefore the result is statistically significant, although this can simply mean that we have a lot of data points!
# 
# The standard error tells us that the average distance of the data points from the regression line is 0.06 years; this is often used to assess the precision of predictions made using the model and is something which we won't cover in this course.

# ## Plotting the regression line
# 
# First of all we need to calculate the values for the line. The regression equation is of the form:
# ````
# Y = slope * X + intercept
# ````
# To plot the line we can calculate the value of y when x = 0, and the value of y when x is at its maximum value:

# In[108]:

xValRange = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]

line = [slope * xValRange[0] + intercept, slope * xValRange[1] + intercept]
line


# We can now add a new trace by plotting another scatter trace, but with <code>'mode'</code> set to <code>'lines'</code>. We're also going to set the colour of the trace to a dark grey, the <code>'showlegend'</code> parameter to <code>False</code>, and the <code>'hoverinfo'</code> to <code>'none'</code> because we don't want this line to appear on the legend or have any hover interaction:

# In[109]:

traces.append({'type' : 'scatter',
              'mode' : 'lines',
              'x' : xValRange,
              'y' : line,
               'marker' : {'color' : '#333'},
               'hoverinfo' : 'none',
               'showlegend' : False })


# In[110]:

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (06) - Fitting a regression line\pyo.iplot-1.png") 
 #

# ## Adding the regression equation as an annotation
# Adding the regresison equation as an annotaion will allow those who are familiar with statistical regression to evaluate the regression equation.
# 
# The Plotly Layout object can contain a list of annotations, each showing a different text string:
# ````python
# layout = {'annotations' : [{'text' : 'Annotation1'},
#                             {'text' : 'Annotation2'}]}
# ````                            
# The annotations can be positioned anywhere on the chart area, either with respect to the relative coordinates of the plot, or as actual data points on the chart. We're going to position the annotation for the regression equation based on the data points on the chart. 
# 
# To do this, we must set <code>'xref'</code> and <code>'yref'</code> to <code>'x'</code> and <code>'y'</code> respectively. We also need to set the x- and y-position of the annotation:
# 
# ````python
# Annotation1 = {'text' : 'Annotation1',
#                 'xref' : 'x',
#                 'yref' : 'y',
#                 'x' : <x coordinate, normally an integer or float>,
#                 'y' : <y coordinate, normally an integer or float>}
# ````             
# A default annotation has an arrow, which we're going to suppress
# ````python
# Annotation1 = {'showarrow' : False}
# ````
# I'm going to write this annotation as:
# 
# ```` y = 0.84x + 17.2
#      R^2 = 0.31
# ````
# 
# To do this, I'll use the python string formatting which we've utilised before to create the text column in the DataFrame. I'll also use the HTML <code>&lt;sup&gt;&lt;/sup&gt;</code> tag to display the R^2 as a superscript.
# 
# I'm going to set the x- and y-coordinates to 10 and 28 respectively; this is a good starting point which I've judged by eye - we can always tweak it later:

# In[111]:

equationAnnotation = {'text' : "y = {:.2f}x + {:.2f}<br>R<sup>2</sup> = {:.2f}".format(slope, intercept, r_value**2),
                     'xref' : 'x',
                     'yref' : 'y',
                      'x' : 10,
                      'y' : 28,
                     'showarrow' : False}


# Let's add this annotation to the layout object (remembering to add it as a list!), refresh the Figure object and plot the chart:

# In[112]:

layout['annotations'] = [equationAnnotation]
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (06) - Fitting a regression line\pyo.iplot-2.png") 
 #

# This plot looks great with the added regression line, let's push it to the Plotly cloud:

# In[113]:

py.plot(fig, filename = "Life expectancy against price of cigarettes (Regression)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (06) - Fitting a regression line\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to calculate a regression equation using the <code>scipy.stats.linregress()</code> function and we've had a brief introduction into the output from this function.
# 
# We've learnt how to use the resulting regression equation to calculate the coordinates of a regression line, plot this line on the chart and use the <code>'showlegend' : False</code> to prevent the trace from appearing as a legend item.
# 
# Finally we've learnt how to add a list of annotations to the layout as well as how to position these annotations using x- and y-coordinates.
# 
# In the next lesson you'll get the opportunity to practise what you've learnt by fitting a regression line to the data for Males and Females separately.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
