
# Chart Presentation (4) - Annotations outside the chart

In this lesson we'll learn about some further styling options for annotations.

We'll learn how to set the position of annotations using normalised coordinates which correspond to the area which contains the chart (the 'paper') rather than by using the coordinates of a data point on the chart. 

This allows us to consistently position annotations in a specific area of the chart without having to make any reference to the data. 

This is especially useful when making a chart that will be updated with different data - you may want an annotation at a specific point on the chart, but when making reference to the data, this specific point will move. Using normalised coordinates prevents this from happening.






 






## Normalised paper coordinates

Whereas we can position annotations relative to the data, it's often helpful to position them relative to the chart itself. To do this, we must set <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code>. This allows us to use normalised coordinates to refer to points on and around the chart.

With <code>'xref'</code> and <code>'yref'</code> set to <code>'paper'</code>, a value of 0 for  <code>'x'</code> would set the point of the annotation to be the left-hand side of the plotting area (on the y-axis), whereas a value of 1 would set the annotation at the right-hand side of the plotting area.

It follows that a value of 0 for <code>'y'</code> would position the annotation at the botton of the plotting area, and a value of 1 would position it at the top.

Let's see this in action.

We're going to create a dummy trace and four annotations; each will be placed at one corner of the plotting area. The default values for text-anchor will position the annotations at the left and right of the anchor point. We must also set a specific range:


```python
trace = [{'type' : 'scatter'}]
layout = {'annotations' : [{'text' : 'x = 0, y = 0',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'x = 1, y = 0',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 0,
                           'showarrow' : False},
                          {'text' : 'x = 0, y = 1',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 0,
                           'y' : 1,
                           'showarrow' : False},
                          {'text' : 'x = 1, y = 1',
                           'font' : {'size' : 20},
                           'xref' : 'paper',
                           'yref' : 'paper',
                           'x' : 1,
                           'y' : 1,
                           'showarrow' : False}],
         'xaxis' : {'range' : [0, 10]},
         'yaxis' : {'range' : [0, 10]}}
fig = Figure(data = trace, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Annotations%20outside%20the%20chart/pyo.iplot-0.png)```





Now let's try changing the range to something very different to make sure that the annotations stay in the same point:


```python
fig['layout']['xaxis']['range'] = [50, 200]
fig['layout']['yaxis']['range'] = [0, 0.5]
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Annotations%20outside%20the%20chart/pyo.iplot-1.png)``





## Placing annotations outside of the plotting area

We can set the x- and y-coordinates to a negative number to place annotations to the left of (or below) the plotting area. We could also set the x- and y-coordinates to a number >1 to place annotations or to the right of (or above) the plotting area.

Let's test this out:


```python
fig['layout']['annotations'] = [{'text' : 'Left of the plotting area',
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
                           'showarrow' : False}]
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Annotations%20outside%20the%20chart/pyo.iplot-2.png)`





So we can see from this chart how to place annotations outside of the plotting area, however the visible area of the chart doesn't change to reflect this. We need to adjust the margins to increase the amount of chart area outside of the plotting area which is shown.

