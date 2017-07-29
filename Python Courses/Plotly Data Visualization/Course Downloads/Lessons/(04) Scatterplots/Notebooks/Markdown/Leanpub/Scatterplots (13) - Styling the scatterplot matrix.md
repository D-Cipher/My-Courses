
# Scatterplots (13) - Styling the scatterplot matrix

In this lesson we're going to style the scatterplot matrix that we created in the last lesson.

We're going to learn how to change the dimensions of the chart, set subplot titles and manipulate each of the x- and y-axes of the subplots object. This will allow us to make sure that any mulitple plots that we create using the Plotly subplots function are clear and well-presented.



We're going to import the tools library again:



from plotly import tools



```python

 
```





## Getting the chart  
We'll copy the code from the previous chart that we created rather than load it from the Plotly cloud because we're going to make the changes from inside the loop which creates the chart:


```python
iris = pd.read_csv("http://www.richard-muir.com/data/public/csv/irisDataset.csv", index_col = 0)
irisSpeciesUnique = list(iris['Species'].unique())
colours = ['green','blue','orange']
colourLookup = dict(zip(irisSpeciesUnique, colours))

fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour},
                                 'name' : species},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]    [ (1,2) x2,y2 ]    [ (1,3) x3,y3 ]    [ (1,4) x4,y4 ]  
    [ (2,1) x5,y5 ]    [ (2,2) x6,y6 ]    [ (2,3) x7,y7 ]    [ (2,4) x8,y8 ]  
    [ (3,1) x9,y9 ]    [ (3,2) x10,y10 ]  [ (3,3) x11,y11 ]  [ (3,4) x12,y12 ]
    [ (4,1) x13,y13 ]  [ (4,2) x14,y14 ]  [ (4,3) x15,y15 ]  [ (4,4) x16,y16 ]
    
    





The first thing we'll do is only show one legend item for each trace. We'll do this by creating a <code>'legendgroup'</code> for each species, and setting <code>'showlegend'</code> to <code>True</code> only for the first trace in each group.

At this point I'm also going to reduce the marker size on the traces:


```python
fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/pyo.iplot-1.png)``

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]    [ (1,2) x2,y2 ]    [ (1,3) x3,y3 ]    [ (1,4) x4,y4 ]  
    [ (2,1) x5,y5 ]    [ (2,2) x6,y6 ]    [ (2,3) x7,y7 ]    [ (2,4) x8,y8 ]  
    [ (3,1) x9,y9 ]    [ (3,2) x10,y10 ]  [ (3,3) x11,y11 ]  [ (3,4) x12,y12 ]
    [ (4,1) x13,y13 ]  [ (4,2) x14,y14 ]  [ (4,3) x15,y15 ]  [ (4,4) x16,y16 ]
    
    





## Styling the subplots object

First of all, we'll set the plots to have shared x- and y-axes. This will make the plot look a lot cleaner and reduce the quantity of lines and numbers inbetween the subplots:


```python
fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True, shared_xaxes = True, shared_yaxes = True)

for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/pyo.iplot-2.png)`

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]  [ (1,3) x3,y1 ]  [ (1,4) x4,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]  [ (2,3) x3,y2 ]  [ (2,4) x4,y2 ]
    [ (3,1) x1,y3 ]  [ (3,2) x2,y3 ]  [ (3,3) x3,y3 ]  [ (3,4) x4,y3 ]
    [ (4,1) x1,y4 ]  [ (4,2) x2,y4 ]  [ (4,3) x3,y4 ]  [ (4,4) x4,y4 ]
    
    





## Changing the axis titles
We now need to add titles to the axes to inform the user which dimensions are being compared. We only need to add y-axis titles to the left-most axes and x-axis titles to the bottom-most axes. We can see from the output from the <code>'print_grid'</code> option that the axes we need to select are:
- x1, x2, x3 & x4
- y1, y2, y3 & y4

Let's add this into our loop. We'll update each axis object inside the layout as we reach the correct position in the loop. We'll update the axis object with the axis title and a new range so that all of the traces are displayed on the scame scale:


```python
fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True, shared_xaxes = True, shared_yaxes = True)

for i, column in enumerate(iris.columns[:-1]):
    fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column + " (cm)",
                                              'range' : [0, max(iris[iris.columns[:-1]].max())]})
    
    for j, row in enumerate(iris.columns[:-1]):
        fig['layout']['yaxis{}'.format(j + 1)].update({'title' : row + " (cm)",
                                                  'range' : [0, max(iris[iris.columns[:-1]].max())]})
        
        if column != row:
            if i == 0 and j == 1:
                show = True
            else:
                show = False
                
            for species, colour in colourLookup.items():
                fig.append_trace({'type' : 'scatter',
                                 'mode' : 'markers',
                                 'x' : iris.loc[iris['Species'] == species, column],
                                  'y' : iris.loc[iris['Species'] == species, row],
                                 'marker' : {'color' : colour,
                                            'size' : 3},
                                 'name' : species,
                                 'legendgroup' : species,
                                 'showlegend' : show},
                                col = i + 1, row = j + 1)
                
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/pyo.iplot-3.png)

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]  [ (1,3) x3,y1 ]  [ (1,4) x4,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]  [ (2,3) x3,y2 ]  [ (2,4) x4,y2 ]
    [ (3,1) x1,y3 ]  [ (3,2) x2,y3 ]  [ (3,3) x3,y3 ]  [ (3,4) x4,y3 ]
    [ (4,1) x1,y4 ]  [ (4,2) x2,y4 ]  [ (4,3) x3,y4 ]  [ (4,4) x4,y4 ]
    
    





The axis titles are looking a bit squashed, let's change the height of the chart to give a bit more space. I'll also take this opportunity to set the chart title and hover behaviour:


```python
fig['layout'].update({'title' : 'Length and width of sepals and petals for Iris supspecies',
                     'height' : 1000})
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/pyo.iplot-4.png)




So this chart has come out looking really well. We've added some axis titles and stretched the chart out a bit to give a bit more space. Let's push it to the Plotly cloud:


```python
py.plot(fig, filename="Iris scatterplot matrix", fileopt = 'overwrite')
```


![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(13)%20-%20Styling%20the%20scatterplot%20matrix/py.plot-0.png)


    'https://plot.ly/~rmuir/220'



