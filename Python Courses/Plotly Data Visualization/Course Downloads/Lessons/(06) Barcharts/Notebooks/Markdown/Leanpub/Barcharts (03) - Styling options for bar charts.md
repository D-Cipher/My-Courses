
# Barcharts (3) - Styling options for bar charts

In the last lesson we created our very first bar chart. In this lesson we're going to learn about some of the different styling options available to us.






 






## Getting the chart

We'll create the chart from scratch rather than load it from the Plotly cloud; it's a good idea to practise new concepts as much as possible!


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




```python
numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count']}

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

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(03)%20-%20Styling%20options%20for%20bar%20charts/pyo.iplot-0.png)```





## Changing the colour of the bars

We can change the colour of the bars in a bar chart in the same way as we change the colour of a scatterplot or lineplot.

Within the trace object, we access the <code>'color'</code> property within <code>'marker'</code> sub-dictionary, setting this colour as normal (CSS colour, HEX codes etc.):


```python
fig['data'][0].update({'marker' : {'color' : 'lightblue'}})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(03)%20-%20Styling%20options%20for%20bar%20charts/pyo.iplot-1.png)``





## Styling the bars
We can also change different styling options for the bars. I'm going to add a grey outline to each bar:


```python
fig['data'][0]['marker'].update({'line' : {'color' : '#333',
                                          'width' : 2}})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(03)%20-%20Styling%20options%20for%20bar%20charts/pyo.iplot-2.png)`





Finally, we can also change the opacity of the bars:


```python
fig['data'][0].update({'opacity' : 0.5})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(03)%20-%20Styling%20options%20for%20bar%20charts/pyo.iplot-3.png)





Let's send this updated and stylish barchart to the Plotly cloud:


```python
py.plot(fig, filename="Number of meteorites found each year", fileopt = "overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(03)%20-%20Styling%20options%20for%20bar%20charts/py.plot-0.png)



    'https://plot.ly/~rmuir/233'



