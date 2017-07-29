
# Scatterplots (14) - Function for scatterplot matrix

In this lesson we'll take what we learnt in the previous lessons about making scatterplot matrices, and use this to write a function which we can use to create a scatterplot matrix from any DataFrame.

This will be quite a hard lesson, so if you do have problems then please ask in the comments.



We'll import the Plotly tools libaray again:



from plotly import tools


This bit of magic here allows us to view the charts inside an iPython Notebook. When coupled with <code>plotly.offline</code>, this allows us to have a very quick iterative process as we develop and tweak the charts.


```python

 
```





## Making the function

The last time we made a function to generalise the creation of a chart, we passed several variables to that function. We'll do the same for this function, and the variable we'll pass will serve as instructions for how to make the chart. We'll need the following variables in this function.

- df - The DataFrame which contains the data
- scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
- categoricalColumn - the column which contains the categories of data which should be plotted
- colours - a list of colours equal in length to the number of categories in the categoricalColumn
- title - the title of the chart

Once again, we'll test this function at every step and we'll use the iris dataset to make sure that the function outputs what we expect.


```python
iris = pd.read_csv("http://www.richard-muir.com/data/public/csv/irisDataset.csv", index_col = 0)
iris.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal length</th>
      <th>Sepal width</th>
      <th>Petal length</th>
      <th>Petal width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
  </tbody>
</table>
</div>



Let's start by passing the variables that we need into the function and thinking about how we'll use the variables to create the scatterplot matrix. We'll also write the docstring for our function.


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    """
    This function create a scatterplot matrix and expects the following inputs:
    - df - The DataFrame which contains the data
    - scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
    - categoricalColumn - the column which contains the categories of data which should be plotted
    - colours - a list of colours equal in length to the number of categories in the categoricalColumn
    - title - the title of the chart
    
    This function does not create a scatterplot where the same variable intersects with itself.
    """
    
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

We'll need to create the list of categories within the categoricalColumn, and map this to the list of colours to create the colour lookup. 

We can also get number of rows and columns in the subplots object from the length of the list of scatterColumns, using this information to create the subplots object:


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    categories = list(df[categoricalColumn].unique())
    print(categories)
    colourLookup = dict(zip(categories, colours))
    print(colourLookup)
    
    print(len(scatterColumns))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    ['I. setosa', 'I. versicolor', 'I. virginica']
    {'I. virginica': 'green', 'I. setosa': 'purple', 'I. versicolor': 'orange'}
    4
    This is the format of your plot grid:
    [ (1,1) x1,y1 ]    [ (1,2) x2,y2 ]    [ (1,3) x3,y3 ]    [ (1,4) x4,y4 ]  
    [ (2,1) x5,y5 ]    [ (2,2) x6,y6 ]    [ (2,3) x7,y7 ]    [ (2,4) x8,y8 ]  
    [ (3,1) x9,y9 ]    [ (3,2) x10,y10 ]  [ (3,3) x11,y11 ]  [ (3,4) x12,y12 ]
    [ (4,1) x13,y13 ]  [ (4,2) x14,y14 ]  [ (4,3) x15,y15 ]  [ (4,4) x16,y16 ]
    
    

Now we can transpose the code which we wrote in the previous lessons into this function. First of all, we'll make the basic traces, then we can add in later some of the styling options which we learnt in the last lesson:


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    for i, column in enumerate(scatterColumns):
        for j, row in enumerate(scatterColumns):
            if column != row:
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category},
                                    col = i + 1,
                                    row = j + 1)
    pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(14)%20-%20Function%20for%20scatterplot%20matrix/pyo.iplot-0.png)    
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]    [ (1,2) x2,y2 ]    [ (1,3) x3,y3 ]    [ (1,4) x4,y4 ]  
    [ (2,1) x5,y5 ]    [ (2,2) x6,y6 ]    [ (2,3) x7,y7 ]    [ (2,4) x8,y8 ]  
    [ (3,1) x9,y9 ]    [ (3,2) x10,y10 ]  [ (3,3) x11,y11 ]  [ (3,4) x12,y12 ]
    [ (4,1) x13,y13 ]  [ (4,2) x14,y14 ]  [ (4,3) x15,y15 ]  [ (4,4) x16,y16 ]
    
    





## Styling the chart

Let's now apply the styling options we learnt about in the previous lesson, but in a more generalised way within the function.

We'll first set the <code>'legendgroup'</code> and <code>'showlegend'</code> options to ensure that only 1 trace of each category is shown on the legend, and that that legend item controls all of the traces within that category:


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    for i, column in enumerate(scatterColumns):
        for j, row in enumerate(scatterColumns):
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
    pyo.iplot(fig)
 
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(14)%20-%20Function%20for%20scatterplot%20matrix/pyo.iplot-1.png)   
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]  [ (1,3) x3,y1 ]  [ (1,4) x4,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]  [ (2,3) x3,y2 ]  [ (2,4) x4,y2 ]
    [ (3,1) x1,y3 ]  [ (3,2) x2,y3 ]  [ (3,3) x3,y3 ]  [ (3,4) x4,y3 ]
    [ (4,1) x1,y4 ]  [ (4,2) x2,y4 ]  [ (4,3) x3,y4 ]  [ (4,4) x4,y4 ]
    
    





Now let's set the chart title and the axis titles, remembering that only the left-most and bottom-most axes need titles. we can also use this opportunity to set the range for the axes.

For the range, we need to take the minimum and maximum values of the columns which we're plotting on the scatterplot matrix. It's best to do this outside of the loop in order to make our code more efficient. 

We're going to take a slightly different approach to calculating the range of the axes to ensure that this function is as generalisable as possible. To get the minimum for the range, we'll subract 10% of the range (the difference between the minimum and maximum value) from the minimum value of the df, likewise for the maximum value:


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    diff = max(df[scatterColumns].max()) - min(df[scatterColumns].min())
    
    minimum = min(df[scatterColumns].min()) - (diff * 0.1)
    maximum = max(df[scatterColumns].max()) + (diff * 0.1)
    
    for i, column in enumerate(scatterColumns):
        fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column,
                                                      'range' : [minimum,maximum]})
        
        for j, row in enumerate(scatterColumns):
            fig['layout']['yaxis{}'.format(i + 1)].update({'title' : row,
                                                      'range' : [minimum,maximum]})
            
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
                    
    fig['layout'].update({'title' : title})
    pyo.iplot(fig)
  
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(14)%20-%20Function%20for%20scatterplot%20matrix/pyo.iplot-2.png)  
scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]  [ (1,3) x3,y1 ]  [ (1,4) x4,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]  [ (2,3) x3,y2 ]  [ (2,4) x4,y2 ]
    [ (3,1) x1,y3 ]  [ (3,2) x2,y3 ]  [ (3,3) x3,y3 ]  [ (3,4) x4,y3 ]
    [ (4,1) x1,y4 ]  [ (4,2) x2,y4 ]  [ (4,3) x3,y4 ]  [ (4,4) x4,y4 ]
    
    





Finally, because we know the scatterplot matrix is going to be a square, we can set the width and height of the chart based on the number of items which we're comparing (ie <code>len(scatterColumns)</code>) multiplied by a sensible number:


```python
def scatterplotMatrix(df, scatterColumns, categoricalColumn, colours, title):
    """
    This function create a scatterplot matrix and expects the following inputs:
    - df - The DataFrame which contains the data
    - scatterColumns - a list of the columns in the DataFrame which we want to plot on a scatterplot matrix
    - categoricalColumn - the column which contains the categories of data which should be plotted
    - colours - a list of colours equal in length to the number of categories in the categoricalColumn
    - title - the title of the chart
    
    This function does not create a scatterplot where the same variable intersects with itself.
    """
    
    categories = list(df[categoricalColumn].unique())
    colourLookup = dict(zip(categories, colours))
    
    fig = tools.make_subplots(rows = len(scatterColumns),
                             cols = len(scatterColumns),
                             print_grid = True,
                             shared_xaxes = True,
                             shared_yaxes = True)
    
    diff = max(df[scatterColumns].max()) - min(df[scatterColumns].min())
    
    minimum = min(df[scatterColumns].min()) - (diff * 0.1)
    maximum = max(df[scatterColumns].max()) + (diff * 0.1)
    
    for i, column in enumerate(scatterColumns):
        fig['layout']['xaxis{}'.format(i + 1)].update({'title' : column,
                                                      'range' : [minimum,maximum]})
        
        for j, row in enumerate(scatterColumns):
            fig['layout']['yaxis{}'.format(i + 1)].update({'title' : row,
                                                      'range' : [minimum,maximum]})
            
            if column != row:
                if i == 0 and j == 1:
                    show = True
                else:
                    show = False
                
                for category, colour in colourLookup.items():
                    fig.append_trace({'type' : 'scatter',
                                     'mode' : 'markers',
                                     'x' : df.loc[df[categoricalColumn] == category, column],
                                     'y' : df.loc[df[categoricalColumn] == category, row],
                                     'marker' : {'color' : colour,
                                                'size' : 3},
                                     'name' : category,
                                     'legendgroup' : category,
                                     'showlegend' : show},
                                    col = i + 1,
                                    row = j + 1)
                    
    fig['layout'].update({'title' : title,
                         'height' : len(scatterColumns * 200),
                         'width' : len(scatterColumns * 200)})
    pyo.iplot(fig)
   
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(14)%20-%20Function%20for%20scatterplot%20matrix/pyo.iplot-3.png) return fig
    
irisScatter = scatterplotMatrix(iris, 
                  ['Sepal length','Sepal width','Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]  [ (1,3) x3,y1 ]  [ (1,4) x4,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]  [ (2,3) x3,y2 ]  [ (2,4) x4,y2 ]
    [ (3,1) x1,y3 ]  [ (3,2) x2,y3 ]  [ (3,3) x3,y3 ]  [ (3,4) x4,y3 ]
    [ (4,1) x1,y4 ]  [ (4,2) x2,y4 ]  [ (4,3) x3,y4 ]  [ (4,4) x4,y4 ]
    
    





Let's test this function with fewer columns:


```python
irisScatter = scatterplotMatrix(iris, 
                  ['Petal length','Petal width'], 
                  'Species', 
                  ['purple','orange','green'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]
    
    





If we want a scatterplot with no categorical variable we have to trick the function slightly; let's create a new column in the DataFrame which only has one value:


```python
iris['noCat'] = 'Iris'
```

We can now pass this column as the categorical column:


```python
irisScatter = scatterplotMatrix(iris, 
                  ['Petal length','Petal width'], 
                  'noCat', 
                  ['purple'],
                 'Scatterplot matrix of Iris dataset')
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y1 ]
    [ (2,1) x1,y2 ]  [ (2,2) x2,y2 ]
    
    





