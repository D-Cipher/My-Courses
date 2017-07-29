
# Tables (8) - Adding tables to a dashboard

In this lesson we'll find out how to add tables to a dashboard. This is different to how we've included other charts together in a dashboard because we must initialise the figure by creating the table, and then add other charts to it.





from plotly.tools import FigureFactory as FF



```python

 
```





## Getting a table

Let's get the table we made in the previous lesson:


```python
table = py.get_figure("rmuir", 311)
pyo.iplot(table)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-0.png)```





## Making a bar chart

Let's now create a bar chart showing some information about the regions compared with the countries. We'll get the information on countries from the csv, but we'll exclude England because we'll be including information about each English region:


```python
countryDf = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
countryDf = countryDf[countryDf['Name'].isin(['Scotland','Wales','Northern Ireland'])][['Name','Population (2011)']]
countryDf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Population (2011)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Scotland</td>
      <td>5299900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wales</td>
      <td>3063758</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Northern Ireland</td>
      <td>1814318</td>
    </tr>
  </tbody>
</table>
</div>



And the data on the regions:


```python
regionsDf = pd.read_csv('http://richard-muir.com/data/public/csv/UKPopulationByRegion.csv', index_col = 0)
regionsDf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Population (2011)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>South East</td>
      <td>8634750</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>8173941</td>
    </tr>
    <tr>
      <th>2</th>
      <td>North West</td>
      <td>7052177</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>5846965</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>5601847</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South West</td>
      <td>5288935</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yorkshire and the Humber</td>
      <td>5283733</td>
    </tr>
    <tr>
      <th>7</th>
      <td>East Midlands</td>
      <td>4533222</td>
    </tr>
    <tr>
      <th>8</th>
      <td>North East</td>
      <td>2596886</td>
    </tr>
  </tbody>
</table>
</div>



And now let's concatenate them together, set the Population column to numeric, sort the values by Population and reset the index:


```python
df = pd.concat([countryDf, regionsDf])
df['Population (2011)'] = pd.to_numeric(df['Population (2011)'])
df = df.sort_values(by = 'Population (2011)', ascending = False).reset_index(drop = True)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Population (2011)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>South East</td>
      <td>8634750</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>8173941</td>
    </tr>
    <tr>
      <th>2</th>
      <td>North West</td>
      <td>7052177</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>5846965</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>5601847</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Scotland</td>
      <td>5299900</td>
    </tr>
    <tr>
      <th>6</th>
      <td>South West</td>
      <td>5288935</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Yorkshire and the Humber</td>
      <td>5283733</td>
    </tr>
    <tr>
      <th>8</th>
      <td>East Midlands</td>
      <td>4533222</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Wales</td>
      <td>3063758</td>
    </tr>
    <tr>
      <th>10</th>
      <td>North East</td>
      <td>2596886</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Northern Ireland</td>
      <td>1814318</td>
    </tr>
  </tbody>
</table>
</div>



We can now make a bar trace. I'm going to change the standard colour as well:


```python
bar = {'type' : 'bar',
      'x' : df['Name'],
      'y' : df['Population (2011)'],
      'marker' : {'color' : '#596dee'}}
pyo.iplot([bar])
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-1.png)``





## Adding the bar trace to our table

We can now add the bar trace to our figure containing the table. We're going to plot this bar chart above the table.

We have to do this in a few steps:

1. Add an axis anchor to our bar trace and add the bar trace to the data
2. Create new axes to hold the bar chart and set the domain of all the axes
3. Anchor the new axes together
4. Update the height

We're going to plot the table after every step to see how it changes:

### Adding an axis anchor and adding the bar trace to the table figure
Because we're adding this chart to a what will be a subplots object we have to specify which axes it will be attached to. Normally the subplots.append_trace() function does this for us.

We're going to add the bar trace to x2 and y2:


```python
bar.update({'xaxis' : 'x2',
           'yaxis' : 'y2'})
table['data'].extend([bar])
pyo.iplot(table)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-2.png)`





### Create new axes and set the domain

We're adding the bar traces to the y2axis, and we want the bar chart to sit above the table. We therefore need to set the domain of the y1axis and the y2axis to they occupy separate vertical space:


```python
table['layout']['yaxis'].update({'domain' : [0, 0.3]})
table['layout']['yaxis2'].update({'domain' : [0.5, 1]})
pyo.iplot(table)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-3.png)





### Anchoring the new axes together

We need to anchor the new axes together so they know which space to reference:


```python
table['layout']['yaxis2'].update({'anchor' : 'x2'})
table['layout']['xaxis2'].update({'anchor' : 'y2'})

pyo.iplot(table)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-4.png)




### Updating the height

Let's now update the height to spread apart the table and chart:


```python
table['layout'].update({'height' : 500})
pyo.iplot(table)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-5.png)



Let's now increase the left and right margins so we can see the yaxis range and the Northern Ireland label respectively and add a title.

We'll also need to increase the width to hold the row labels in the table (specifically Northern Ireland)


```python
table['layout'].update({'margin' : {'r' : 60, 'l' : 20, 't' : 40}})
table['layout'].update({'title' : 'Size of English Regions',
                       'width' : 900})
pyo.iplot(table)
```



![pyo.iplot-6](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/pyo.iplot-6.png)



```python
py.plot(table, filename="Population of English Regions (table & barchart)", fileopt = "overwrite")
```


![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(8)%20-%20Adding%20tables%20to%20a%20dashboard/py.plot-0.png)