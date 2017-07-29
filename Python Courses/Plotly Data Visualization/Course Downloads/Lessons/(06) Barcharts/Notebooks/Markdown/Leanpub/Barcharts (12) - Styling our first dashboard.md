
# Barcharts (12) - Styling our first dashboard

In this lesson we're going to take the code we wrote in the previous lesson and add some different styling options as we review it.

We're going to set a cohesive colourscheme for our dashboard, move the legend items so that they fit with the charts and add an annotation showing our source.



We'll use the Plotly sub-plots module:



from plotly.tools import make_subplots



```python

 
```





### Changing the colour for the continents stacked proportional bar charts

Let's remake the chart using the code from the previous lesson, but making the stylistic changes on the way. Here's the initial chart. Let's change the bar colours to a colourscheme of our choosing. I've made my own theme using the incredible <a href="http://vrl.cs.brown.edu/color">Colorgorical</a> site:


```python
fig = make_subplots(rows = 3, cols = 3,
                   specs = [[{'rowspan' : 2, 'colspan' : 2}, None, {'rowspan' : 2}],
                            [None, None, None],
                            [{'colspan' : 3}, None, None]],
                   subplot_titles = ["Types of meteorite by weight", 
                                     "Number of meteorites by continent",
                                     "Weight categories of meteorite",])



stackedBarColours = ["rgb(95,134,183)", "rgb(177,200,235)", "rgb(1,54,136)", 
                     "rgb(237,180,236)", "rgb(104,12,113)", "rgb(241,82,182)", 
                     "rgb(101,230,249)",]    

stacked = py.get_figure("rmuir", 241)
for i, d in enumerate(stacked['data']):
    xVals = d['y']
    yVals = d['x']
    d.update({'orientation' : 'h',
             'x' : xVals,
             'y' : yVals,
             'marker' : {'color' : stackedBarColours[i]},
             'legendgroup' : 'continents'})
    fig.append_trace(d, row = 1, col = 3)
    
    
    
fig['layout']['xaxis2'].update({'tickformat' : '%',
                               'hoverformat' : '%'})
fig['layout'].update({'barmode' : 'stack',
                      'height' : 1000})

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(12)%20-%20Styling%20our%20first%20dashboard/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1           -      ]  [ (1,3) x2,y2 ]
           |                |                |       
    [ (3,1) x3,y3           -                -      ]
    
    





### Styling the weight-by-year chart

We'll firstly set the colour and legendgroup for the weight categories by year chart.


```python
sizes = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoriteLandingsbyWeightPerYear.csv", index_col = 0)

sizeStrings = sizes.columns.tolist()

sizes['total'] = sizes.sum(axis = 1)
for s in sizeStrings:
    sizes["{}_pc".format(s)] = sizes[s] / sizes['total']
    
sizeColours = ["rgb(194,87,211)", "rgb(77,87,168)", "rgb(223,184,245)", "rgb(88,38,166)"]

    
for i, s in enumerate(sizeStrings):
    fig.append_trace({'type' : 'scatter',
                     'mode' : 'markers+lines',
                     'x' : sizes.index,
                     'y' : sizes["{}_pc".format(s)],
                     'name' : s,
                     'marker' : {'color' : sizeColours[i]},
                     'legendgroup' : 'weightsbyyear'},
                    row = 3, col = 1)
    
fig['layout']['yaxis3'].update({'tickformat' : '%',
                               'hoverformat' : '%'})

pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(12)%20-%20Styling%20our%20first%20dashboard/pyo.iplot-1.png)``





### Changing the colour for size and type of meteorites, changing hover behaviour and setting the gap between legend groups

We can now set the colour for the chart which shows the size and type of meteorites. I'll also change the opacity so we can see the overplotting more clearly.

I'm setting the opacity by using an <code>rgba</code> value rather than by changing the opacity key in the plot. By doing it this way, we can see the overplotting of the datapoints; were we to use the opacity key, all of the points would have the same opacity.


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




```python
fig.append_trace({'type' : 'scatter',
             'mode' : "markers",
             'x' : typeWeight['wideClass'],
             'y' : typeWeight['mass (g)'],
                'showlegend' : False,
                  
                  #NEW CODE GOES HERE:
                 'hoverinfo' : 'x+y',
                 'marker' : {'color' : "rgba(107,20,214, 0.5)"}},
                row = 1, col = 1)

fig['layout']['yaxis1'].update({'title' : 'Weight (g)'})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(12)%20-%20Styling%20our%20first%20dashboard/pyo.iplot-2.png)`





Finally, let's make some changes to the layout. We'll first set the <code>'hovermode'</code> to <code>'closest'</code>:


```python
fig['layout'].update({'hovermode' : 'closest'})
```

We'll now add the source annotation and set the <code>tracegroupgap</code> to a large value to space these legend items apart even more, placing each by its parent chart:


```python
fig['layout'].update({'legend' : {'tracegroupgap' : 600}})

fig['layout'].update({'annotations' : 
                      [{'font': {'color': 'grey', 'size': 10},
                      'showarrow': False,
                      'text': '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                      'x': 0.1,
                      'xref': 'paper',
                      'y': -0.1,
                      'yref': 'paper'}]})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(12)%20-%20Styling%20our%20first%20dashboard/pyo.iplot-3.png)





I'm really happy with how this dashboard has turned out. Let's push it to the Plotly cloud!


```python
py.plot(fig, filename='Meteorite dashboard', fileopt = 'overwrite')
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(12)%20-%20Styling%20our%20first%20dashboard/py.plot-0.png)



    'https://plot.ly/~rmuir/253'



