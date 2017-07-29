
# Lineplots (07) - Making dashed and dotted lines

In the last lesson we saw how to change the colour and thickness of the lines in our plot. 

In this lesson we'll learn how to displayed a dashed or dotted line instead of a solid line. In the next lesson we'll find out how to set the marker symbol for each trace. Changing these two properties in addition to manipulating the colour and line width gives us the ability to distinguish between a large number of different data items.






 






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



## Plotting the data

We'll plot the data for the different years using a For loop:


```python
traces = []
for i in range(2010, 2016):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(i)],
             'name' : i,
             'mode' : 'lines'})
```


```python
data = Data(traces)
```


```python
layout = {'title' : 'Number of expenses by month for 2010 - 2015',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Yaxis title1'}}
```


```python
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(07)%20-%20Making%20dashed%20and%20dotted%20lines/pyo.iplot-0.png)```





## Changing the solidity of a line

We can change the solidity of a line by using the <code>'dash'</code> option in the <code>'line'</code> dictionary in the trace:
````python
trace = {'type' : 'scatter',
        'line' : {'dash' : <Dash string/Dash length in pixels/Variable>}
````

Some valid dash strings are:
- <code>'solid'</code>
- <code>'dash'</code>
- <code>'dot'</code>
- <code>'dashdot'</code>

Here's what the dash strings look like. 

I'm using a list of dash strings to contain the possible values.

I'm using the enumerate function and floor division to give me the number of the index to pass to the list. The <code>enumerate()</code> creates a variable which holds the value of each item's index in the list in addition to the variable which holds the actual value of the variable. This value starts at 0 for the first item and increments by one for each subsequent item.


```python
dashes = ['dash', 'dot', 'dashdot']

for i, yr in enumerate(range(2010, 2016)):
    print(i, yr)
```

    0 2010
    1 2011
    2 2012
    3 2013
    4 2014
    5 2015
    


```python
for i, yr in enumerate(range(2010, 2016)):
    print(dashes[(i//2)])
```

    dash
    dash
    dot
    dot
    dashdot
    dashdot
    

Now I'll apply this to our loop which creates the traces:


```python
traces = []
for i, yr in enumerate(range(2010, 2016)):
    traces.append({'type' : 'scatter',
             'x' : expenseData['month'],
             'y' : expenseData['NumberOfClaims' + str(yr)],
                   'line' : {'dash' : dashes[i//2]},
             'name' : yr,
             'mode' : 'lines'})
```

Refreshing the Data and Figure objects to see the effect on the chart:


```python
data = Data(traces)
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(07)%20-%20Making%20dashed%20and%20dotted%20lines/pyo.iplot-1.png)``





Let's push this chart to the cloud. It's not quite production-ready, but it's good to record our progress!


```python
py.plot(fig, filename = "MP expenses by month 2010-2015 (Line solidity)", filopt="overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(07)%20-%20Making%20dashed%20and%20dotted%20lines/py.plot-0.png)`




    'https://plot.ly/~rmuir/152'



### Changing line solidity - what have we learnt?

We've seen how to manipulate the value of the <code>'dash'</code> key in the <code>'line'</code> dictionary to change the solidity of the line. We can use a string such as <code>'dashdot'</code> or set the dash length to be an integer number of pixels. We also utilised the <code>enumerate()</code> function to help us choose an item from a list by index and value.

In the next lesson we'll find out how to specify that Plotly shows the marker in addition to the line. We'll also see how to change the marker symbol.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>