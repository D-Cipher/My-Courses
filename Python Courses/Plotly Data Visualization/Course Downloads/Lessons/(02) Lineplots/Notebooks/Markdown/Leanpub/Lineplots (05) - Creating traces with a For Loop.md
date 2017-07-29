
# Lineplots (5) - Creating traces with a For Loop

In the last lesson we saw how to create multiple traces and plot them on the same chart. We did this manually and found that it took quite some time. Fortunately, we can solve this problem!

In this lesson I'm going to show you how to use a For loop to create multiple traces. We'll then plot these traces on the same chart.

One benefit of using a For loop to create multiple traces is that you don't have to write as much code as if you did them all by hand. Secondly, you can also write your code in such a way that you can include future updates to the data with only minimal changes to the code. We'll learn how to do this in two different ways.






 






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



### Making our first trace

Below is the code that we used to create our traces in the previous lesson. With a few changes we can adapt this code to make it suitable to be run in a For loop. We'll make the same chart with two different For loops to give you some different options for when you make your own chart.


```python
trace_2010 = {'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2010'],
             'name' : '2010',
             'mode' : 'lines'}
```

### Looping through the years of data

I have set up my data in a way that allows us to loop through it easily. The data for each year has been named in a consistent way - we can use a For loop to loop through the years.

The first step is to create an empty list to store the traces in:


```python
traces = []
```

Next, I'll create the loop:


```python
for i in range(2010, 2016):
    print(i)
```

    2010
    2011
    2012
    2013
    2014
    2015
    

You can see how in each iteration of the loop, the variable <code>i</code> takes the value of a different year.

Now, I'll loop through the years again, but this time I need to append some items to our list of traces. I'll start by just appending the values of <code>i</code>:


```python
for i in range(2010, 2016):
    traces.append(i)
    
traces
```




    [2010, 2011, 2012, 2013, 2014, 2015]



Now, let's add in the code we used to create the traces in the previous lesson. I've reset the variable <code>traces</code> to be an empty list:


```python
traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims2010'],
             'name' : '2010',
             'mode' : 'lines'})
traces
```




    [{'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': '2010', 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64}]



So each list in the list of traces contains data for the same year - we have simply copied it. Before you continue, think about what changes we need to make to the code in order to get the data for different years.
 
  
   
We'll use the value of the variable <code>i</code> to access different columns in the DataFrame and to set a different name for the trace:


```python
traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
             'mode' : 'lines'})
traces
```




    [{'mode': 'lines', 'name': 2010, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines', 'name': 2011, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     16594
      1     16060
      2     19507
      3     13056
      4     15454
      5     17104
      6     15446
      7     11036
      8     14487
      9     17025
      10    18238
      11    14670
      Name: NumberOfClaims2011, dtype: int64},
     {'mode': 'lines', 'name': 2012, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     18280
      1     16632
      2     20934
      3     15158
      4     17693
      5     16914
      6     16474
      7     11625
      8     15488
      9     16500
      10    19149
      11    14820
      Name: NumberOfClaims2012, dtype: int64},
     {'mode': 'lines', 'name': 2013, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     18096
      1     15954
      2     21204
      3     18070
      4     17586
      5     18859
      6     17541
      7     12182
      8     15594
      9     18882
      10    18173
      11    15040
      Name: NumberOfClaims2013, dtype: int64},
     {'mode': 'lines', 'name': 2014, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0     15864
      1     14272
      2     16946
      3     16146
      4     15725
      5     17207
      6     16568
      7     10784
      8     14778
      9     15783
      10    15844
      11    13679
      Name: NumberOfClaims2014, dtype: int64},
     {'mode': 'lines', 'name': 2015, 'type': 'scatter', 'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64, 'y': 0      2728.0
      1         0.0
      2         1.0
      3      5708.0
      4     11556.0
      5     17555.0
      6     15992.0
      7     10152.0
      8     14207.0
      9     14909.0
      10    15070.0
      11     9104.0
      Name: NumberOfClaims2015, dtype: float64}]



Now you can see that each trace holds different data.

We need to turn the list of traces into a Data object. The variable <code>traces</code> is already a list so we don't need to contain it in square brackets:


```python
data = Data(traces)
```

Let's reuse the layout that we utilised in the previous lesson - we just have to change the title to reflect the data held in the chart.


```python
layout = {'title' : 'Expense claims by month for 2010 - 2015',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of expense claims'}}
```

Now, we'll create the Figure object:


```python
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(05)%20-%20Creating%20traces%20with%20a%20For%20Loop/pyo.iplot-0.png)#py.plot(fig, filename = "Expenses by month in 2012 & 2013")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(05)%20-%20Creating%20traces%20with%20a%20For%20Loop/py.plot-0.png)``





Now you can see 6 of the standard colours that Plotly uses. We can also see the relationship between the data much more clearly than if all the traces we on separate charts. It looks like 2010 and 2015 don't follow the same pattern as the other years.

### Loop through the column names in a DataFrame

For cases when the column names don't follow a particular convention, we can instead loop through the column names.


```python
for col in expenseData.columns.tolist():
    print(col)
```

    month
    NumberOfClaims2010
    NumberOfClaims2011
    NumberOfClaims2012
    NumberOfClaims2013
    NumberOfClaims2014
    NumberOfClaims2015
    

We don't want to plot the <code>month</code> variable as a Y-value, as we're already plotting it as an X-value...


```python
for col in expenseData.columns.tolist():
    if col != 'month':
        print(col)
```

    NumberOfClaims2010
    NumberOfClaims2011
    NumberOfClaims2012
    NumberOfClaims2013
    NumberOfClaims2014
    NumberOfClaims2015
    

Now, let's adjust the code slightly:


```python
traces = []
for col in expenseData.columns.tolist():
    if col != 'month':
        traces.append({'type' : 'scatter',
                 'x' : expenseData['month'],
                 'y' : expenseData[col],
                 'name' : col,
                 'mode' : 'lines'})
traces
```




    [{'mode': 'lines',
      'name': 'NumberOfClaims2010',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0     14982
      1     14168
      2     18678
      3         3
      4      6404
      5     11767
      6     14721
      7      8678
      8     14033
      9     15331
      10    17173
      11    12768
      Name: NumberOfClaims2010, dtype: int64},
     {'mode': 'lines',
      'name': 'NumberOfClaims2011',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0     16594
      1     16060
      2     19507
      3     13056
      4     15454
      5     17104
      6     15446
      7     11036
      8     14487
      9     17025
      10    18238
      11    14670
      Name: NumberOfClaims2011, dtype: int64},
     {'mode': 'lines',
      'name': 'NumberOfClaims2012',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0     18280
      1     16632
      2     20934
      3     15158
      4     17693
      5     16914
      6     16474
      7     11625
      8     15488
      9     16500
      10    19149
      11    14820
      Name: NumberOfClaims2012, dtype: int64},
     {'mode': 'lines',
      'name': 'NumberOfClaims2013',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0     18096
      1     15954
      2     21204
      3     18070
      4     17586
      5     18859
      6     17541
      7     12182
      8     15594
      9     18882
      10    18173
      11    15040
      Name: NumberOfClaims2013, dtype: int64},
     {'mode': 'lines',
      'name': 'NumberOfClaims2014',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0     15864
      1     14272
      2     16946
      3     16146
      4     15725
      5     17207
      6     16568
      7     10784
      8     14778
      9     15783
      10    15844
      11    13679
      Name: NumberOfClaims2014, dtype: int64},
     {'mode': 'lines',
      'name': 'NumberOfClaims2015',
      'type': 'scatter',
      'x': 0      1
      1      2
      2      3
      3      4
      4      5
      5      6
      6      7
      7      8
      8      9
      9     10
      10    11
      11    12
      Name: month, dtype: int64,
      'y': 0      2728.0
      1         0.0
      2         1.0
      3      5708.0
      4     11556.0
      5     17555.0
      6     15992.0
      7     10152.0
      8     14207.0
      9     14909.0
      10    15070.0
      11     9104.0
      Name: NumberOfClaims2015, dtype: float64}]



We have to refresh the Data and Figure objects, but we can reuse the Layout from the previous chart, only having to slightly change the title.


```python
layout = {'title' : 'Expense claims by month for 2010-2015',
         'xaxis' : {'title' : 'month'},
         'yaxis' : {'title' : 'Number of expense claims'}}
```


```python
data = Data(traces)
fig = Figure(data = data, layout = layout)

pyo.iplot(fig)
``
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(05)%20-%20Creating%20traces%20with%20a%20For%20Loop/pyo.iplot-1.png)`





You can see how the data that has been plotted is identical. The only thing that has changed is that the legend items now have different names (HINT: you can use string slicing to remove this difference).

These two methods for using a For loop to create traces from a DataFrame are very versatile and powerful; we'll be using them a lot in this course.

Let's sent this plot to our Plotly account!


```python
py.plot(fig, filename="MP Expense claims by month 2010-2015", fileopt="overwrite")
```
![py.plot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(05)%20-%20Creating%20traces%20with%20a%20For%20Loop/py.plot-1.png)




    'https://plot.ly/~rmuir/148'



### Using a For loop to plot multiple traces - what have we learnt?

We've seen how to use a For loop in two different ways to allow us to dynamically create multiple traces.

We saw that if the columns in our data have a consistent naming convention, then we may be able to loop through a list of numbers and use the loop variable to access the column names.

For data where the naming convention is not consistent, we can instead loop through a list of the column names, being careful not to plot one of the variables as both an x-variable and a y-variable (month, in this case).

In the next lesson we'll look at how to style these different traces.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>