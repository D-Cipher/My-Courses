
# Chart Presentation (4) - Changing the orientation of the legend

In this lesson we're going to find out how to change the orientation of the legend from vertical to horizontal. This can be useful when you have legend items with long names, and limited horizontal space in which to place the chart. Placing the legend items above or below the chart can give you more options when styling your chart to make it clear to your user.






 






## Changing the orientation of the legend

We can change the orientation of the legend by setting the <code>'orientation'</code> parameter to either <code>'h'</code>, for a horizontally-oriented legend, or <code>'v'</code> for a vertically-oriented legend. The default setting is <code>'v'</code>.

Let's get the chart that we made in the previous lesson to practise on:


```python
stacked = py.get_figure("rmuir", 259)
pyo.iplot(stacked)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Changing%20the%20orientation%20of%20the%20legend/pyo.iplot-0.png)```





Let's now change the orientation of the legend to horizontal. You can see how Plotly has retained the legend grouping when moving the legend to horizontal:


```python
stacked['layout']['legend'].update({'orientation' : 'h'})
pyo.iplot(stacked)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Changing%20the%20orientation%20of%20the%20legend/pyo.iplot-1.png)``





I'll now remove the grouping using <code>'traceorder'</code>. This shows the legend items in a long line:


```python
stacked['layout']['legend'].update({'traceorder' : 'normal'})
pyo.iplot(stacked)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Changing%20the%20orientation%20of%20the%20legend/pyo.iplot-2.png)`





This legend isn't positioned very well, let's improve this! I used trial and error to find the best position for it:


```python
stacked['layout']['legend'].update({'y' : 1.125})
pyo.iplot(stacked)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Changing%20the%20orientation%20of%20the%20legend/pyo.iplot-3.png)





Part of the legend item for the line trace is now chopped off. We need to increase the width of the chart to account for this:


```python
stacked['layout'].update({'width' : 1050})
pyo.iplot(stacked)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Changing%20the%20orientation%20of%20the%20legend/pyo.iplot-4.png)




