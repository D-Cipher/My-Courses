
# Chart Presentation (7) - Changing subplot options

We'll now move away from annotations for a couple of lessons and instead learn some different ways we can control the Plotly sub-plots figure.

In this lesson we'll see how to change the horizontal and vertical spacing between the different plots within the subplots object.



#### New Modules:

We'll import the <code>subplots</code> library:



from plotly.tools import make_subplots



```python

 
```





## Making a subplots object

We're going to make a dummy subplots object which we'll use to demonstrate changing the horizontal and vertical spacing:


```python
testFig = make_subplots(rows = 2, cols = 2)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





## Changing the horizontal spacing

The easiest way of changing the horizontal and vertical spacing of the subplots object is by using the <code>horizontal_spacing</code> and <code>vertical_spacing</code> options. Each of these options requires a float between 0 and 1:


```python
testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-1.png)``

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





You can see that setting <code>horizontal_spacing</code> to 0 moves the subplots next to each other on the horizontal axis. Likewise, setting it to 1 moves them further apart:


```python
testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0.95)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-2.png)`

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





We probably wouldn't want to ever make a plot like this, but you can now see the range of values available. Let's return it to the default of 0.2:


```python
testFig = make_subplots(rows = 2, cols = 2,
                       horizontal_spacing = 0.2)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-3.png)

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





## Changing the vertical spacing
Let's now change the vertical spacing between the different charts on the subplots object. 

We'll first set it to the minimum value of 0:


```python
testFig = make_subplots(rows = 2, cols = 2,
                       vertical_spacing = 0)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-4.png)
    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





This has the expected effect of moving the plots closer together in the vertical dimension.

Increasing this to a value near the maximum produces the following result:


```python
testFig = make_subplots(rows = 2, cols = 2,
                       vertical_spacing = 0.95)
testFig.append_trace({'type' : 'scatter',
                     'mode' : 'markers',}, row = 1, col = 1)
pyo.iplot(testFig)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(7)%20-%20Changing%20subplot%20options/pyo.iplot-5.png)    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





So once agains, we're unlikely to ever make a plot that looks like this, but this should give you some idea of the magnitude of the effect you expect from manipulating the <code>vertical_spacing</code> option.

