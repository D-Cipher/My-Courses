
# Scatterplots (07) - Fitting and styling regression lines

In this lesson we're going to fit and display a regression line and equation to the data for males and females separately. This is a great opportunity to practise this skill, and it also results in a very striking chart.

We'll also learn how apply some styling to the text annotations, changing their colours to that each can be attributed to the correct data source.

We're going to get the DataFrame, then calculate the regressions and create the regression traces and annotations within a loop. We'll then get the original chart from the Plotly cloud and add these new traces and annotations to it.



#### New Modules:

We're going to use the <code>stats</code> module from the <code>scipy</code> library again:



from scipy.stats import linregress



```python

 
```





## Getting the data

We'll get the data and use it to calculate the regressions for the males and females separately:


```python
lifeExpectancy = pd.read_csv("http://www.richard-muir.com/data/public/csv/LifeExpectancyCigarettePrices.csv", index_col = 0)
```


```python
lifeExpectancy
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Region</th>
      <th>Country</th>
      <th>Sex</th>
      <th>Most sold cigarette brand (US$)</th>
      <th>Years</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Eastern Mediterranean</td>
      <td>Afghanistan</td>
      <td>Male</td>
      <td>0.22</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Eastern Mediterranean</td>
      <td>Afghanistan</td>
      <td>Female</td>
      <td>0.22</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Europe</td>
      <td>Albania</td>
      <td>Male</td>
      <td>1.43</td>
      <td>18</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Europe</td>
      <td>Albania</td>
      <td>Female</td>
      <td>1.43</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Africa</td>
      <td>Algeria</td>
      <td>Male</td>
      <td>1.14</td>
      <td>18</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Africa</td>
      <td>Algeria</td>
      <td>Female</td>
      <td>1.14</td>
      <td>20</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Europe</td>
      <td>Andorra</td>
      <td>Male</td>
      <td>3.13</td>
      <td>23</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Europe</td>
      <td>Andorra</td>
      <td>Female</td>
      <td>3.13</td>
      <td>27</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Americas</td>
      <td>Antigua and Barbuda</td>
      <td>Male</td>
      <td>2.41</td>
      <td>21</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Americas</td>
      <td>Antigua and Barbuda</td>
      <td>Female</td>
      <td>2.41</td>
      <td>23</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Americas</td>
      <td>Argentina</td>
      <td>Male</td>
      <td>1.37</td>
      <td>19</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Americas</td>
      <td>Argentina</td>
      <td>Female</td>
      <td>1.37</td>
      <td>23</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Europe</td>
      <td>Armenia</td>
      <td>Male</td>
      <td>1.49</td>
      <td>15</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Europe</td>
      <td>Armenia</td>
      <td>Female</td>
      <td>1.49</td>
      <td>19</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Western Pacific</td>
      <td>Australia</td>
      <td>Male</td>
      <td>10.77</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Western Pacific</td>
      <td>Australia</td>
      <td>Female</td>
      <td>10.77</td>
      <td>26</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Europe</td>
      <td>Austria</td>
      <td>Male</td>
      <td>5.21</td>
      <td>22</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Europe</td>
      <td>Austria</td>
      <td>Female</td>
      <td>5.21</td>
      <td>26</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Europe</td>
      <td>Azerbaijan</td>
      <td>Male</td>
      <td>0.87</td>
      <td>17</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Europe</td>
      <td>Azerbaijan</td>
      <td>Female</td>
      <td>0.87</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Americas</td>
      <td>Bahamas</td>
      <td>Male</td>
      <td>2.69</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Americas</td>
      <td>Bahamas</td>
      <td>Female</td>
      <td>2.69</td>
      <td>24</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Eastern Mediterranean</td>
      <td>Bahrain</td>
      <td>Male</td>
      <td>1.86</td>
      <td>21</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Eastern Mediterranean</td>
      <td>Bahrain</td>
      <td>Female</td>
      <td>1.86</td>
      <td>23</td>
    </tr>
    <tr>
      <th>24</th>
      <td>South-East Asia</td>
      <td>Bangladesh</td>
      <td>Male</td>
      <td>0.48</td>
      <td>18</td>
    </tr>
    <tr>
      <th>25</th>
      <td>South-East Asia</td>
      <td>Bangladesh</td>
      <td>Female</td>
      <td>0.48</td>
      <td>18</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Americas</td>
      <td>Barbados</td>
      <td>Male</td>
      <td>5.50</td>
      <td>21</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Americas</td>
      <td>Barbados</td>
      <td>Female</td>
      <td>5.50</td>
      <td>25</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Europe</td>
      <td>Belarus</td>
      <td>Male</td>
      <td>0.84</td>
      <td>14</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Europe</td>
      <td>Belarus</td>
      <td>Female</td>
      <td>0.84</td>
      <td>21</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>334</th>
      <td>Western Pacific</td>
      <td>Tuvalu</td>
      <td>Male</td>
      <td>5.39</td>
      <td>14</td>
    </tr>
    <tr>
      <th>335</th>
      <td>Western Pacific</td>
      <td>Tuvalu</td>
      <td>Female</td>
      <td>5.39</td>
      <td>15</td>
    </tr>
    <tr>
      <th>336</th>
      <td>Africa</td>
      <td>Uganda</td>
      <td>Male</td>
      <td>0.66</td>
      <td>16</td>
    </tr>
    <tr>
      <th>337</th>
      <td>Africa</td>
      <td>Uganda</td>
      <td>Female</td>
      <td>0.66</td>
      <td>17</td>
    </tr>
    <tr>
      <th>338</th>
      <td>Europe</td>
      <td>Ukraine</td>
      <td>Male</td>
      <td>0.70</td>
      <td>15</td>
    </tr>
    <tr>
      <th>339</th>
      <td>Europe</td>
      <td>Ukraine</td>
      <td>Female</td>
      <td>0.70</td>
      <td>20</td>
    </tr>
    <tr>
      <th>340</th>
      <td>Eastern Mediterranean</td>
      <td>United Arab Emirates</td>
      <td>Male</td>
      <td>1.91</td>
      <td>18</td>
    </tr>
    <tr>
      <th>341</th>
      <td>Eastern Mediterranean</td>
      <td>United Arab Emirates</td>
      <td>Female</td>
      <td>1.91</td>
      <td>19</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Europe</td>
      <td>United Kingdom</td>
      <td>Male</td>
      <td>9.80</td>
      <td>22</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Europe</td>
      <td>United Kingdom</td>
      <td>Female</td>
      <td>9.80</td>
      <td>25</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Africa</td>
      <td>United Republic of Tanzania</td>
      <td>Male</td>
      <td>1.81</td>
      <td>17</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Africa</td>
      <td>United Republic of Tanzania</td>
      <td>Female</td>
      <td>1.81</td>
      <td>18</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Americas</td>
      <td>United States of America</td>
      <td>Male</td>
      <td>5.72</td>
      <td>21</td>
    </tr>
    <tr>
      <th>347</th>
      <td>Americas</td>
      <td>United States of America</td>
      <td>Female</td>
      <td>5.72</td>
      <td>24</td>
    </tr>
    <tr>
      <th>348</th>
      <td>Americas</td>
      <td>Uruguay</td>
      <td>Male</td>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>349</th>
      <td>Americas</td>
      <td>Uruguay</td>
      <td>Female</td>
      <td>3.32</td>
      <td>24</td>
    </tr>
    <tr>
      <th>350</th>
      <td>Europe</td>
      <td>Uzbekistan</td>
      <td>Male</td>
      <td>0.69</td>
      <td>16</td>
    </tr>
    <tr>
      <th>351</th>
      <td>Europe</td>
      <td>Uzbekistan</td>
      <td>Female</td>
      <td>0.69</td>
      <td>18</td>
    </tr>
    <tr>
      <th>352</th>
      <td>Western Pacific</td>
      <td>Vanuatu</td>
      <td>Male</td>
      <td>6.56</td>
      <td>17</td>
    </tr>
    <tr>
      <th>353</th>
      <td>Western Pacific</td>
      <td>Vanuatu</td>
      <td>Female</td>
      <td>6.56</td>
      <td>19</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Americas</td>
      <td>Venezuela (Bolivarian Republic of)</td>
      <td>Male</td>
      <td>6.17</td>
      <td>21</td>
    </tr>
    <tr>
      <th>355</th>
      <td>Americas</td>
      <td>Venezuela (Bolivarian Republic of)</td>
      <td>Female</td>
      <td>6.17</td>
      <td>24</td>
    </tr>
    <tr>
      <th>356</th>
      <td>Western Pacific</td>
      <td>Viet Nam</td>
      <td>Male</td>
      <td>0.75</td>
      <td>20</td>
    </tr>
    <tr>
      <th>357</th>
      <td>Western Pacific</td>
      <td>Viet Nam</td>
      <td>Female</td>
      <td>0.75</td>
      <td>22</td>
    </tr>
    <tr>
      <th>358</th>
      <td>Eastern Mediterranean</td>
      <td>Yemen</td>
      <td>Male</td>
      <td>0.75</td>
      <td>16</td>
    </tr>
    <tr>
      <th>359</th>
      <td>Eastern Mediterranean</td>
      <td>Yemen</td>
      <td>Female</td>
      <td>0.75</td>
      <td>17</td>
    </tr>
    <tr>
      <th>360</th>
      <td>Africa</td>
      <td>Zambia</td>
      <td>Male</td>
      <td>1.64</td>
      <td>16</td>
    </tr>
    <tr>
      <th>361</th>
      <td>Africa</td>
      <td>Zambia</td>
      <td>Female</td>
      <td>1.64</td>
      <td>17</td>
    </tr>
    <tr>
      <th>362</th>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>Male</td>
      <td>0.50</td>
      <td>17</td>
    </tr>
    <tr>
      <th>363</th>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>Female</td>
      <td>0.50</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
<p>364 rows × 5 columns</p>
</div>



We'll get a list which contains the unique values for the Sex column and adapt the markerLookup dictionary to contain the colours which correspond to each sex. We'll use this to style the regression lines and equations.


```python
sexes = list(lifeExpectancy['Sex'].unique())
markerLookup = {'Male' : {'color' : '#663399'}, 
                'Female' :{'color' : '#FF6347'}}
```

### Fitting the regressions
We'll now fit the regression equation to the data for males and females separately. I'll store the results of the regression in a dictionary, with separate keys for Males and Females.

We'll calculate the x- and y-values of the regression line in the same way as in the previous lesson, I'm going to store the coordinates of the regression line so we can plot them easily:


```python
regressions = {}
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]
```

### Creating the traces
Now, within the same loop I can create the traces for the regression lines which we can then add to the chart. I'm setting the colours of these traces using the <code>markerLookup</code> dictionary:


```python
regressions = {}
traces = []
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]
    
    traces.append({'type' : 'scatter',
                  'mode' : 'lines',
                  'x' : regressions[sex]['x-values'],
                  'y' : regressions[sex]['y-values'],
                   'marker' : {'color' : markerLookup[sex]['color']},
                   'showlegend' : False })   
    
```

### Creating the annotations
Finally I can create the annotations within the loop. I'm going to loosely set the x- and y-coordinates and then fine-tune them when we have positioned them on the chart.

I also need to set the colour of the annotation text. This parameter is within the <code>'font'</code> dictionary:


```python
regressions = {}
traces = []
annotations = []
for sex in sexes:
    regressions[sex] = {}
    slope, intercept, r_value, p_value, std_err = linregress(lifeExpectancy['Most sold cigarette brand (US$)'][lifeExpectancy['Sex'] == sex],
                                                              lifeExpectancy['Years'][lifeExpectancy['Sex'] == sex])
    
    regressions[sex]['x-values'] = [0, lifeExpectancy['Most sold cigarette brand (US$)'].max()]
    regressions[sex]['y-values'] = [slope * regressions[sex]['x-values'][0] + intercept,
                                    slope * regressions[sex]['x-values'][1] + intercept]
    
    traces.append({'type' : 'scatter',
                  'mode' : 'lines',
                  'x' : regressions[sex]['x-values'],
                  'y' : regressions[sex]['y-values'],
                   'marker' : {'color' : markerLookup[sex]['color']},
                   'showlegend' : False }) 
    
    annotations.append({'text' : "<b>{}s: y = {:.2f}x + {:.2f}<br>R<sup>2</sup> = {:.2f}</b>".format(sex,slope, intercept, r_value**2),
                       'xref' : 'x',
                       'yref' : 'y',
                        'x' : 10,
                        'y' : 28,
                        'showarrow' : False,
                       'font' : {'color' : markerLookup[sex]['color']}})
```

Let's have a look at the objects we've created:


```python
regressions
```




    {'Female': {'x-values': [0, 13.300000000000001],
      'y-values': [18.231326567738115, 30.856333637129719]},
     'Male': {'x-values': [0, 13.300000000000001],
      'y-values': [16.165650623380085, 25.811627034189343]}}




```python
traces
```




    [{'marker': {'color': '#663399'},
      'mode': 'lines',
      'showlegend': False,
      'type': 'scatter',
      'x': [0, 13.300000000000001],
      'y': [16.165650623380085, 25.811627034189343]},
     {'marker': {'color': '#FF6347'},
      'mode': 'lines',
      'showlegend': False,
      'type': 'scatter',
      'x': [0, 13.300000000000001],
      'y': [18.231326567738115, 30.856333637129719]}]




```python
annotations
```




    [{'font': {'color': '#663399'},
      'showarrow': False,
      'text': '<b>Males: y = 0.73x + 16.17<br>R<sup>2</sup> = 0.33</b>',
      'x': 10,
      'xref': 'x',
      'y': 28,
      'yref': 'y'},
     {'font': {'color': '#FF6347'},
      'showarrow': False,
      'text': '<b>Females: y = 0.95x + 18.23<br>R<sup>2</sup> = 0.40</b>',
      'x': 10,
      'xref': 'x',
      'y': 28,
      'yref': 'y'}]



Both annotations have the same x- and y-coordinates. I'll change one so we can tell them apart:


```python
annotations[0]['y'] = 20
```

## Modifying the original chart
I'll use the <code>py.get_figure()</code> function to get the original chart:


```python
lifeExp = py.get_figure('rmuir',206)
pyo.iplot(lifeExp)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(07)%20-%20Fitting%20and%20styling%20regression%20lines/pyo.iplot-0.png)```





Now I can add the traces to the Data object within the Figure:


```python
lifeExp['data'] = lifeExp['data'] + traces
pyo.iplot(lifeExp)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(07)%20-%20Fitting%20and%20styling%20regression%20lines/pyo.iplot-1.png)``





And now the annotations can be added to the layout:


```python
lifeExp['layout']['annotations'] = annotations
pyo.iplot(lifeExp)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(07)%20-%20Fitting%20and%20styling%20regression%20lines/pyo.iplot-2.png)`





I'll move the annotation for females left and up a bit:


```python
lifeExp['layout']['annotations'][1]['x'] = 8
lifeExp['layout']['annotations'][1]['y'] = 29
pyo.iplot(lifeExp)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(07)%20-%20Fitting%20and%20styling%20regression%20lines/pyo.iplot-3.png)





So this chart looks pretty good to me! We have a different regression line for males and females, with the text annotations and lines styled to be consistent with the data points. You can clearly see the difference in the life expectancies for males and females; not only do females tend to live longer in all countries, but as the price of cigarettes increases their life expectancy at age 60 increases more than for males.

Let's send this to the Plotly cloud:


```python
py.plot(lifeExp, filename="Life expectancy against cost of cigarettes (Male & female regressions)", fileopt = "overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(07)%20-%20Fitting%20and%20styling%20regression%20lines/py.plot-0.png)



    'https://plot.ly/~rmuir/210'



