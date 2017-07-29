
# Scatterplots (09) - Making Bubbleplots

In this lesson we're going to learn how to make a bubbleplot. A bubbleplot is a variation on a scatterplot which allows us to visualise three variables on the same chart; the x- and y-variables are displayed as normal, and the third variable is shown by the size of the scatter markers.

Perhaps the most famous bubbleplot is that created by Hans Rosling of <a href="http://www.gapminder.org/tools/#_chart-type=bubbles">Gapminder</a>. This plot shows the life expectancy plotted against GDP for many countries. The size of the countries are shown by the size of the bubble, and the region to which they belong is shown by the colour. This plot encodes four different types of information in one plot. We'll learn how to recreate it in the next lesson:
<img src="https://openlab.citytech.cuny.edu/ganguli-math1372-fall2014/files/2014/11/gapminder.jpg"/>






 






## Changing the marker size
We've already seen how to change the marker size by accessing the <code>'size'</code> property in the <code>'marker'</code> option within the trace. To make a bubbleplot we pass a list of values to this property instead of a fixed number. Each item in the list of values which we pass to the <code>'marker' : {'size' :}</code> option corresponds to the data point at the same index.

The numbers that we pass to <code>'marker' : 'size'</code> set the marker size in pixels. We also need to set the <code>'sizemode'</code> property to <code>'area'</code> to ensure that the bubbles are sized correctly. <a href="http://themendozaline.org/post/95757674381/this-bubble-chart-is-killing-me">This article</a> explains why, but the basic idea is that using the circle's diameter exaggerates the degree of change between two numbers that area being compared.

In the below example, the first data point would have a size of 10 pixels, the second a size of 20 pixels, and the third a size of 30 pixels.
````python
trace = {'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [100, 200, 300],
                    'sizemode' : 'area'}}
````
When setting the marker size to a list of values, we may need to manipulate the <code>'sizeref'</code> property within the <code>'marker'</code> option in the trace. For example, if we were to set the marker size to the population, the marker for London would be 8,173,941 pixels. This is obviously quite large. We can reduce the size of all of the markers whilst keeping the same ratio by using <code>'sizeref'</code>:
````python
trace = {'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [10000, 20000, 30000],
                    'sizemode' : 'area'
                    'sizeref' : 10}}
````
Here's what the first example would look like as a chart:


```python
pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [100, 200, 300],
                   'sizemode' : 'area'}}])
```





And the second, without setting the <code>'sizeref'</code>:


```python
pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [10000, 20000, 30000],
                   'sizemode' : 'area'}}])
```





And with the <code>'sizeref'</code> set, the circles are scaled down in size whilst keeping the same ratio:


```python
pyo.iplot([{'x' : [1,2,3],
        'y' : [5,6,7],
        'marker' : {'size' : [10000, 20000, 30000],
                   'sizemode' : 'area',
                   'sizeref' : 10}}])
```





## Getting the data
We're going to practise making bubbleplots by using data on English regions which is available from Wikipedia. We'll once again use the <code>pd.read_html()</code> function to access this data:


```python
regionalData= pd.read_html("https://en.wikipedia.org/wiki/Regions_of_England", header=0)
```

The DataFrame with the data we want is the second item in the list that is returned:


```python
regionalData[3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name[29]</th>
      <th>Population</th>
      <th>10-year % increase (to 2011 Census)</th>
      <th>Area km²</th>
      <th>Pop. density /km²</th>
      <th>Median gross annual earnings (£) 2014[30]</th>
      <th>% of population claiming Income Support or JSA (August 2012)</th>
      <th>% as at August 2001</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>South East</td>
      <td>8634750</td>
      <td>7.9%</td>
      <td>19095</td>
      <td>452.20</td>
      <td>28629</td>
      <td>3.0%</td>
      <td>5.4%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>8173941</td>
      <td>14.0%</td>
      <td>1572</td>
      <td>5199.71</td>
      <td>35069</td>
      <td>5.3%</td>
      <td>10.1%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>North West</td>
      <td>7052177</td>
      <td>4.8%</td>
      <td>14165</td>
      <td>497.86</td>
      <td>25229</td>
      <td>5.3%</td>
      <td>10.4%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>5846965</td>
      <td>8.5%</td>
      <td>19120</td>
      <td>305.80</td>
      <td>26830</td>
      <td>3.5%</td>
      <td>6.2%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>5601847</td>
      <td>6.4%</td>
      <td>13000</td>
      <td>430.00</td>
      <td>24920</td>
      <td>5.1%</td>
      <td>9.2%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South West</td>
      <td>5288935</td>
      <td>7.3%</td>
      <td>23829</td>
      <td>221.95</td>
      <td>25571</td>
      <td>3.3%</td>
      <td>6.8%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yorkshire and the Humber</td>
      <td>5283733</td>
      <td>6.4%</td>
      <td>15420</td>
      <td>342.65</td>
      <td>24999</td>
      <td>5.2%</td>
      <td>9.3%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>East Midlands</td>
      <td>4533222</td>
      <td>8.7%</td>
      <td>15627</td>
      <td>290.09</td>
      <td>25027</td>
      <td>4.2%</td>
      <td>7.7%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>North East</td>
      <td>2596886</td>
      <td>3.2%</td>
      <td>8592</td>
      <td>302.24</td>
      <td>24876</td>
      <td>6.1%</td>
      <td>11.6%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>England</td>
      <td>53012456</td>
      <td>overall increase: 7.88%</td>
      <td>130395</td>
      <td>406.55</td>
      <td>27487</td>
      <td>overall average: 4.45%</td>
      <td>overall average: 8.32%[31]</td>
    </tr>
  </tbody>
</table>
</div>



Let's remove England from the DataFrame by using the <code>df.loc[]</code> selector:


```python
regions = regionalData[3][regionalData[3]['Name[29]'] != 'England']
regions
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name[29]</th>
      <th>Population</th>
      <th>10-year % increase (to 2011 Census)</th>
      <th>Area km²</th>
      <th>Pop. density /km²</th>
      <th>Median gross annual earnings (£) 2014[30]</th>
      <th>% of population claiming Income Support or JSA (August 2012)</th>
      <th>% as at August 2001</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>South East</td>
      <td>8634750</td>
      <td>7.9%</td>
      <td>19095</td>
      <td>452.20</td>
      <td>28629</td>
      <td>3.0%</td>
      <td>5.4%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>8173941</td>
      <td>14.0%</td>
      <td>1572</td>
      <td>5199.71</td>
      <td>35069</td>
      <td>5.3%</td>
      <td>10.1%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>North West</td>
      <td>7052177</td>
      <td>4.8%</td>
      <td>14165</td>
      <td>497.86</td>
      <td>25229</td>
      <td>5.3%</td>
      <td>10.4%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>5846965</td>
      <td>8.5%</td>
      <td>19120</td>
      <td>305.80</td>
      <td>26830</td>
      <td>3.5%</td>
      <td>6.2%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>5601847</td>
      <td>6.4%</td>
      <td>13000</td>
      <td>430.00</td>
      <td>24920</td>
      <td>5.1%</td>
      <td>9.2%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South West</td>
      <td>5288935</td>
      <td>7.3%</td>
      <td>23829</td>
      <td>221.95</td>
      <td>25571</td>
      <td>3.3%</td>
      <td>6.8%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yorkshire and the Humber</td>
      <td>5283733</td>
      <td>6.4%</td>
      <td>15420</td>
      <td>342.65</td>
      <td>24999</td>
      <td>5.2%</td>
      <td>9.3%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>East Midlands</td>
      <td>4533222</td>
      <td>8.7%</td>
      <td>15627</td>
      <td>290.09</td>
      <td>25027</td>
      <td>4.2%</td>
      <td>7.7%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>North East</td>
      <td>2596886</td>
      <td>3.2%</td>
      <td>8592</td>
      <td>302.24</td>
      <td>24876</td>
      <td>6.1%</td>
      <td>11.6%</td>
    </tr>
  </tbody>
</table>
</div>



We'll also create a text column to show the hovertext. The hovertext will display the region's name and area - we'll show the area of the region by the size of the marker, so it's important to display this information clearly in the hovertext.


```python
regions['text'] = regions.apply(lambda x: "<b>{}</b><br>Area: {} Km<sup>2</sup>".format(x['Name[29]'], 
                                                                                                      x['Area km²']), 
                                               axis = 1)
regions
```

    C:\Users\Rytch\Anaconda3\lib\site-packages\ipykernel\__main__.py:3: SettingWithCopyWarning:
    
    
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name[27]</th>
      <th>Population</th>
      <th>10-year % increase (to 2011 Census)</th>
      <th>Area km²</th>
      <th>Pop. density /km²</th>
      <th>Median gross annual earnings (£) 2014[28]</th>
      <th>% of population claiming Income Support or JSA (August 2012)</th>
      <th>% as at August 2001</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>South East</td>
      <td>8634750</td>
      <td>7.9%</td>
      <td>19095</td>
      <td>452.20</td>
      <td>28629</td>
      <td>3.0%</td>
      <td>5.4%</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;Area: 19095 Km&lt;sup&gt;2&lt;/sup&gt;</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>8173941</td>
      <td>14.0%</td>
      <td>1572</td>
      <td>5199.71</td>
      <td>35069</td>
      <td>5.3%</td>
      <td>10.1%</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;Area: 1572 Km&lt;sup&gt;2&lt;/sup&gt;</td>
    </tr>
    <tr>
      <th>2</th>
      <td>North West</td>
      <td>7052177</td>
      <td>4.8%</td>
      <td>14165</td>
      <td>497.86</td>
      <td>25229</td>
      <td>5.3%</td>
      <td>10.4%</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;Area: 14165 Km&lt;sup&gt;2&lt;/sup&gt;</td>
    </tr>
    <tr>
      <th>3</th>
      <td>East of England</td>
      <td>5846965</td>
      <td>8.5%</td>
      <td>19120</td>
      <td>305.80</td>
      <td>26830</td>
      <td>3.5%</td>
      <td>6.2%</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;Area: 19120 Km&lt;sup&gt;2...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Midlands</td>
      <td>5601847</td>
      <td>6.4%</td>
      <td>13000</td>
      <td>430.00</td>
      <td>24920</td>
      <td>5.1%</td>
      <td>9.2%</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;Area: 13000 Km&lt;sup&gt;2&lt;/...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South West</td>
      <td>5288935</td>
      <td>7.3%</td>
      <td>23829</td>
      <td>221.95</td>
      <td>25571</td>
      <td>3.3%</td>
      <td>6.8%</td>
      <td>&lt;b&gt;South West&lt;/b&gt;&lt;br&gt;Area: 23829 Km&lt;sup&gt;2&lt;/sup&gt;</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Yorkshire and the Humber</td>
      <td>5283733</td>
      <td>6.4%</td>
      <td>15420</td>
      <td>342.65</td>
      <td>24999</td>
      <td>5.2%</td>
      <td>9.3%</td>
      <td>&lt;b&gt;Yorkshire and the Humber&lt;/b&gt;&lt;br&gt;Area: 15420...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>East Midlands</td>
      <td>4533222</td>
      <td>8.7%</td>
      <td>15627</td>
      <td>290.09</td>
      <td>25027</td>
      <td>4.2%</td>
      <td>7.7%</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;Area: 15627 Km&lt;sup&gt;2&lt;/...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>North East</td>
      <td>2596886</td>
      <td>3.2%</td>
      <td>8592</td>
      <td>302.24</td>
      <td>24876</td>
      <td>6.1%</td>
      <td>11.6%</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;Area: 8592 Km&lt;sup&gt;2&lt;/sup&gt;</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting the data
Let's create our scatterplot. On this plot we're going to represent the population on the x-axis, the median earnings on the y-axis, and the area by the size of the bubble.

We'll create the basic scatterplot first, and then add in the <code>'marker' : {'size' : }</code> property after.

I'm going to set the hoverinfo to <code>'text+x+y'</code> so that all the information about a data point will be shown on hover.


```python
regionTrace = {'type' : 'scatter',
              'mode' : 'markers',
              'x' : regions['Population'],
              'y' : regions['Median gross annual earnings (£) 2014[30]'],
              'text' : regions['text'],
              'hoverinfo' : 'text+x+y'}
```

In the layout, I'll set the range of the axes dynamically, as well as adding a <code>'tickformat'</code> and <code>'tickprefix'</code> to the y-axis:


```python
layout = {'title' : 'Population, median earnings and area of English regions',
         'xaxis' : {'title' : 'Population',
                   'range' : [regions['Population'].min() * 0.95, 
                             regions['Population'].max() * 1.05]},
         'yaxis' : {'title' : 'Median earnings',
                   'tickformat' : ',',
                   'tickprefix' : '£',
                   'range' : [regions['Median gross annual earnings (£) 2014[30]'].min() * 0.95, 
                             regions['Median gross annual earnings (£) 2014[30]'].max() * 1.05]}}

fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(09)%20-%20Making%20Bubbleplots/pyo.iplot-0.png)```





Now, let's add the marker size to the trace and replot the chart:


```python
regionTrace.update({'marker' : {'size' : regions['Area km²'],
                               'sizemode' : 'area'}})
fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(09)%20-%20Making%20Bubbleplots/pyo.iplot-1.png)``





It seems as though we'll have to set the <code>'sizeref'</code>:


```python
regionTrace['marker'].update({'sizeref' : 5 })
fig = Figure(data = [regionTrace], layout = layout)
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(09)%20-%20Making%20Bubbleplots/pyo.iplot-2.png)`





I'm going to increase the range so we can see the full markers:


```python
fig['layout']['xaxis'].update({'range' : [regions['Population'].min() * 0.75, 
                                         regions['Population'].max() * 1.05]})

fig['layout']['yaxis'].update({'range' : [regions['Median gross annual earnings (£) 2014[30]'].min() * 0.75, 
                                         regions['Median gross annual earnings (£) 2014[30]'].max() * 1.05]})

pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(09)%20-%20Making%20Bubbleplots/pyo.iplot-3.png)





That allows us to see the entire bubble for each region. Let's push this to the Plotly cloud:


```python
py.plot(fig, filename = "Population, median earnings and area of English regions", fileopt="overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(09)%20-%20Making%20Bubbleplots/py.plot-0.png)



    'https://plot.ly/~rmuir/214'



