
# Lineplots (3) - Plotting Data from a Pandas DataFrame

In the last lesson we saw how to change the data and layout of our chart with the <code>dict.update()</code> method. 

In this lesson we're going to plot data from a Pandas DataFrame which we've created from a .csv file.

In the previous lessons we used dummy data to introduce a line plot. I'm going to keep the use of dummy data to an absolute minimum in this course; when you apply what you've learnt in these lessons you'll be using real data, so why not learn with it too! 






 






## Reading a .csv and making a DataFrame

We're going to use the <code>read_csv()</code> function to read in some data from a .csv file and display it as a DataFrame.

I'm going to get the data straight from my website, but if you'd like to download the data to your computer, click <a href="http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv">here</a>. When the data is downloaded, simply pass the folder location and filename to <code>pd.read_csv()</code>, rather than the web address.


```python
expenseData = pd.read_csv("http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv")
```

Let's have a quick look at the data. The .csv hold information on the number of expense claims submitted each month by British MPs between 2010 and 2015.


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



Let's see some summary statistics:


```python
expenseData.describe()
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
      <th>count</th>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>12.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.500000</td>
      <td>12392.166667</td>
      <td>15723.083333</td>
      <td>16638.916667</td>
      <td>17265.083333</td>
      <td>15299.666667</td>
      <td>9748.500000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.605551</td>
      <td>5158.031140</td>
      <td>2276.059372</td>
      <td>2347.924827</td>
      <td>2302.409586</td>
      <td>1759.354599</td>
      <td>6283.133244</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>11036.000000</td>
      <td>11625.000000</td>
      <td>12182.000000</td>
      <td>10784.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.750000</td>
      <td>10994.750000</td>
      <td>14624.250000</td>
      <td>15405.500000</td>
      <td>15864.000000</td>
      <td>14651.500000</td>
      <td>4963.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.500000</td>
      <td>14100.500000</td>
      <td>15757.000000</td>
      <td>16566.000000</td>
      <td>17828.000000</td>
      <td>15813.500000</td>
      <td>10854.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.250000</td>
      <td>15069.250000</td>
      <td>17044.750000</td>
      <td>17839.750000</td>
      <td>18344.500000</td>
      <td>16251.500000</td>
      <td>14949.250000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12.000000</td>
      <td>18678.000000</td>
      <td>19507.000000</td>
      <td>20934.000000</td>
      <td>21204.000000</td>
      <td>17207.000000</td>
      <td>17555.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting the Data

So, let's make a lineplot which shows these expenses.

First of all, we need to tell Plotly that we're going to make a scatterplot, but that we only want to see the lines. I'm also going to name the trace:


```python
trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1'}
```

Next, we need to pass the data from the DataFrame to Plotly. Because we're plotting a time series, I'll put the time element on the horizontal axis (X-axis) as this is the convention.

In this case, the time element is contained within the <code>'month'</code> column in <code>expenseData</code>. It looks like this (the numbers on the left-hand side are the index):


```python
expenseData['month']
```




    0      1
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
    Name: month, dtype: int64



Let's pass this to our trace:


```python
trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1',
         'x' : expenseData['month']}
```

Now, let's pass the Y-values. I'm going to plot the number of expense claims in 2010.

The number of expense claims in 2010 is held in the <code>'NumberOfClaims2010'</code> column in <code>expenseData</code>. It looks like this:


```python
expenseData['NumberOfClaims2010']
```




    0     14982
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
    Name: NumberOfClaims2010, dtype: int64



Let's add this to the trace:


```python
trace1 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace1',
         'x' : expenseData['month'],
         'y' : expenseData['NumberOfClaims2010']}
```

OK, so now we need to create a Data object as a list of traces. We only have one trace:


```python
data = Data([trace1])
```

Now it's time to create the layout. I'm setting the chart title and the axis titles:


```python
layout = {'title' : 'Expenses by month in 2010',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of Claims'}}
```

Finally, I'll create the Figure object and plot the chart:


```python
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(03)%20-%20Plotting%20Data%20from%20a%20Pandas%20DataFrame/pyo.iplot-0.png)#py.plot(fig, filename = "Something in 2012")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(03)%20-%20Plotting%20Data%20from%20a%20Pandas%20DataFrame/py.plot-0.png)``





OK, so we have our first trace; you can see that the quantity of expense claims changes every month, but is it like that every year? 

Let's make a new chart with the expense claims for 2011.

I'm going to copy the code that we used to create trace1, and make a few changes so that we can reuse it for trace2.

I'm going to change the name of the trace and change the column in the DataFrame from which we get the data:


```python
trace2 = {'type' : 'scatter',
         'mode' : 'lines',
         'name' : 'trace2',
         'x' : expenseData['month'],
         'y' : expenseData['NumberOfClaims2011']}
```

Now I'm going to create a new Data object because I don't want to affect the one which we used to create our first chart:


```python
data2 = Data([trace2])
```

Next I'm going to create a new layout and change the title. We have to create a new layout object because we don't want to affect the original.


```python
layout2 = {'title' : 'Expenses by month in 2011',
         'xaxis' : {'title' : 'Month'},
         'yaxis' : {'title' : 'Number of Claims'}}
```

Finally, I need to create a new Figure object:


```python
fig2 = Figure(data = data2, layout = layout2)

pyo.iplot(fig2)
``
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(03)%20-%20Plotting%20Data%20from%20a%20Pandas%20DataFrame/pyo.iplot-1.png)`





### Creating and styling charts with multiple traces - what have we learnt?

So we've seen how to create different charts from the same DataFrame - if you feel that you need more practise in doing this, you can try to create some more charts using the other columns in the DataFrame.

This said, it's difficult to compare the data for each year when they are all on different charts. In the next lesson we'll see how to create a chart with multiple traces.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>