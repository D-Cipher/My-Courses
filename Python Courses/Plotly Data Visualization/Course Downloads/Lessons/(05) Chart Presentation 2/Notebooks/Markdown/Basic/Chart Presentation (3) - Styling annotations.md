
# Chart Presentation (3) - Positioning annotation text

In this lesson we'll learn about some further styling options for annotations.

We'll learn how to position the annotation text on the chart with greater precision by using the <code>'textangle'</code>, <code>'xanchor'</code> and <code>'yanchor'</code> options.






 






## Using <code>'xanchor'</code> and <code>'yanchor'</code> to position annotations

We can use the <code>'xanchor'</code> and <code>'yanchor'</code> options to position annotations relative to the point at which they were placed, binding the x (or y) position to the top/bottom/left/right/middle/center of the annotation.

- <code>'xanchor'</code> positions the annotation horizontally and can take the following values:
    - <code>'left'</code> - the left-most part of the annotation lines up with the specified position (moves the annotation right)
    - <code>'center'</code> - the horizontal centre of the annotation lines up with the specified position
    - <code>'right'</code> - the right-most part of the annotation lines up with the specified position (moves the annotation left)
    - <code>'auto'</code> - works like 'center' when positioning annotations on according to a data point
  
  
- <code>'yanchor'</code> positions the annotation vertically and can take the following values:
    - <code>'top'</code> - the top-most part of the annotation lines up with the specified position (moves the annotation down)
    - <code>'middle'</code> - the vertical centre of the annotation lines up with the specified position
    - <code>'bottom'</code> - the bottom-most part of the annotation lines up with the specified position (moves the annotation up)
    - <code></code>'auto' - works like 'middle' when positioning annotations on according to a data point

Let's see this in action.

We're going to make a trace with a single point which will also act as the annotation's anchor point; we will then find out how to move the annotation relative to this point by using the <code>'xanchor'</code> and <code>'yanchor'</code> options.


```python
trace = [{'type' : 'scatter',
         'x' : [5],
         'y' : [5],}]
layout = {'annotations' : [{'text' : 'Testing',
                          'xref' : 'x',
                          'yref' : 'y',
                           'x' : 5,
                           'y' : 5,
                           'showarrow' : False,
                           'font' : {'size' : 16}}]}
fig = {'data' : trace, 'layout' : layout}
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-0.png)```





Let's try varying the <code>'xanchor'</code> and <code>'yanchor'</code> values:


```python
fig['layout']['annotations'][0].update({'xanchor' : 'left'})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-1.png)``






```python
fig['layout']['annotations'][0].update({'yanchor' : 'bottom'})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-2.png)`






```python
fig['layout']['annotations'][0].update({'xanchor' : 'right'})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-3.png)





You can see how these two options give us a grid of 9 spaces where we can place the text around the the central point.

## Using <code>'textangle'</code>

We can specify the <code>'textangle'</code> to change the angle at which the text is drawn in relation to the horizontal (0). <code>'textangle'</code> must be an integer:


```python
fig['layout']['annotations'][0].update({'textangle' : 45})
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-4.png)





```python
fig['layout']['annotations'][0].update({'textangle' : 90})
pyo.iplot(fig)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Styling%20annotations/pyo.iplot-5.png)



You can see how this rotates the text around the anchor point, taking into account the xanchor and yanchor options.

