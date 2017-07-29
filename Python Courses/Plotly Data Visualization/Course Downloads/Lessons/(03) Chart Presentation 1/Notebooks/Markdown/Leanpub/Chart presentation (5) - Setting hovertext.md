
# Chart presentation (5) - Setting hovertext

In the last lesson we saw how to set specific ticklabels on the axis. 

In this lesson we'll find out how to set the hovertext and control what is displayed when a user hovers over a point on the chart.

Hovertext is one of the best features about Plotly; it's this functionality which sets it apart from static charts. Without hovertext, a user who noticed an interesting data point would have to consult a table to find the values of that data point, or read through the description of the chart to see if there is an explanation for it. With hovertext, you can provide this information directly to the user when they hover their mouse pointer over a particular data point. Creating hoverinfo which is clear and intuitive is therefore really important when creating charts with Plotly.






 






## Setting and controlling hovertext

There are three elements that we can manipulate to control what is displayed when a user moves their mouse over a particular data point.

The first is the <code>'text'</code> element contained within each trace object. This allows you to choose exactly what words and numbers are displayed when a user moves their mouse over a point. This attribute expects a list of values the same length as the x- and y-values. In the example below, each point of data would have one of the letters a-e attributed to it:

````python
trace = {'x' : [1,2,3,4,5],
        'y' : [1,2,3,4,5],
        'text' : ['a','b','c','d','e'],
        'type' : 'scatter'}
````        

The second element which controls the hovertext is also contained within the trace. The <code>'hoverinfo'</code> element  determines which information appears when the user moves their mouse over a data point. It differs from the <code>'text'</code> attribute in that it doesn't allow you to choose the exact number and letters which are displayed, merely a more high-level view. This attribute expects a string:
````python
trace = {'hoverinfo' : <'x', 'y', 'z', 'text', 'name' (or any joined with a '+'), 'all', 'none'>}
````

The potential values for <code>'hoverinfo'</code> have the following effects:
- <code>'x'</code> : shows the x-values of the data over the x-axis
- <code>'y'</code> : shows the y-values of the data at the point of hover
- <code>'z'</code> : shows the z-values of the data at the point of hover (3d charts only)
- <code>'text'</code> : shows the information contained in the <code>'text'</code> attribute at the point of hover
- <code>'name'</code> : shows the name of the trace
- <code>'all'</code> : shows all the information (except the name)
- <code>'none'</code> : shows nothing

You can select multiple hover options by concatenating them together with a '+':
- <code>'text+x'</code> : shows the information contained in the <code>'text'</code> attribute and the x-values

We'll investigate these different options using some dummy data before discussing the third element which controls hover info.


```python
trace = {'type' : 'scatter',
        'mode' : 'lines',
        'x' : [1,2,3,4,5,6,7,8,9],
        'y' : [4,9,6,7,5,8,1,3,2],
        'text' : ['a','b','c','d','e','f','g','h','i','j'],
        'name' : 'Testing Trace'}
pyo.iplot([trace])

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Setting%20hovertext/pyo.iplot-0.png)```





You can see that the default behaviour is for Plotly to show the x-value at the x-axis, and the y-value and text attribute at the hoverpoint. We can get this functionality by setting the <code>'hoverinfo'</code> to <code>'text+x+y'</code>.

I'll use a function to update the hoverinfo each time:


```python
def updateHoverInfo(info):
    trace.update({'hoverinfo' : info})
    pyo.iplot([trace])
 
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Setting%20hovertext/pyo.iplot-1.png)   
updateHoverInfo('text+x+y')
```





Let's try some different values for <code>'hoverinfo'</code>. This shows only the x-values:


```python
updateHoverInfo('x')
```





This shows only the y-values:


```python
updateHoverInfo('y')
```





This shows only the name of the trace:


```python
updateHoverInfo('name')
```





And this shows only the text attribute:


```python
updateHoverInfo('text')
```





And this shows nothing:


```python
updateHoverInfo('none')
```





This shows everything apart from the trace name:


```python
updateHoverInfo('all')
```





## Changing how the hovertext is displayed

The third element which controls the hovertext is contained within the layout. The <code>'hovermode'</code> attribute controls which hover info the user sees depending on the location of their mouse pointer relative to the points. It also changes which value is displayed on the axis and which is displayed near the mouse pointer.
````python
layout = {'hovermode' : <'x', 'y', 'closest' or False>}
````

This attribute expects a string which can take one of three values:
- <code>'x'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's x-position, x-value is displayed on the axis
- <code>'y'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's y-position, y-value is displayed on the axis
- <code>'closest'</code> : shows the hoverinfo relating to the point closest to the mouse pointer's x- and y-positions
- <code>'False'</code> : No hoverinfo

Let's create a layout and a Figure object and learn how changing the <code>'hovermode'</code> affects our chart:


```python
layout = {'hovermode' : 'x'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Setting%20hovertext/pyo.iplot-2.png)`





The hoverinformation that is shown hasn't changed, but you can see that where it is shown depends on the location of the mouse pointer relative to the x-axis. Let's set <code>'hovermode'</code> to <code>'y'</code>:


```python
layout = {'hovermode' : 'y'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Setting%20hovertext/pyo.iplot-3.png)





You can see that the information shown now depends on the y-position of the cursor. The y-value is now shown next to the axis, rather than the left.

Finally, let's set <code>'hovermode'</code> to <code>'closest'</code>:


```python
layout = {'hovermode' : 'closest'}
fig = Figure(layout = layout, data = [trace])
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Setting%20hovertext/pyo.iplot-4.png)




This now only shows the hover information when the mouse moves near a point. Furthermore, the hoverinfo which is shown is all contained near the data point.

