
# Barcharts (5) - Making horizontal barcharts

So far in this section we've seen how to apply different styling options to a simple bar chart. In this lesson we'll learn how to change our vertical bar chart to a horizontal bar chart. This will give us greater flexibility when designing clear and concise charts. Horizontal bar charts are very useful when we have categories with long label names; the names often overlap when a vertical bar chart is used.






 






## Getting the chart

We'll use the same chart again:


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
colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                     'x' : meteorite.index,
                     'y' : meteorite['count'],
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

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
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                                       'x' : 2003, 
                                       'y' : 3323,
                                       'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(05)%20-%20Making%20horizontal%20barcharts/pyo.iplot-0.png)```





## Creating a horizontal barchart

Now we can create a horizontal barchart. As with most things in Plotly, this is fairly straightforward.

The first thing we have to do is set the <code>'orientation'</code> parameter in the trace to <code>'h'</code> to tell Plotly that we want this trace to be for a horizontal barchart. To change the barchart back to vertical, we can set this parameter to <code>'v'</code>.


```python
colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                      #NEW CODE GOES HERE
                      'orientation' : 'h',
                     'x' : meteorite.index,
                     'y' : meteorite['count'],
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

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
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                                       'x' : 2003, 
                                       'y' : 3323,
                                       'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(05)%20-%20Making%20horizontal%20barcharts/pyo.iplot-1.png)``





You can see that this creates the same problem that we saw in the second lesson of this section. We now need to swap the x-values and y-values because Plotly is now expecting the y-values to be the categories, rather than the x-values.

We'll also need to change the x- and y-coordinates of our "Comet Bradfield" annotation (but not the source), and the x- and y-axis titles:


```python
colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
numberOfMeteorites = {'type' : 'bar',
                      'orientation' : 'h',
                      #SWAP X- AND Y-COORDINATES HERE
                     'x' : meteorite['count'],
                     'y' : meteorite.index,
                     'marker' : {'color' : colours,
                                'line' : {'color' : '#333',
                                          'width' : 2}},
                     'opacity' : 0.5,}
                     

layout = {'title' : "Number of meteorites found per year",
         'xaxis' : {'title' : 'Number of meteorites'},
         'yaxis' : {'title' : 'Year'},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False},
                         {'text' : 'Comet Bradfield 12,000km from Earth',
                          #SWAP X- AND Y-COORDINATES HERE
                            'x' : 3323, 
                            'y' : 2003,
                            'showarrow' : True}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(05)%20-%20Making%20horizontal%20barcharts/pyo.iplot-2.png)`





So you can see how by making a few small changes to our code, the look of the chart can be changed drastically.

Let's push this chart to the Plotly cloud:


```python
py.plot(fig, filename="Number of meteorites found each year (Horizontal)", fileopt = "overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(05)%20-%20Making%20horizontal%20barcharts/py.plot-0.png)




    'https://plot.ly/~rmuir/239'



