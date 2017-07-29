
# Pie charts (4) - Highlighting specific segments

In this lesson we're going to learn how to pull specific segments out from the main body of the pie chart to highlight them to our readers. 

This allows us to focus our readers on a specific message in the data, but does carry the risk of making the chart less easy to understand.






 






## Moving all the segments

In the trace object, we can use the parameter <code>'pull'</code> to spread the segments of the pie chart out. 

By specifying an number we can move all of the segments an equal amount, and by specifying a list of numbers we can choose to move a specific segment or segments that we wish to highlight. 

Each number must be between 0 and 1 inclusive.

Let's try this out on the chart we styled in the last lesson:


```python
ethPie = py.get_figure("rmuir", 265)
pyo.iplot(ethPie)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-0.png)```





Let's move all of the sectors out the maximum amount:


```python
ethPie['data'][0].update({'pull' : 1})
pyo.iplot(ethPie)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-1.png)``





And maybe a little less. . .


```python
ethPie['data'][0].update({'pull' : 0.1})
pyo.iplot(ethPie)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-2.png)`





Let's now try moving a specific segment. I'm going to move the segment for Black students out to highlight it:


```python
ethPie['data'][0].update({'pull' : [0, 0, 0.2, 0, 0]})
pyo.iplot(ethPie)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-3.png)





Well that doesn't appear to have worked . . .

If we look at the data in the chart, we can see that the category for black students is in fact the fourth category in the list of values. It looks like Plotly applies the value for the <code>'pull'</code> parameter before sorting the segments based on size.


```python
ethPie['data'][0]
```




    {'direction': 'clockwise',
     'labels': ['White', 'Other', 'Not known', 'Black', 'Asian'],
     'labelssrc': 'rmuir:266:571af0',
     'marker': {'colors': ['rgb(12,192,170)',
       'rgb(190,252,250)',
       'rgb(77,194,84)',
       'rgb(211,238,128)',
       'rgb(97,167,193)'],
      'colorssrc': 'rmuir:266:b9b126',
      'line': {'color': '#333', 'width': '1'}},
     'pull': [0, 0, 0.2, 0, 0],
     'sort': True,
     'type': 'pie',
     'values': [1418685.0, 84525.0, 33290.0, 117460.0, 175240.0],
     'valuessrc': 'rmuir:266:a11fa7'}



## Finding a workaround for this problem

We could go into the data and count along the lists of values and labels to find the segment that we want, but that seems like a lot of hard work. Let's pre-sort our data and put it back into the trace object.

We'll create a <code>dict()</code> by <code>zip()</code>ping together the lists of labels and values and using the python <code>sorted()</code> function to output this dictionary in a sorted fashion. We could also have sorted the data in our DataFrame, but we may not always have that luxury . . .


```python
labelValues = dict(zip(ethPie['data'][0]['labels'], 
                       ethPie['data'][0]['values']))
labelValues
```




    {'Asian': 175240.0,
     'Black': 117460.0,
     'Not known': 33290.0,
     'Other': 84525.0,
     'White': 1418685.0}




```python
newLabels = []
newValues = []
for w in sorted(labelValues, key=labelValues.get, reverse=True):
    label = w
    value = labelValues[w]
    
    newLabels.append(label)
    newValues.append(value)
    
newLabels, newValues
```




    (['White', 'Asian', 'Black', 'Other', 'Not known'],
     [1418685.0, 175240.0, 117460.0, 84525.0, 33290.0])



Let's put this sorted data back into the trace and replot it!


```python
ethPie['data'][0]['labels'] = newLabels
ethPie['data'][0]['values'] = newValues

pyo.iplot(ethPie)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-4.png)




Success! Let's try changing which segment we're pulling:


```python
ethPie['data'][0].update({'pull' : [0,0,0,0,0.5]})
pyo.iplot(ethPie)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/pyo.iplot-5.png)




```python
py.plot(ethPie, filename="Ethnicity of UK students (highlight)", fileopt = "overwrite")
```



![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(4)%20-%20Highlighting%20specific%20segments/py.plot-0.png)

    'https://plot.ly/~rmuir/267'



