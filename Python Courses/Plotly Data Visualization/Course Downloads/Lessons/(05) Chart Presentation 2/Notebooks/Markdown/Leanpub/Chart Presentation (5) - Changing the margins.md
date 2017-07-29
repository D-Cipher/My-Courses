
# Chart Presentation (5) - Changing the margins

In this lesson we're going to learn how to increase the margins of our chart. This will allow us to see in full any annotations which we place outside the plotting area.






 






## Getting the chart

We'll copy the code to create the same chart as in the previous lesson:


```python
trace = [{'type' : 'scatter'}]
layout = {'annotations' : [{'text' : 'Left of the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : -1,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'Right of the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 2,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'Below the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : -1,
                           'showarrow' : False},
                          {'text' : 'Above the plotting area',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 2,
                           'showarrow' : False}],
         'xaxis' : {'range' : [0, 10]},
         'yaxis' : {'range' : [0, 10]}}
fig = Figure(data = trace, layout = layout)

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(5)%20-%20Changing%20the%20margins/pyo.iplot-0.png)```





## Changing the margins

The options which control the margins are contained within the layout part of the figure. We can pass an integer value to set the top, bottom, left and right margins separately. This number sets the size of the margin in pixels. We can control the margin information as so:
````python
layout = {'margin' : {'b' : <integer>,
                        't' : <integer>,
                        'l' : <integer>,
                        'r' : <integer>}}
````
<code>'l'</code>, <code>'r'</code>, <code>'t'</code> and <code>'b'</code> control the left, right, top and bottom margin sizes respectively.

Let's put this into practise. We'll increase the margin sizes until we can see the annotations that we created in the previous lesson. First of all, let's change the height and width of the plot to accomodate the increased margins:


```python
fig['layout'].update({'height' : 600, 'width' : 800})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(5)%20-%20Changing%20the%20margins/pyo.iplot-1.png)``





Now we can update the bottom margin:


```python
fig['layout'].update({'margin' : {'b' : 250}})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(5)%20-%20Changing%20the%20margins/pyo.iplot-2.png)`





And the top:


```python
fig['layout'].update({'margin' : {'t' : 250}})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(5)%20-%20Changing%20the%20margins/pyo.iplot-3.png)





And the left and right:


```python
fig['layout'].update({'margin' : {'l' : 300, 'r' : 300}})
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(5)%20-%20Changing%20the%20margins/pyo.iplot-4.png)




You can see that we've had to drastically increase the margins in order to fit the text in. In practise, we could also change the annotation font size, add line breaks to the annotations, and the reduce the distance of the annotation from the chart.

