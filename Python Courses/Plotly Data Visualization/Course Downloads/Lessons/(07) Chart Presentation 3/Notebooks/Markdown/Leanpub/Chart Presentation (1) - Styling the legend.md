
# Chart Presentation (1) - Styling the legend

In this third section on chart presentation we'll mainly focus on how to style the legend. We'll see how to colour and position the legend, as well as how to change how the items within it are postioned. Finally, we'll also learn how to change the background colour of our plotting area.

In this lesson we're going to learn how to apply some styling options to the legend. We're going to see how to set a border for the legend and find out how to change the thickness and color of the border. We'll also look at how the set a background colour for the legend.






 






## Styling the legend border

Putting a border around your legend is a great way to visually separate it from your chart. In Plotly we can control the thickness and colour of the legend border. 

Let's grab our stacked bar chart showing meteorite landings per continent and the percentage of meteorites under 101 grams in mass; we'll use this to practise on in this section.


```python
stacked = py.get_figure("rmuir", 251)
pyo.iplot(stacked)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/pyo.iplot-0.png)```





The legend styling options are contained within the layout. We're going to use the <code>bordercolor</code> and <code>borderwidth</code> keys to style the legend's border.

Let's set the borderwidth to 5 to see how that affects the legend:


```python
stacked['layout'].update({'legend' : {'borderwidth' : 5}})
pyo.iplot(stacked)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/pyo.iplot-1.png)``





So that's a bit thick, let's reduce it slighlty:


```python
stacked['layout'].update({'legend' : {'borderwidth' : 2}})
pyo.iplot(stacked)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/pyo.iplot-2.png)`





We can now change the colour the legend border. I'm going to try something a little lighter:


```python
stacked['layout']['legend'].update({'bordercolor' : '#e0e0e0'})
pyo.iplot(stacked)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/pyo.iplot-3.png)





## Changing the background colour for the legend

By changing the background colour of the legend we can force it to stand out even more from the chart. I'm going to set the background colour to be slightly lighter than the border:


```python
stacked['layout']['legend'].update({'bgcolor' : '#ededed'})
pyo.iplot(stacked)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/pyo.iplot-4.png)




By slightly changing background and border colour of the legend we have distinguished it from the rest of the chart. This can be useful if the legend is key to your readers understanding the chart.

I'm going to push this chart to the Plotly cloud:


```python
py.plot(stacked, filename="Meteorites by continent and weight (styled legend)", fileopt="overwrite")
```


![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20legend/py.plot-0.png)


    'https://plot.ly/~rmuir/255'



