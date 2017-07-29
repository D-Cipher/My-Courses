
# Barcharts (4) - Styling individual bars

In the last lesson we learnt how to apply some different styling options to the bars of our bar chart. In this lesson we'll find out how to set the colour of specific bars. This allows us to draw attention to particular categories.

In order to make this chart as clear as possible we'll add an annotation to highlight why some of the bars are different.






 






## Getting the chart

We'll use the same chart, creating it from scratch rather than loading it from the Plotly cloud.


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
                     'y' : meteorite['count'],
                     'marker' : {'color' : 'lightblue',
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
                          'showarrow' : False}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(04)%20-%20Styling%20individual%20bars/pyo.iplot-0.png)```





## Changing the colour of individual bars

After some research into meteorites, a possible explanation for the high number of meteorites found in 2003 is the appearance of <a href="https://science.nasa.gov/science-news/science-at-nasa/2003/28feb_tucanids">Comet Bradfield</a> which passes the earth very infrequently. Let's set the bar for 2003 to have a different colour from the others, noting this in the legend.

In order to change the colour of a specific bar we must pass a list of colours to the <code>'marker' : {'color' : }</code> parameter. This list must contain as many colours as there are categories, and each colour corresponds to a different category. I'm going to make the bar for 2003 purple to distinguish it from the others.

Let's make this list of colours using a conditional expression. First we'll make a list of the colour 'lightblue' which is as long as the number of categories:


```python
colours = ['lightblue' for x in meteorite.index ]
colours
```




    ['lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue']



Then, we'll ask Python to replace 'lightblue' with 'purple' if the year is 2003:


```python
colours = ['lightblue' if x != 2003 else 'purple' for x in meteorite.index ]
colours
```




    ['lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'purple',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue',
     'lightblue']



Now let's add this list of colours to our code:


```python
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
                          'showarrow' : False}]}
fig = {'data' : [numberOfMeteorites],
      'layout' : layout}
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(04)%20-%20Styling%20individual%20bars/pyo.iplot-1.png)``





Finally, we can add an annotation to explain why the bar for 2003 is different. Note that I'm setting <code>'showarrow' : True</code> to make this explanation explicit. I'm also positioning this annotation relative to the data, rather than the 'paper':


```python
fig['layout']['annotations'].append({'text' : 'Comet Bradfield 12,000km from Earth',
                                       'x' : 2003, 
                                       'y' : 3323,
                                       'showarrow' : True})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(04)%20-%20Styling%20individual%20bars/pyo.iplot-2.png)`





Let's send this new barchart to the Plotly cloud:


```python
py.plot(fig, filename="Number of meteorites found each year (Comet Bradfield)", fileopt = "overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(04)%20-%20Styling%20individual%20bars/py.plot-0.png)




    'https://plot.ly/~rmuir/237'



