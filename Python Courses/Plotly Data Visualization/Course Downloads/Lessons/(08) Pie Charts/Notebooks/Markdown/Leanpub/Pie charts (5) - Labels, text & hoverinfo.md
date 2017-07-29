
# Pie charts (5) - Labels, text & hoverinfo

In this lesson we're going to learn how text is displayed on a Plotly pie chart. When making line and scatter charts, we can choose to set a <code>'text'</code> property for the text which is displayed at the position of the points. We can do a similar thing for pie charts, instead deciding what is displayed next to each segment.






 






## Getting the data

We're going to use a new data source for this lesson. This .csv file contains data on the number of students studying at each level of study for several years. We're going to plot the number of students at each level of study for the most recent year:


```python
level = pd.read_csv("http://richard-muir.com/data/public/csv/StudentsByLevelAndYear.csv", index_col = 0)
level
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2005/06</th>
      <th>2006/07</th>
      <th>2007/08</th>
      <th>2008/09</th>
      <th>2009/10</th>
      <th>2010/11</th>
      <th>2011/12</th>
      <th>2012/13</th>
      <th>2013/14</th>
      <th>2014/15</th>
      <th>2015/16</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Postgraduate part-time</th>
      <td>114940</td>
      <td>116220</td>
      <td>116570</td>
      <td>129055</td>
      <td>132790</td>
      <td>127750</td>
      <td>109535</td>
      <td>102890</td>
      <td>106260</td>
      <td>107950</td>
      <td>107120</td>
    </tr>
    <tr>
      <th>Postgraduate full-time</th>
      <td>155665</td>
      <td>162575</td>
      <td>161015</td>
      <td>177595</td>
      <td>200880</td>
      <td>207595</td>
      <td>207665</td>
      <td>203155</td>
      <td>211875</td>
      <td>209805</td>
      <td>210945</td>
    </tr>
    <tr>
      <th>Undergraduate part-time</th>
      <td>337240</td>
      <td>341035</td>
      <td>332320</td>
      <td>344775</td>
      <td>334820</td>
      <td>301025</td>
      <td>278530</td>
      <td>199940</td>
      <td>175375</td>
      <td>157835</td>
      <td>148570</td>
    </tr>
    <tr>
      <th>Undergraduate full-time</th>
      <td>450485</td>
      <td>437775</td>
      <td>458575</td>
      <td>493425</td>
      <td>516770</td>
      <td>509065</td>
      <td>521605</td>
      <td>466270</td>
      <td>502230</td>
      <td>513295</td>
      <td>525490</td>
    </tr>
  </tbody>
</table>
</div>



Let's keep only the column we want, and sort the DataFrame by the values in that column. We saw previously that it can be a good idea to sort the data before putting it into the trace object.


```python
level = level[['2015/16']]
level.sort_values(by='2015/16', ascending = False, inplace = True)
level
```

    C:\Users\Rytch\Anaconda3\lib\site-packages\ipykernel\__main__.py:2: SettingWithCopyWarning:
    
    
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2015/16</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undergraduate full-time</th>
      <td>525490</td>
    </tr>
    <tr>
      <th>Postgraduate full-time</th>
      <td>210945</td>
    </tr>
    <tr>
      <th>Undergraduate part-time</th>
      <td>148570</td>
    </tr>
    <tr>
      <th>Postgraduate part-time</th>
      <td>107120</td>
    </tr>
  </tbody>
</table>
</div>



## Making our chart

Let's put the data into a pie chart, remembering to set the <code>'direction'</code> to <code>'clockwise'</code>. I'm also going to change the colours from the default.


```python
fig = {'data' : [{'type' : 'pie',
                  'name' : "Students by level of study",
                 'labels' : level.index,
                 'values' : level['2015/16'],
                 'direction' : 'clockwise',
                 'marker' : {'colors' : ["rgb(183,101,184)", "rgb(236,77,216)", "rgb(176,164,216)", "rgb(255,168,255)"]}}],
      'layout' : {'title' : 'Students by level of study in 2015-16'}}

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(5)%20-%20Labels,%20text%20&%20hoverinfo/pyo.iplot-0.png)```





## Different text options on pie charts

As well as hoverinfo, pie charts also have a parameter called <code>'textinfo'</code>. This determines which trace information appears written on the pie chart.

<code>'textinfo'</code> can take any of the following values, joined with a '+':
- <code>'label'</code> - displays the label on the segment
- <code>'text'</code> - displays the text on the segment (this can be set separately to the label)
- <code>'value'</code> - displays the value passed into the trace
- <code>'percent'</code> - displayed the computer percentage

You can see that the default is to only show <code>'percent'</code>. Let's add a <code>'text'</code> parameter to our trace and experiment with different options for the <code>textinfo</code>.

I'm going to use the <code>'text'</code> parameter to provide shortened versions of the label.


```python
fig['data'][0].update({'text' : ['Undergrad FT',' Postgrad FT','Undergrad PT','Postgrad PT'],
                      'textinfo' : 'label+text+value+percent'})

pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(5)%20-%20Labels,%20text%20&%20hoverinfo/pyo.iplot-1.png)``





So this has given us a lot of information on the chart. You can see that Plotly positions the text on the chart in several different ways.

I'm going to stop displaying the label because I think it's too long. Because we're showing this info on the pie chart, we can also remove the legend.


```python
fig['data'][0].update({'textinfo' : 'text+value+percent',
                      'showlegend' : False})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(5)%20-%20Labels,%20text%20&%20hoverinfo/pyo.iplot-2.png)`





## Hoverinfo

We also have the same options available to us for displaying the hoverinfo (we can also show the name of the trace on hover).

Let's set the hoverinfo to be the label. This way, if somebody doesn't understand one of the abbreviations they can still read the chart:


```python
fig['data'][0].update({'hoverinfo' : 'label'})
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(5)%20-%20Labels,%20text%20&%20hoverinfo/pyo.iplot-3.png)





Let's push this chart to the Plotly cloud:


```python
py.plot(fig, filename="Students by level of study in 2015-16", fileopt="overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(5)%20-%20Labels,%20text%20&%20hoverinfo/py.plot-0.png)



    'https://plot.ly/~rmuir/269'



