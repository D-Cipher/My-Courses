
# Chart Presentation 2 (8) - Combining subplot grid spaces

In this lesson we're going to learn how to use the <code>'colspan'</code> and <code>'rowspan'</code> options to create a complex subplots object.

We're going to take a 3x3 grid of plots and combine some of them together to fit only three charts into the same space. The plot grid will start out looking like this:
`
+-----+-----+-----+
|     |     |     |
|     |     |     |
+-----------------+
|     |     |     |
|     |     |     |
+-----------------+
|     |     |     |
|     |     |     |
+-----+-----+-----+

`
And finish looking like this:
````python
+-----+-----+-----+
|           |     |
|           |     |
+           +     +
|           |     |
|           |     |
+-----------------+
|                 |
|                 |
+-----+-----+-----+

````
We'll create this as a skeleton subplots object, and I'll leave it to you to populate it with data - please post the results in the comments section!



#### New Modules:

We'll import the Plotly subplots module again:


```python
from plotly.tools import make_subplots
```


```python

 
```





## Making the subplots object
We'll make a subplots object with three rows and 3 columns, append a dummy trace to it and plot it as before:


```python
fig = make_subplots(rows = 3, cols = 3)
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(8)%20-%20Combining%20subplot%20grid%20spaces/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]  [ (1,3) x3,y3 ]
    [ (2,1) x4,y4 ]  [ (2,2) x5,y5 ]  [ (2,3) x6,y6 ]
    [ (3,1) x7,y7 ]  [ (3,2) x8,y8 ]  [ (3,3) x9,y9 ]
    
    





## Combining columns and rows
We can use the special keyword argument <code>'specs'</code> to specify how the rows and columns are combined.

The <code>'specs'</code> parameter acts like a set of instructions which determine the behaviour of each 'cell' in the subplots grid.

The <code>'specs'</code> parameter is made of a list of lists. The indices of the outer list correspond to the rows in the subplots object, whilst the indices of the inner list correspond to columns. The instructions passed to the <code>'specs'</code> parameter must match the shape of the subplots object.

Each item in the list of lists of specs therefore corresponds to a single subplot grid space. 

The <code>'specs'</code> parameter that we will use for this subplots object will be shaped as so:
````python
specs = [[{}, {}, {}],
         [{}, {}, {}],
         [{}, {}, {}]]
````

The spaces in the <code>'specs'</code> parameter will therefore correspond to the following grid spaces:
````python
specs = [[{1, 1}, {1, 2}, {1, 3}],
         [{2, 1}, {2, 2}, {2, 3}],
         [{3, 1}, {3, 2}, {3, 3}]]
````

Let's add the list of specs to our subplot object:



```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {}],
                            [{}, {}, {}],
                            [{}, {}, {}]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(8)%20-%20Combining%20subplot%20grid%20spaces/pyo.iplot-1.png)``

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]  [ (1,3) x3,y3 ]
    [ (2,1) x4,y4 ]  [ (2,2) x5,y5 ]  [ (2,3) x6,y6 ]
    [ (3,1) x7,y7 ]  [ (3,2) x8,y8 ]  [ (3,3) x9,y9 ]
    
    





## Manipulating <code>'colspan'</code> and <code>'rowspan'</code>

Each item in the list of lists of specs corresponds to a single subplot grid space. Each item can be a dictionary or <code>None</code>.

By putting <code>None</code> at that list index, we are telling Plotly that we do no wish to make any changes to that particular space. A dictionary allows us to change certain parameters.

There are several different parameters for the specs, however we will only focus on <code>'rowspan'</code> and <code>'colspan'</code> as these are sufficient for our aims.

Let's make the bottom-left cell on our grid. This will have a <code>colspan</code> of 3. We'll start the <code>colspan</code> in the bottom-left corner and therefore need to set the spec of the cell which will be overwritten (the cell immediately to the right) to <code>None</code>:


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {}],
                            [{}, {}, {}],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(8)%20-%20Combining%20subplot%20grid%20spaces/pyo.iplot-2.png)`

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]  [ (1,3) x3,y3 ]
    [ (2,1) x4,y4 ]  [ (2,2) x5,y5 ]  [ (2,3) x6,y6 ]
    [ (3,1) x7,y7           -                -      ]
    
    





We can now create the right-most cell, which will have a <code>rowspan</code> of two, starting in the top-right corner. The cell directly below it will therefore have a <code>None</code> value:


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{}, {}, {'rowspan' : 2}],
                            [{}, {}, None],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(8)%20-%20Combining%20subplot%20grid%20spaces/pyo.iplot-3.png)

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]  [ (1,3) x3,y3 ]
    [ (2,1) x4,y4 ]  [ (2,2) x5,y5 ]         |       
    [ (3,1) x6,y6           -                -      ]
    
    





Finally we can create the top-left plotting area which will have both a <code>'rowspan'</code> and <code>'colspan'</code> of 2. We'll therefore set the remaining cells to <code>None</code>:


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]])
fig.append_trace({'type' : 'scatter'}, row = 1, col = 1)
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(8)%20-%20Combining%20subplot%20grid%20spaces/pyo.iplot-4.png)
    This is the format of your plot grid:
    [ (1,1) x1,y1           -      ]  [ (1,3) x2,y2 ]
           |                |                |       
    [ (3,1) x3,y3           -                -      ]
    
    





Great, that's our plotting area finished! It's now up to you to fill this template with some beautiful charts! Post your examples in the comments section.

