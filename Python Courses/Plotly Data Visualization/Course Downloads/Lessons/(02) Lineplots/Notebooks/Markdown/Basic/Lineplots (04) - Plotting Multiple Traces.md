
# Lineplots
(4) - Plotting Multiple Traces

In the last lesson we saw how to plot data from a Pandas DataFrame; we plotted two different traces from the same DataFrame on different charts.

In this lesson we're going to combine multiple data traces in the same chart. This will allow us to easily compare variables in our DataFrame.






 






## Getting the data

We'll get the data from the same source as the previous lesson.


```python
expenseData = pd.read_csv("http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv")
```


```python
expenseData.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>NumberOfClaims2010</th>
      <th>NumberOfClaims2011</th>
      <th>NumberOfClaims2012</th>
      <th>NumberOfClaims2013</th>
      <th>NumberOfClaims2014</th>
      <th>NumberOfClaims2015</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>14982</td>
      <td>16594</td>
      <td>18280</td>
      <td>18096</td>
      <td>15864</td>
      <td>2728.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>14168</td>
      <td>16060</td>
      <td>16632</td>
      <td>15954</td>
      <td>14272</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>18678</td>
      <td>19507</td>
      <td>20934</td>
      <td>21204</td>
      <td>16946</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3</td>
      <td>13056</td>
      <td>15158</td>
      <td>18070</td>
      <td>16146</td>
      <td>5708.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>6404</td>
      <td>15454</td>
      <td>17693</td>
      <td>17586</td>
      <td>15725</td>
      <td>11556.0</td>
    </tr>
  </tbody>
</table>
</div>



## Making two traces

We'll now create our first trace using data for 2010. 

This trace is identical to that which we created in the previous lesson.


```python
trace_2010 = {'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2010'],
             'name' : '2010',
             'mode' : 'lines'}
```

At the end of the last lesson, we saw that it can be difficult to compare data for different years when they are on different charts. We'll now create a second trace to add to our chart. This will let us compare the data for 2010 and 2011.


```python
trace_2011 = {'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2011'],
             'name' : '2011',
             'mode' : 'lines'}
```

We saw that Plotly expects the Data object to contain a list of traces. Until now, we've only passed one trace to this list, however if we want to plot two traces, we simply have to bass both traces to the Data object:


```python
data = Data([trace_2010, trace_2011])
```

Let's now create a layout. We need to make sure that the title and axis titles reflect the data being displayed in the chart:


```python
layout = {'title' : 'Expense claims by month for 2010 - 2011',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of expense claims'}}
```

We can pass the Data and Layout objects to the Figure object, and plot the chart!


```python
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(04)%20-%20Plotting%20Multiple%20Traces/pyo.iplot-0.png)#py.plot(fig, filename = "Expenses by month in 2012 & 2013")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(04)%20-%20Plotting%20Multiple%20Traces/py.plot-0.png)``





So, from plotting two traces on the same chart, we can see that the number of expense claims in each year is broadly similar for most of the months, however there was a big drop in April 2010, with numbers not returning to the same level as 2011 until July.

We've seen that adding a second trace is as easy as creating the first; the main thing to remember is to include both traces in the Data object.

You can see that Plotly automatically sets the colours to be different for each trace (Plotly has a set of ten colours that it cycles through). It has also produced a legend for us to show which trace corresponds to which year. The 'name' we gave to each trace is what appears in the legend. If you click on the legend items, you can choose to show and display the individual traces.

## Mini-Challenge - Add some more traces!

This is your chance to practise what you've learnt and add some more traces to the chart. Add as many as you wish - if you feel that you need the practise, then why not add a trace for each year of data? Otherwise, it's a good opportunity to solidify the knowledge you've gained so far.

Have a go before reading my solution!

I'm going to add a trace for the 2012 data. This will be similar for the traces for 2010 and 2011, however I'm going to change the object name to be <code>trace_2012</code>, change the column reference to be <code>'NumberOfClaims2012'</code>, and the trace name to be <code>2012</code>:


```python
trace_2012 = {'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2012'],
             'name' : '2012',
             'mode' : 'lines'}
```

Next, I need to refresh the Data object by including this third trace in the list:


```python
data = Data([trace_2010, trace_2011, trace_2012])
```

Now, I need to update the layout to make sure that it is relevant to the data being displayed in the chart.


```python
layout.update({'title' : 'Expense claims by month for 2010 - 2012'})
```

Finally, I can refresh the Figure object and plot it:


```python
fig = Figure(data = data, layout = layout)

pyo.iplot(fig)
``
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(04)%20-%20Plotting%20Multiple%20Traces/pyo.iplot-1.png)`





### Creating and styling charts with multiple traces - what have we learnt?

We've seen that we can create multiple traces and collate them together into one Data object. When we do this, Plotly will automatically choose the colours for the traces and create a legend to help the user discern the traces from each other.

In the next lesson we'll see how to use a For loop to create many traces dynamically.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>