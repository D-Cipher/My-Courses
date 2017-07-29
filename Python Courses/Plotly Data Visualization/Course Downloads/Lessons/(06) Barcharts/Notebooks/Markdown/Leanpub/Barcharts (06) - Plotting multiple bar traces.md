
# Barcharts (6) - Plotting multiple bar traces

In this lesson we're going to make a slightly more complex barchart which shows multiple categories.

We're going to plot the number of meteorites by continent since the year 2000, and by doing so we'll get some experience of how Plotly creates a bar chart with multiple traces.






 






## Getting the data
We're going to use a different dataset for this chart. The data comes from the same source as the previous chart, however I have disaggregated the total number of meteorites found and split them by which continent they were found on. The total number of meteorites does not correspond to the previous dataset because there were many instances where the latitude and longitude of the found meteorite could not be translated by the Google Maps API.


```python
meteorites = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoritesByContinent.csv", index_col = 0)
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>continent</th>
      <th>year</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Africa</td>
      <td>2000</td>
      <td>239</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Africa</td>
      <td>2001</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Africa</td>
      <td>2002</td>
      <td>109</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>2003</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Africa</td>
      <td>2004</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting the data

We'll now create a bar trace for each continent. We'll do this by getting a list of the unique values in the 'continent' column, then looping through this list, selecting only the rows which belong the that particular continent.


```python
continents = list(meteorites['continent'].unique())
continents
```




    ['Africa',
     'Antarctica',
     'Asia',
     'Australia',
     'Europe',
     'North America',
     'South America']




```python
traces = []
for c in continents:
    traces.append({'type' : 'bar',
                  'name' : c,
                  'x' : meteorites.loc[meteorites['continent'] == c, 'year'],
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count']})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Number of meteorites'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : traces, 'layout' : layout}
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(06)%20-%20Plotting%20multiple%20bar%20traces/pyo.iplot-0.png)```





So that gives us this striking chart. The standard Plotly colours are very bright! 

Plotly's default option when working with bar charts is to create a grouped bar chart. We'll find out how to change this to a stacked or overlaid bar chart in the next lessons.

You can see that there are distinct groups of bars for each Year, with the bars in each group corresponding to a particular continent.

Let's try looking at this data another way, grouping the number of meteorites by continent rather than year. We'll also tone down those colours a little bit!


```python
years = list(meteorites['year'].unique())
years
```




    [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]




```python
traces = []
for y in years:
    traces.append({'type' : 'bar',
                  'name' : y,
                   # CHANGE TO SPLIT BY YEAR
                  'x' : meteorites.loc[meteorites['year'] == y, 'continent'],
                  'y' : meteorites.loc[meteorites['year'] == y, 'count'],
                  'opacity' : 0.7})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
         'xaxis' : {'title' : 'Continent'},
         'yaxis' : {'title' : 'Number of meteorites'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : traces, 'layout' : layout}
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(06)%20-%20Plotting%20multiple%20bar%20traces/pyo.iplot-1.png)``





Changing the grouping like this gives us another perspective on the data; it shifts the focus to the differences between each year for each continent. Let's send this chart to the Plotly cloud:


```python
py.plot(fig, filename="Meteorites found by continent (2000 - 2012)", fileopt = "overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(06)%20-%20Plotting%20multiple%20bar%20traces/py.plot-0.png)`




    'https://plot.ly/~rmuir/243'



