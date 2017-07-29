
# Chart Presentation (1) - Styling the global font

In this lesson we're going to learn how to apply styling options to text displayed in Plotly. Text can be displayed on the chart as a datapoint, on the chart as an annotation, in the legend, as a ticklabel, or as an axis or chart title.

In this lesson we'll learn how to set the global font on the chart, learning about the styling options and how this affects each type of chart text.






 






## Styling text

By setting the global font we can style the font colour, font family and font size. In each case, the styling options are contained in a dictionary within the layout:
````python
{'font' : {'color' : <HTML colour representation>,
            'family' : <HTML font family (only some available)>,
            'size' : <integer >= 1>}}
````

The most restrictive of these options in the <code>'family'</code> option. Plotly has a number of fonts installed on their server, including:
- Arial
- Balto
- Courier New
- Droid Sans
- Droid Serif
- Droid Sans Mono
- Times New Roman

However in practise these fonts don't often work on every machine. For this reason, I suggest sticking to Arial, Courier New or Times New Roman.

Let's now look at how the styling options affect text on a chart by creating a dummy chart with each of the types of text, and trying out some different styling options:

### Making the chart

Here's our dummy chart which contains each type of text: text as a data point, annotation text, ticklabels, axis titles, chart title and a legend:


```python
traces = [{'type' : 'scatter',
          'mode' : 'text',
          'x' : [1,2,3,4,5],
          'y' : [1,2,3,4,5],
          'text' : ['apples','oranges','pears','bananas','cherries'],
          'name' : 'Fruit'},
         {'type' : 'scatter',
          'mode' : 'text',
          'x' : [10,9,8,7,6],
          'y' : [10,9,8,7,6],
          'text' : ['cheddar','stilton','monterey jack','edam','wensleydale'],
          'name' : 'Cheese'}]

layout = {'title' : 'Cheese and Fruits',
         'xaxis' : {'title' : 'Who likes fruit?'},
         'yaxis' : {'title' : 'Who likes cheese?'},
         'annotations' : [{'text' : 'The perfect combination of fruit and cheese',
                          'xref' : 'x',
                          'yref' : 'y',
                          'x' : 11,
                          'y' : 1,
                          'showarrow' : False}]}
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20global%20font/pyo.iplot-0.png)```





Let's now set the global <code>'font'</code> within the <code>'layout'</code>. I'm going to start by setting the <code>'color'</code> to a dark grey, and the <code>'family'</code> to a Serif font.

The default font <code>'size'</code> is <code>12</code>, and each separate text item inherirts its size from this number:


```python
textStyling = {'color' : '#333',
              'family' : 'Times New Roman',
              'size' : 12}

fig['layout']['font'] = textStyling

pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20global%20font/pyo.iplot-1.png)``





I'm going to try a slightly darker colour, and a more modern font family:


```python
textStyling = {'color' : '#292929',
              'family' : 'Arial',
              'size' : 12}

fig['layout']['font'] = textStyling

pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20global%20font/pyo.iplot-2.png)`





Let's try changing the global <code>'font'</code> <code>'size'</code> to see the effect this has on the chart:


```python
textStyling = {'color' : '#333',
              'family' : 'Droid Serif, Raleway,Times New Roman',
              'size' : 20}

fig['layout']['font'] = textStyling

pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(1)%20-%20Styling%20the%20global%20font/pyo.iplot-3.png)





You can see that each different text option has changed size relative to the global font size.

