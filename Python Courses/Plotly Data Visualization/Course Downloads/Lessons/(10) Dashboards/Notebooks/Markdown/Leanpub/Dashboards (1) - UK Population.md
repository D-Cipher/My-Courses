
# Dashboards (1) - UK Population

In this lesson we're going to make the first of three dashboards in this section.

This dashboard will display information about the UK population. 

We're going to visualise the life expectancy at birth, and again at 65 for men and women in each constituent country of the UK. This data will be shown on two line charts.

Next, we'll look at the share of men and women in each region, displaying this data in a bar chart.

We'll then show the number of children, adults and pensioners in each region in the UK, once again, shown as a bar chart.

We're aiming for the dashboard to be in the following format:

<img src='http://richard-muir.com/images/db1.png'/>



#### New Modules:

Because we\re making a dashboard we'll need to include the <code>make_subplots()</code> function:



from plotly.tools import make_subplots



```python

 
```





## Setting up the dashboard object

We'll firstly create the dashboard object. We are going to include four charts, so our subplots object will need two rows and two columns and we'll need to set the titles accordingly.

When we've finished development of the dashboard, we'll set the width and height of it to be in a landscape view. We'll keep it to the default size while we develop though; it's easier to see that way!


```python
db = make_subplots(rows = 2, cols = 2,
                  subplot_titles = ['Life expectancy at birth',
                                   'Life expectancy at 65',
                                   'Share of men and women in UK',
                                    'Age of people in the UK'])

db['data'] = [{'type' : 'scatter'}]
pyo.iplot(db)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





## Getting the data

We'll use two .csv files for our data. The first contains information on life expectancy and the second has the data on the population breakdown by age and sex.


```python
demographic = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKRegionsPopulation.csv",
                         index_col = 0)
demographic.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Children</th>
      <th>Adults</th>
      <th>Pensioners</th>
      <th>Male</th>
      <th>Female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North East</td>
      <td>524417.0</td>
      <td>1601007.0</td>
      <td>499197.0</td>
      <td>1287177</td>
      <td>1337444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>1521365.0</td>
      <td>4351005.0</td>
      <td>1301465.0</td>
      <td>3534396</td>
      <td>3639439</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Yorkshire and The Humber</td>
      <td>1145643.0</td>
      <td>3271192.0</td>
      <td>973741.0</td>
      <td>2658411</td>
      <td>2732165</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East Midlands</td>
      <td>971538.0</td>
      <td>2827943.0</td>
      <td>877557.0</td>
      <td>2309197</td>
      <td>2367841</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>1261883.0</td>
      <td>3443312.0</td>
      <td>1045805.0</td>
      <td>2844758</td>
      <td>2906242</td>
    </tr>
  </tbody>
</table>
</div>




```python
lifeExp = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKCountriesLifeExpectancy.csv",
                         index_col = 0)

lifeExp.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Var</th>
      <th>Country</th>
      <th>N</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2002</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>15.73</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2003</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>15.92</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.17</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.40</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.70</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
</div>



## Making the line charts

#### Lookups

Let's now create our line charts. 

We're going to have lines for males and females on each chart. We'll distinguish these by setting the colour of the trace. We'll also have lines for each country, which we'll distinguish by setting the marker symbol.

We'll need a sex-colour and a country-symbol lookup, as well as a list of all trhe years in the Year column:


```python
sexColour = {'Male' : "rgb(114,229,239)",
            'Female' : 'rgb(125,26,110)'}

countrySymbol = {'England' : 'cross',
                'Scotland' : 'x',
                'Wales' : 'circle',
                'Scotland' : 'square',
                'N Ireland' : 'triangle'}
years = lifeExp['Year'].unique()
```

#### Creating the hovertext column

Let's now create a hovertext column so we can display the hovertext exactly as we wish.

We're going to write a function which will concatenate together all the values of the variables to create the text field. 


```python
def hoverText(row):
    return "<b>{}</b><br>{:.0f} years<br><i>{}</i>".format(row['Country'], row['N'], row['Sex'])

lifeExp['text'] = lifeExp.apply(hoverText, axis = 1)

lifeExp.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Var</th>
      <th>Country</th>
      <th>N</th>
      <th>Sex</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2002</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>15.73</td>
      <td>Male</td>
      <td>&lt;b&gt;N Ireland&lt;/b&gt;&lt;br&gt;16 years&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2003</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>15.92</td>
      <td>Male</td>
      <td>&lt;b&gt;N Ireland&lt;/b&gt;&lt;br&gt;16 years&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.17</td>
      <td>Male</td>
      <td>&lt;b&gt;N Ireland&lt;/b&gt;&lt;br&gt;16 years&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.40</td>
      <td>Male</td>
      <td>&lt;b&gt;N Ireland&lt;/b&gt;&lt;br&gt;16 years&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006</td>
      <td>age 65</td>
      <td>N Ireland</td>
      <td>16.70</td>
      <td>Male</td>
      <td>&lt;b&gt;N Ireland&lt;/b&gt;&lt;br&gt;17 years&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
    </tr>
  </tbody>
</table>
</div>



Let's now add the traces to our chart. We're going to do this in three loops. 

The first, and outer loop will place the traces on the correct grid space in the subplots. 

The traces for life expectancy at birth will go at <code>row = 1, col = 1</code>, whilst the traces for life expectancy at 65 will go at <code>row = 1, col= 2</code>. We'll also create a variable that will allow us to only show the first trace. This way, the legend won't be cluttered.

The second loop will cycle through the countries, and we'll set the symbol for the traces using the lookup we created.

The innermost loop will cycle through the sexes, and we'll set the colour for the traces using the other lookup.


```python
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
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/pyo.iplot-1.png)``





## (2) Making the bar charts

If you're following along with the videos, the second lesson starts here.

Now we've added the line traces, we can start to put the bar traces in the remaining cells. These traces will show a bar for each of the English regions and the other countries (Scotland, Wales & Northern Ireland).

#### Number of males and females in each country

We'll first of all append the Male/Female bar traces to the bottom-left cell, but let's first remind ourselves what the demographics dataset looks like:


```python
demographic.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Children</th>
      <th>Adults</th>
      <th>Pensioners</th>
      <th>Male</th>
      <th>Female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North East</td>
      <td>524417.0</td>
      <td>1601007.0</td>
      <td>499197.0</td>
      <td>1287177</td>
      <td>1337444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>1521365.0</td>
      <td>4351005.0</td>
      <td>1301465.0</td>
      <td>3534396</td>
      <td>3639439</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Yorkshire and The Humber</td>
      <td>1145643.0</td>
      <td>3271192.0</td>
      <td>973741.0</td>
      <td>2658411</td>
      <td>2732165</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East Midlands</td>
      <td>971538.0</td>
      <td>2827943.0</td>
      <td>877557.0</td>
      <td>2309197</td>
      <td>2367841</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>1261883.0</td>
      <td>3443312.0</td>
      <td>1045805.0</td>
      <td>2844758</td>
      <td>2906242</td>
    </tr>
  </tbody>
</table>
</div>



We'll now add a text column for each of the columns we're going to plot. I'm going to create a new function to apply. 

We'll use another parameter of the <code>pandas.DataFrame.apply()</code> method to pass in the name of the column which holds the value of the variable.

We pass this argument within the <code>args=()</code> parameter, and it's really important that the column name is followed by a comma. Following the column name with a comma means that Python interprets it as a tuple, and not a string within two sets of brackets.

Finally, we'll create a lookup between the column which contains the variable and the respective text column.


```python
def hoverText(row, varName):
    return "<b>{}</b><br>{:,.0f}<br><i>{}</i>".format(row['Country'], row[varName], varName)

demoTextLookup = {}

for col in demographic.columns:
    if col != 'Country':
        demographic['text{}'.format(col)] = demographic.apply(hoverText, args=(col,), axis = 1)
        demoTextLookup[col] = 'text{}'.format(col)

demographic.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Children</th>
      <th>Adults</th>
      <th>Pensioners</th>
      <th>Male</th>
      <th>Female</th>
      <th>textChildren</th>
      <th>textAdults</th>
      <th>textPensioners</th>
      <th>textMale</th>
      <th>textFemale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North East</td>
      <td>524417.0</td>
      <td>1601007.0</td>
      <td>499197.0</td>
      <td>1287177</td>
      <td>1337444</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;524,417&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;1,601,007&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;499,197&lt;br&gt;&lt;i&gt;Pensioners&lt;/i&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;1,287,177&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;1,337,444&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>1521365.0</td>
      <td>4351005.0</td>
      <td>1301465.0</td>
      <td>3534396</td>
      <td>3639439</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,521,365&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;4,351,005&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,301,465&lt;br&gt;&lt;i&gt;Pensioner...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,534,396&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,639,439&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Yorkshire and The Humber</td>
      <td>1145643.0</td>
      <td>3271192.0</td>
      <td>973741.0</td>
      <td>2658411</td>
      <td>2732165</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;1,145,643&lt;b...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;3,271,192&lt;b...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;973,741&lt;br&gt;...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;2,658,411&lt;b...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;2,732,165&lt;b...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East Midlands</td>
      <td>971538.0</td>
      <td>2827943.0</td>
      <td>877557.0</td>
      <td>2309197</td>
      <td>2367841</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;971,538&lt;br&gt;&lt;i&gt;Children...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;2,827,943&lt;br&gt;&lt;i&gt;Adults...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;877,557&lt;br&gt;&lt;i&gt;Pensione...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;2,309,197&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;2,367,841&lt;br&gt;&lt;i&gt;Female...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>1261883.0</td>
      <td>3443312.0</td>
      <td>1045805.0</td>
      <td>2844758</td>
      <td>2906242</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,261,883&lt;br&gt;&lt;i&gt;Childr...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;3,443,312&lt;br&gt;&lt;i&gt;Adults...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,045,805&lt;br&gt;&lt;i&gt;Pensio...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,844,758&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,906,242&lt;br&gt;&lt;i&gt;Female...</td>
    </tr>
  </tbody>
</table>
</div>



Let's first sort the demographic dataset from largest to smallest; this will make it easier to read.


```python
mf = demographic.sort_values(by=['Male','Female'], ascending = False)
mf.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Children</th>
      <th>Adults</th>
      <th>Pensioners</th>
      <th>Male</th>
      <th>Female</th>
      <th>textChildren</th>
      <th>textAdults</th>
      <th>textPensioners</th>
      <th>textMale</th>
      <th>textFemale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>South East</td>
      <td>1918075.0</td>
      <td>5350219.0</td>
      <td>1679619.0</td>
      <td>4404373</td>
      <td>4543540</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;1,918,075&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;5,350,219&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;1,679,619&lt;br&gt;&lt;i&gt;Pensioner...</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;4,404,373&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;4,543,540&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>6</th>
      <td>London</td>
      <td>1952870.0</td>
      <td>5719477.0</td>
      <td>1001366.0</td>
      <td>4309512</td>
      <td>4364201</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;1,952,870&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;5,719,477&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;1,001,366&lt;br&gt;&lt;i&gt;Pensioners&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;4,309,512&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;4,364,201&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>1521365.0</td>
      <td>4351005.0</td>
      <td>1301465.0</td>
      <td>3534396</td>
      <td>3639439</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,521,365&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;4,351,005&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,301,465&lt;br&gt;&lt;i&gt;Pensioner...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,534,396&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,639,439&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>5</th>
      <td>East of England</td>
      <td>1299984.0</td>
      <td>3612599.0</td>
      <td>1163868.0</td>
      <td>2993366</td>
      <td>3083085</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;1,299,984&lt;br&gt;&lt;i&gt;Chil...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;3,612,599&lt;br&gt;&lt;i&gt;Adul...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;1,163,868&lt;br&gt;&lt;i&gt;Pens...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;2,993,366&lt;br&gt;&lt;i&gt;Male...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;3,083,085&lt;br&gt;&lt;i&gt;Fema...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>1261883.0</td>
      <td>3443312.0</td>
      <td>1045805.0</td>
      <td>2844758</td>
      <td>2906242</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,261,883&lt;br&gt;&lt;i&gt;Childr...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;3,443,312&lt;br&gt;&lt;i&gt;Adults...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,045,805&lt;br&gt;&lt;i&gt;Pensio...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,844,758&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,906,242&lt;br&gt;&lt;i&gt;Female...</td>
    </tr>
  </tbody>
</table>
</div>



I'm going to set the marker colour to be consistent with the chart above, and I'm also going to set the traces in each cell to have the same legendgroup so we can make sure they are spread apart:


```python
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
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/pyo.iplot-2.png)`





#### Number of people in each age group in each country

Now we'll add the bar traces showing the number of people in the different age groups in the UK.

Once again, we'll sort the DataFrame in descending order before we plot it:


```python
ages = demographic.sort_values(by=['Adults','Pensioners','Children'],
                              ascending = False)
ages.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Children</th>
      <th>Adults</th>
      <th>Pensioners</th>
      <th>Male</th>
      <th>Female</th>
      <th>textChildren</th>
      <th>textAdults</th>
      <th>textPensioners</th>
      <th>textMale</th>
      <th>textFemale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>London</td>
      <td>1952870.0</td>
      <td>5719477.0</td>
      <td>1001366.0</td>
      <td>4309512</td>
      <td>4364201</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;1,952,870&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;5,719,477&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;1,001,366&lt;br&gt;&lt;i&gt;Pensioners&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;4,309,512&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;4,364,201&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>7</th>
      <td>South East</td>
      <td>1918075.0</td>
      <td>5350219.0</td>
      <td>1679619.0</td>
      <td>4404373</td>
      <td>4543540</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;1,918,075&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;5,350,219&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;1,679,619&lt;br&gt;&lt;i&gt;Pensioner...</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;4,404,373&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;4,543,540&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>North West</td>
      <td>1521365.0</td>
      <td>4351005.0</td>
      <td>1301465.0</td>
      <td>3534396</td>
      <td>3639439</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,521,365&lt;br&gt;&lt;i&gt;Children&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;4,351,005&lt;br&gt;&lt;i&gt;Adults&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;1,301,465&lt;br&gt;&lt;i&gt;Pensioner...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,534,396&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;3,639,439&lt;br&gt;&lt;i&gt;Female&lt;/i&gt;</td>
    </tr>
    <tr>
      <th>5</th>
      <td>East of England</td>
      <td>1299984.0</td>
      <td>3612599.0</td>
      <td>1163868.0</td>
      <td>2993366</td>
      <td>3083085</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;1,299,984&lt;br&gt;&lt;i&gt;Chil...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;3,612,599&lt;br&gt;&lt;i&gt;Adul...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;1,163,868&lt;br&gt;&lt;i&gt;Pens...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;2,993,366&lt;br&gt;&lt;i&gt;Male...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;3,083,085&lt;br&gt;&lt;i&gt;Fema...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>1261883.0</td>
      <td>3443312.0</td>
      <td>1045805.0</td>
      <td>2844758</td>
      <td>2906242</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,261,883&lt;br&gt;&lt;i&gt;Childr...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;3,443,312&lt;br&gt;&lt;i&gt;Adults...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;1,045,805&lt;br&gt;&lt;i&gt;Pensio...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,844,758&lt;br&gt;&lt;i&gt;Male&lt;/i&gt;</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;2,906,242&lt;br&gt;&lt;i&gt;Female...</td>
    </tr>
  </tbody>
</table>
</div>



First of all we need to get a list of the different age categories, then, looping through this list, we can add a trace for each region or country, setting <code>row = 2, col = 2</code>.

We'll also create a new lookup for the colours for the age groups. I've set these colours to contrast heavily with the colours we set for the males and females.


```python
ageColours = [ "rgb(133,199,156)", "rgb(82,239,153)", "rgb(52,75,70)"]
ageGroups = ['Children','Adults','Pensioners']
ageLookup = dict(zip(ageGroups, ageColours))
ageLookup
```




    {'Adults': 'rgb(82,239,153)',
     'Children': 'rgb(133,199,156)',
     'Pensioners': 'rgb(52,75,70)'}



Now, we'll create the traces. We're also going to set the trace names and legendgroup:


```python
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
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/pyo.iplot-3.png)





## (3) Setting the layout

If you're following along with the videos, the third lesson for this dashboard starts here.

We've now got a few changes to make to the layout:
1. Set the range to be static for the y-axes on the bar charts
1. Set the tracegroupgap
2. Add a tickangle to the x-axes
1. Add axis titles where appropriate
3. Set the width and height of the dashboard
4. Add some margins if necessary
5. Add a title for the dashboard
7. Set the hovermode to 'closest'




```python
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
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/pyo.iplot-4.png)




Let's send this dashboard to the Plotly cloud:


```python
py.plot(db, filename="Population demographics of the UK", fileopt="overwrite")
```


![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Dashboards%20(1)%20-%20UK%20Population/py.plot-0.png)


    'https://plot.ly/~rmuir/325'



