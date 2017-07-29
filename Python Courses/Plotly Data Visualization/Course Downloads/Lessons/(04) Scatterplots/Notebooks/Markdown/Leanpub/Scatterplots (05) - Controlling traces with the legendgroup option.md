
# Scatterplots (05) - Controlling traces with the legendgroup option

In this lesson we're going to learn how to control the show/hide behaviour of multiple traces at the same time by using the <code>'legendgroup'</code> option within the trace object.

We're going to plot data on life expectancy at age 60 against the dollar price of the most popular brand of cigarettes. The dataset contains data for 182 countries, each belonging to one of six regions. Each country has an observation on the life expectancy for males and females.

This will be quite a complex chart, but by grouping the observations for Sex by colour, and allowing the user to select which region(s) they can view, we can make this data easier to understand.






 






## Getting and preparing the data
We'll get the data as a .csv file from my website:


```python
lifeExpectancy = pd.read_csv("http://www.richard-muir.com/data/public/csv/LifeExpectancyCigarettePrices.csv", index_col = 0)
lifeExpectancy.head()
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
  </tbody>
</table>
</div>



Let's create a text column:


```python
lifeExpectancy['text'] = lifeExpectancy.apply(lambda x: 
    "<b>{}</b><br>Life expectancy for {}s at 60: {} years<br>Price of cigarettes: ${:.2f}".format(x['Country'], 
                                                                                  x['Sex'],
                                                                                x['Years'],
                                                                                 float(x['Most sold cigarette brand (US$)'])), axis = 1)
```

And check that it has worked as expected:


```python
lifeExpectancy.loc[0, 'text']
```




    '<b>Afghanistan</b><br>Life expectancy for Males at 60: 15 years<br>Price of cigarettes: $0.22'



We need to get a list of the unique values of the Region column so that we can loop through these to create the traces:


```python
regions = list(lifeExpectancy['Region'].unique())
regions
```




    ['Eastern Mediterranean',
     'Europe',
     'Africa',
     'Americas',
     'Western Pacific',
     'South-East Asia']



We need to do the same for the values in the Sex column


```python
sexes = list(lifeExpectancy['Sex'].unique())
sexes
```




    ['Male', 'Female']



We can now use this to build our region-to-symbol and sex-to-colour lookup:


```python
markerLookup = {'Eastern Mediterranean' : {'symbol' : 'circle'},
                     'Europe' :           {'symbol' : 'square'},
                     'Africa' :           {'symbol' : 'diamond'},
                     'Americas' :         {'symbol' : 'triangle-up'},
                     'Western Pacific' :  {'symbol' : 'cross'},
                     'South-East Asia' :  {'symbol' : 'x'},
                'Male' : {'color' : '#663399'}, 
                'Female' :{'color' : '#FF6347'}}
```

## Plotting the data

For this chart we're going to create a trace for each of the Regions and for each of 'Male' and 'Female'. This will result in our chart having a total of 12 legend items! We'll then use <code>'legendgroup'</code> to control how these traces are displayed in the legend, and make the chart a lot clearer.

Let's now make the traces for our chart. We're going to do this in a nested loop; the outer loop will cycle through the list of sexes, whilst the inner loop will cycle through the regions; we'll create a trace for each combination. 

We'll plot the Life expectancy from age 60 on the y-axis, as it is the dependent variable; in this case I'm hypothesising that as the price of cigarettes increases, the life expectancy from age 60 will also increase.

We'll set the x-values, y-values and text for each trace by using the <code>df.loc[]</code> indexer in the same way as in the previous lesson, however rather than only using a condition on one column, we're going to select only the rows which fulfill two conditions on two columns. Namely that the values for Region and Sex match those which we are plotting for this trace. Notice that each condition is contained within parentheses:
````python
lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years']
````

We're also going to use the colour lookup we created earlier to style each trace, and I'm setting the name of the trace by inserting the values of <code>region</code> and <code>sex</code> into a string using the <code>str.format()</code> method:


```python
traces = []

for sex in sexes:
    for reg in regions:
        traces.append({'type' : 'scatter',
                      'mode' : 'markers',
                      'x' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),
                                               'Most sold cigarette brand (US$)'],
                        'y' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years'],
                       'text' : lifeExpectancy.loc [(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),'text'],
                       'hoverinfo' : 'text',
                       'marker' : {'color' : markerLookup[sex]['color'],
                                   'symbol' : markerLookup[reg]['symbol'],
                                  'opacity' : 0.7},
                      'name' : "{}, {}".format(reg, sex)})
```

Let's create the layout, Figure and plot the chart.

I'm setting the range for each axis (with the price of cigarettes going down to 0), the hovermode to 'closest', and a tickformat for the y-axis:


```python
layout = {'title' : 'Life expectancy against price of most popular brand of cigarettes (2011)',
         'xaxis' : {'title' : 'Price of most popular brand of cigarettes',
                    'range' : [0, 
                               lifeExpectancy['Most sold cigarette brand (US$)'].max() * 1.05],
                   'tickformat' : "${:}"},
         'yaxis' : {'title' : 'Life expectancy at age 60 (years)',
                    'range' : [lifeExpectancy['Years'].min()*0.9, 
                              lifeExpectancy['Years'].max()*1.05],},
         'hovermode' : 'closest'}
```


```python
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(05)%20-%20Controlling%20traces%20with%20the%20legendgroup%20option/pyo.iplot-0.png)```





So this chart seems to show that as the price of cigarettes increases, the life expectancy at age 60 also increases. We've got a pretty clear split between the life expectancies of males and females which is clear from the colour of the markers, but it's difficult to discern the differences within regions - you have to click on many different legend items to reduce the number of regions which are shown.

Let's use <code>'legendgroup'</code> to change this:

## Using <code>'legendgroup'</code>

The <code>'legendgroup'</code> option allows us to group traces together so that they are shown and hidden by clicking any of the legend items in that group. A <code>'legendgroup'</code> must be a string:
````python
trace = {'legendgroup' : <string>}
````

We're going to set the <code>'legendgroup'</code> to be equal to the current <code>region</code>; each <code>'legendgroup'</code> will therefore contain two traces; one for males and one for females.


```python
traces = []

for sex in sexes:
    for reg in regions:
        traces.append({'type' : 'scatter',
                      'mode' : 'markers',
                      'x' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),
                                               'Most sold cigarette brand (US$)'],
                        'y' : lifeExpectancy.loc[(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex), 'Years'],
                       'text' : lifeExpectancy.loc [(lifeExpectancy['Region'] == reg) & (lifeExpectancy['Sex'] == sex),'text'],
                       
                       'legendgroup' : reg,                 
                       
                       'hoverinfo' : 'text',
                       'marker' : {'color' : markerLookup[sex]['color'],
                                   'symbol' : markerLookup[reg]['symbol'],
                                  'opacity' : 0.7},
                      'name' : "{}, {}".format(reg, sex)})
```

Let's refresh the Figure object and plot the data:


```python
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(05)%20-%20Controlling%20traces%20with%20the%20legendgroup%20option/pyo.iplot-1.png)``





So this is a great improvement on the legend - although the number of legend items hasn't changed, they are grouped in such a way that it is intuitive for the reader to use. The legend items are now connected; should the user want to only view the data for a single region, they don't have to remove every single trace:

Let's push this chart to the Plotly cloud:


```python
py.plot(fig, filename="Life expectancy and cigarette prices", fileopt = 'overwrite')
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(05)%20-%20Controlling%20traces%20with%20the%20legendgroup%20option/py.plot-0.png)`




    'https://plot.ly/~rmuir/206'



