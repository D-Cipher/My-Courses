
# coding: utf-8

# # Dashboards (2) - Crime in London

# In this second lesson on dashboards we're going to visualise some data about crime in London. The dataset we'll be using contains information on all the different crimes recorded by the Metropolitan police during 2016.
# 
# This is a 40mb raw dataset, so we'll be using the pandas groupby() function to summarise the data in different ways.
# 
# Our dashboard will have seven rows; the first two charts will occupy two rows each, whilst the last three charts will have one each.
# 
# The final three charts will show simple summaries of the data and will serve to give contextual information about the data to the data to help our readers understand the situation better. The first two charts we make will be a little more complex and are the focal point of this visualisation.
# 
# We'll create the contextual charts first, as doing so will help us to familiarise ourselves with the dataset.
# 
# First of all we'll use a line chart to show how the number of crimes changes each month.
# 
# Next, we'll create a bar chart showing the number of crimes in each location.
# 
# The next step will be to create another bar chart, this one showing the number of each different type of crime.
# 
# Now for the more complex charts . . . These will be a special type of scatterplot which allows us to show the interaction between different categories.
# 
# The first chart will show, for each type of crime, what is the most common outcome.
# 
# The second chart will show for each location, what is the most common type of crime.
# 

# <img src='http://richard-muir.com/images/db2.png'/>

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


# #### New Modules:
# 
# We'll need the make_subplots() module as well as the Python datetime module to help us get the month names from the dates:

# In[2]:

from plotly.tools import make_subplots
import datetime


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# This dataset is a 40mb file containing individual records for the crimes recorded by the Metropolitan Police in 2016. It might take a little while to download.

# In[4]:

crimes = pd.read_csv('http://richard-muir.com/data/public/csv/MetPoliceCrimeStats.csv',
                    index_col = 0)
crimes.head()


# ## Making the subplots object
# 
# Let's now get the template for our dashboard. We want to combine the first two rows, and the third and fourth rows:

# In[5]:

metCrimes = make_subplots(rows = 7,
                         cols = 1,
                         specs = [[{'rowspan' : 2}],
                                 [None],
                                  [{'rowspan' : 2}],
                                 [None],
                                 [{}],
                                 [{}],
                                 [{}]],
                         subplot_titles = [ 'Outcomes for crime',
                                           'Types of crime by location',
                                           'Crimes by month',
                                          'Crimes by location',
                                          'Types of crime'
                                         ])


# ## Line chart of crimes by month
# 
# Let's now group our dataset by 'Crime Month'. We'll count the number of observations in each month to give us the quantity of crimes which ocurred in that month. By setting <code>as_index = False</code> the column which is being grouped is not stored as the index.
# 
# Because we're calling <code>.count()</code> on the groupby object, this returns a count of the number of rows within each group. We can use any column as tghe y-values in our chart.

# In[6]:

crimesByMonth = crimes.groupby('Crime Month', as_index = False).count()
crimesByMonth


# Let's add a text column which will show the month name and the number of crimes. First of all we need to convert the Crime Month column to a datetime using the <code>pd.to_datetime()</code> function. We have to tell this function in which format the date is.
# 
# <code>"%Y-%m"</code> means that the date string is a four-digit year, followed by a hyphen, followed by a two-digit month.
# 
# Then, we'll use the <code>strftime</code> function to get the month name from our datetime object. <code>"%B"</code> is the datetime format for the month name.

# In[7]:

crimesByMonth['Crime Month'] = pd.to_datetime(crimesByMonth['Crime Month'], format='%Y-%m')

crimesByMonth['Month'] = crimesByMonth['Crime Month'].apply(lambda x: x.strftime("%B"))
crimesByMonth.head()


# In[8]:

crimesByMonth['text'] = crimesByMonth.apply(lambda x: "<b>{}:</b><br>{:,} crimes".format(x['Month'], x['Crime type']), axis = 1)
crimesByMonth.head()


# Let's create this line chart outside of the subplots object, then, when we're happy with it, we can use the append_trace() function to put it in our dashboard.
# 
# Because each of the charts will only have a single trace, we don't need a legend for this dashboard. I'll set 'showlegend' to False on every trace:

# In[9]:

monthCrime = {'type' : 'scatter',
              'x' : crimesByMonth['Month'],
              'y' : crimesByMonth['Area'],
              'text' : crimesByMonth['text'],
              'showlegend' : False,
               'marker' : {'color' : '#944dc7',
                          'size' : 8,
                          'line' : {'width' : 1,
                                   'color' : '#333'}},
               'name' : 'Number of crimes<br>by month',
              'hoverinfo' : 'text'}

pyo.iplot([monthCrime])


py.image.save_as([monthCrime], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-0.png") 
 #

# I'm happy with that, but I have noticed that the y-axis doesn't start from 0. This gives the false impression that crime fell almost to 0 in December.
# 
# Let's append the trace and change the range of the y2 axis. We'll also increase the height of the dashboard to make it easier to build.

# In[10]:

metCrimes.append_trace(monthCrime, 5, 1)

metCrimes['layout']['yaxis3'].update({'range' : [0, max(crimesByMonth['Area']) * 1.05]})
metCrimes['layout'].update({'height' : 1000})

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-1.png") 
 #

# ## (2) Number of crimes in each location
# 
# If you're using the videos, the second lesson starts here
# 
# To get the number of crimes in each location we must group by the 'Area' column and count the number of rows in each group:

# In[11]:

areaCrime = crimes.groupby('Area', as_index=False).count()
areaCrime.head(10)


# The rows can clearly be split into two groups; those which have thousands of crimes, and are therefore in London, and those which only have a few crimes, and are therefore not in London. 
# 
# Let's recode the areas that aren't in London, and groupby again to get 'Not in London' as a separate Area category. We'll have to call <code>.sum()</code> on the groupby object:

# In[12]:

def inLondon(row):
    if row['Outcome Month'] > 1000: 
        return row['Area']
    else: 
        return 'Not in London'

areaCrime['Area'] = areaCrime.apply(inLondon, axis = 1)
areaCrime.head(10)


# In[13]:

areaCrime = areaCrime.groupby('Area', as_index = False).sum()
areaCrime


# That seems to have worked correctly. I'm not an expert on the London areas, but there seems to be nothing out of place. Let's sort this data from largest to smallest and plot a bar chart:

# In[14]:

areaCrime.sort_values(by='Outcome Month', ascending=False, inplace = True)

areaBar = {'type' : 'bar',
      'x' : areaCrime['Area'],
      'y' : areaCrime['Outcome Month'],
       'name' : 'Crimes by Area',
           'showlegend' : False,
       'hoverinfo' : 'x+y',
      'marker' : {'color' : 'rgba(77, 83, 199, 0.6)',
                 'line' : {'width' : 1,
                          'color' : '#333'}}}

pyo.iplot([areaBar])


py.image.save_as([areaBar], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-2.png") 
 #

# OK, that's looking pretty good; let's append it to the dashboard. I'm going to rotate the ticks on the x-axis to make them easier to read.

# In[15]:

metCrimes.append_trace(areaBar, row = 6, col = 1)

metCrimes['layout']['xaxis4'].update({'tickangle' : 45})

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-3.png") 
 #

# ## (3) Types of crime
# 
# If you're following along with the videos, the third lesson starts here.
# 
# Now let's make another bar chart showing the number of different types of crime. We'll once again use the groupby method to get our data:

# In[16]:

crimeTypes = crimes.groupby('Crime type', as_index=False).count()
crimeTypes.head()


# Let's sort this from largest to smallest and make another bar chart:

# In[17]:

crimeTypes.sort_values(by='Outcome Month', ascending = False, inplace = True)

crimeBar = {'type' : 'bar',
      'x' : crimeTypes['Crime type'],
      'y' : crimeTypes['Outcome Month'],
       'name' : 'Crimes by type',
            'showlegend' : False,
       'hoverinfo' : 'x+y',
      'marker' : {'color' : 'rgba(226, 97, 50, 0.6)',
                 'line' : {'width' : 1,
                          'color' : '#333'}}}

pyo.iplot([crimeBar])


py.image.save_as([crimeBar], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-4.png") 
 #

# That's looking good. I'll now append it to the dashboard:

# In[18]:

metCrimes.append_trace(crimeBar, row = 7, col = 1)

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-5.png") 
 #

# ## (4) Type of crime and location
# 
# If you're following along with the videos, the fourth lesson starts here.
# 
# We're going to make a special kind of scatterplot to show the type of crime by the location. The x-values will show the type of crime, whilst the y-values will show the location. The size of the marker will display how many crimes of a type happened at a location.
# 
# We first need to group the DataFrame by type and location:

# In[19]:

typeLoc = crimes.groupby(['Crime type', 'Area'], as_index=False).count()
typeLoc.head()


# Now we need to find out which locations are outside London. We did this earlier for the bar chart showing the number of crimes by area, but this time, rather than recoding the Area column we must instead make a new column showing whether the area is in London or not.
# 
# We'll create a new column by applying the inLondon() function:

# In[20]:

locationRecode = crimes.groupby(['Area'], as_index=False).count()
locationRecode['Recoded Area'] = locationRecode.apply(inLondon, axis = 1)
locationRecode.head(10)


# Now let's merge this recoded DataFrame onto our grouped DataFrame using the <code>DataFrame.merge()</code> method.
# 
# I'm only selecting the Recoded Area and Area columns from the DataFrame.
# 
# We must specify a key common to each DataFrame as the merge key. We're also using a 'left join'. This means that we discard any observations from the locationRecode DataFrame which aren't in the typeLoc DataFrame.

# In[21]:

typeLoc = typeLoc.merge(locationRecode[['Area','Recoded Area']], how = 'left', on='Area')
typeLoc.head(20)


# So we can see that we now have a new column which adds a 'Not in London' description for those areas which aren't in the jurisdiction of the Metropolitan police (the City of London is a strange example of this!). Let's now drop the old Area column, rename the 'Recoded Area' to 'Area', and do the group by again but calling <code>.sum()</code> rather than <code>.count()</code> (as we did earlier):

# In[22]:

typeLoc = typeLoc.drop(['Area'], axis = 1).rename(columns={'Recoded Area' : 'Area'})
typeLoc.head()


# In[23]:

typeLoc = typeLoc.groupby(['Crime type','Area'], as_index=False).sum()
typeLoc


# Before we plot, let's make a text column:

# In[24]:

typeLoc['text'] = typeLoc.apply(lambda x: "<b>{}</b><br>{}<br>{:,}".format(x['Area'], 
                                                                           x['Crime type'],
                                                                          x['Outcome Month']),
                               axis = 1)
typeLoc.head()


# So we've got over 400 observations to plot. Let's make our scatterplot. We're going to set the marker size to show the number of crimes of a particular type in each area. We need to remember to set the <code>sizeref</code> and <code>sizemin</code> to appropriate values.

# In[25]:

typeLocScatter = {'type' : 'scatter',
                  'mode' : 'markers',
                 'x' : typeLoc['Area'],
                 'y' : typeLoc['Crime type'],
                  'text' : typeLoc['text'],
                  'opacity' : 0.8,
                  'hoverinfo' : 'text',
                  'showlegend' : False,
                  'name' : 'Type and Location of crime',
                  'marker' : {'size' : typeLoc['Outcome Month'],
                             'sizeref' : 150,
                             'sizemin' : 1.5}
                 }

pyo.iplot([typeLocScatter])


py.image.save_as([typeLocScatter], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-6.png") 
 #

# So there's quite a lot of information there. Let's add this chart to the dashboard:

# In[26]:

metCrimes.append_trace(typeLocScatter, row = 3, col = 1)

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-7.png") 
 #

# ## (5) Types of crime by outcome
# 
# If you're following along with the videos the fifth lesson starts here.
# 
# We'll now make the final chart for this dashboard. This chart will show for each type of crime, how many crimes of that type resulted in a specifc outcome. 
# 
# There are many different kinds of outcome. We first of all need to recode all of the different outcomes into fewer categories to allow us to plot them more easily.
# 
# We'll apply the function below to recode the different outcomes:

# In[27]:

def wideCoding(crime):
    if crime in ['Court case unable to proceed',
                 'Investigation complete; no suspect identified',
                'Formal action is not in the public interest',
                 'Offender given absolute discharge',
                'Unable to prosecute suspect']:
        return 'No judicial outcome'
    elif crime in ['Local resolution','Offender given a caution',
                   'Offender given a drugs possession warning',
                   'Offender given community sentence',
                   'Offender given conditional discharge',
                   'Offender given penalty notice',
                   'Offender fined',
                   'Offender deprived of property',
                   'Offender given suspended prison sentence',
                   'Offender otherwise dealt with',
                   'Offender ordered to pay compensation']:
        return 'Punished, not prison'
    elif crime in ['Suspect charged',
                   'Suspect charged as part of another case',
                  'Defendant sent to Crown Court']:
        return 'Outcome not yet known'
    else:
        return crime
    
crimes['Broad Outcome'] = crimes['Outcome type'].apply(wideCoding)
crimes.head()


# Let's now group the DataFrame by the Crime type and Broad Outcome to get the data for our chart. We'll also make a text column:

# In[28]:

typeOutcome = crimes.groupby(['Crime type','Broad Outcome'], as_index=False).count()
typeOutcome['text'] = typeOutcome.apply(lambda x: "<b>{}</b><br>{}<br>{:,}".format(x['Crime type'],
                                                                                   x['Broad Outcome'],
                                                                                  x['Outcome Month']),
                               axis = 1)
typeOutcome.head()


# We're going to make the same type of chart that we just previously made. This is quite complex data, and that type of bubble plot simplifies it very well. 

# In[29]:

typeOutcomeScatter = {'type' : 'scatter',
                  'mode' : 'markers',
                 'x' : typeOutcome['Broad Outcome'],
                 'y' : typeOutcome['Crime type'],
                  'text' : typeOutcome['text'],
                  'opacity' : 0.8,
                  'hoverinfo' : 'text',
                      'showlegend' : False,
                  'name' : 'Type of crime and outcome',
                  'marker' : {'size' : typeOutcome['Outcome Month'],
                             'sizeref' : 1000,
                             'sizemin' : 2}
                 }

pyo.iplot([typeOutcomeScatter])


py.image.save_as([typeOutcomeScatter], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-8.png") 
 #

# The bubbles for 'No judicial outcome' are very large compared to the rest, but it's also interesting to see the differnces in outcomes for different types of crime.
# 
# Let's add this chart to our dashboard:

# In[30]:

metCrimes.append_trace(typeOutcomeScatter, row = 1, col = 1)

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-9.png") 
 #

# ## (6) Changing the layout
# 
# If you're following along with the videos, the sixth and final lesson starts here.
# 
# Although we've got all of the traces and charts on the dashboard, there's still a bit of work to do. 
# 
# There is quite a lot of overlap for the place, crime and outcome names and the chart titles. We'll need to change the height of the dashboard, the domains of the charts, the position of the chart titles and the dashboard margins.
# 
# We also need to leave room for the dashboard title which we'll place last of all.

# ## Fitting the charts
# 
# There are a few things we can do to make sure the charts all fit:
# 2. Rotate the ticklabels
# 3. Increase the margins
# 4. Change the domain of the charts
# 1. Increase the height of the dashboard
# 
# If these don't work, then we need to think about changing the ticklabels for the categories.
# 
# Let's rotate the ticklabels on the x2 axis. I'm also going to set showgrid to False for the x1 axis:

# In[31]:

metCrimes['layout']['xaxis2'].update({'tickangle' : 45})
metCrimes['layout']['xaxis1'].update({'showgrid' : False})

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-10.png") 
 #

# We'll now change the left, bottom and right margins to accomodate the ticklabels:

# In[32]:

metCrimes['layout'].update({'margin' : {'l' : 180,
                                        'b' : 120,
                                        'r' : 90}})

pyo.iplot(metCrimes)

print(metCrimes)
py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-11.png") 
 #

# ### Updating chart titles and domains
# 
# First, let's increase the height of the dashboard:

# In[33]:

metCrimes['layout'].update({'height' : 1500})
pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-12.png") 
 #

# The title needs to move down on the first chart:

# In[34]:

metCrimes['layout']['annotations'][0]['y'] = 0.95


# We'll move the entire second chart up by changing the domain and y-position of the chart title:

# In[35]:

metCrimes['layout']['yaxis2'].update({'domain' : [0.51, 0.74]})
metCrimes['layout']['annotations'][1]['y'] = 0.73
pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-13.png") 
 #

# We'll do the same for the Crimes by location chart:

# In[36]:

metCrimes['layout']['annotations'][3]['y'] 


# In[37]:

metCrimes['layout']['yaxis4'].update({'domain' : [0.19, 0.27]})
metCrimes['layout']['annotations'][3]['y'] = 0.26
pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-14.png") 
 #

# ### Setting a title and changing hovermode
# 
# Finally, let's add in the title and set the hovermode to closest:

# In[38]:

metCrimes['layout']['annotations'].append({'text' : 'Crime recorded by the Metropolitan Police in 2016',
                                      'showarrow' : False,
                                       'xref' : 'paper',
                                      'x' : 0.5,
                                      'xanchor' : 'centre',
                                      'yref' : 'paper',
                                      'y' : 1,
                                      'yanchor' : 'top',
                                      'font' : {'size' : 24}})

metCrimes['layout'].update({'hovermode' : 'closest'})

pyo.iplot(metCrimes)


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\pyo.iplot-15.png") 
 #

# We've managed to fit a lot of data into this dashboard; let's push it to the Plotly cloud! You won't be able to see it clearly in the window that pops up, but click on 'full size' and zoom out to see it in all its glory!

# In[39]:

py.plot(metCrimes, filename="Crimes recorded by the Metropolitan Police", fileopt="overwrite")


py.image.save_as(metCrimes, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (2) - Crime in London\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've seen how to use the pandas groupby function to pull different stories out of a dataset. We've made a linear dashboard that presents a situation to our readers; namely that most crimes go unpunished, and then gives contextual information to help them understand the situation.
# 
# We've seen how to make the charts and titles fit on our dashboard by manipulating the domains and title positions.
# 
# In the next and final lesson, we'll make our most complex dashboard yet. We're going to look at football hooliganism in the UK. We're going to include a table, some pie charts and the layout will more complex than any we have made so far.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
