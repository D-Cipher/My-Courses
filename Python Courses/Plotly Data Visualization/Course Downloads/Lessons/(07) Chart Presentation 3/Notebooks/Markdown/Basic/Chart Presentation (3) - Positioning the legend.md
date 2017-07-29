
# Chart Presentation (3) - Positioning the legend

In this lesson we're going to learn how to position the legend. The legend can be positioned in the same way that we position annotations - by setting an x- and y-position.






 






## Changing the x- and y-values for the legend position

The legend is always positioned using normalised coordinates; that is, we don't position the legend relative to any data items, instead positioning it relative to the chart. 

The x- and y-values for the normalised coordinates can be between -2 and 3, with the coordinate (0, 0) positioning the legend at the bottom-left corner of the chart.

Let's load a chart and practise moving the legend:


```python
stacked = py.get_figure("rmuir", 255)
pyo.iplot(stacked)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Positioning%20the%20legend/pyo.iplot-0.png)```





We'll first change the x-values for the legend position. By setting the x-value to the maximum (3), we move the legend far away from the chart, squashing the chart up. This doesn't look great.


```python
stacked['layout']['legend'].update({'x' : 3})
pyo.iplot(stacked)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Positioning%20the%20legend/pyo.iplot-1.png)``





By setting the x-value to the minimum (-2), the same happens, but the legend moves to the left instead.


```python
stacked['layout']['legend'].update({'x' : -2})
pyo.iplot(stacked)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Positioning%20the%20legend/pyo.iplot-2.png)`





By setting the x-value to 0, we line the legend up with the y-axis (where x = 0). Note that the legend obscures the chart when it is placed over it. This might work for a scatterplot where there are no points plotted in the top-left corner, but it doesn't work here.


```python
stacked['layout']['legend'].update({'x' : 0})
pyo.iplot(stacked)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Positioning%20the%20legend/pyo.iplot-3.png)





Let's move the legend down by changing the y-value to position the legend underneath the chart:


```python
stacked['layout']['legend'].update({'y' : -1})
pyo.iplot(stacked)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(3)%20-%20Positioning%20the%20legend/pyo.iplot-4.png)




