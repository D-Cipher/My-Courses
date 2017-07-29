
# Lineplots (11) - Stepwise Lines

In the last lesson we saw how to implement smoothing on stock market data.

In this lesson we'll some at some other options for the <code>'shape'</code> parameter in the trace. We'll learn how to implement a stepwise line shape and find out when we might want to do this.






 






## Step-wise line shapes

Step-wise line shapes are only useful for displaying data of a specific nature. These plots display the data as a series of horizontal and vertical steps, rather than a smooth curve (as with smoothing), or a series of diagonal lines (as is normally the case).

For this reason, stepped lines should only be used to display data where the points change at a specific place. For example, the temperature change over a day should not be displayed used a step-wise line as the temperature can change fractionally every minute. On the other hand, something like the Bank of England base rate could be displayed using a step-wise line. Each month the Bank's board meets to decide what the base rate will be for that month. In the time between these meetings, the base rate doesn't change.

Let's use the Bank of England base rate to see what different kinds of step-wise line charts we can create.

Firstly, I'll get the data (which I previously prepared) from my website using <code>pd.read_csv()</code>.

In the data there is an observation for the base rate on for each working day since the middle of last century; this means that there are a lot of duplicate values which I need to drop. I also only want the 10 most recent values which I can get by using <code>DataFrame.tail(10)</code>.

Note that this chart doesn't give the true picture of the changes in the base rate; each change is given the same amount of space on the x-axis, regardless of how long that particular base rate was being used. This said, the data serves to illustrate the use of stepwise line shapes.


```python
baserate = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")
baserate.drop_duplicates(subset="VALUE", inplace=True)
baserate = baserate.tail(10)
baserate
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VALUE</th>
      <th>DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6767</th>
      <td>4.50</td>
      <td>04/10/2001</td>
    </tr>
    <tr>
      <th>6792</th>
      <td>4.00</td>
      <td>08/11/2001</td>
    </tr>
    <tr>
      <th>7105</th>
      <td>3.75</td>
      <td>06/02/2003</td>
    </tr>
    <tr>
      <th>7211</th>
      <td>3.50</td>
      <td>10/07/2003</td>
    </tr>
    <tr>
      <th>7419</th>
      <td>4.25</td>
      <td>06/05/2004</td>
    </tr>
    <tr>
      <th>8560</th>
      <td>3.00</td>
      <td>06/11/2008</td>
    </tr>
    <tr>
      <th>8580</th>
      <td>2.00</td>
      <td>04/12/2008</td>
    </tr>
    <tr>
      <th>8602</th>
      <td>1.50</td>
      <td>08/01/2009</td>
    </tr>
    <tr>
      <th>8622</th>
      <td>1.00</td>
      <td>05/02/2009</td>
    </tr>
    <tr>
      <th>8642</th>
      <td>0.50</td>
      <td>05/03/2009</td>
    </tr>
  </tbody>
</table>
</div>



Now, I'll create the trace and layout. The possible step-wise line options and their effects are:

<code>
    "hv" - marker point is at the start of the horizontal section of the step
    "vh" - marker point is at the start of the vertical section of the step
    "hvh" - marker point is at the middle of the horizontal section of the step
    "vhv" - marker point is at the middle of the vertical section of the step
</code>

We'll look at each of these in turn to see the different effects.


```python
baseRateTrace = {'type' : 'scatter',
                 'x' : baserate['DATE'],
                 'y' : baserate['VALUE'],
                'mode' : 'lines+markers',
                 'line' : {'shape' : 'hv'},
                'name' : 'BoE Base Rate'}

layout = {'title' : 'Bank of England Base Rate, 2001 - 2009',
         'xaxis' : {'title' : 'Date'},
         'yaxis' : {'title' : 'Base Rate (%)'}}

data = Data([baseRateTrace])

fig = Figure(data = data, layout = layout)

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(11)%20-%20Stepwise%20Lines/pyo.iplot-0.png)```





Let's push this stepwise line chart to the Plotly cloud:


```python
py.plot(fig, filename="Bank of England Base Rate 2001 - 2009", fileopt="overwrite")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(11)%20-%20Stepwise%20Lines/py.plot-0.png)``




    'https://plot.ly/~rmuir/198'



You can see that the line extends horizontally from the marker point until the x-value of the next marker point when it travels upward to meet the next point. In my opinion, this setting is superior for visualising this particular data because it conveys the message that the base rate was set at a particular point, and remained as such until the next change.

I'll quickly repeat this graph without the step-wise line, but first I'll define a quick function to make this a little easier:


```python
def updateLine(val):
    baseRateTrace['line'].update({'shape' : val})
    data = Data([baseRateTrace])
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)
``
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(11)%20-%20Stepwise%20Lines/pyo.iplot-1.png)`


```python
updateLine('linear')
```





You can see that this chart suggests that the base rate moved steadily from one change to the next; it implies that the base rate changed fractionally each day, when in fact this is not the case.

You may also notice the the values on the x-axis are formatted as a date, and that this date is displayed differently to that in the DataFrame. We'll look at how to format the ticklabels in a future lesson, but I thought that this is worth pointing out.

I'll now demonstrate the other step-wise line options:


```python
updateLine('vh')
```





Here, the line descends (or ascends) from the marker point until the y-value of the next marker point before moving horizontally to meet that point. You could also argue that this represents the BoE interest rate well, however I think that using <code>'hv'</code> is conceptually clearer.

Let's now see what <code>'hvh'</code> looks like:


```python
updateLine('hvh')
```





Here the point is in the middle of the horizontal portion of the step. I don't think this option is particularly suitable for this data, but that doesn't mean it won't be useful for another visualisation!

Finally, we'll look at <code>'vhv'</code>:


```python
updateLine('vhv')
```





So this has made a rather unusual-looking graph which I think is not clear at all for this data; this option may prove useful at another time though!

### Stepwise line shapes - what have we learnt?

In this lesson we've seen how to create a stepwise line chart. We've learnt that this is only suitable for certain types of data, but that it is very effective when used correctly. We've found out how to use the four different options (at the time of writing) for the stepwise shape; 'h', 'v', 'hvh' and 'vhv'.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>