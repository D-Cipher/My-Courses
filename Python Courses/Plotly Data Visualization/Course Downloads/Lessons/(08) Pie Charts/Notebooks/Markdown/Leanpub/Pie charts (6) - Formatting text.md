
# Pie charts (6) - Formatting text

In this lesson we're going to learn how to position and style the labels on a pie chart.

We'll learn how to control whether the labels sit inside or outside of the segments, as well as how to change the font style separately for labels inside and outside.






 






## Setting the <code>'textposition'</code>

The <code>'textposition'</code> parameter determines whether the labels are drawn inside or outside the segments. It can take one of four values:

- <code>'inside'</code> - all labels are inside the segments
- <code>'outside'</code> - all labels are outside the segments
- <code>'none'</code> - no labels are shown
- <code>'auto'</code> - labels are positioned inside and outside the segment based on their length and the space available inside the segment (we saw this in action in the previous lesson)

Let's get the chart we made in the last lesson and practise moving the labels:



```python
level = py.get_figure("rmuir", 269)
pyo.iplot(level)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-0.png)```





Firstly let's set the <code>'textposition'</code> to <code>'none'</code> to remove the labels. You'll notice that it's probably a good idea to reinstate the legend. We're going to move on quickly, so there's not much point in doing this.


```python
level['data'][0].update({'textposition' : 'none'})
pyo.iplot(level)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-1.png)``





Let's now change <code>'textposition'</code> to <code>'outside'</code>:


```python
level['data'][0].update({'textposition' : 'outside'})
pyo.iplot(level)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-2.png)`





And finally to <code>'inside'</code> (which replicates the effect of setting it to auto for this chart):


```python
level['data'][0].update({'textposition' : 'inside'})
pyo.iplot(level)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-3.png)





## Styling text inside and outside the segments

We'll now look at how to style the text differently depending on if it's inside or outside the segments. This is useful because the colours used in your pie chart may be dark, necessitating light text for the labels inside the segment, whilst still requiring the labels outside to be dark in colour.

Let's practise on the previous pie chart we made showing the ethnicity of UK students:


```python
eth = py.get_figure("rmuir", 267)
pyo.iplot(eth)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-4.png)




We can set the text separately using <code>'outsidetextfont'</code> and <code>'insidetextfont'</code>. Both of these parameters contain a dictionary which allows us to set the font family, colour and size exactly as we have for other types of text.

Let's make the inside text darker and slightly larger, and the outside text much larger. This will make the chart easier to read, whilst also drawing more attention to the segment which we previously pulled out:


```python
eth['data'][0].update({'outsidetextfont' : {'size' : 16},
                      'insidetextfont' : {'color' : 'black',
                                         'size' : 13}})
pyo.iplot(eth)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/pyo.iplot-5.png)



Let's send this styled chart to the Plotly cloud:


```python
py.plot(eth, filename="Ethnicity of UK students (text styled)", fileopt="overwrite")
```



![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(6)%20-%20Formatting%20text/py.plot-0.png)

    'https://plot.ly/~rmuir/271'



