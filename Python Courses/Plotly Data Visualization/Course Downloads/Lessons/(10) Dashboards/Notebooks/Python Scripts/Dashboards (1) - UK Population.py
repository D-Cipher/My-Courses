
# coding: utf-8

# # Dashboards (1) - UK Population

# In this lesson we're going to make the first of three dashboards in this section.
# 
# This dashboard will display information about the UK population. 
# 
# We're going to visualise the life expectancy at birth, and again at 65 for men and women in each constituent country of the UK. This data will be shown on two line charts.
# 
# Next, we'll look at the share of men and women in each region, displaying this data in a bar chart.
# 
# We'll then show the number of children, adults and pensioners in each region in the UK, once again, shown as a bar chart.
# 
# We're aiming for the dashboard to be in the following format:

# <img src='http://richard-muir.com/images/db1.png'/>

# ## Module Imports

# In[20]:

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
# Because we\re making a dashboard we'll need to include the <code>make_subplots()</code> function:

# In[21]:

from plotly.tools import make_subplots


# In[22]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Setting up the dashboard object
# 
# We'll firstly create the dashboard object. We are going to include four charts, so our subplots object will need two rows and two columns and we'll need to set the titles accordingly.
# 
# When we've finished development of the dashboard, we'll set the width and height of it to be in a landscape view. We'll keep it to the default size while we develop though; it's easier to see that way!

# In[23]:

db = make_subplots(rows = 2, cols = 2,
                  subplot_titles = ['Life expectancy at birth',
                                   'Life expectancy at 65',
                                   'Share of men and women in UK',
                                    'Age of people in the UK'])

db['data'] = [{'type' : 'scatter'}]
pyo.iplot(db)


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\pyo.iplot-0.png") 
 #

# ## Getting the data
# 
# We'll use two .csv files for our data. The first contains information on life expectancy and the second has the data on the population breakdown by age and sex.

# In[24]:

demographic = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKRegionsPopulation.csv",
                         index_col = 0)
demographic.head()


# In[25]:

lifeExp = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKCountriesLifeExpectancy.csv",
                         index_col = 0)

lifeExp.head()


# ## Making the line charts
# 
# #### Lookups
# 
# Let's now create our line charts. 
# 
# We're going to have lines for males and females on each chart. We'll distinguish these by setting the colour of the trace. We'll also have lines for each country, which we'll distinguish by setting the marker symbol.
# 
# We'll need a sex-colour and a country-symbol lookup, as well as a list of all trhe years in the Year column:

# In[26]:

sexColour = {'Male' : "rgb(114,229,239)",
            'Female' : 'rgb(125,26,110)'}

countrySymbol = {'England' : 'cross',
                'Scotland' : 'x',
                'Wales' : 'circle',
                'Scotland' : 'square',
                'N Ireland' : 'triangle'}
years = lifeExp['Year'].unique()


# #### Creating the hovertext column
# 
# Let's now create a hovertext column so we can display the hovertext exactly as we wish.
# 
# We're going to write a function which will concatenate together all the values of the variables to create the text field. 

# In[28]:

def hoverText(row):
    return "<b>{}</b><br>{:.0f} years<br><i>{}</i>".format(row['Country'], row['N'], row['Sex'])

lifeExp['text'] = lifeExp.apply(hoverText, axis = 1)

lifeExp.head()


# Let's now add the traces to our chart. We're going to do this in three loops. 
# 
# The first, and outer loop will place the traces on the correct grid space in the subplots. 
# 
# The traces for life expectancy at birth will go at <code>row = 1, col = 1</code>, whilst the traces for life expectancy at 65 will go at <code>row = 1, col= 2</code>. We'll also create a variable that will allow us to only show the first trace. This way, the legend won't be cluttered.
# 
# The second loop will cycle through the countries, and we'll set the symbol for the traces using the lookup we created.
# 
# The innermost loop will cycle through the sexes, and we'll set the colour for the traces using the other lookup.

# In[29]:

for life in ['birth', 'age 65']:
    
    if life == 'age 65':
        show = True
        col = 2
    else:
        show = False
        col = 1
        
    for country in lifeExp['Country'].unique():
        
        for sex in lifeExp['Sex'].unique():
            db.append_trace({'type' : 'scatter',
                            'mode' : 'markers+lines',
                            'x' : years,
                            'y' : lifeExp['N'][(lifeExp['Country'] == country) & (lifeExp['Sex'] == sex) & (lifeExp['Var'] == life)],
                             'text' : lifeExp['text'][(lifeExp['Country'] == country) & (lifeExp['Sex'] == sex) & (lifeExp['Var'] == life)],
                             'hoverinfo' : 'text',
                             'legendgroup' : country,
                             'showlegend' : show,
                             'name' : "{}, {}".format(country,sex),
                            'marker' : {'symbol' : countrySymbol[country],
                                        'color' : sexColour[sex],
                                        'size' : 6,
                                        'line' : {'width' : 1,
                                                 'color' : '#333'}}},
                           row = 1, col = col)
pyo.iplot(db)


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\pyo.iplot-1.png") 
 #

# ## (2) Making the bar charts
# 
# If you're following along with the videos, the second lesson starts here.
# 
# Now we've added the line traces, we can start to put the bar traces in the remaining cells. These traces will show a bar for each of the English regions and the other countries (Scotland, Wales & Northern Ireland).
# 
# #### Number of males and females in each country
# 
# We'll first of all append the Male/Female bar traces to the bottom-left cell, but let's first remind ourselves what the demographics dataset looks like:

# In[30]:

demographic.head()


# We'll now add a text column for each of the columns we're going to plot. I'm going to create a new function to apply. 
# 
# We'll use another parameter of the <code>pandas.DataFrame.apply()</code> method to pass in the name of the column which holds the value of the variable.
# 
# We pass this argument within the <code>args=()</code> parameter, and it's really important that the column name is followed by a comma. Following the column name with a comma means that Python interprets it as a tuple, and not a string within two sets of brackets.
# 
# Finally, we'll create a lookup between the column which contains the variable and the respective text column.

# In[31]:

def hoverText(row, varName):
    return "<b>{}</b><br>{:,.0f}<br><i>{}</i>".format(row['Country'], row[varName], varName)

demoTextLookup = {}

for col in demographic.columns:
    if col != 'Country':
        demographic['text{}'.format(col)] = demographic.apply(hoverText, args=(col,), axis = 1)
        demoTextLookup[col] = 'text{}'.format(col)

demographic.head()


# Let's first sort the demographic dataset from largest to smallest; this will make it easier to read.

# In[32]:

mf = demographic.sort_values(by=['Male','Female'], ascending = False)
mf.head()


# I'm going to set the marker colour to be consistent with the chart above, and I'm also going to set the traces in each cell to have the same legendgroup so we can make sure they are spread apart:

# In[33]:

for sex in ['Male', 'Female']:
    textCol = demoTextLookup[sex]
    db.append_trace({'type' : 'bar',
                    'x' : mf['Country'],
                    'y' : mf[sex],
                     'name' : sex,
                     'text' : mf[textCol],
                     'hoverinfo' : 'text',
                     'legendgroup' : 'maleFemale',
                    'marker' : {'color' : sexColour[sex],
                               'line' : {'width' : 1,
                                        'color' : '#333'}}},
                   row = 2, col = 1)
pyo.iplot(db)


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\pyo.iplot-2.png") 
 #

# #### Number of people in each age group in each country
# 
# Now we'll add the bar traces showing the number of people in the different age groups in the UK.
# 
# Once again, we'll sort the DataFrame in descending order before we plot it:

# In[34]:

ages = demographic.sort_values(by=['Adults','Pensioners','Children'],
                              ascending = False)
ages.head()


# First of all we need to get a list of the different age categories, then, looping through this list, we can add a trace for each region or country, setting <code>row = 2, col = 2</code>.
# 
# We'll also create a new lookup for the colours for the age groups. I've set these colours to contrast heavily with the colours we set for the males and females.

# In[35]:

ageColours = [ "rgb(133,199,156)", "rgb(82,239,153)", "rgb(52,75,70)"]
ageGroups = ['Children','Adults','Pensioners']
ageLookup = dict(zip(ageGroups, ageColours))
ageLookup


# Now, we'll create the traces. We're also going to set the trace names and legendgroup:

# In[36]:

for age in ageGroups:
    textCol = demoTextLookup[age]
    db.append_trace({'type' : 'bar',
                    'x' : ages['Country'],
                    'y' : ages[age],
                     'text' : ages[textCol],
                     'hoverinfo' : 'text',
                     'name' : age,
                     'legendgroup' : 'ages',
                    'marker' : {'color' : ageLookup[age],
                               'line' : {'width' : 1,
                                        'color' : '#333'}}},
                   row = 2, col = 2)
    
pyo.iplot(db)


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\pyo.iplot-3.png") 
 #

# ## (3) Setting the layout
# 
# If you're following along with the videos, the third lesson for this dashboard starts here.
# 
# We've now got a few changes to make to the layout:
# 1. Set the range to be static for the y-axes on the bar charts
# 1. Set the tracegroupgap
# 2. Add a tickangle to the x-axes
# 1. Add axis titles where appropriate
# 3. Set the width and height of the dashboard
# 4. Add some margins if necessary
# 5. Add a title for the dashboard
# 7. Set the hovermode to 'closest'
# 
# 

# In[37]:

#Get the minimum and maximum to set the static range
maximum = max(demographic[ageGroups].max())
minimum = min(demographic[ageGroups].min())
diff = maximum - minimum

for i in range(3, 5):
    #1. Setting static range for bar chart
    db['layout']['yaxis{}'.format(i)].update({'range' : [0,maximum + (diff * 0.1)]})
    #3. Tickangle for x-axes on bar charts
    db['layout']['xaxis{}'.format(i)].update({'tickangle' : -45})
    
#4. Line chart axis titles
db['layout']['yaxis1'].update({'title' : 'Years'})
db['layout']['yaxis3'].update({'title' : 'Number of people'})

#2. Setting tracegroupgap
db['layout'].update({'legend' : {'tracegroupgap' : 25},
                     #5. Setting width and height
                    'width' : 1000,
                    'height' : 750,
                     #6. Add a bottom margin
                    'margin' : {'b' : 130},
                     #9. Hovermode to closest
                    'hovermode' : 'closest'})

#8. Adding a title for the dashboard  
db['layout']['annotations'] +=[{'text' : 'Demographics of the UK Population',
                                     'xref' : 'paper',
                                     'yref' : 'paper',
                                      'xanchor' : 'center',
                                    'showarrow' : False,
                                'font' : {'size' : 24},
                                     'x' : 0.5,
                                     'y' : 1.15}]

pyo.iplot(db)


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\pyo.iplot-4.png") 
 #

# Let's send this dashboard to the Plotly cloud:

# In[38]:

py.plot(db, filename="Population demographics of the UK", fileopt="overwrite")


py.image.save_as(db, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (1) - UK Population\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# This first dashboard lesson has allowed us to recap what we have learnt so far in this course about making dashboards in Plotly.
# 
# We've reviewed how to add traces to the subplots object, how to use lookup dictionaries to set colours and symbols for the traces, how to set the legendgroup and showlegend to reduce the quantity of legend items.
# 
# We've learnt how to use the pd.DataFrame.apply() method with the <code>args=( ,)</code> parameter to pass an extra argument to the function which we apply, allowing us to reuse the same function to create multiple columns.
# 
# We've also seen a little of dashboard design; how to choose the colours in a dashboard to set a consistent theme, but also to add contrast

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
