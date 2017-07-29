
# Chart presentation (3) - Modifying tickvalues

In the last lesson we saw how to apply different tickformats to the ticks on the x- and y-axes.

In this lesson we'll learn how to modify the standard tickvalues by adding a tick prefix or suffix. We'll also learn how to specify the number of ticks that Plotly shows.






 






## Getting a chart to modify:

We'll use the stacked area chart showing total emissions for 5 countries to practise setting the tickprefix, ticksuffix and number of ticks:


```python
C02 = py.get_figure('rmuir', 156)
pyo.iplot(C02)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-0.png)```





## Modifying the tick values

We can change how the tick values are displayed by adding a tick suffix or prefix.
Both of these options are contained within in the x- and y-axis objects:
````python
layout = {'xaxis' : {'ticksuffix' :  <string>}}
````

Let's add a tick suffix of <code>'Kt'</code> to the ticks on the y-axis:


```python
C02['layout']['yaxis'].update({'ticksuffix' : ' Kt'})
pyo.iplot(C02)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-1.png)``





We can also add a tick prefix if we wish. I'm removing the title so that it doesn't overlap with the longer ticks:


```python
C02['layout']['yaxis'].update({'tickprefix' : 'C02: ', 'title' : ''})
pyo.iplot(C02)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-2.png)`





I'm not a fan of the tick prefix in this case, however it is useful when plotting currencies which aren't available as a tickformat. I'll remove the tick prefix and reinstate the title before we continue:


```python
C02['layout']['yaxis'].update({'tickprefix' : '', 'title' : 'C02 Emissions'})
pyo.iplot(C02)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-3.png)





Let's make a chart to practise using the <code>'tickprefix'</code> parameter.

We'll plot a line which shows the average house prices in England in £. There is no currency format which displays '£', but we can use a tick prefix to achieve this:


```python
housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKAvgHousePrices.csv")
housePrices.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Aberdeenshire</th>
      <th>Adur</th>
      <th>Allerdale</th>
      <th>Amber Valley</th>
      <th>Angus</th>
      <th>Antrim and Newtownabbey</th>
      <th>Argyll and Bute</th>
      <th>Armagh Banbridge and Craigavon</th>
      <th>Arun</th>
      <th>...</th>
      <th>Worcester</th>
      <th>Worcestershire</th>
      <th>Worthing</th>
      <th>Wrexham</th>
      <th>Wychavon</th>
      <th>Wycombe</th>
      <th>Wyre</th>
      <th>Wyre Forest</th>
      <th>York</th>
      <th>Yorkshire and The Humber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>0.0</td>
      <td>54516.42545</td>
      <td>44464.03724</td>
      <td>45424.80814</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>59473.60257</td>
      <td>...</td>
      <td>47392.61779</td>
      <td>57568.84958</td>
      <td>52047.16697</td>
      <td>46228.36134</td>
      <td>68571.03489</td>
      <td>85190.64525</td>
      <td>54934.17104</td>
      <td>48334.54374</td>
      <td>56382.41699</td>
      <td>44803.42878</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1995-02-01</td>
      <td>0.0</td>
      <td>55708.33312</td>
      <td>43864.48876</td>
      <td>45781.05509</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>57861.89776</td>
      <td>...</td>
      <td>48904.13429</td>
      <td>58907.10840</td>
      <td>51716.22929</td>
      <td>47401.20659</td>
      <td>69423.98457</td>
      <td>82237.40416</td>
      <td>55768.74570</td>
      <td>51027.41252</td>
      <td>55159.06106</td>
      <td>44528.80721</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1995-03-01</td>
      <td>0.0</td>
      <td>55724.54586</td>
      <td>43911.90021</td>
      <td>45469.23802</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>58035.46157</td>
      <td>...</td>
      <td>49067.61504</td>
      <td>58413.36820</td>
      <td>51950.24026</td>
      <td>46263.41484</td>
      <td>66847.52505</td>
      <td>82952.46904</td>
      <td>54466.45530</td>
      <td>52159.83267</td>
      <td>55953.15462</td>
      <td>45200.46775</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1995-04-01</td>
      <td>0.0</td>
      <td>55440.83646</td>
      <td>44669.46265</td>
      <td>42670.47853</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>57728.05671</td>
      <td>...</td>
      <td>50456.84930</td>
      <td>59299.84595</td>
      <td>51638.19424</td>
      <td>44885.56449</td>
      <td>65650.42169</td>
      <td>82091.98471</td>
      <td>53917.72064</td>
      <td>53413.52366</td>
      <td>55883.21855</td>
      <td>45614.34341</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995-05-01</td>
      <td>0.0</td>
      <td>53334.35175</td>
      <td>45593.71536</td>
      <td>41767.45702</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>58973.01254</td>
      <td>...</td>
      <td>49653.84590</td>
      <td>59236.78137</td>
      <td>51422.33415</td>
      <td>43715.76930</td>
      <td>66545.97518</td>
      <td>83927.37148</td>
      <td>52473.73282</td>
      <td>54010.00522</td>
      <td>56531.82376</td>
      <td>44830.98563</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 442 columns</p>
</div>




```python
EnglandAvgPrices = {'type' : 'scatter',
                   'x' : housePrices['Date'],
                   'y' : housePrices['England']}

data = Data([EnglandAvgPrices])
layout = {'title' : 'Average house prices in England 1995 - 2016',
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Average price'}}

fig = Figure(data = data, layout = layout)
pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-4.png)




Let's set the tickformat on the yaxis to have a thousand separator of a ' , ':


```python
fig['layout']['yaxis'].update({'tickformat' : ','})
pyo.iplot(fig)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-5.png)



We can now change the tick prefix to show a '£':


```python
fig['layout']['yaxis'].update({'tickprefix' : '£'})
pyo.iplot(fig)
```



![pyo.iplot-6](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-6.png)


Let's send this chart to the Plotly cloud:


```python
py.plot(fig, filename="Average House Prices in England 1995-2016")
```




![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/py.plot-0.png)
    'https://plot.ly/~rmuir/181'



## Changing the number of ticks

We'll use the C02 emissions plot from earlier to practise changing the number of ticks.

First of all, let's increase the number of tick along the x-axis. We can do this by setting the <code>'tickmode'</code> to <code>'auto'</code> and specifying the number of ticks with the <code>'nticks'</code> parameter. Both of these options are contained within in the axis object:
````python
layout = {'xaxis' : {'tickmode' : 'auto', 'nticks' : <integer>}}
````

Let's try doubling the number of ticks to show a tick every 5 years:


```python
C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 12})
pyo.iplot(C02)
```





![pyo.iplot-7](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-7.png)
We can also make the ticks more sparse:


```python
C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 3})
pyo.iplot(C02)
```






![pyo.iplot-8](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-8.png)But note that Plotly views the value for<code>'nticks'</code> as being the maximum number of ticks; it may not actually draw the requested number of ticks:


```python
C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 5})
pyo.iplot(C02)
```





L
![pyo.iplot-9](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-9.png)et's set the <code>'nticks'</code> parameter to 12 and update the chart in the Plotly cloud:


```python
C02['layout']['xaxis'].update({'tickmode' : 'auto', 'nticks' : 12})
pyo.iplot(C02)
```






`
![pyo.iplot-10](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/pyo.iplot-10.png)``python
py.plot(C02, filename="C02 Emissions for UAE, USA, UK, India & China 1960 - 2015", fileopt = 'overwrite')
```




    
![py.plot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(3)%20-%20Modifying%20tickvalues/py.plot-1.png)'https://plot.ly/~rmuir/166'



