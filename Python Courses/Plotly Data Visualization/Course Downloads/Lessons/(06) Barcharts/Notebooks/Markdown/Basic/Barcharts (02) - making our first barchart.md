
# Barcharts (2) - Making our first barchart

In this lesson we're going to make our first barchart. We're going to make a really simple chart which we will then use to learn about the different styling options available to us.

For the majority of this section we're going to focus on a single dataset; the <a href="https://data.nasa.gov/view/ak9y-cwf9">NASA Meteorite Landings</a> dataset. This is a very rich dataset which will allow us to make some diverse and interesting bar charts.






 






## Getting the data

The data is available from my website; I've done some pre-processing and summarising to make it as easy as possible to plot. You could also download it yourself from https://data.nasa.gov/view/ak9y-cwf9, and have a play around with it - it's a really rich and interesting dataset!

I've restricted the source data to only the years 1970 - 2012.


```python
meteorite = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsPerYear.csv", index_col = 0)
meteorite.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1970</th>
      <td>48</td>
    </tr>
    <tr>
      <th>1971</th>
      <td>49</td>
    </tr>
    <tr>
      <th>1972</th>
      <td>32</td>
    </tr>
    <tr>
      <th>1973</th>
      <td>31</td>
    </tr>
    <tr>
      <th>1974</th>
      <td>691</td>
    </tr>
  </tbody>
</table>
</div>



## Making a barchart

In the same way that we make a scatter trace by specifying <code>{'type' : 'scatter'}</code>, we can make a bar trace by specifying <code>{'type' : 'bar'}</code>.

For this barchart, we'll set the x-values as the year (the index in meteorite DataFrame), and the y-values as the number of meteorites found in that year:


```python
numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count']}

pyo.iplot([numberOfMeteorites])

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(02)%20-%20making%20our%20first%20barchart/pyo.iplot-0.png)```





#### What happens if we don't set our x- and y-values correctly; will the chart still plot? 

Yes, it will, however for a vertical bar chart, Plotly expects each vlaue to be of a distinct category. As you can see from the chart below, Plotly has treated each distinct value of <code>'count'</code> as a separate category. If your bar charts don't come out as you expect, try switching your x- and y-values first - a simple mistake can make your chart look very strange indeed!


```python
pyo.iplot([ {'type' : 'bar',
                     'y' : meteorite.index,
                     'x' : meteorite['count']}])
```





Let's add a source and titles to our chart:


```python
layout = {'title' : "Number of meteorites found per year",
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
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(02)%20-%20making%20our%20first%20barchart/pyo.iplot-1.png)``





Let's send our first barchart to the Plotly cloud:


```python
py.plot(fig, filename="Number of meteorites found each year", fileopt = "overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(02)%20-%20making%20our%20first%20barchart/py.plot-0.png)`




    'https://plot.ly/~rmuir/233'



