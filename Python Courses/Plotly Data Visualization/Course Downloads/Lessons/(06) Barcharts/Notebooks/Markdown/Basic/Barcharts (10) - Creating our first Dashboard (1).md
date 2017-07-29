
# Barcharts (10) - Creating our first Dashboard (1)

In this lesson we're going to create our first dashboard. We're going to take the subplots template object that we created at the end of the last section and populate it with three different charts.

We're going to include the stacked proportional barchart that shows the number of meteorites by continent as well as two new charts. The first will display a time series line chart of the number of meteorites found in different weight categories each year, and the second will be a scatterplot showing the different weights of the different types of meteorite.



We'll use the Plotly sub-plots module:



from plotly.tools import make_subplots



```python

 
```





## Getting our subplots 'skeleton'

We'll copy the code which we wrote at the end of the last section and use the resulting subplots object as the skeleton into which we'll insert our charts.

We'll take this opportunity to add the titles to our plots. We pass a list of strings to <code>subplot_titles</code>; each title corresponds to a different subplot, from top left to bottom right.


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]],
                   subplot_titles = ["Types of meteorite by weight", 
                                     "Number of meteorites by continent",
                                     "Weight categories of meteorite",
                                    ])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(10)%20-%20Creating%20our%20first%20Dashboard%20(1)/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1           -      ]  [ (1,3) x2,y2 ]
           |                |                |       
    [ (3,1) x3,y3           -                -      ]
    
    





## Adding a chart to the subplots skeleton

Let's now retrieve the stacked proportional area plot from the Plotly cloud. We'll need to strip the data from it and append those traces to the subplots object. 

I think this plot will fit best in the right-most space, but in order to make it fit well, we'll change the orientations of the bars from vertical to horizontal. This also means we need to switch the x- and y-values round:


```python
stacked = py.get_figure("rmuir", 241)
for d in stacked['data']:
    xVals = d['y']
    yVals = d['x']
    d.update({'orientation' : 'h',
             'x' : xVals,
             'y' : yVals})
    fig.append_trace(d, row = 1, col = 3)
    
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(10)%20-%20Creating%20our%20first%20Dashboard%20(1)/pyo.iplot-1.png)``





### Styling this chart
Let's now add the chart and axis titles and some of the other styling options which exist on the main chart.

Note that by changing <code>'barmode'</code> to <code>'stack'</code>, all of the bar charts on this subplot will be stacked; this is one limitation of using a subplots object to make a dashboard.

I think we should also increase the height of the chart.


```python
fig['layout']['xaxis2'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

fig['layout'].update({'barmode' : 'stack',
                      'height' : 1000})

pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(10)%20-%20Creating%20our%20first%20Dashboard%20(1)/pyo.iplot-2.png)`





This chart isn't quite finished yet, but we'll return to it in the next lesson.

