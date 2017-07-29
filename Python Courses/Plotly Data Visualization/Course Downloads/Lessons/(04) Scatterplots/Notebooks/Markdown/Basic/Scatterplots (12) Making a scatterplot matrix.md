
# Scatterplots (12) Making a scatterplot matrix

In this lesson we're going to revisit the Iris dataset and create a scatterplot matrix to see the relationships between the different sepal and petal widths and lengths.

We're going to apply what we learnt in the previous lesson about the <code>make_subplots()</code> function to this task of making a scatterplot matrix, using a loop to determine at which point on the grid the traces will be placed.



We're going to import the <code>tools</code> library again:



from plotly import tools



```python

 
```





## Getting the data
We're going to load the Iris dataset which we used at the beginning of this section:


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



We need to get a list of the unique values in the Species column; this will help us to plot only the observations for each species.


```python
irisSpeciesUnique = list(iris['Species'].unique())
irisSpeciesUnique
```




    ['I. setosa', 'I. versicolor', 'I. virginica']



We'll now take this list of species and map it to a list of colours to create a lookup dictionary to assign the same colour to each species name. We'll usew this dictionary to choose the rows for each species in the DataFrame and assign that species a specific colour.

The <code>zip</code> function is used here to combine the list of colours with the list of Iris species. We then turn the resulting object into a <code>dict</code> which has the species as keys and the colours as values.


```python
colours = ['green','blue','orange']
colourLookup = dict(zip(irisSpeciesUnique, colours))
colourLookup
```




    {'I. setosa': 'green', 'I. versicolor': 'blue', 'I. virginica': 'orange'}



## Creating the subplots object

Our scatterplot matrix will plot each of Sepal Length, Sepal Width, Petal Length and Petal Width against every other variable.

Because we have four variables to plot against each other we need to create a 4x4 grid. Each variable will have be plotted at one row location and one column location. I'm setting <code>print_grid</code> to <code>True</code> to help with the development process - we can turn this off when we've finished.


```python
fig = tools.make_subplots(rows = 4, cols = 4, print_grid = True)
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]    [ (1,2) x2,y2 ]    [ (1,3) x3,y3 ]    [ (1,4) x4,y4 ]  
    [ (2,1) x5,y5 ]    [ (2,2) x6,y6 ]    [ (2,3) x7,y7 ]    [ (2,4) x8,y8 ]  
    [ (3,1) x9,y9 ]    [ (3,2) x10,y10 ]  [ (3,3) x11,y11 ]  [ (3,4) x12,y12 ]
    [ (4,1) x13,y13 ]  [ (4,2) x14,y14 ]  [ (4,3) x15,y15 ]  [ (4,4) x16,y16 ]
    
    

## Appending each trace to a space on the grid

We're going to write a nested loop which will give each trace a position on the grid.

The outermost loop will cycle through the variables to be plotted on the columns. The next loop will cycle through these same variables, but will track the row position. The innermost loop will cycle through the different species of Iris, appending three traces to that particular (row, column) coordinate.

Let's write a dummy loop to take care of the behaviour of the outer two loops as these are the most difficult. The output should look like this:
````python
(1,1)
(1,2)
(1,3)
(1,4)
(2,1) etc.
````
Let's do the outer loop first:


```python
for column in range(1, 5):
    print(column)
```

    1
    2
    3
    4
    

Now the inner loop:


```python
for column in range(1, 5):
    for row in range(1, 5):
        print(column, row)
```

    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    4 1
    4 2
    4 3
    4 4
    

Let's test this with a list of columns from the DataFrame. I'm not including the last column, Species, as we won't be plotting the data in this column:


```python
for column in iris.columns[:-1]:
    print(column)
```

    Sepal length
    Sepal width
    Petal length
    Petal width
    


```python
for column in iris.columns[:-1]:
    for row in iris.columns[:-1]:
        print(column," , ", row)
```

    Sepal length  ,  Sepal length
    Sepal length  ,  Sepal width
    Sepal length  ,  Petal length
    Sepal length  ,  Petal width
    Sepal width  ,  Sepal length
    Sepal width  ,  Sepal width
    Sepal width  ,  Petal length
    Sepal width  ,  Petal width
    Petal length  ,  Sepal length
    Petal length  ,  Sepal width
    Petal length  ,  Petal length
    Petal length  ,  Petal width
    Petal width  ,  Sepal length
    Petal width  ,  Sepal width
    Petal width  ,  Petal length
    Petal width  ,  Petal width
    

We don't want to plot a variable against itself, so we'll exclude cases where <code>column == row</code>. I'll also use the <code>enumerate()</code> function to generate the numbers which will position the trace on the subplots object (remembering to add 1 to each number because the subplots are indexed from 1):


```python
for i, column in enumerate(iris.columns[:-1]):
    for j, row in enumerate(iris.columns[:-1]):
        if column == row:
            print("")
        else:
            print(column," , ", row, " | ", (i + 1, j + 1))
```

    
    Sepal length  ,  Sepal width  |  (1, 2)
    Sepal length  ,  Petal length  |  (1, 3)
    Sepal length  ,  Petal width  |  (1, 4)
    Sepal width  ,  Sepal length  |  (2, 1)
    
    Sepal width  ,  Petal length  |  (2, 3)
    Sepal width  ,  Petal width  |  (2, 4)
    Petal length  ,  Sepal length  |  (3, 1)
    Petal length  ,  Sepal width  |  (3, 2)
    
    Petal length  ,  Petal width  |  (3, 4)
    Petal width  ,  Sepal length  |  (4, 1)
    Petal width  ,  Sepal width  |  (4, 2)
    Petal width  ,  Petal length  |  (4, 3)
    
    

We can now create our traces by creating one more loop within the two we have just created.

In this innermost loop we'll cycle through the items in the lookup dictionary we created earlier, assigning each species the same colour from the lookup we created earlier.

We'll use the <code>df.loc[]</code> indexer to choose the rows which relate to each sub-species.

One point to remember is that if you make a mistake and run the loop more than once, you may have to reset your subplots object (<code>fig</code> in this case) otherwise you'll just append even more traces to the object!


```python
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
```

Let's have a look at the plot:


```python
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(12)%20Making%20a%20scatterplot%20matrix/pyo.iplot-0.png)```





So I'm really happy with that. As a first attempt at making a scatterplot matrix it's turned out really well. Let's push it to the Plotly cloud as a record of what we achieved with eleven lines of code and we'll polish it up a bit in the next lesson!


```python
py.plot(fig, filename = "Iris dataset scatterplot matrix (1)", fileopt = "overwrite")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(12)%20Making%20a%20scatterplot%20matrix/py.plot-0.png)``




    'https://plot.ly/~rmuir/216'



