
# Barcharts (7) - Creating stacked barcharts

In this lesson we're going to learn how to use the Plotly <code>'barmode'</code> option in the layout to switch between stacked and grouped bar charts.

Using stacked and grouped bar charts allows us to compare the same data in different ways. Grouped bar charts allow us to compare quantities between different sub-categories, whilst stacked bar charts allow us to make comparisons between the sub-categories as part of the whole category.






 






## Creating the chart
We're going to use the first chart that we created in a previous lesson as a base. We'll take this opportunity to tone down the colours a little bit!


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
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count'],
                  'opacity' : 0.7})
    
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

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(07)%20-%20Creating%20stacked%20barcharts/pyo.iplot-0.png)```





## Changing the <code>'barmode'</code>

The <code>'barmode'</code> option is contained within the layout and can take one of two options:
- <code>'stack'</code> - makes a stacked bar chart
- <code>'group'</code> - the default, makes a grouped bar chart (as above)

Let's change the <code>'barmode'</code> to <code>'stacked'</code> for this chart:


```python
fig['layout'].update({'barmode' : 'stack'})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(07)%20-%20Creating%20stacked%20barcharts/pyo.iplot-1.png)``





You can see that making such a small change in the layout has had drastic effects on how this chart is displayed. The bars are now stacked on top of each other. 

There are pros and cons to using a stacked bar chart. One advantage is that by stacking the bars, we can easily see how the total number of meteorites changes each year, whilst still getting some idea (but not an exact comparison) of the distribution between the continents. When the bars are grouped however, it becomes much easier to compare the numbers per continent, but nearly impossible to ascertain the total number of meteorites found each year.

It's conventional to order the traces in a stacked bar chart by placing the category with the largest amount at the bottom. We'll re-order our list of continents to achieve this, with Antartica being first in our list of traces:


```python
continents = ['Antarctica',
              'Asia',
              'Africa',
              'South America',
              'North America',
              'Australia',
              'Europe',]
```


```python
traces = []
for c in continents:
    traces.append({'type' : 'bar',
                  'name' : c,
                  'x' : meteorites.loc[meteorites['continent'] == c, 'year'],
                  'y' : meteorites.loc[meteorites['continent'] == c, 'count'],
                  'opacity' : 0.7})
    
layout = {'title' : "Meteorites found by continent, 2000 - 2012",
          'barmode' : 'stack',
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
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(07)%20-%20Creating%20stacked%20barcharts/pyo.iplot-2.png)`






```python
py.plot(fig, filename="Meteorites found by continent (2000 - 2012, stacked bar)", fileopt = "overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(07)%20-%20Creating%20stacked%20barcharts/py.plot-0.png)




    'https://plot.ly/~rmuir/241'



