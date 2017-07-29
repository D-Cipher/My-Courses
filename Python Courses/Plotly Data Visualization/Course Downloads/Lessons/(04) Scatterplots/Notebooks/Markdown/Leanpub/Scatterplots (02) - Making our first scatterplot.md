
# Scatterplots (02) - Making our first scatterplot

In this lesson we're going to make our first scatterplot showing the relationship between revenue and number of employees for around 50 different companies. 

With Plotly, we make scatterplots and lineplots in very similar ways, so the next few lessons should not only teach you about scatterplots, but also serve as a handy revision guide for the Lineplots section.






 






## Getting the data

We'll get the data on company revenue and number of employees (which I've previously prepared) as a .csv from my website:


```python
companies = pd.read_csv("http://www.richard-muir.com/data/public/csv/CompaniesRevenueEmployees.csv", index_col = 0)
companies.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Industry</th>
      <th>Revenue (USD billions)</th>
      <th>Employees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
      <td>Retail</td>
      <td>482</td>
      <td>2200000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sinopec Group</td>
      <td>Oil and gas</td>
      <td>455</td>
      <td>358571</td>
    </tr>
    <tr>
      <th>2</th>
      <td>China National Petroleum Corporation</td>
      <td>Oil and gas</td>
      <td>428</td>
      <td>1636532</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Saudi Aramco</td>
      <td>Oil and gas</td>
      <td>338</td>
      <td>60000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>State Grid</td>
      <td>Electric utility</td>
      <td>333</td>
      <td>1564000</td>
    </tr>
  </tbody>
</table>
</div>



### Adding the hovertext
Now we'll create the column which contains the text that will be shown when a user moves their mouse pointer over a data point. Scatterplots are used to show the relationship between two variables, but adding coherent hovertext is a great way of ensuring that the user can check and outlying points - those which may lie outside the general trend of the data.

We're going to have the hovertext show the company's name in bold and the industry in italics on the first line, then the revenue and number of employees on two further lines.

I'm using <code>df.apply(lambda x: . . .)</code> along with the Python <code>str.format()</code> method to create this text field, accessing each column in turn within the lambda function:


```python
companies['text'] = companies.apply(lambda x: 
                                    """<b>{}</b> (<i>{}</i>)<br>Revenue: ${} billion<br>Employees: {:,}""".format(x['Name'], 
                                                                                                                  x['Industry'], 
                                                                                                                  x['Revenue (USD billions)'],
                                                                                                                  x['Employees']),
                                    axis = 1)
```


```python
companies.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Industry</th>
      <th>Revenue (USD billions)</th>
      <th>Employees</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
      <td>Retail</td>
      <td>482</td>
      <td>2200000</td>
      <td>&lt;b&gt;Walmart&lt;/b&gt; (&lt;i&gt;Retail&lt;/i&gt;)&lt;br&gt;Revenue: $48...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sinopec Group</td>
      <td>Oil and gas</td>
      <td>455</td>
      <td>358571</td>
      <td>&lt;b&gt;Sinopec Group&lt;/b&gt; (&lt;i&gt;Oil and gas&lt;/i&gt;)&lt;br&gt;R...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>China National Petroleum Corporation</td>
      <td>Oil and gas</td>
      <td>428</td>
      <td>1636532</td>
      <td>&lt;b&gt;China National Petroleum Corporation&lt;/b&gt; (&lt;...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Saudi Aramco</td>
      <td>Oil and gas</td>
      <td>338</td>
      <td>60000</td>
      <td>&lt;b&gt;Saudi Aramco&lt;/b&gt; (&lt;i&gt;Oil and gas&lt;/i&gt;)&lt;br&gt;Re...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>State Grid</td>
      <td>Electric utility</td>
      <td>333</td>
      <td>1564000</td>
      <td>&lt;b&gt;State Grid&lt;/b&gt; (&lt;i&gt;Electric utility&lt;/i&gt;)&lt;br...</td>
    </tr>
  </tbody>
</table>
</div>



Let's look at a specific cell to make sure the numbers have been formatted correctly:


```python
companies.loc[0, 'text']
```




    '<b>Walmart</b> (<i>Retail</i>)<br>Revenue: $482 billion<br>Employees: 2,200,000'



## Making our scatter trace
We can now make our scatter trace. We'll do this is a similar way to how we made the traces for our line charts in the previous section, however rather than specifying <code>'mode' : 'lines'</code>, we'll instead specify <code>'mode' : 'markers'</code>.

It's not clear from the data if there is a variable that we consider to be especially independent or dependent (an independent variable is conventionally plotted on the x-axis), so we can plot the variables on whichever axis:


```python
companiesTrace = {'type' : 'scatter',
                 'mode' : 'markers',
                 'x' : companies['Revenue (USD billions)'],
                  'y' : companies['Employees'],
                  'text' : companies['text'],
                  'hoverinfo' : 'text'}
```

Now we'll set the chart and axis titles in the layout:


```python
layout = {'title' : 'Revenue by number of employees',
         'xaxis' : {'title' : 'Revenue (Billion $)'},
          'yaxis' : {'title' : 'Employees'}}
```

Let's create the figure object and plot it!


```python
fig = Figure(data = [companiesTrace], layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(02)%20-%20Making%20our%20first%20scatterplot/pyo.iplot-0.png)```





So you can clearly see the relationship between revenue and the number of employees for these companies. It looks like there's a slight upwards trend, but most of the data points are clustered around the bottom left corner.

Let's send this chart to the Plotly cloud.


```python
py.plot(fig, filename="Companies by revenue and number of employees", fileopt = 'overwrite')
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(02)%20-%20Making%20our%20first%20scatterplot/py.plot-0.png)``




    'https://plot.ly/~rmuir/200'



