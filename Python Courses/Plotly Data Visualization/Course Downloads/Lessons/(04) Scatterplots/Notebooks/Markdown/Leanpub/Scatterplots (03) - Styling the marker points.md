
# Scatterplots (03) - Styling the marker points

In this lesson we're going to learn how to apply different styling options to  the marker points. We've already briefly touched upon this in the lineplots section, however in this lesson we'll take a more in-depth look at the styling options available.

In the lineplots section, the aim of utilising the marker styling options was to enable us to distinguish between the different data points, however this lesson will focus more on the stylistic aspect of manipulating the marker symbols - let's make them look GOOD!

We'll quickly review the available marker symbol shapes, then find out how to change their size, opacity, colour and outline.






 






## Getting a chart
We'll use the same chart that we made in the previous lesson:


```python
revEmp = py.get_figure("rmuir", 200)
pyo.iplot(revEmp)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-0.png)```





### Changing the marker symbols
Let's quickly review how to change the marker symbol on this scatterplot. Through the use of different marker symbols we can allow the reader to discern between two different categories on the same plot. These categories are often distinguished through the use of colour, but using different marker symbols accounts for those times when the colour is not sufficient (black and white printing, colour-blindness etc).

You can find a list of the available symbols <a href="https://plot.ly/python/reference/#scatter-marker-symbol">here</a>.

To change the marker symbol we need to change the <code>'symbol'</code> option within the <code>'marker'</code> dictionary. 
````python
trace = {'marker' : {'symbol' : <symbol string or numer>}}
````
Marker symbols are represented by a string or a number, and there are four different stying options available (although not every marker symbol has all available styling options):
- solid (default)
- open
- dot
- open-dot



Let's try out a few of these marker symbols and see how they look on the chart:


```python
revEmp['data'][0].update({'marker' : {'symbol' : 'square'}})
pyo.iplot(revEmp)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-1.png)``






```python
revEmp['data'][0].update({'marker' : {'symbol' : 'square-open'}})
pyo.iplot(revEmp)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-2.png)`






```python
revEmp['data'][0].update({'marker' : {'symbol' : 'triangle-left'}})
pyo.iplot(revEmp)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-3.png)





I'll change the marker symbols on this chart back to 'circle', but you can explore your own options for the marker symbols to create your own style for your charts.


```python
revEmp['data'][0].update({'marker' : {'symbol' : 'circle'}})
pyo.iplot(revEmp)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-4.png)




### Changing marker size, opacity and colour

Plotly allows us to control different aspects of the marker style. We can change the size, opacity and colour by manipulating different options within the marker dictionary:
````python
trace = {'marker' : {'opacity' : <number between 0 and 1 inclusive>,
                     'size' : <number >= 0>,
                     'color' : <a colour name, hex, rgb or rgba value>}}
````                     

#### Marker size

Let's see how we can change the marker size. I've increased the size to 8 (the default is 6) because I'd like the styling of the points to be clear. There's some overplotting here, but we can make this obvious by changing the opacity of the marker point


```python
revEmp['data'][0].update({'marker' : {'size' : '8'}})
pyo.iplot(revEmp)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-5.png)



#### Marker opacity

We'll now change the marker opacity; the markers are currently totally opaque, but I find that adding a slight opacity to the marker symbols can greatly enhance the look of a chart:


```python
revEmp['data'][0].update({'marker' : {'opacity' : '0.7'}})
pyo.iplot(revEmp)
```



![pyo.iplot-6](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-6.png)


#### Changing the colour

I'm going to change the colour to something a little different to the standard Plotly blue:


```python
revEmp['data'][0].update({'marker' : {'color' : '#6A5ACD'}})
pyo.iplot(revEmp)
```




![pyo.iplot-7](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-7.png)

## Changing the marker line

Every marker can have an outline, and Plotly allows us very fine control over the appearance of this line. We're only going to look at the line width and colour. Because we've set our points to be slightly transparent, adding a dark outline to them will really make them stand out. I chose the width of this line after some trial and error, but feel free to spend some time developing your own style.


```python
revEmp['data'][0].update({'marker' : {'line' : {'width' : 1.25, 'color' : 'black'}}})
pyo.iplot(revEmp)
```





![pyo.iplot-8](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/pyo.iplot-8.png)
I'm going to push this chart to the Plotly cloud:


```python
py.plot(revEmp, filename="Revenue by number of employees (styled)", fileopt = "overwrite")
```




 
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(03)%20-%20Styling%20the%20marker%20points/py.plot-0.png)   'https://plot.ly/~rmuir/202'



