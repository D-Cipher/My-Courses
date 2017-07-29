
# Barcharts (9) - Two types of trace on the same chart

In this lesson we're going to find out how to plot two different traces on the same chart.

We're going to recreate the stacked proportional bar chart we made in the previous lesson and add some information about the size of the meteorites which were found.






 






## Creating the chart
Let's load our stacked proportional bar chart from the Plotly cloud:


```python
stacked = py.get_figure("rmuir", 241)
pyo.iplot(stacked)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(09)%20-%20Two%20types%20of%20trace%20on%20the%20same%20chart/pyo.iplot-0.png)```





Let's now load the .csv file which contains the information on the size of the meteorites. We'll use the same approach that we used to get the proportions for the chart above to get the the propportion of total meteorites which weight less than 101 grams.


```python
sizes = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightPerYear.csv", index_col = 0)
sizes.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>101 - 500g</th>
      <th>501 - 1000g</th>
      <th>less than 101g</th>
      <th>more than 1000g</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>522</td>
      <td>137</td>
      <td>888</td>
      <td>232</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>503</td>
      <td>144</td>
      <td>818</td>
      <td>185</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>497</td>
      <td>123</td>
      <td>1249</td>
      <td>203</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>555</td>
      <td>134</td>
      <td>2425</td>
      <td>208</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>394</td>
      <td>119</td>
      <td>1289</td>
      <td>136</td>
    </tr>
  </tbody>
</table>
</div>



We'll now get the column names for the sizes:


```python
sizeStrings = sizes.columns.tolist()
sizeStrings
```




    ['101 - 500g', '501 - 1000g', 'less than 101g', 'more than 1000g']



Calculating the total and percentages:


```python
sizes['total'] = sizes.sum(axis = 1)
for s in sizeStrings:
    sizes["{}_pc".format(s)] = sizes[s] / sizes['total']
    
sizes.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>101 - 500g</th>
      <th>501 - 1000g</th>
      <th>less than 101g</th>
      <th>more than 1000g</th>
      <th>total</th>
      <th>101 - 500g_pc</th>
      <th>501 - 1000g_pc</th>
      <th>less than 101g_pc</th>
      <th>more than 1000g_pc</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>522</td>
      <td>137</td>
      <td>888</td>
      <td>232</td>
      <td>1779</td>
      <td>0.293423</td>
      <td>0.077010</td>
      <td>0.499157</td>
      <td>0.130410</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>503</td>
      <td>144</td>
      <td>818</td>
      <td>185</td>
      <td>1650</td>
      <td>0.304848</td>
      <td>0.087273</td>
      <td>0.495758</td>
      <td>0.112121</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>497</td>
      <td>123</td>
      <td>1249</td>
      <td>203</td>
      <td>2072</td>
      <td>0.239865</td>
      <td>0.059363</td>
      <td>0.602799</td>
      <td>0.097973</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>555</td>
      <td>134</td>
      <td>2425</td>
      <td>208</td>
      <td>3322</td>
      <td>0.167068</td>
      <td>0.040337</td>
      <td>0.729982</td>
      <td>0.062613</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>394</td>
      <td>119</td>
      <td>1289</td>
      <td>136</td>
      <td>1938</td>
      <td>0.203302</td>
      <td>0.061404</td>
      <td>0.665119</td>
      <td>0.070175</td>
    </tr>
  </tbody>
</table>
</div>



## Adding the line trace to our chart

Now let's add a single trace showing the percentage of meteorites found each year that weighed under 101g. We'll make the trace very dark so it stands out from the rest of the chart:


```python
stacked['data'].append({'type' : 'scatter',
                       'mode' : 'lines+markers',
                       'x' : sizes.index,
                       'y' : sizes['less than 101g_pc'],
                       'marker' : {'color' : '#333'},
                       'name' : 'Meteorite < 101g'})
pyo.iplot(stacked)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(09)%20-%20Two%20types%20of%20trace%20on%20the%20same%20chart/pyo.iplot-1.png)``





By plotting a completely different type of trace on our chart we can show some very different information, and when the presentation of the chart is considered, this can be done so clearly, as we have done. You may have seen some charts which have two y-axes, one at each side of the plotting area - it's generally not a great idea to do this as it can be difficult to determine which trace relates to which side of the plotting area. I would always recommend plotting the same type of variable on the y-axis - percentages in this case.

Let's send this chart to the Plotly cloud.


```python
py.plot(stacked, filename="Meteorites found by continent and weight", fileopt = "overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(09)%20-%20Two%20types%20of%20trace%20on%20the%20same%20chart/py.plot-0.png)`




    'https://plot.ly/~rmuir/251'



