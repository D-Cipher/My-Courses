
# Barcharts (11) - Creating our first Dashboard (2)

In this lesson we're going to finish adding the data to this dashboard. We'll get the traces we need to create the final two charts and add these traces to the subplots object.



We'll use the Plotly sub-plots module:



from plotly.tools import make_subplots



```python

 
```





## Getting the chart from the previous lesson

Below is all the code we wrote in the last lesson to make this chart:


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]],
                   subplot_titles = ["Types of meteorite by weight", 
                                     "Number of meteorites by continent",
                                     "Weight categories of meteorite",
                                    ])

stacked = py.get_figure("rmuir", 241)
for d in stacked['data']:
    xVals = d['y']
    yVals = d['x']
    d.update({'orientation' : 'h',
             'x' : xVals,
             'y' : yVals})
    fig.append_trace(d, row = 1, col = 3)
    
fig['layout']['xaxis2'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

fig['layout'].update({'barmode' : 'stack',
                      'height' : 1000})

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(11)%20-%20Creating%20our%20first%20Dashboard%20(2)/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1           -      ]  [ (1,3) x2,y2 ]
           |                |                |       
    [ (3,1) x3,y3           -                -      ]
    
    





## How many meteorites were found each year in each weight category?

Let's add the traces for the number of meteorites in each weight category which were found each year. We'll get this data from my website:


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



Let's take our code from a previous lesson to calculate the proportion for each weight category:


```python
sizeStrings = sizes.columns.tolist()

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



Now we'll add a trace for each of the weight categories and append these traces to the bottom-most cell.

Because we're using proportions, we also need to set the tickformat and hoverformat:


```python
for s in sizeStrings:
    fig.append_trace({'type' : 'scatter',
                     'mode' : 'markers+lines',
                     'x' : sizes.index,
                     'y' : sizes["{}_pc".format(s)],
                     'name' : s},
                    row = 3, col = 1)
    
fig['layout']['yaxis3'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(11)%20-%20Creating%20our%20first%20Dashboard%20(2)/pyo.iplot-1.png)``





You'll notice that Plotly keeps cycling through its default list of colours as we add each additional trace. We'll set the colours ourselves later to avoid this behaviour.

### Adding the size and type of meteorites

We'll now get the final data for this chart as a .csv from my website. This .csv file contains information on the type of and weight of each meteorite.


```python
typeWeight = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightAndType.csv", index_col = 0)
typeWeight.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wideClass</th>
      <th>mass (g)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>LL</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Eucrite</td>
      <td>252.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ureilite</td>
      <td>3950.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>L</td>
      <td>9500.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>H</td>
      <td>29560.0</td>
    </tr>
  </tbody>
</table>
</div>



Let's now make a scatter trace showing the type of meteorite against the weight for that meteorite. We'll show the type on the xaxis and weight on the yaxis. We'll append this trace with row = 1 and col = 1.

We won't show a legend for this chart because there will only be one trace.


```python
fig.append_trace({'type' : 'scatter',
             'mode' : "markers",
             'x' : typeWeight['wideClass'],
             'y' : typeWeight['mass (g)'],
                'showlegend' : False},
                row = 1, col = 1)

fig['layout']['yaxis1'].update({'title' : 'Weight (g)'})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(11)%20-%20Creating%20our%20first%20Dashboard%20(2)/pyo.iplot-2.png)`





So there's our first (almost) finished Dashboard. I say almost finished because we still have some work to do to style the chart. We should change the colours so the dashboard itself looks coherent, set the hover behaviour so that it's optimal for all the charts and find a way to break up the legend items so it's clear they relate to different charts.

