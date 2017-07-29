
# coding: utf-8

# # Dashboards (3) - Football Hooligans in the UK

# In this final lesson on dashboards, we're going to make our most complex dashboard yet.
# 
# We're going to make a dashboard which explores the phenomenon of football hooligans in the UK. I'm not a big football fan, but this is a very rich and interesting dataset which I'm sure you'll enjoy exploring.
# 
# There's a few things you should know before we begin. Football in the UK takes places over several leagues. The highest league is the Premiership, then the Championship, then yo have Leagues 1 and 2. Teams play each other twice, once in each home city. There are also parallel knockout competitions as well as international matches. Some people really love football.
# 
# Our dashboard will have 12 cells in 3 rows of 4 and we're going to use an offset-grid style which you can see in the image below.
# 
# The top-left chart will be a table showing the football clubs whose fans have the most and least banning orders, whilst the top right pie chart will show the breakdown of banning orders by competition.
# 
# The middle-left bar chart will show the number of arrests per 100,000 attendees, broken down by competition whilst the middle-right chart will show how the number of offenses has changed over time.
# 
# Finally, the bottom-left bar chart will show how the types of offenses change depending on the competition whilst the bottom-right pie chart will show the split of offenses by whether the team was playing at home or away.
# 
# The plan of our dashboard is shown below:

# <img src='http://richard-muir.com/images/db3.png'/>

# ## Module Imports

# In[5]:

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
# Because we're making a table, we need to get the <code>create_table()</code> function from the Figure Factory. You may remember that we have to put a table in a dashboard in a very specific way, without using the <code>make_subplots()</code>. 
# 
# Regardless, we'll import the make subplots to help us apply the complex layout of the dashboard.

# In[6]:

from plotly.tools import FigureFactory as FF, make_subplots


# In[7]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# I have prepared five datasets for us to use to make this dashboard. They all come from different tables in the same source dataset. Let's have a look at them before we start:

# #### Number of banning orders by club and league
# We'll use this dataset to create the table and pie chart in the top row of the dashboard. The charts will show respectively, the best and worst clubs for banning orders, and the best and worst competitions for banning orders.

# In[8]:

banningOrders = pd.read_csv('http://www.richard-muir.com/data/public/csv/BanningOrdersByClubAndLeague.csv',
                           index_col = 0)
banningOrders.head()


# #### Arrests per 100,000 attendees
# 
# We'll use this dataset to create the bar in the middle-right cell of the dashboard. This chart will show the number of arrests per 100,000 attendees broken down by competition.

# In[9]:

arrests = pd.read_csv('http://www.richard-muir.com/data/public/csv/ArrestsPer100kByLeague.csv',
                           index_col = 0)
arrests.head()


# #### Offenses by year and league
# 
# We'll use this dataset to create the line chart showing the time series of the number of offenses by league. This chart will go in the middle-right cell.

# In[10]:

offenses = pd.read_csv('http://www.richard-muir.com/data/public/csv/OffensesByYearAndLeague.csv',
                           index_col = 0)
offenses.head()


# #### Types of offense
# 
# This dataset shows the types of offense, broken down by competition. We'll use this to create the grouped bar chart in the bottom-left cell.

# In[11]:

typesOffense = pd.read_csv('http://www.richard-muir.com/data/public/csv/TypesOfOffensesByLeague.csv',
                           index_col = 0)
typesOffense.head()


# #### Arrests at home and away
# 
# This dataset shows the number of arrests at home, away and neutral football matches. We'll use this to create the pie chart in the bottom-right corner;

# In[12]:

homeAway = pd.read_csv('http://www.richard-muir.com/data/public/csv/ArrestsAtHomeAndAway.csv',
                           index_col = 0)
homeAway.head()


# ## (2) Making the table
# 
# If you're following along with the videos, this is where the second lesson starts.
# 
# We're going to make the table which shows the five best and worst performing clubs by the number of arrests their fans have. 
# 
# We need to make this table first, and then add all the other charts around it, but let's get the styling right for the table before we go any further.
# 
# We need to take the top and bottom five clubs from the dataset and save them as new DataFrames. The dataset is already sorted, so we can use <code>DataFrame.head()</code> and <code>DataFrame.tail()</code> to get the rows we need. 
# 
# We're also going to make a spacing row as its own DataFrame. We'll use this to separate the top and bottom five clubs to indicate to the reader that there are many more. 
# 
# We can then concatenate these three tables together and add in some spacing columns to reduce the size of the index column.

# In[13]:

top5 = banningOrders.head(5)
bottom5 = banningOrders.tail(5)
middle = pd.DataFrame.from_dict({'League' : ['...'],
                                'Club' : ['...'],
                                 'Banning Orders' : ['...']}).set_index('Club', drop = False)

bestWorst = pd.concat([top5, middle, bottom5])
bestWorst[''] = ''
bestWorst[' '] = ' '
bestWorst['  '] = '  '

bestWorst = bestWorst[['League','', 'Club',' ','Banning Orders', '  ']]
bestWorst


# Let's now make a Plotly table from this DataFrame. I'm calling it 'hooligans' because this object will eventually become our final dashboard.
# 
# We want to set an index column and an index title, and reduce the height_constant slightly to compress the table a little.

# In[14]:

hooligans = FF.create_table(bestWorst, index=True, index_title='Rank', height_constant = 20,)
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-0.png") 
 #

# ### Styling the table
# 
# Let's right-align the numbers in the Banning Orders column. We need to make sure that we don't select the numbers in the Rank index.
# 
# We'll do this by only taking annotations that have an x-position greater than 3. The annotations in the Club column are all positioned at x = 2.55, so anything to the left of this will be in the Banning Orders column.
# 

# In[15]:

hooligans['layout']['annotations'][10]


# In[16]:

for ann in hooligans['layout']['annotations']:
    if ann['x'] > 3:
        ann['xanchor'] = 'right'
        ann['x'] += 0.9
        
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-1.png") 
 #

# Let's now change the colour of the table. We're going to edit the colours used in the colorscale and z-index.
# 
# Rather than alternating colours for the rows, we'll set the worst five clubs to be coloured different shades of red, and the best five to be in green and white. 
# 
# We'll also change the colour of the index text to be black and the background colour of the index cells to white.

# In[17]:

#Changing the annotation colour:
for ann in hooligans['layout']['annotations']:
    if ann['font']['color'] == '#ffffff':
        ann['font']['color'] = 'black'
        
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-2.png") 
 #

# In order to change the colour of the cells we need to change the color_scale and the z-index of the cells.
# 
# Let's change the colour of the index row and column first:

# In[18]:

hooligans['data'][0]['colorscale'][0][1] = '#ffffff'
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-3.png") 
 #

# Here's the green and red colour we'll use:

# In[19]:

red = '#E61A1A'
green = '#1FAD39'


# Let's now change the z-values for each row, and attach the relevant colour to the colorscale.
# 
# We want each row to have a different z-index, but we'll leave the middle row in white.
# 
# The values for the z-index must be spread out so that the colour scale doesn't fade quickly from green to red, instead, the first 5 rows should be slightly different shades of green, whilst the last five should be slightly different shades of red.
# 
# By setting the z-index of the first five rows to be a small number, we're ensuring that these will be coloured green. The z-index of the last five rows is very large compared to the first. This means that the gradient of these rows will be applied properly

# In[20]:

for i, row in enumerate(hooligans['data'][0]['z']):
    # Setting the green rows
    if i != 0 and i < 6:
        hooligans['data'][0]['z'][i] = [0] + [i for j in range(6)]
    # Setting the white spacer row
    if i == 6:
        hooligans['data'][0]['z'][i] = [0, 0, 0, 0, 0, 0, 0]
    # setting the red rows
    if i > 6:
        hooligans['data'][0]['z'][i] = [0] + [i * 10 for j in range(6)]
    
hooligans['data'][0]['z']


# Now let's change the colour scale. We need to make sure that the rows with a z-index of 0 remain white, but that the other rows will change from green to red.
# 
# I've set the colorscale so that any rows with a z-index of 0 will be white, then, the rows with a low z-index will be green, and those with a high z-index will be red.
# 
# Setting the zmin and zmax makes sure that the colours will be represented properly:

# In[21]:

hooligans['data'][0]['colorscale'] = [[0, '#ffffff'], [0.1, green], [1, red]]
hooligans['data'][0]['zmin'] = 0
hooligans['data'][0]['zmax'] = 90

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-4.png") 
 #

# ## (3) Creating the dashboard object
# 
# For those following along with the videos, this is where the third lesson starts.
# 
# Now we've created the initial table we can build the dashboard around it. We did this in the previous section with a single chart, but we're now going to add five more. 
# 
# We have to add the other plots by updating the domains and anchor points of the additional axes. Let's use the <code>make_subplots()</code> function to create a template which we can then apply to our dashboard.

# In[22]:

template = make_subplots(rows = 3, cols = 4,
                        specs = [[{'colspan' : 3}, None, None, {}],
                                [{'colspan' : 2}, None, {'colspan' : 2}, None],
                                [{'colspan' : 3}, None, None, {}]])
template


# Let's take the layout from our subplots object and transplant that into our table to get the axis domains right. 
# 
# First we're going to update the axes for the table. Let's also expand the height and width to the full size of the dashboard:

# In[23]:

hooligans['layout']['xaxis'].update(template['layout']['xaxis1'])
hooligans['layout']['yaxis'].update(template['layout']['yaxis1'])

hooligans['layout'].update({'height' : 1000, 'width' : 1000})

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-5.png") 
 #

# Now, let's add in the other axes:

# In[24]:

for axis in range(2, 7):
    hooligans['layout'].update({'xaxis{}'.format(axis) : template['layout']['xaxis{}'.format(axis)]})
    hooligans['layout'].update({'yaxis{}'.format(axis) : template['layout']['yaxis{}'.format(axis)]})
    
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-6.png") 
 #

# # Adding the other charts
# 
# For those of you following the videos, this is where the fourth lesson starts.
# 
# Let's now add the other charts to our dashboard.
# 
# ## (4) Banning orders by competition
# 
# This pie chart will show the number of banning order by competition. We'll use the same DataFrame that we used for the table, but in order to get the total number of banning orders in each competition, we have to use the <code>pandas.DataFrame.groupby()</code> method to aggregate the data. We'll also sort the data in descending order.

# In[25]:

totalByCompetition = banningOrders.groupby(by='League',
                                          ).sum().sort_values(by='Banning Orders', 
                                                              ascending = False)
totalByCompetition


# Let's now make this pie chart. I'm going to set the colours for the six different competitions here as well. There are only four in this pie chart, but in the arrests per competition dataset, there are six. We want the colours for the competitions to be consistent throughout this dashboard.
# 
# We're also going to set the legendgroup so we can space the legend items out, and set an insidetextfont and outsidetextfont so that the segment labels are nice and big. We'll also set the hoverinfo to just show the label, percent and value.

# In[26]:

competitionColours = ["rgb(228,204,241)", "rgb(132,109,255)", "rgb(246,131,218)", 
                      "rgb(216,160,108)", "rgb(93,54,118)", "rgb(154,16,115)"]

banningOrdersPie = {'type' : 'pie',
                   'labels' : totalByCompetition.index,
                   'values' : totalByCompetition['Banning Orders'],
                    'hoverinfo' : 'label+percent+value',
                    'legendgroup' : 'banningOrderPie',
                    'insidetextfont' : {'size' : 16},
                    'outsidetextfont' : {'size' : 16},
                    'marker' : {'colors' : competitionColours[:4],
                               'line' : {'width' : 1,
                                        'color' : '#333'}},
                   'direction' : 'clockwise'}

pyo.iplot([banningOrdersPie])


py.image.save_as([banningOrdersPie], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-7.png") 
 #

# Now let's add this pie chart to the dashboard by setting the domain. I'm going to move it slightly to the right to prevent it overlapping the table.

# In[27]:

print(hooligans['layout']['xaxis2'])
print(hooligans['layout']['yaxis2'])


# In[28]:

banningOrdersPie.update({'domain' : {
                                'x' : [0.78, 1.0],
                                   'y' : [0.7111, 1.0]}
                        })
hooligans['data'].append(banningOrdersPie)
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-8.png") 
 #

# Now let's remove the axis marks from the axes under this pie chart and from the axes in the bottom-right cell; we're going to put a pie chart there later.

# In[29]:

blankAxis = {'showline' : False,
            'zeroline' : False,
            'ticks' : None,
            'showticklabels' : False,
            'showgrid' : False}

for axis in [2, 6]:
    hooligans['layout']['xaxis{}'.format(axis)].update(blankAxis)
    hooligans['layout']['yaxis{}'.format(axis)].update(blankAxis)
    
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-9.png") 
 #

# ## (5) Number of arrests per 100,000 attendees
# 
# If you're following the video lessons, the fifth lesson starts here.
# 
# Now let's add this bar chart showing, for each competition, the number of arrests per 100,000 attendees. We'll also plot a line showing the average so we can compare each competition to this average.
# 
# Let's sort the arrests DataFrame by descending value and create a text column so we can format the number to two decimal places.

# In[30]:

arrests = arrests.rename(columns={'Arrests per 100,000 attendees (2015-16)' : 'Arrests'},
              ).sort_values(by='Arrests', ascending = False)
arrests['text'] = arrests.apply(lambda x: "<b>{}</b><br>{:.2f} arrests per 100,000".format(x['Competition'], 
                                                                       x['Arrests']), 
                                axis = 1)
arrests


# We now need to remove the 'Total' row from the DataFrame - we don't want to plot this as a bar, but we do need to keep the information so we can plot a line as an annotation. 
# 
# I'm also going to change the text for 'National League National Division', 'Football League Trophy' and 'European competitions' to reduce the size of the ticklabel.

# In[31]:

total = arrests.loc[10, ['Competition','Arrests']]
total


# In[32]:

arrests = arrests[arrests['Competition'] != 'Total']

arrests.loc[4, 'Competition'] = 'National League'
arrests.loc[7, 'Competition'] = 'Football League'
arrests.loc[8, 'Competition'] = 'European'
arrests


# Let's now append this bar trace to the dashboard. We're going to colour red all of the bars that are above the average, and colour green those that are below. Only the last two are below the average (these are the two competitions with the largest attendance).
# 
# We need to anchor this bar trace to the <code>'x3'</code> and <code>'y3'</code> axes:

# In[33]:

hooligans['data'].append({'type' : 'bar',
                            'x' : arrests['Competition'],
                            'y' : arrests['Arrests'],
                             'opacity' : 0.6,
                             'text' : arrests['text'],
                             'hoverinfo' : 'text',
                             'showlegend' : False,
                            'marker' : {'color' : [red for i in range(8)] + [green, green],
                                       'line' : {'width' : 1,
                                                'color' : '#333'}},
                            'xaxis' : 'x3',
                            'yaxis' : 'y3'})

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-10.png") 
 #

# Now let's add the average line and an explaining annotation to the layout. We'll also need to anchor both of these to the <code>'x3'</code> and <code>'y3'</code> axes.
# 
# We're going to use an arrow to move the annotation away from the average line; it is difficult to read when the text is over the bars. By setting the <code>'ayref'</code> and <code>'ay'</code> parameters, we can move the annotation text away from the location where the arrow points. Because the <code>'ay'</code> value is negative, the annotation will move up relative to the point of the arrow.

# In[34]:

hooligans['layout']['annotations'].append({'text' : "<b>Average in all competitions: {:.2f}</b>".format(total['Arrests']),
                                             'showarrow' : True,
                                              'ayref' : 'y3',
                                              'ay' : -90,
                                              'xanchor' : 'middle',
                                             'x' : 5,
                                             'xref' : 'x3',
                                             'y' : total['Arrests'] * 1.05,
                                             'yref' : 'y3'})

hooligans['layout']['shapes'] = [{'type' : "line",
                                     'x0' : -0.5,
                                     'x1' : 10.5,
                                     'y0' : total['Arrests'],
                                     'y1' : total['Arrests'],
                                     'xref' : 'x3',
                                     'yref' : 'y3'}]

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-11.png") 
 #

# Let's now style the axes for these plots. I'm going to change the domain of the x-axis slightly to allow room for the y-axis title.

# In[35]:

hooligans['layout']['xaxis3'].update({'tickangle' : 45,
                                        'domain' : [0.05, 0.475]})
hooligans['layout']['yaxis3'].update({'title' : 'Arrests/100,000 attendees'})
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-12.png") 
 #

# ## (6) Adding the line chart showing the change in the number of arrests
# 
# For those of you following the video, the sixth lesson starts here.
# 
# We'll now add the line chart which will give us a time series of the number of arrests in each competition. 
# 
# First I'll rename the columns to just show the year. I'll do this with a dictionary comprehension. 
# 
# I'll also change the league name for 'National League National Division clubs', as well as removing the word 'clubs' from every row. It's possible to do this using the <code>pd.DataFrame.replace()</code> method, but I had problems getting this to work, so I went for a guaranteed method!

# In[36]:

offenses.rename(columns={col : col[:4] if col != 'League' else col for col in offenses.columns},
                inplace = True)

for loc in range(6):
    offenses.loc[loc, 'League'] = offenses.loc[loc, 'League'].replace(" clubs", '')
offenses.loc[4, 'League'] = 'National League'
offenses


# Finally, before we plot this, we're going to transpose the DataFrame to make it easier to plot. Let's set the index to be the League column, then call <code>DataFrame.T</code> to switch the row and column indexes round:

# In[37]:

offenses.set_index('League',drop = True, inplace = True)
offenses = offenses.T
offenses


# Now let's plot this line chart, not forgetting to set the xaxis and yaxis reference to x4 and y4 respectively.

# In[38]:

lines = []
years = list(range(2011, 2016))
for i, comp in enumerate(offenses.columns):
    lines.append({'type' : 'scatter',
                 'mode' : 'markers+lines',
                 'x' : years,
                 'y' : offenses[comp],
                  'marker' : {'color' : competitionColours[i],
                             'size' : 8,
                             'line' : {'width' : 1,
                                      'color' : '#333'}},
                  'name' : comp,
                  'legendgroup' : 'offensesLineChart',
                  'xaxis' : 'x4',
                  'yaxis' : 'y4'
})
    
hooligans['data'] += lines
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-13.png") 
 #

# Much as we did for the previous chart, I'll now change the domain on the xaxis to make space for a yaxis title:

# In[39]:

hooligans['layout']['xaxis4'].update({'domain' : [0.55, 1],})
hooligans['layout']['yaxis4'].update({'title' : 'Arrests'})

                                
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-14.png") 
 #

# ## (7) Types of offense by competition
# 
# The seventh video lesson starts here.
# 
# We'll now populate the bottom-left cell with a bar chart showing the number of each type of offense by competition.
# 
# We've got to prepare the DataFrame before we can plot it.
# 
# I'll firstly change the name of 'National League National Division'.
# 
# Next I'm going to set the index to the Competition column so we can more easily loop through the columns of offenses.
# 
# Next, we'll sort the columns from most offenses to least. For simplicity we'll only sort based on the 'Premier League' row. To sort the columns, we pass axis = 1 to the <code>sort_values()</code> function.

# In[40]:

#Changing name
typesOffense.loc[4, 'Competition'] = 'National League'

#Setting index
typesOffense.set_index('Competition', drop=True, inplace=True)


#Sorting the order of the columns
typesOffense.sort_values(by='Premier League', axis = 1, ascending = False, inplace = True)

typesOffense


# Now we'll combine the final 3 columns into an 'Other Offense' category:

# In[41]:

otherOffenses = ['Breach of banning order ','Racist and indecent chanting','Possession of an offensive weapon']
typesOffense['Other Offenses'] = typesOffense[otherOffenses].sum(axis = 1)

typesOffense.drop(otherOffenses, axis = 1, inplace = True)

typesOffense


# In order to combine the last three rows, we have to select them separately using the .loc indexer, then sum just those rows and create a DataFrame from them.
# 
# Next, we'll tranpose and rename the DataFrame before appending it to the original.
# 
# Finally, we'll drop the columns which we summed.

# In[42]:

competitions = ['Football League Trophy','Champions League and Europa League','Internationals']

#Making a DataFrame of the sum of the final three rows
otherComps = DataFrame(typesOffense.loc[competitions, :].sum(axis = 0))

#Transposing that DataFrame and renaming the index
otherComps = otherComps.T.rename(index={0 : 'Other Competitions'})

#Appending the new rows to the bottom, and dropping the three which comprise the new row
typesOffense = typesOffense.append(otherComps)
typesOffense.drop(competitions, axis=0, inplace = True)

typesOffense


# Finally, we'll get a list of the types of offense columns which we'll loop through to make the bar chart. We'll also use this list to add a text column for each type of offense.

# In[43]:

#List of columns
offenseCols = typesOffense.columns.tolist()

#Creating text columns
for col in offenseCols:
    typesOffense['{}_text'.format(col,)] = typesOffense[col].apply(lambda x: '<b>{}</b><br>{} offenses'.format(col, x))
typesOffense.head()


# First of all let's get a new colour scheme. The colour here will represent the different types of offense:

# In[44]:

offenseColours = ["rgb(250,46,85)", "rgb(136,20,72)", "rgb(252,178,199)", 
                  "rgb(250,46,85)", "rgb(249,13,160)", "rgb(202,98,133)", 
                  "rgb(154,42,6)", "rgb(240,126,79)", "rgb(83,12,153)"]


# Now we can add our bar traces to the dashboard. We'll put the competition type on the x-axis:

# In[45]:

bars = []
for i, off in enumerate(offenseCols):
    hooligans['data'].append({'type' : 'bar',
                'x' : typesOffense.index,
                'y' : typesOffense[off],
                 'text' : typesOffense['{}_text'.format(off)],
                 'name' : off,
                'opacity' : 0.7,
                 'hoverinfo' : 'text',
                 'legendgroup' : 'typesOffense',
                'marker' : {'color' : offenseColours[i],
                           'line' : {'width' : 0.5,
                                    'color' : '#333'}},
                 'xaxis' : 'x5',
                 'yaxis' : 'y5'
                })
    
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-15.png") 
 #

# Let's now change the domain of the x5 and y5 axes so we can see the ticklabels for this chart:

# In[46]:

hooligans['layout']['xaxis5'].update({'domain' : [0.06, 0.69]})

hooligans['layout']['yaxis5'].update({'domain' : [0.08, 0.26667],
                                        'title' : 'Number of offenses'})


pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-16.png") 
 #

# ## (8) Showing offenses by home and away
# 
# The eighth video lesson starts here.
# 
# We'll now make the final chart for this dashboard. We're going to make a pie chart that shows the breakdown of offenses by whether the supporter/offender's team was playing at home or away.
# 
# The data is below. First of all we need to sum the DataFrame. This will give us the totals for Home, Away and Neutral. It will also concatenate the club names together, but we'll drop this column. Next we'll rename the resulting column to N and finally, sort the DataFrame.

# In[47]:

homeAway = DataFrame(homeAway.sum())
homeAway = homeAway.drop(['Club'], axis = 0,
                        ).rename(columns={0 : 'N'},).sort_values(by='N', ascending=False)
homeAway


# Let's now create our pie chart. We'll use red for away, green for home and blue for neutral. I'll also set an insidetextfont and outsidetextfont so we can easily read the labels when the chart is on the dashboard.

# In[48]:

competitionColours = ["rgb(228,204,241)", "rgb(132,109,255)", "rgb(246,131,218)", 
                      "rgb(216,160,108)", "rgb(93,54,118)", "rgb(154,16,115)"]

homeAwayColours = [red, green, "rgb(132,109,255)"]

homeawayPie = {'type' : 'pie',
                   'labels' : homeAway.index,
                   'values' : homeAway['N'],
                   'hoverinfo' : 'label+percent+value',
                    'legendgroup' : 'homeAway',
                    'insidetextfont' : {'size' : 16},
                    'outsidetextfont' : {'size' : 16},
                    'marker' : {'colors' : homeAwayColours,
                               'line' : {'width' : 1,
                                        'color' : '#333'}},
                   'direction' : 'clockwise'}

pyo.iplot([homeawayPie])


py.image.save_as([homeawayPie], r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-17.png") 
 #

# Let's now append this to the dashboard; we'll need to set the domain of this pie chart to be the same as the x6 and y6 axes:

# In[49]:

print(hooligans['layout']['xaxis6']['domain'])
print(hooligans['layout']['yaxis6']['domain'])


# In[50]:

homeawayPie.update({'domain' : {
                                'x' : [0.78, 1.0],
                                   'y' : [0, 0.267]}
                        })
hooligans['data'].append(homeawayPie)
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-18.png") 
 #

# ## (9) Adding titles and finetuning the layout
# 
# The ninth and final video lesson starts here.
# 
# We've now added all the charts to our dashboard. There's still a few things to do before we finish:
# 1. Add chart titles
# 2. Add a title for the dashboard
# 3. Set hovermode to closest
# 4. Spread out the legend items
# 
# ### Adding chart titles
# 
# The easiest way to add chart titles is by using the make_subplots() function to generate a new subplot grid with titles. These titles are stored as annotations. We can then take the list of annotations from the subplot grid and put it straight into the dashboard.
# 

# In[51]:

template = make_subplots(rows = 3, cols = 4,
                        specs = [[{'colspan' : 3}, None, None, {}],
                                [{'colspan' : 2}, None, {'colspan' : 2}, None],
                                [{'colspan' : 3}, None, None, {}]],
                        subplot_titles = ['Most and least arrests by club',
                                         'Arrests by competition',
                                         'Arrests per 100,000 attendees',
                                         'Total arrests by season',
                                         'Types of offense',
                                         'Offenses at home and away'],
                        print_grid =False)
template['layout']['annotations']


# Let's add these annotations to our dashboard. We'll also add in our dashboard title.
# 
# We'll probably have to move the annotations about and change the domain of some of the charts to prevent any overlap, but let's take a look at the dashboard first:

# In[52]:

titleAnn = [{'text' : 'Football Hooligans in the UK',
           'showarrow' : False,
           'xref' : 'paper',
           'yref' : 'paper',
           'x' : 0.5,
           'y' : 1,
           'xanchor' : 'center',
           'yanchor' : 'bottom',
           'font' : {'size' : 30}}]

hooligans['layout']['annotations'] += (template['layout']['annotations'] + titleAnn)
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-19.png") 
 #

# So you can see that we've got a little bit of work to do to move the annotations and charts around so they don't overlap. We'll start at the top and move the table down by changing the domain of the y1 axis. We'll also change the domain of the pie trace so that it stays aligned with the table.

# In[53]:

hooligans['layout']['yaxis'].update({'domain' : [0.67333, 0.95]})
hooligans['data'][1]['domain'].update({'y' : [0.651, 0.95]})

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-20.png") 
 #

# Let's now move the dashboard, table and arrests pie chart titles down, and the other titles up.
# 
# These title annotations were the last seven we added to the dashboard, so they should be at the end of the list of annotations.
# 
# We know that we have to move the first two chart titles down, and the rest of the chart titles up a bit. We also have to move the dashboard title annotation (the last one we added) down:

# In[54]:

for i, ann in enumerate(hooligans['layout']['annotations'][-7:]):
    if i in [0, 1]:
        ann['y'] -= 0.05
    elif i == 6:
        ann['y'] -=0.025
    else:
        ann['y'] += 0.03
        
pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-21.png") 
 #    


# Let's now change the hovermode, legend position and tracegroupgap. We're not going to get the legend items to line up perfectly with the charts, but we should be able to spread them out enough to make it clear.

# In[55]:

hooligans['layout'].update({'hovermode' : 'closest'})
hooligans['layout']['legend'].update({'tracegroupgap' : 160})

pyo.iplot(hooligans)


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\pyo.iplot-22.png") 
 #

# Let's send our dashboard to the Plotly cloud:

# In[56]:

#py.plot(hooligans, filename="Football hooligans in the UK", fileopt = 'overwrite')


py.image.save_as(hooligans, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(10) Dashboards\Notebooks\images\Dashboards (3) - Football Hooligans in the UK\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this last lesson ih the course we've brought together everything that we previously learnt to create our most complex dashboard yet. We've included tables, pie charts, bar charts, line charts, chart titles and a dashboard title.
# 
# I really hope you've enjoyed this course.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
