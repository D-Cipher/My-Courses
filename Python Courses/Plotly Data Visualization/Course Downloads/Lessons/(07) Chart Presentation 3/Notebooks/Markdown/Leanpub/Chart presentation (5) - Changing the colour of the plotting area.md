
# Chart presentation (5) - Changing the colour of the plotting area

In this lesson we're going to learn how to change the colour of the plotting area. This is especially useful for if you need to align the presentation of your charts with a specific theme or brand.






 






## Options for changing the colour.

There are two colours we can change; the <code>'paper_bgcolor'</code> and the <code>'plot_bgcolor'</code>. 

<code>'paper_bgcolor'</code> changes the colour of the area around the plotting area, whilst <code>'plot_bgcolor'</code> changes the colour of the background of the plotting area. Just to keep things interesting, let's test this on a different chart to the one that we've been using.


```python
lifeExp = py.get_figure('rmuir', 225)
pyo.iplot(lifeExp)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Changing%20the%20colour%20of%20the%20plotting%20area/pyo.iplot-0.png)```





Let's change the <code>'paper_bgcolor'</code> first. I'm going to change it to an off-white colour:


```python
lifeExp['layout'].update({'paper_bgcolor' : '#faebd7'})
pyo.iplot(lifeExp)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Changing%20the%20colour%20of%20the%20plotting%20area/pyo.iplot-1.png)``





You can see how this changes the colour for everything but the plotting area. We can now change the colour within the plotting area:


```python
lifeExp['layout'].update({'plot_bgcolor' : '#faebd7'})
pyo.iplot(lifeExp)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Changing%20the%20colour%20of%20the%20plotting%20area/pyo.iplot-2.png)`





You can see that by changing the background colour of the chart, it would be very easy to make it fit seamlessly into a theme on a website or in a report.

I'm going to send this to the Plotly cloud:


```python
py.plot(lifeExp, filename="Life expectancy and GDP per capita (coloured background)", fileopt='overwrite')
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(5)%20-%20Changing%20the%20colour%20of%20the%20plotting%20area/py.plot-0.png)




    'https://plot.ly/~rmuir/257'



