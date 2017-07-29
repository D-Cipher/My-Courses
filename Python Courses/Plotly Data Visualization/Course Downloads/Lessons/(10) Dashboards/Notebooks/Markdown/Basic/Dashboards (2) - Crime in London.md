
# Dashboards (2) - Crime in London

In this second lesson on dashboards we're going to visualise some data about crime in London. The dataset we'll be using contains information on all the different crimes recorded by the Metropolitan police during 2016.

This is a 40mb raw dataset, so we'll be using the pandas groupby() function to summarise the data in different ways.

Our dashboard will have seven rows; the first two charts will occupy two rows each, whilst the last three charts will have one each.

The final three charts will show simple summaries of the data and will serve to give contextual information about the data to the data to help our readers understand the situation better. The first two charts we make will be a little more complex and are the focal point of this visualisation.

We'll create the contextual charts first, as doing so will help us to familiarise ourselves with the dataset.

First of all we'll use a line chart to show how the number of crimes changes each month.

Next, we'll create a bar chart showing the number of crimes in each location.

The next step will be to create another bar chart, this one showing the number of each different type of crime.

Now for the more complex charts . . . These will be a special type of scatterplot which allows us to show the interaction between different categories.

The first chart will show, for each type of crime, what is the most common outcome.

The second chart will show for each location, what is the most common type of crime.


<img src='http://richard-muir.com/images/db2.png'/>



#### New Modules:

We'll need the make_subplots() module as well as the Python datetime module to help us get the month names from the dates:



from plotly.tools import make_subplots
import datetime



```python

 
```





## Getting the data

This dataset is a 40mb file containing individual records for the crimes recorded by the Metropolitan Police in 2016. It might take a little while to download.


```python
crimes = pd.read_csv('http://richard-muir.com/data/public/csv/MetPoliceCrimeStats.csv',
                    index_col = 0)
crimes.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
      <th>Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01</td>
      <td>Court case unable to proceed</td>
      <td>2016-01</td>
      <td>Violence and sexual offences</td>
      <td>Enfield</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Criminal damage and arson</td>
      <td>Lambeth</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Theft from the person</td>
      <td>Lambeth</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Violence and sexual offences</td>
      <td>Lambeth</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Theft from the person</td>
      <td>Lambeth</td>
    </tr>
  </tbody>
</table>
</div>



## Making the subplots object

Let's now get the template for our dashboard. We want to combine the first two rows, and the third and fourth rows:


```python
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

```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]
           |       
    [ (3,1) x2,y2 ]
           |       
    [ (5,1) x3,y3 ]
    [ (6,1) x4,y4 ]
    [ (7,1) x5,y5 ]
    
    

## Line chart of crimes by month

Let's now group our dataset by 'Crime Month'. We'll count the number of observations in each month to give us the quantity of crimes which ocurred in that month. By setting <code>as_index = False</code> the column which is being grouped is not stored as the index.

Because we're calling <code>.count()</code> on the groupby object, this returns a count of the number of rows within each group. We can use any column as tghe y-values in our chart.


```python
crimesByMonth = crimes.groupby('Crime Month', as_index = False).count()
crimesByMonth
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime Month</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime type</th>
      <th>Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-02</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-04</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-05</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-06</td>
      <td>41860</td>
      <td>41860</td>
      <td>41860</td>
      <td>41860</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-07</td>
      <td>43823</td>
      <td>43823</td>
      <td>43823</td>
      <td>43823</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016-08</td>
      <td>39992</td>
      <td>39992</td>
      <td>39992</td>
      <td>39992</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016-09</td>
      <td>37803</td>
      <td>37803</td>
      <td>37803</td>
      <td>37803</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016-10</td>
      <td>36541</td>
      <td>36541</td>
      <td>36541</td>
      <td>36541</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016-11</td>
      <td>28835</td>
      <td>28835</td>
      <td>28835</td>
      <td>28835</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016-12</td>
      <td>14669</td>
      <td>14669</td>
      <td>14669</td>
      <td>14669</td>
    </tr>
  </tbody>
</table>
</div>



Let's add a text column which will show the month name and the number of crimes. First of all we need to convert the Crime Month column to a datetime using the <code>pd.to_datetime()</code> function. We have to tell this function in which format the date is.

<code>"%Y-%m"</code> means that the date string is a four-digit year, followed by a hyphen, followed by a two-digit month.

Then, we'll use the <code>strftime</code> function to get the month name from our datetime object. <code>"%B"</code> is the datetime format for the month name.


```python
crimesByMonth['Crime Month'] = pd.to_datetime(crimesByMonth['Crime Month'], format='%Y-%m')

crimesByMonth['Month'] = crimesByMonth['Crime Month'].apply(lambda x: x.strftime("%B"))
crimesByMonth.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime Month</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-01</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
      <td>January</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-02-01</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
      <td>February</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-01</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
      <td>March</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-04-01</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
      <td>April</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-05-01</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
      <td>May</td>
    </tr>
  </tbody>
</table>
</div>




```python
crimesByMonth['text'] = crimesByMonth.apply(lambda x: "<b>{}:</b><br>{:,} crimes".format(x['Month'], x['Crime type']), axis = 1)
crimesByMonth.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime Month</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Month</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01-01</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
      <td>40293</td>
      <td>January</td>
      <td>&lt;b&gt;January:&lt;/b&gt;&lt;br&gt;40,293 crimes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-02-01</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
      <td>39376</td>
      <td>February</td>
      <td>&lt;b&gt;February:&lt;/b&gt;&lt;br&gt;39,376 crimes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-01</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
      <td>40524</td>
      <td>March</td>
      <td>&lt;b&gt;March:&lt;/b&gt;&lt;br&gt;40,524 crimes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-04-01</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
      <td>39700</td>
      <td>April</td>
      <td>&lt;b&gt;April:&lt;/b&gt;&lt;br&gt;39,700 crimes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-05-01</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
      <td>42753</td>
      <td>May</td>
      <td>&lt;b&gt;May:&lt;/b&gt;&lt;br&gt;42,753 crimes</td>
    </tr>
  </tbody>
</table>
</div>



Let's create this line chart outside of the subplots object, then, when we're happy with it, we can use the append_trace() function to put it in our dashboard.

Because each of the charts will only have a single trace, we don't need a legend for this dashboard. I'll set 'showlegend' to False on every trace:


```python
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

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-0.png)```





I'm happy with that, but I have noticed that the y-axis doesn't start from 0. This gives the false impression that crime fell almost to 0 in December.

Let's append the trace and change the range of the y2 axis. We'll also increase the height of the dashboard to make it easier to build.


```python
metCrimes.append_trace(monthCrime, 5, 1)

metCrimes['layout']['yaxis3'].update({'range' : [0, max(crimesByMonth['Area']) * 1.05]})
metCrimes['layout'].update({'height' : 1000})

pyo.iplot(metCrimes)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-1.png)``





## (2) Number of crimes in each location

If you're using the videos, the second lesson starts here

To get the number of crimes in each location we must group by the 'Area' column and count the number of rows in each group:


```python
areaCrime = crimes.groupby('Area', as_index=False).count()
areaCrime.head(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adur</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ashford</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Aylesbury Vale</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Babergh</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Barking and Dagenham</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Barnet</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Basildon</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bassetlaw</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bedford</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bexley</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
    </tr>
  </tbody>
</table>
</div>



The rows can clearly be split into two groups; those which have thousands of crimes, and are therefore in London, and those which only have a few crimes, and are therefore not in London. 

Let's recode the areas that aren't in London, and groupby again to get 'Not in London' as a separate Area category. We'll have to call <code>.sum()</code> on the groupby object:


```python
def inLondon(row):
    if row['Outcome Month'] > 1000: 
        return row['Area']
    else: 
        return 'Not in London'

areaCrime['Area'] = areaCrime.apply(inLondon, axis = 1)
areaCrime.head(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Not in London</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Not in London</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Not in London</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Not in London</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Barking and Dagenham</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Barnet</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Not in London</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Not in London</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Not in London</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bexley</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
    </tr>
  </tbody>
</table>
</div>




```python
areaCrime = areaCrime.groupby('Area', as_index = False).sum()
areaCrime
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Barking and Dagenham</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Barnet</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bexley</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Brent</td>
      <td>15911</td>
      <td>15911</td>
      <td>15911</td>
      <td>15911</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bromley</td>
      <td>12499</td>
      <td>12499</td>
      <td>12499</td>
      <td>12499</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Camden</td>
      <td>17274</td>
      <td>17274</td>
      <td>17274</td>
      <td>17274</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Croydon</td>
      <td>17711</td>
      <td>17711</td>
      <td>17711</td>
      <td>17711</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Ealing</td>
      <td>17265</td>
      <td>17265</td>
      <td>17265</td>
      <td>17265</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Enfield</td>
      <td>14058</td>
      <td>14058</td>
      <td>14058</td>
      <td>14058</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Greenwich</td>
      <td>14483</td>
      <td>14483</td>
      <td>14483</td>
      <td>14483</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Hackney</td>
      <td>16877</td>
      <td>16877</td>
      <td>16877</td>
      <td>16877</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hammersmith and Fulham</td>
      <td>12694</td>
      <td>12694</td>
      <td>12694</td>
      <td>12694</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Haringey</td>
      <td>16286</td>
      <td>16286</td>
      <td>16286</td>
      <td>16286</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Harrow</td>
      <td>7579</td>
      <td>7579</td>
      <td>7579</td>
      <td>7579</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Havering</td>
      <td>9961</td>
      <td>9961</td>
      <td>9961</td>
      <td>9961</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Hillingdon</td>
      <td>15088</td>
      <td>15088</td>
      <td>15088</td>
      <td>15088</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Hounslow</td>
      <td>13524</td>
      <td>13524</td>
      <td>13524</td>
      <td>13524</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Islington</td>
      <td>16810</td>
      <td>16810</td>
      <td>16810</td>
      <td>16810</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Kensington and Chelsea</td>
      <td>12332</td>
      <td>12332</td>
      <td>12332</td>
      <td>12332</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Kingston upon Thames</td>
      <td>6578</td>
      <td>6578</td>
      <td>6578</td>
      <td>6578</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Lambeth</td>
      <td>20459</td>
      <td>20459</td>
      <td>20459</td>
      <td>20459</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Lewisham</td>
      <td>15397</td>
      <td>15397</td>
      <td>15397</td>
      <td>15397</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Merton</td>
      <td>7408</td>
      <td>7408</td>
      <td>7408</td>
      <td>7408</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Newham</td>
      <td>17134</td>
      <td>17134</td>
      <td>17134</td>
      <td>17134</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Not in London</td>
      <td>760</td>
      <td>760</td>
      <td>760</td>
      <td>760</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Redbridge</td>
      <td>11871</td>
      <td>11871</td>
      <td>11871</td>
      <td>11871</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Richmond upon Thames</td>
      <td>6235</td>
      <td>6235</td>
      <td>6235</td>
      <td>6235</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Southwark</td>
      <td>18499</td>
      <td>18499</td>
      <td>18499</td>
      <td>18499</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Sutton</td>
      <td>6283</td>
      <td>6283</td>
      <td>6283</td>
      <td>6283</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Tower Hamlets</td>
      <td>17460</td>
      <td>17460</td>
      <td>17460</td>
      <td>17460</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Waltham Forest</td>
      <td>12221</td>
      <td>12221</td>
      <td>12221</td>
      <td>12221</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Wandsworth</td>
      <td>14205</td>
      <td>14205</td>
      <td>14205</td>
      <td>14205</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Westminster</td>
      <td>28748</td>
      <td>28748</td>
      <td>28748</td>
      <td>28748</td>
    </tr>
  </tbody>
</table>
</div>



That seems to have worked correctly. I'm not an expert on the London areas, but there seems to be nothing out of place. Let's sort this data from largest to smallest and plot a bar chart:


```python
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
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-2.png)`





OK, that's looking pretty good; let's append it to the dashboard. I'm going to rotate the ticks on the x-axis to make them easier to read.


```python
metCrimes.append_trace(areaBar, row = 6, col = 1)

metCrimes['layout']['xaxis4'].update({'tickangle' : 45})

pyo.iplot(metCrimes)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-3.png)





## (3) Types of crime

If you're following along with the videos, the third lesson starts here.

Now let's make another bar chart showing the number of different types of crime. We'll once again use the groupby method to get our data:


```python
crimeTypes = crimes.groupby('Crime type', as_index=False).count()
crimeTypes.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>8531</td>
      <td>8531</td>
      <td>8531</td>
      <td>8531</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Burglary</td>
      <td>31245</td>
      <td>31245</td>
      <td>31245</td>
      <td>31245</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Criminal damage and arson</td>
      <td>30280</td>
      <td>30280</td>
      <td>30280</td>
      <td>30280</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Drugs</td>
      <td>31644</td>
      <td>31644</td>
      <td>31644</td>
      <td>31644</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Other crime</td>
      <td>7205</td>
      <td>7205</td>
      <td>7205</td>
      <td>7205</td>
    </tr>
  </tbody>
</table>
</div>



Let's sort this from largest to smallest and make another bar chart:


```python
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
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-4.png)




That's looking good. I'll now append it to the dashboard:


```python
metCrimes.append_trace(crimeBar, row = 7, col = 1)

pyo.iplot(metCrimes)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-5.png)



## (4) Type of crime and location

If you're following along with the videos, the fourth lesson starts here.

We're going to make a special kind of scatterplot to show the type of crime by the location. The x-values will show the type of crime, whilst the y-values will show the location. The size of the marker will display how many crimes of a type happened at a location.

We first need to group the DataFrame by type and location:


```python
typeLoc = crimes.groupby(['Crime type', 'Area'], as_index=False).count()
typeLoc.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>Barking and Dagenham</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>Barnet</td>
      <td>106</td>
      <td>106</td>
      <td>106</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>Bexley</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>Brent</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>Bromley</td>
      <td>102</td>
      <td>102</td>
      <td>102</td>
    </tr>
  </tbody>
</table>
</div>



Now we need to find out which locations are outside London. We did this earlier for the bar chart showing the number of crimes by area, but this time, rather than recoding the Area column we must instead make a new column showing whether the area is in London or not.

We'll create a new column by applying the inLondon() function:


```python
locationRecode = crimes.groupby(['Area'], as_index=False).count()
locationRecode['Recoded Area'] = locationRecode.apply(inLondon, axis = 1)
locationRecode.head(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
      <th>Recoded Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adur</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ashford</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Aylesbury Vale</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Babergh</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Barking and Dagenham</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
      <td>10401</td>
      <td>Barking and Dagenham</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Barnet</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
      <td>14321</td>
      <td>Barnet</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Basildon</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bassetlaw</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bedford</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bexley</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
      <td>7837</td>
      <td>Bexley</td>
    </tr>
  </tbody>
</table>
</div>



Now let's merge this recoded DataFrame onto our grouped DataFrame using the <code>DataFrame.merge()</code> method.

I'm only selecting the Recoded Area and Area columns from the DataFrame.

We must specify a key common to each DataFrame as the merge key. We're also using a 'left join'. This means that we discard any observations from the locationRecode DataFrame which aren't in the typeLoc DataFrame.


```python
typeLoc = typeLoc.merge(locationRecode[['Area','Recoded Area']], how = 'left', on='Area')
typeLoc.head(20)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Recoded Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>Barking and Dagenham</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>Barking and Dagenham</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>Barnet</td>
      <td>106</td>
      <td>106</td>
      <td>106</td>
      <td>Barnet</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>Bexley</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>Bexley</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>Brent</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>Brent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>Bromley</td>
      <td>102</td>
      <td>102</td>
      <td>102</td>
      <td>Bromley</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bicycle theft</td>
      <td>Camden</td>
      <td>499</td>
      <td>499</td>
      <td>499</td>
      <td>Camden</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Bicycle theft</td>
      <td>Central Bedfordshire</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bicycle theft</td>
      <td>City of London</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bicycle theft</td>
      <td>Croydon</td>
      <td>129</td>
      <td>129</td>
      <td>129</td>
      <td>Croydon</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bicycle theft</td>
      <td>Dartford</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bicycle theft</td>
      <td>Ealing</td>
      <td>276</td>
      <td>276</td>
      <td>276</td>
      <td>Ealing</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bicycle theft</td>
      <td>Elmbridge</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Not in London</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Bicycle theft</td>
      <td>Enfield</td>
      <td>131</td>
      <td>131</td>
      <td>131</td>
      <td>Enfield</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Bicycle theft</td>
      <td>Greenwich</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>Greenwich</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Bicycle theft</td>
      <td>Hackney</td>
      <td>700</td>
      <td>700</td>
      <td>700</td>
      <td>Hackney</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Bicycle theft</td>
      <td>Hammersmith and Fulham</td>
      <td>400</td>
      <td>400</td>
      <td>400</td>
      <td>Hammersmith and Fulham</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Bicycle theft</td>
      <td>Haringey</td>
      <td>259</td>
      <td>259</td>
      <td>259</td>
      <td>Haringey</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Bicycle theft</td>
      <td>Harrow</td>
      <td>80</td>
      <td>80</td>
      <td>80</td>
      <td>Harrow</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Bicycle theft</td>
      <td>Havering</td>
      <td>78</td>
      <td>78</td>
      <td>78</td>
      <td>Havering</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Bicycle theft</td>
      <td>Hillingdon</td>
      <td>174</td>
      <td>174</td>
      <td>174</td>
      <td>Hillingdon</td>
    </tr>
  </tbody>
</table>
</div>



So we can see that we now have a new column which adds a 'Not in London' description for those areas which aren't in the jurisdiction of the Metropolitan police (the City of London is a strange example of this!). Let's now drop the old Area column, rename the 'Recoded Area' to 'Area', and do the group by again but calling <code>.sum()</code> rather than <code>.count()</code> (as we did earlier):


```python
typeLoc = typeLoc.drop(['Area'], axis = 1).rename(columns={'Recoded Area' : 'Area'})
typeLoc.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>Barking and Dagenham</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>106</td>
      <td>106</td>
      <td>106</td>
      <td>Barnet</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>Bexley</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>Brent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>102</td>
      <td>102</td>
      <td>102</td>
      <td>Bromley</td>
    </tr>
  </tbody>
</table>
</div>




```python
typeLoc = typeLoc.groupby(['Crime type','Area'], as_index=False).sum()
typeLoc
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>Barking and Dagenham</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>Barnet</td>
      <td>106</td>
      <td>106</td>
      <td>106</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>Bexley</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>Brent</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>Bromley</td>
      <td>102</td>
      <td>102</td>
      <td>102</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bicycle theft</td>
      <td>Camden</td>
      <td>499</td>
      <td>499</td>
      <td>499</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Bicycle theft</td>
      <td>Croydon</td>
      <td>129</td>
      <td>129</td>
      <td>129</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bicycle theft</td>
      <td>Ealing</td>
      <td>276</td>
      <td>276</td>
      <td>276</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bicycle theft</td>
      <td>Enfield</td>
      <td>131</td>
      <td>131</td>
      <td>131</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bicycle theft</td>
      <td>Greenwich</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bicycle theft</td>
      <td>Hackney</td>
      <td>700</td>
      <td>700</td>
      <td>700</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bicycle theft</td>
      <td>Hammersmith and Fulham</td>
      <td>400</td>
      <td>400</td>
      <td>400</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Bicycle theft</td>
      <td>Haringey</td>
      <td>259</td>
      <td>259</td>
      <td>259</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Bicycle theft</td>
      <td>Harrow</td>
      <td>80</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Bicycle theft</td>
      <td>Havering</td>
      <td>78</td>
      <td>78</td>
      <td>78</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Bicycle theft</td>
      <td>Hillingdon</td>
      <td>174</td>
      <td>174</td>
      <td>174</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Bicycle theft</td>
      <td>Hounslow</td>
      <td>303</td>
      <td>303</td>
      <td>303</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Bicycle theft</td>
      <td>Islington</td>
      <td>499</td>
      <td>499</td>
      <td>499</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Bicycle theft</td>
      <td>Kensington and Chelsea</td>
      <td>233</td>
      <td>233</td>
      <td>233</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Bicycle theft</td>
      <td>Kingston upon Thames</td>
      <td>140</td>
      <td>140</td>
      <td>140</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Bicycle theft</td>
      <td>Lambeth</td>
      <td>482</td>
      <td>482</td>
      <td>482</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Bicycle theft</td>
      <td>Lewisham</td>
      <td>169</td>
      <td>169</td>
      <td>169</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bicycle theft</td>
      <td>Merton</td>
      <td>165</td>
      <td>165</td>
      <td>165</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Bicycle theft</td>
      <td>Newham</td>
      <td>233</td>
      <td>233</td>
      <td>233</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Bicycle theft</td>
      <td>Not in London</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Bicycle theft</td>
      <td>Redbridge</td>
      <td>96</td>
      <td>96</td>
      <td>96</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Bicycle theft</td>
      <td>Richmond upon Thames</td>
      <td>257</td>
      <td>257</td>
      <td>257</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Bicycle theft</td>
      <td>Southwark</td>
      <td>566</td>
      <td>566</td>
      <td>566</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bicycle theft</td>
      <td>Sutton</td>
      <td>68</td>
      <td>68</td>
      <td>68</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Bicycle theft</td>
      <td>Tower Hamlets</td>
      <td>660</td>
      <td>660</td>
      <td>660</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>399</th>
      <td>Violence and sexual offences</td>
      <td>Brent</td>
      <td>5300</td>
      <td>5300</td>
      <td>5300</td>
    </tr>
    <tr>
      <th>400</th>
      <td>Violence and sexual offences</td>
      <td>Bromley</td>
      <td>4060</td>
      <td>4060</td>
      <td>4060</td>
    </tr>
    <tr>
      <th>401</th>
      <td>Violence and sexual offences</td>
      <td>Camden</td>
      <td>4153</td>
      <td>4153</td>
      <td>4153</td>
    </tr>
    <tr>
      <th>402</th>
      <td>Violence and sexual offences</td>
      <td>Croydon</td>
      <td>6471</td>
      <td>6471</td>
      <td>6471</td>
    </tr>
    <tr>
      <th>403</th>
      <td>Violence and sexual offences</td>
      <td>Ealing</td>
      <td>5681</td>
      <td>5681</td>
      <td>5681</td>
    </tr>
    <tr>
      <th>404</th>
      <td>Violence and sexual offences</td>
      <td>Enfield</td>
      <td>4829</td>
      <td>4829</td>
      <td>4829</td>
    </tr>
    <tr>
      <th>405</th>
      <td>Violence and sexual offences</td>
      <td>Greenwich</td>
      <td>5322</td>
      <td>5322</td>
      <td>5322</td>
    </tr>
    <tr>
      <th>406</th>
      <td>Violence and sexual offences</td>
      <td>Hackney</td>
      <td>5177</td>
      <td>5177</td>
      <td>5177</td>
    </tr>
    <tr>
      <th>407</th>
      <td>Violence and sexual offences</td>
      <td>Hammersmith and Fulham</td>
      <td>3409</td>
      <td>3409</td>
      <td>3409</td>
    </tr>
    <tr>
      <th>408</th>
      <td>Violence and sexual offences</td>
      <td>Haringey</td>
      <td>5171</td>
      <td>5171</td>
      <td>5171</td>
    </tr>
    <tr>
      <th>409</th>
      <td>Violence and sexual offences</td>
      <td>Harrow</td>
      <td>2672</td>
      <td>2672</td>
      <td>2672</td>
    </tr>
    <tr>
      <th>410</th>
      <td>Violence and sexual offences</td>
      <td>Havering</td>
      <td>3609</td>
      <td>3609</td>
      <td>3609</td>
    </tr>
    <tr>
      <th>411</th>
      <td>Violence and sexual offences</td>
      <td>Hillingdon</td>
      <td>4505</td>
      <td>4505</td>
      <td>4505</td>
    </tr>
    <tr>
      <th>412</th>
      <td>Violence and sexual offences</td>
      <td>Hounslow</td>
      <td>4399</td>
      <td>4399</td>
      <td>4399</td>
    </tr>
    <tr>
      <th>413</th>
      <td>Violence and sexual offences</td>
      <td>Islington</td>
      <td>4636</td>
      <td>4636</td>
      <td>4636</td>
    </tr>
    <tr>
      <th>414</th>
      <td>Violence and sexual offences</td>
      <td>Kensington and Chelsea</td>
      <td>2590</td>
      <td>2590</td>
      <td>2590</td>
    </tr>
    <tr>
      <th>415</th>
      <td>Violence and sexual offences</td>
      <td>Kingston upon Thames</td>
      <td>1926</td>
      <td>1926</td>
      <td>1926</td>
    </tr>
    <tr>
      <th>416</th>
      <td>Violence and sexual offences</td>
      <td>Lambeth</td>
      <td>6331</td>
      <td>6331</td>
      <td>6331</td>
    </tr>
    <tr>
      <th>417</th>
      <td>Violence and sexual offences</td>
      <td>Lewisham</td>
      <td>5489</td>
      <td>5489</td>
      <td>5489</td>
    </tr>
    <tr>
      <th>418</th>
      <td>Violence and sexual offences</td>
      <td>Merton</td>
      <td>2472</td>
      <td>2472</td>
      <td>2472</td>
    </tr>
    <tr>
      <th>419</th>
      <td>Violence and sexual offences</td>
      <td>Newham</td>
      <td>5718</td>
      <td>5718</td>
      <td>5718</td>
    </tr>
    <tr>
      <th>420</th>
      <td>Violence and sexual offences</td>
      <td>Not in London</td>
      <td>254</td>
      <td>254</td>
      <td>254</td>
    </tr>
    <tr>
      <th>421</th>
      <td>Violence and sexual offences</td>
      <td>Redbridge</td>
      <td>3976</td>
      <td>3976</td>
      <td>3976</td>
    </tr>
    <tr>
      <th>422</th>
      <td>Violence and sexual offences</td>
      <td>Richmond upon Thames</td>
      <td>1906</td>
      <td>1906</td>
      <td>1906</td>
    </tr>
    <tr>
      <th>423</th>
      <td>Violence and sexual offences</td>
      <td>Southwark</td>
      <td>5505</td>
      <td>5505</td>
      <td>5505</td>
    </tr>
    <tr>
      <th>424</th>
      <td>Violence and sexual offences</td>
      <td>Sutton</td>
      <td>2341</td>
      <td>2341</td>
      <td>2341</td>
    </tr>
    <tr>
      <th>425</th>
      <td>Violence and sexual offences</td>
      <td>Tower Hamlets</td>
      <td>5419</td>
      <td>5419</td>
      <td>5419</td>
    </tr>
    <tr>
      <th>426</th>
      <td>Violence and sexual offences</td>
      <td>Waltham Forest</td>
      <td>4591</td>
      <td>4591</td>
      <td>4591</td>
    </tr>
    <tr>
      <th>427</th>
      <td>Violence and sexual offences</td>
      <td>Wandsworth</td>
      <td>4200</td>
      <td>4200</td>
      <td>4200</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Violence and sexual offences</td>
      <td>Westminster</td>
      <td>5628</td>
      <td>5628</td>
      <td>5628</td>
    </tr>
  </tbody>
</table>
<p>429 rows × 5 columns</p>
</div>



Before we plot, let's make a text column:


```python
typeLoc['text'] = typeLoc.apply(lambda x: "<b>{}</b><br>{}<br>{:,}".format(x['Area'], 
                                                                           x['Crime type'],
                                                                          x['Outcome Month']),
                               axis = 1)
typeLoc.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>Barking and Dagenham</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>&lt;b&gt;Barking and Dagenham&lt;/b&gt;&lt;br&gt;Bicycle theft&lt;b...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>Barnet</td>
      <td>106</td>
      <td>106</td>
      <td>106</td>
      <td>&lt;b&gt;Barnet&lt;/b&gt;&lt;br&gt;Bicycle theft&lt;br&gt;106</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>Bexley</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>&lt;b&gt;Bexley&lt;/b&gt;&lt;br&gt;Bicycle theft&lt;br&gt;77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>Brent</td>
      <td>196</td>
      <td>196</td>
      <td>196</td>
      <td>&lt;b&gt;Brent&lt;/b&gt;&lt;br&gt;Bicycle theft&lt;br&gt;196</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>Bromley</td>
      <td>102</td>
      <td>102</td>
      <td>102</td>
      <td>&lt;b&gt;Bromley&lt;/b&gt;&lt;br&gt;Bicycle theft&lt;br&gt;102</td>
    </tr>
  </tbody>
</table>
</div>



So we've got over 400 observations to plot. Let's make our scatterplot. We're going to set the marker size to show the number of crimes of a particular type in each area. We need to remember to set the <code>sizeref</code> and <code>sizemin</code> to appropriate values.


```python
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
```



![pyo.iplot-6](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-6.png)


So there's quite a lot of information there. Let's add this chart to the dashboard:


```python
metCrimes.append_trace(typeLocScatter, row = 3, col = 1)

pyo.iplot(metCrimes)
```




![pyo.iplot-7](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-7.png)

## (5) Types of crime by outcome

If you're following along with the videos the fifth lesson starts here.

We'll now make the final chart for this dashboard. This chart will show for each type of crime, how many crimes of that type resulted in a specifc outcome. 

There are many different kinds of outcome. We first of all need to recode all of the different outcomes into fewer categories to allow us to plot them more easily.

We'll apply the function below to recode the different outcomes:


```python
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
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Crime type</th>
      <th>Area</th>
      <th>Broad Outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-01</td>
      <td>Court case unable to proceed</td>
      <td>2016-01</td>
      <td>Violence and sexual offences</td>
      <td>Enfield</td>
      <td>No judicial outcome</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Criminal damage and arson</td>
      <td>Lambeth</td>
      <td>No judicial outcome</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Theft from the person</td>
      <td>Lambeth</td>
      <td>No judicial outcome</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Violence and sexual offences</td>
      <td>Lambeth</td>
      <td>No judicial outcome</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-01</td>
      <td>Investigation complete; no suspect identified</td>
      <td>2016-01</td>
      <td>Theft from the person</td>
      <td>Lambeth</td>
      <td>No judicial outcome</td>
    </tr>
  </tbody>
</table>
</div>



Let's now group the DataFrame by the Crime type and Broad Outcome to get the data for our chart. We'll also make a text column:


```python
typeOutcome = crimes.groupby(['Crime type','Broad Outcome'], as_index=False).count()
typeOutcome['text'] = typeOutcome.apply(lambda x: "<b>{}</b><br>{}<br>{:,}".format(x['Crime type'],
                                                                                   x['Broad Outcome'],
                                                                                  x['Outcome Month']),
                               axis = 1)
typeOutcome.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime type</th>
      <th>Broad Outcome</th>
      <th>Outcome Month</th>
      <th>Outcome type</th>
      <th>Crime Month</th>
      <th>Area</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bicycle theft</td>
      <td>Defendant found not guilty</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>&lt;b&gt;Bicycle theft&lt;/b&gt;&lt;br&gt;Defendant found not gu...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bicycle theft</td>
      <td>No judicial outcome</td>
      <td>8128</td>
      <td>8128</td>
      <td>8128</td>
      <td>8128</td>
      <td>&lt;b&gt;Bicycle theft&lt;/b&gt;&lt;br&gt;No judicial outcome&lt;br...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bicycle theft</td>
      <td>Offender sent to prison</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>&lt;b&gt;Bicycle theft&lt;/b&gt;&lt;br&gt;Offender sent to priso...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bicycle theft</td>
      <td>Outcome not yet known</td>
      <td>272</td>
      <td>272</td>
      <td>272</td>
      <td>272</td>
      <td>&lt;b&gt;Bicycle theft&lt;/b&gt;&lt;br&gt;Outcome not yet known&lt;...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bicycle theft</td>
      <td>Punished, not prison</td>
      <td>123</td>
      <td>123</td>
      <td>123</td>
      <td>123</td>
      <td>&lt;b&gt;Bicycle theft&lt;/b&gt;&lt;br&gt;Punished, not prison&lt;b...</td>
    </tr>
  </tbody>
</table>
</div>



We're going to make the same type of chart that we just previously made. This is quite complex data, and that type of bubble plot simplifies it very well. 


```python
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
```





![pyo.iplot-8](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-8.png)
The bubbles for 'No judicial outcome' are very large compared to the rest, but it's also interesting to see the differnces in outcomes for different types of crime.

Let's add this chart to our dashboard:


```python
metCrimes.append_trace(typeOutcomeScatter, row = 1, col = 1)

pyo.iplot(metCrimes)
```






![pyo.iplot-9](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-9.png)## (6) Changing the layout

If you're following along with the videos, the sixth and final lesson starts here.

Although we've got all of the traces and charts on the dashboard, there's still a bit of work to do. 

There is quite a lot of overlap for the place, crime and outcome names and the chart titles. We'll need to change the height of the dashboard, the domains of the charts, the position of the chart titles and the dashboard margins.

We also need to leave room for the dashboard title which we'll place last of all.

## Fitting the charts

There are a few things we can do to make sure the charts all fit:
2. Rotate the ticklabels
3. Increase the margins
4. Change the domain of the charts
1. Increase the height of the dashboard

If these don't work, then we need to think about changing the ticklabels for the categories.

Let's rotate the ticklabels on the x2 axis. I'm also going to set showgrid to False for the x1 axis:


```python
metCrimes['layout']['xaxis2'].update({'tickangle' : 45})
metCrimes['layout']['xaxis1'].update({'showgrid' : False})

pyo.iplot(metCrimes)
```





W
![pyo.iplot-10](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-10.png)e'll now change the left, bottom and right margins to accomodate the ticklabels:


```python
metCrimes['layout'].update({'margin' : {'l' : 180,
                                        'b' : 120,
                                        'r' : 90}})

pyo.iplot(metCrimes)
```





##
![pyo.iplot-11](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-11.png)# Updating chart titles and domains

First, let's increase the height of the dashboard:


```python
metCrimes['layout'].update({'height' : 1500})
pyo.iplot(metCrimes)
```





The
![pyo.iplot-12](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-12.png) title needs to move down on the first chart:


```python
metCrimes['layout']['annotations'][0]['y'] = 0.95
```

We'll move the entire second chart up by changing the domain and y-position of the chart title:


```python
metCrimes['layout']['yaxis2'].update({'domain' : [0.51, 0.74]})
metCrimes['layout']['annotations'][1]['y'] = 0.73
pyo.iplot(metCrimes)
```





We'l
![pyo.iplot-13](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-13.png)l do the same for the Crimes by location chart:


```python
metCrimes['layout']['annotations'][3]['y'] 
```




    0.2346938775510204




```python
metCrimes['layout']['yaxis4'].update({'domain' : [0.19, 0.27]})
metCrimes['layout']['annotations'][3]['y'] = 0.26
pyo.iplot(metCrimes)
```





### S
![pyo.iplot-14](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-14.png)etting a title and changing hovermode

Finally, let's add in the title and set the hovermode to closest:


```python
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
```





We've 
![pyo.iplot-15](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/pyo.iplot-15.png)managed to fit a lot of data into this dashboard; let's push it to the Plotly cloud! You won't be able to see it clearly in the window that pops up, but click on 'full size' and zoom out to see it in all its glory!


```python
py.plot(metCrimes, filename="Crimes recorded by the Metropolitan Police", fileopt="overwrite")
```




    'htt
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(2)%20-%20Crime%20in%20London/py.plot-0.png)ps://plot.ly/~rmuir/323'



