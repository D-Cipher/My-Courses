
# Scatterplots (11) - Plotly sub-plots

Plotly's sub-plots allow us to plot several different charts on the same figure. Over the next few lessons we'll learn how to utilise this feature to create a scatterplot matrix showing the relationships between several different variables. 

The example below shows a scatterplot where several different variables are plotted against each other. Where the same variable would be plotted against itself, a histogram of that variable's observations is shown:

<img src="http://176.32.230.52/richard-muir.com/blog/wp-content/uploads/2015/09/correlations1.png"/>

By the end of the next few lessons you'll be able to create your own scatterplot matrix.

In this lesson we're going to learn how to place charts on the Plotly sub-plot object. Later we'll learn how to place those charts procedurally using a loop to generate a scatterplot matrix. We'll then write a function to which will allow us to pass any DataFrame which contains appropriate variables, and make a scatterplot matrix of those variables.



We're going to import the <code>tools</code> library which contains the <code>make_subplots()</code> function which will be the main focus of this lesson. We'll also import the <code>random</code> library to help is create some dummy data to plot:



from plotly import tools
import random



```python

 
```





## The Plotly <code>make_subplots()</code> function

The Plotly <code>make_subplots()</code> function allows us to create a grid of plots. Each plot is numbered with an (x,y) coordinate, starting at (1,1) in the top-left corner. Note that the grid created by the <code>make_subplots()</code> function is not zero-indexed!

The <code>make_subplots()</code> function can take the following arguments (amongst others):
- <code>rows</code> - how many rows of charts are in the subplot
- <code>cols</code> - how many columns of charts are in the subplot
- <code>print_grid</code> - whether or not to print a string representation of the grid (this helps when developing the subplot
- <code>shared_xaxes</code> - whether or not the plots share an x-axis
- <code>shared_yaxes</code> - whether or not the plots share a y-axis
- <code>subplot_titles</code> - A list of the titles for each subplot. These are distributed from top-left to bottom-right.

We'll learn about all of these options as we develop our understanding of the <code>make_subplots()</code> function.

## Making subplots
In order to utilise the <code>make_subplots()</code> functionality, we have to create a subplots object, and then assign a chart to each location in the grid of available spaces.

Let's make our first subplots object with 2 rows and 2 columns. We also want to set <code>print_grid</code> to <code>True</code> so we can see where each plot will go:


```python
plots = tools.make_subplots(cols = 2, rows = 2, print_grid = True)
```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    

We can see the shape that our 2 by 2 chart will take. We can also see that Plotly has set up the beginnings of the subplots chart. 

There is space for us to add the traces to the chart, as well as separate x- and y-axis objects for each subplot. The <code>'domain'</code> information tells us the space that the axis covers on the chart. You can style each of these axes individually, setting the axis titles and range for example, just as we have done with previous charts. 


```python
plots
```




    {'data': [],
     'layout': {'xaxis1': {'anchor': 'y1', 'domain': [0.0, 0.45]},
      'xaxis2': {'anchor': 'y2', 'domain': [0.55, 1.0]},
      'xaxis3': {'anchor': 'y3', 'domain': [0.0, 0.45]},
      'xaxis4': {'anchor': 'y4', 'domain': [0.55, 1.0]},
      'yaxis1': {'anchor': 'x1', 'domain': [0.575, 1.0]},
      'yaxis2': {'anchor': 'x2', 'domain': [0.575, 1.0]},
      'yaxis3': {'anchor': 'x3', 'domain': [0.0, 0.425]},
      'yaxis4': {'anchor': 'x4', 'domain': [0.0, 0.425]}}}



## Adding charts to the subplots object
We'll now add a trace to the subplots object. We'll use some dummy data for this so we can focus on learning how to manipulate the subplots object, rather than how to manipulate the individual charts.

To add a trace to the subplot object, we use the <code>append_trace()</code> method of the subplot object, specifying the row and column location where we'll put the trace.

The <code>append_trace()</code> method takes 3 arguments:
- <code>trace</code> - the trace object we're adding to the subplots
- <code>row</code> - the row reference (enumerated from 1)
- <code>col</code> - the column reference (also enumerated from 1)

We're going to append the traces one at a time to the subplots object, plotting it each time to see how it changes. Each trace will be comprised of 10 random x- and y-values which we'll make using the <code>random.random()</code> function:


```python
plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace1'},
                    row = 1, col = 1)

pyo.iplot(plots)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(11)%20-%20Plotly%20sub-plots/pyo.iplot-0.png)```





Let's add another trace to a different sub-plot:


```python
plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace2'},
                    row = 1, col = 2)
pyo.iplot(plots)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(11)%20-%20Plotly%20sub-plots/pyo.iplot-1.png)``





We can now fill in the final two spaces:


```python
plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace3'},
                    row = 2, col = 1)

plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace4'},
                    row = 2, col = 2)
pyo.iplot(plots)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(11)%20-%20Plotly%20sub-plots/pyo.iplot-2.png)`





We can also add more than 1 trace to a grid space. Here I'm adding trace5 to the top-left space in the subplots:


```python
plots.append_trace(trace = {'type' : 'scatter',
                            'mode' : 'markers',
                           'x' : [random.random() for i in range(10)],
                           'y' : [random.random() for i in range(10)],
                           'name' : 'trace5'},
                    row = 1, col = 1)
pyo.iplot(plots)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(11)%20-%20Plotly%20sub-plots/pyo.iplot-3.png)





We'll see in a later section how to manipulate some of the styling options for the subplots object itself, but the remainder of the lessons in this section will focus on getting the data into the subplots object and making the subsequent chart clear and informative.

