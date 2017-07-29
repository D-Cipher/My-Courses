
# Chart presentation (7) - Applying custom hovertext

In the last lesson we found out how to create a custom text field in a Pandas DataFrame using the <code>apply()</code> and <code>lambda</code> functions.

In this lesson we'll plot a chart which will show this custom hovertext field.






 






### Getting the data

We'll load the house price and ranks dataset from my website and use the code we wrote in the previous lesson to create the text column for each region.


```python
housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/RegionalHousePricesAndRanksJan16.csv")

regions = ['South West','South East','London', 
           'East of England','West Midlands','East Midlands',
           'Yorkshire and The Humber','North West','North East']

for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(round(x, 0)))) + "<br><i>Rank of average price: " + housePrices[r + "_rank"].apply(lambda x: 
                                                                                                             str(int(x))) + "</i>"
housePrices.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>...</th>
      <th>North East_rank</th>
      <th>South West_text</th>
      <th>South East_text</th>
      <th>London_text</th>
      <th>East of England_text</th>
      <th>West Midlands_text</th>
      <th>East Midlands_text</th>
      <th>Yorkshire and The Humber_text</th>
      <th>North West_text</th>
      <th>North East_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.1579</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.5961</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>...</td>
      <td>9.0</td>
      <td>&lt;b&gt;South West&lt;/b&gt;&lt;br&gt;Average Price: £54,705&lt;br...</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;Average Price: £64,019&lt;br...</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;Average Price: £74,436&lt;br&gt;&lt;i&gt;...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;Average Price: £56,7...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,091...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,545...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;Average Pri...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;Average Price: £43,958&lt;br...</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;Average Price: £42,076&lt;br...</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 28 columns</p>
</div>



### Plotting the data

Now, let's create our plot of the changes in the average house price:


```python
traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(7)%20-%20Applying%20custom%20hovertext/pyo.iplot-0.png)```





So you can see that the default hovertext makes things a little clearer, but it's not quite there. The average price is the full floating point number, when we really don't need that much precision, and the trace name isn't particularly clear. Let's add the  text field that we created and see how this changes the chart:


```python
traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"]})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(7)%20-%20Applying%20custom%20hovertext/pyo.iplot-1.png)``





So that's a little better; we have the information that we placed in the text field - the region name, formatted average price and the rank, but Plotly is still showing the default hover information. Let's change the <code>'hoverinfo'</code> option to on show the <code>'text'</code> and the x-values:


```python
traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"],
                  'hoverinfo' : 'text+x'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(7)%20-%20Applying%20custom%20hovertext/pyo.iplot-2.png)`





Much better! But still not there yet.

When we hover over the chart, we only ever see the information for the first five traces, as the hoverinfo fills all the available space. Let's change <code>'hovermode'</code> in the layout object to <code>'closest'</code> and see if that improves things:


```python
traces = []
for r in regions:
    traces.append({'type' : 'scatter',
                   'x' : housePrices['Date'], 
                   'y' : housePrices[r + "_avg"],
                  'name' : r,
                  'mode' : 'lines',
                  'text' : housePrices[r + "_text"],
                  'hoverinfo' : 'text+x'})
    
data = Data(traces)    
layout = {'title' : "Yearly changes in average house price for English regions, 1995-2016",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'tickformat' : ",",
                    'tickprefix' : "£",
                    'title' : 'Average price'},
         'hovermode' : 'closest'}

fig = Figure(data = data, layout = layout)    
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(7)%20-%20Applying%20custom%20hovertext/pyo.iplot-3.png)





I think that's done it! Let's push this chart to the Plotly cloud:


```python
py.plot(fig, "Average UK houses prices by region (1995 - 2016)")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(7)%20-%20Applying%20custom%20hovertext/py.plot-0.png)



    'https://plot.ly/~rmuir/184'



