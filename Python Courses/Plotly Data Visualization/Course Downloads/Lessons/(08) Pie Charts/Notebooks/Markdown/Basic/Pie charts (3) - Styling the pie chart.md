
# Pie charts (3) - Styling the pie chart

In this lesson we're going to find out how to change the colour and outlines of the segments in our pie chart. This is useful becuase it allows us to style our pie charts to be in keeping with the rest of the charts we make.






 






## Getting the chart

We'll load the chart that we made last lesson:


```python
ethPie = py.get_figure("rmuir", 263)
pyo.iplot(ethPie)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(3)%20-%20Styling%20the%20pie%20chart/pyo.iplot-0.png)```





We can change the colour of the individual segments by passing a list of colours into the trace:


```python
ethPie['data'][0].update({'marker' : {'colors' : ["rgb(12,192,170)", 
                                                  "rgb(190,252,250)", 
                                                  "rgb(77,194,84)", 
                                                  "rgb(211,238,128)", 
                                                  "rgb(97,167,193)"]}})

pyo.iplot(ethPie)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(3)%20-%20Styling%20the%20pie%20chart/pyo.iplot-1.png)``





We can also change the width and colour of the line that surrounds each segment:


```python
ethPie['data'][0]['marker'].update({'line' : {'color' : '#333',
                                             'width' : '1'}})
pyo.iplot(ethPie)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(3)%20-%20Styling%20the%20pie%20chart/pyo.iplot-2.png)`





Changing these parameters is a very easy way of making some big changes to the presentation of the chart. Let's send this to the Plotly cloud:


```python
py.plot(ethPie, filename="Ethnicity of UK students (styled)", fileopt = "overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(3)%20-%20Styling%20the%20pie%20chart/py.plot-0.png)




    'https://plot.ly/~rmuir/265'



