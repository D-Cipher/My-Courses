
# Scatterplot (10) - Recreating the Gapminder plot

In this lesson we're going to recreate Hans Rosling's famous <a href="https://www.gapminder.org/data/">Gapminder</a> bubbleplot.

We'll practise how to use the <code>'marker' : {'size' : }</code> and <code>'sizeref'</code> options to change the size of the bubbles and we'll also learn how to set the <code>'sizemin'</code> property to set the minimum size of the bubbles on the plot to help us account for the large difference in sizes between the countries; the smallest country has just 104,000 people, whilst the largest has 1.3 billion.






 






## Getting the data

I've sourced the data we need from the <a href="https://www.gapminder.org/data/">Gapminder</a> data page and done some pre-processing to merge the various data files together. We'll download it as a .csv file from my website.

The GDP per capita is in US$ at <a href="https://en.wikipedia.org/wiki/Purchasing_power_parity">purchasing power parity</a>


```python
LifePopGDP = pd.read_csv("http://www.richard-muir.com/data/public/csv/GapminderData.csv", index_col = 0)
LifePopGDP.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Continent</th>
      <th>Country</th>
      <th>Life Expectancy</th>
      <th>GDP per Capita</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Africa</td>
      <td>Algeria</td>
      <td>70.874</td>
      <td>12779.0</td>
      <td>36488669.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Africa</td>
      <td>Angola</td>
      <td>51.498</td>
      <td>7230.0</td>
      <td>20039259.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Africa</td>
      <td>Benin</td>
      <td>59.165</td>
      <td>1685.0</td>
      <td>9775152.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>Botswana</td>
      <td>47.152</td>
      <td>14905.0</td>
      <td>2030287.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Africa</td>
      <td>Burundi</td>
      <td>53.637</td>
      <td>737.0</td>
      <td>8899077.0</td>
    </tr>
  </tbody>
</table>
</div>



Let's create a column to hold the hovertext. We'll put the country name in bold, the life expectancy as an integer, and the GDP per capita and Population as integers with a comma as a thousand separator.


```python
LifePopGDP['text'] = LifePopGDP.apply(lambda x: 
        "<b>{}</b><br>Life Expectancy: {:.0f} years<br>GDP/Capita: ${:,.0f}<br>Population: {:,.0f}".format(x['Country'], 
                                                                                                 x['Life Expectancy'],
                                                                                                x['GDP per Capita'],
                                                                                                x['Population']),
                                     axis = 1)
LifePopGDP.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Continent</th>
      <th>Country</th>
      <th>Life Expectancy</th>
      <th>GDP per Capita</th>
      <th>Population</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Africa</td>
      <td>Algeria</td>
      <td>70.874</td>
      <td>12779.0</td>
      <td>36488669.0</td>
      <td>&lt;b&gt;Algeria&lt;/b&gt;&lt;br&gt;Life Expectancy: 71 years&lt;br...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Africa</td>
      <td>Angola</td>
      <td>51.498</td>
      <td>7230.0</td>
      <td>20039259.0</td>
      <td>&lt;b&gt;Angola&lt;/b&gt;&lt;br&gt;Life Expectancy: 51 years&lt;br&gt;...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Africa</td>
      <td>Benin</td>
      <td>59.165</td>
      <td>1685.0</td>
      <td>9775152.0</td>
      <td>&lt;b&gt;Benin&lt;/b&gt;&lt;br&gt;Life Expectancy: 59 years&lt;br&gt;G...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>Botswana</td>
      <td>47.152</td>
      <td>14905.0</td>
      <td>2030287.0</td>
      <td>&lt;b&gt;Botswana&lt;/b&gt;&lt;br&gt;Life Expectancy: 47 years&lt;b...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Africa</td>
      <td>Burundi</td>
      <td>53.637</td>
      <td>737.0</td>
      <td>8899077.0</td>
      <td>&lt;b&gt;Burundi&lt;/b&gt;&lt;br&gt;Life Expectancy: 54 years&lt;br...</td>
    </tr>
  </tbody>
</table>
</div>



And check that it's worked properly:


```python
LifePopGDP.loc[0, 'text']
```




    '<b>Algeria</b><br>Life Expectancy: 71 years<br>GDP/Capita: $12,779<br>Population: 36,488,669'



## Creating the chart

The chart we'll create will have a data point for each country. The y-value will be the life expectancy in years. The x-value will be the GDP per capita. The bubbles will be sized for the population, but we'll have to specify the <code>'sizeref'</code>  to be <code>500,000</code> because the numbers are so large. Each country's data point will be coloured depending on which continent it belongs to.

We'll first of all need a list of continents which we'll use to create a trace for each continent:


```python
continents = LifePopGDP['Continent'].unique()
continents
```




    array(['Africa', 'Asia', 'Europe', 'North America', 'Oceania',
           'South America'], dtype=object)



Now let's loop through this list of continents, selecting the rows where the value for Continent matches the current continent in the loop, and selecting the column which relates to the x-variable, y-variable or size variable. We'll do this using the <code>df.loc[]</code> indexer:


```python
traces = []
for c in continents:
    traces.append({'type' : 'scatter',
                   'mode' : 'markers',
                   'name' : c,
                   'hoverinfo' : 'text',
                  'x' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'GDP per Capita'],
                  'y' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Life Expectancy'],
                  'text' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'text'],
                  'marker' : {'size' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Population'],
                             'sizeref' : 500000,
                             'sizemode' : 'area'}})
```

Let's plot these traces to get an idea of how the chart looks before we start to style it:


```python
pyo.iplot(traces)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(10)%20-%20Recreating%20the%20Gapminder%20plot/pyo.iplot-0.png)```





So we can see straight away that because we've had to set <code>'sizeref'</code> to 500,000, the smaller countries are practically invisible on the plot. Let's update each trace with a <code>'sizemin'</code> value in the <code>'marker'</code> dictionary to set the minimum possible size for each marker point:


```python
traces = []
for c in continents:
    traces.append({'type' : 'scatter',
                   'mode' : 'markers',
                   'name' : c,
                   'hoverinfo' : 'text',
                  'x' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'GDP per Capita'],
                  'y' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Life Expectancy'],
                  'text' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'text'],
                  'marker' : {'size' : LifePopGDP.loc[LifePopGDP['Continent'] == c, 'Population'],
                             'sizeref' : 500000,
                              'sizemode' : 'area',
                             'sizemin' : 2.5}})
pyo.iplot(traces)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(10)%20-%20Recreating%20the%20Gapminder%20plot/pyo.iplot-1.png)``





Now let's tweak the layout to finish styling the chart. We'll set the axis titles as normal and I'm also going to set the range  of each axis in the normal way, being aware that we'll have to expand this number to accomodate the large population bubbles for India and China.

Finally, we'll set the <code>'hovermode'</code> to <code>'closest'</code>:


```python
layout = {'title' : 'Life Expectancy and GDP per capita',
         'xaxis' : {'title' : 'GDP per capita at PPP ($)',
                   'range' : [LifePopGDP['GDP per Capita'].min() * 0.95, 
                              LifePopGDP['GDP per Capita'].max() * 1.05]},
         'yaxis' : {'title' : 'Life expectancy (years)',
                   'range' : [LifePopGDP['Life Expectancy'].min() * 0.95, 
                              LifePopGDP['Life Expectancy'].max() * 1.05]},
         'hovermode' : 'closest'}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(10)%20-%20Recreating%20the%20Gapminder%20plot/pyo.iplot-2.png)`





Let's update the x-axis range. We'll do this in a slighlty different way because we need to extend the range below 0. Rather than reducing the minimum amount by 5%, we'll instead reduce the minimum amount by 5% of the total range of the data:


```python
difference = LifePopGDP['GDP per Capita'].max() - LifePopGDP['GDP per Capita'].min()
fig['layout']['xaxis'].update({'range' : [LifePopGDP['GDP per Capita'].min() - (difference * 0.05), 
                                          LifePopGDP['GDP per Capita'].max() * 1.05]})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(10)%20-%20Recreating%20the%20Gapminder%20plot/pyo.iplot-3.png)





Let's send this chart to the Plotly cloud:


```python
py.plot(fig, filename="Life Expectancy and GDP per Capita", fileopt = "overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(10)%20-%20Recreating%20the%20Gapminder%20plot/py.plot-0.png)



    'https://plot.ly/~rmuir/218'



