
# Barcharts (8) - Stacked proportional bar charts

In this lesson we'll learn how to create a special type of stacked bar chart; a stacked proportional bar chart. This is similar in concept to the stacked area chart that we learnt how to make in the Lineplot section.






 






## Getting the data
We're going to get the same dataset that we used for the previous chart. We'll need to do some reshaping and data manipulation in order to calculate the the proportions.


```python
meteorites = pd.read_csv("http://richard-muir.com/data/public/csv/MeteoritesByContinent.csv", index_col = 0)
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>continent</th>
      <th>year</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Africa</td>
      <td>2000</td>
      <td>239</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Africa</td>
      <td>2001</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Africa</td>
      <td>2002</td>
      <td>109</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Africa</td>
      <td>2003</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Africa</td>
      <td>2004</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>



Firstly we need a list of the unique continents, which we'll use to calculate the proportions:


```python
continents = list(meteorites['continent'].unique())
continents
```




    ['Africa',
     'Antarctica',
     'Asia',
     'Australia',
     'Europe',
     'North America',
     'South America']



The first step is to pivot the DataFrame. We want a DataFrame which shows for each year, the number of meteorites found in each continent.

I'll use <code>df.pivot()</code>, setting <code>index='year'</code>, <code>columns='continent'</code> and <code>values='count'</code>. This means that each of the unique values in the 'year' column will become a row and each of the unique values in the 'continent' column will become a column. The intersection of each row and column will then be filled with the value held in the 'count' column.


```python
meteorites = meteorites.pivot(index='year',columns = 'continent', values='count')
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>continent</th>
      <th>Africa</th>
      <th>Antarctica</th>
      <th>Asia</th>
      <th>Australia</th>
      <th>Europe</th>
      <th>North America</th>
      <th>South America</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>239.0</td>
      <td>806.0</td>
      <td>389.0</td>
      <td>NaN</td>
      <td>15.0</td>
      <td>46.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>87.0</td>
      <td>499.0</td>
      <td>636.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>50.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>109.0</td>
      <td>586.0</td>
      <td>281.0</td>
      <td>2.0</td>
      <td>10.0</td>
      <td>37.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>30.0</td>
      <td>1422.0</td>
      <td>207.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>32.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>17.0</td>
      <td>30.0</td>
      <td>155.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>53.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



We now need to replace the <code>NaN</code> values with a 0:


```python
meteorites.fillna(value = 0, inplace = True)
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>continent</th>
      <th>Africa</th>
      <th>Antarctica</th>
      <th>Asia</th>
      <th>Australia</th>
      <th>Europe</th>
      <th>North America</th>
      <th>South America</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>239.0</td>
      <td>806.0</td>
      <td>389.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>46.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>87.0</td>
      <td>499.0</td>
      <td>636.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>50.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>109.0</td>
      <td>586.0</td>
      <td>281.0</td>
      <td>2.0</td>
      <td>10.0</td>
      <td>37.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>30.0</td>
      <td>1422.0</td>
      <td>207.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>32.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>17.0</td>
      <td>30.0</td>
      <td>155.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>53.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



Then use the <code>df.sum()</code> method to get the total for each row:


```python
meteorites['total'] = meteorites.sum(axis = 1)
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>continent</th>
      <th>Africa</th>
      <th>Antarctica</th>
      <th>Asia</th>
      <th>Australia</th>
      <th>Europe</th>
      <th>North America</th>
      <th>South America</th>
      <th>total</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>239.0</td>
      <td>806.0</td>
      <td>389.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>46.0</td>
      <td>4.0</td>
      <td>1499.0</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>87.0</td>
      <td>499.0</td>
      <td>636.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>50.0</td>
      <td>5.0</td>
      <td>1278.0</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>109.0</td>
      <td>586.0</td>
      <td>281.0</td>
      <td>2.0</td>
      <td>10.0</td>
      <td>37.0</td>
      <td>5.0</td>
      <td>1030.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>30.0</td>
      <td>1422.0</td>
      <td>207.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>32.0</td>
      <td>14.0</td>
      <td>1713.0</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>17.0</td>
      <td>30.0</td>
      <td>155.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>53.0</td>
      <td>3.0</td>
      <td>264.0</td>
    </tr>
  </tbody>
</table>
</div>



We can now loop through our list of continents, calculating the proportion of meteorites each year that fell in each continent:


```python
for c in continents:
    meteorites["{}_pc".format(c)] = meteorites[c] / meteorites['total']
    
meteorites.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>continent</th>
      <th>Africa</th>
      <th>Antarctica</th>
      <th>Asia</th>
      <th>Australia</th>
      <th>Europe</th>
      <th>North America</th>
      <th>South America</th>
      <th>total</th>
      <th>Africa_pc</th>
      <th>Antarctica_pc</th>
      <th>Asia_pc</th>
      <th>Australia_pc</th>
      <th>Europe_pc</th>
      <th>North America_pc</th>
      <th>South America_pc</th>
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
      <td>239.0</td>
      <td>806.0</td>
      <td>389.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>46.0</td>
      <td>4.0</td>
      <td>1499.0</td>
      <td>0.159440</td>
      <td>0.537692</td>
      <td>0.259506</td>
      <td>0.000000</td>
      <td>0.010007</td>
      <td>0.030687</td>
      <td>0.002668</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>87.0</td>
      <td>499.0</td>
      <td>636.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>50.0</td>
      <td>5.0</td>
      <td>1278.0</td>
      <td>0.068075</td>
      <td>0.390454</td>
      <td>0.497653</td>
      <td>0.000000</td>
      <td>0.000782</td>
      <td>0.039124</td>
      <td>0.003912</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>109.0</td>
      <td>586.0</td>
      <td>281.0</td>
      <td>2.0</td>
      <td>10.0</td>
      <td>37.0</td>
      <td>5.0</td>
      <td>1030.0</td>
      <td>0.105825</td>
      <td>0.568932</td>
      <td>0.272816</td>
      <td>0.001942</td>
      <td>0.009709</td>
      <td>0.035922</td>
      <td>0.004854</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>30.0</td>
      <td>1422.0</td>
      <td>207.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>32.0</td>
      <td>14.0</td>
      <td>1713.0</td>
      <td>0.017513</td>
      <td>0.830123</td>
      <td>0.120841</td>
      <td>0.000584</td>
      <td>0.004086</td>
      <td>0.018681</td>
      <td>0.008173</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>17.0</td>
      <td>30.0</td>
      <td>155.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>53.0</td>
      <td>3.0</td>
      <td>264.0</td>
      <td>0.064394</td>
      <td>0.113636</td>
      <td>0.587121</td>
      <td>0.003788</td>
      <td>0.018939</td>
      <td>0.200758</td>
      <td>0.011364</td>
    </tr>
  </tbody>
</table>
</div>



We'll now order the traces in order to show the trace with the largest proprtion at the bottom. I'll do this heuristically by calculating the sum of the proportions and ordering the traces based on that sum.

We'll use the <code>sorted()</code> function in conjunction with the <code>lambda</code> function to sort the list by the values of the dictionary. I'll set <code>reverse=True</code> to sort by descending values:


```python
pcContinents = [c + "_pc" for c in continents]

sortKeys = dict(meteorites[pcContinents].sum())

pcContinents = sorted(pcContinents, key=lambda k: sortKeys[k], reverse=True)
pcContinents
```




    ['Asia_pc',
     'Antarctica_pc',
     'North America_pc',
     'South America_pc',
     'Africa_pc',
     'Europe_pc',
     'Australia_pc']



## Making the chart
We can now pass the percentages into the bar chart traces, modifying the loop slightly to take into account the changed data structure:


```python
traces = []

for c in pcContinents:
    traces.append({'type' : 'bar',
                  'name' : c[:-3],
                  'x' : meteorites.index,
                  'y' : meteorites[c],
                  'opacity' : 0.7})

pyo.iplot(traces)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(08)%20-%20Stacked%20proportional%20bar%20charts/pyo.iplot-0.png)```





## Stacking the bars and polishing the chart

Let's now add the layout:


```python
layout = {'title' : "Proportion of meteorites found by continent, 2000 - 2012",
          'barmode' : 'stack',
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Proportion of meteorites',
                   'tickformat' : '%',
                   'hoverformat' : '%',},
         'annotations' : [{'text' : '<i>Source: https://data.nasa.gov/view/ak9y-cwf9</i>',
                          'font' : {'color' : 'grey',
                                   'size' : 10},
                          'xref' : 'paper',
                          'yref' : 'paper',
                          'x' : 0,
                          'y' : -0.2,
                          'showarrow' : False}]}
fig = {'data' : traces, 'layout' : layout}
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(08)%20-%20Stacked%20proportional%20bar%20charts/pyo.iplot-1.png)``





Thus completes our stacked proportional bar chart. There seems to be a lot of variability in where meteorites are found in the world, however the majority are found in Antartica abd Asia, with very few being found in Australia.

Let's send this chart to the Plotly cloud.


```python
py.plot(fig, filename="Meteorites found by continent (2000 - 2012, stacked bar)", fileopt = "overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Barcharts%20(08)%20-%20Stacked%20proportional%20bar%20charts/py.plot-0.png)`




    'https://plot.ly/~rmuir/241'



