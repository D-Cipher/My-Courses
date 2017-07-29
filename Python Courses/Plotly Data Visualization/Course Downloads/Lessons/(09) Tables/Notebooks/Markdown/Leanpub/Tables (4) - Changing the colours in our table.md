
# Tables (4) - Changing the colours in a table

In this lesson we're going to learn how to change the colours in our table. This is useful because it allows us to style our table to fit the theme of other charts we produce.



#### New Modules:

Not forgetting the FigureFactory!



from plotly.tools import FigureFactory as FF



```python

 
```





## Getting a table to practise on

Let's get the chart we created in the last lesson:


```python
table = py.get_figure("rmuir", 313)
pyo.iplot(table)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(4)%20-%20Changing%20the%20colours%20in%20our%20table/pyo.iplot-0.png)```





## How are the colours set on this table?

We learnt previously that a Plotly table is actually made from a heatmap. There are certain parameters in the Plotly heatmap that control what colour a particular section is.

We don't need to learn how to make a heatmap to change these, but let's look at the data part of our table and find out how the colour is specified: 


```python
table['data']
```




    [{'colorscale': [[0, '#00083e'], [0.5, '#ededee'], [1, '#ffffff']],
      'hoverinfo': 'none',
      'opacity': 0.75,
      'showscale': False,
      'type': 'heatmap',
      'z': [[0, 0, 0, 0, 0, 0],
       [0, 0.5, 0.5, 0.5, 0.5, 0.5],
       [0, 1, 1, 1, 1, 1],
       [0, 0.5, 0.5, 0.5, 0.5, 0.5],
       [0, 1, 1, 1, 1, 1]],
      'zsrc': 'rmuir:314:'}]



You can see that the data items have a <code>'colorscale'</code> specifed, and that this colorscale is a list of three lists. The first list links together a colour with the value 0, the second links a colour to the value 0.5, and the third links a colour to the value 1.


```python
table['data'][0]['colorscale']
```




    [[0, '#00083e'], [0.5, '#ededee'], [1, '#ffffff']]



Now, when we look at the <code>'z'</code> parameter within the data, you will notice that this is a list of lists, each populated by one of three numbers: 0, 0.5 and 1.

Each list within the <code>'z'</code> parameter relates to a row on the table. The first list in the <code>'z'</code> parameter is populated entirely by zeroes. The cells in the top row therefore all have the colour <code>'#00083e'</code>.

The second list in the <code>'z'</code> parameter has a 0, which relates to the first column, followed by five 0.5 values. This means that the first cell in the second row (the index cell) is dark in colour (<code>'#00083e'</code>), whilst the other cells in that row are coloured a light grey (<code>'#ededee'</code>).


```python
table['data'][0]['z']
```




    [[0, 0, 0, 0, 0, 0],
     [0, 0.5, 0.5, 0.5, 0.5, 0.5],
     [0, 1, 1, 1, 1, 1],
     [0, 0.5, 0.5, 0.5, 0.5, 0.5],
     [0, 1, 1, 1, 1, 1]]



## Controlling the colours in a table

We can control the colours in the table by changing the colours in the <code>'colorscale'</code> parameter. 

The text in our table has already had the colours set. The text in the header and index is white, whilst the text in the rows is dark. I chose these colours so that they will allow the text to contrast against the background colour.

Let's now change the <code>'colorscale'</code> parameter, remembering that 0 should be a dark colour and 0.5 and 1 specify the colours to be used alternately in the rows:


```python
table['data'][0]['colorscale'] = [[0, "#2f4b4e"],
                                 [0.5, "#86e6ca"],
                                 [1, "#ffffff"]]
pyo.iplot(table)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(4)%20-%20Changing%20the%20colours%20in%20our%20table/pyo.iplot-1.png)``





Let's try a different colour scheme:


```python
table['data'][0]['colorscale'] = [[0, "#a73830"],
                                  [0.5, "#fbcab9"],
                                 [1, "#ffffff"]]
pyo.iplot(table)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(4)%20-%20Changing%20the%20colours%20in%20our%20table/pyo.iplot-2.png)`





