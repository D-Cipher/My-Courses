
# Pie charts (2) - Making our first pie chart

In this lesson we're going to make our first pie chart. This chart will show the breakdown of ethnicity for students at UK universities. We're going to do this using data from the UK's <a href="https://www.hesa.ac.uk/">Higher Education Statistics Agency</a> (HESA).

We'll also learn how to use the <code>'sort'</code> and <code>'direction'</code> parameters to change the order in which the segments are placed.






 






## Getting the data
I've prepared a small extract of the data available from the HESA website for use in this lesson. 

We're getting this .csv file in a slightly different way; the .csv file doesn't have a header column, so we're telling pandas that this is the case and specifying a name for the column:


```python
ethnicity = pd.read_csv("http://www.richard-muir.com/data/public/csv/UKStudentsEthnicity.csv",
                        index_col = 0, header=None, names=['N'])
ethnicity
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>N</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>White</th>
      <td>1418685.0</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>84525.0</td>
    </tr>
    <tr>
      <th>Not known</th>
      <td>33290.0</td>
    </tr>
    <tr>
      <th>Black</th>
      <td>117460.0</td>
    </tr>
    <tr>
      <th>Asian</th>
      <td>175240.0</td>
    </tr>
  </tbody>
</table>
</div>



## Making a pie chart

To make a pie chart with Plotly, we only need to pass three parameters to our trace; <code>'labels'</code>, <code>'values'</code> and <code>'type'</code>.

- <code>'labels'</code> is a list of the categories that we're plotting
- <code>'values'</code> is a list of the number of things in that category
- <code>'type'</code> should be set to <code>'pie'</code> to tell Plotly that we're making a pie chart

The lists for <code>'labels'</code> and <code>'values'</code> must be the same length.

Plotly does all the calculations to determine the angle for each slice of the pie; it's that easy!

Let's make our first trace:


```python
pieTrace = {'type' : 'pie',
           'labels' : ethnicity.index,
           'values' : ethnicity['N']}

data = [pieTrace]

layout = {'title' : 'Ethnicity of students in the UK'}

fig = {'data' : data, 'layout' : layout}

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(2)%20-%20Making%20our%20first%20pie%20chart/pyo.iplot-0.png)```





## Is this a clear and easy-to-understand pie chart?
You may remember from the next lesson that the (excellent) ONS guidelines recommend that the segments in a pie chart be sorted from largest to smallest. 

Plotly have included a <code>'sort'</code> parameter in the pie chart trace and by default it is set to <code>True</code>, although it doesn't appear to have sorted our segments in the correct order; I would expect the segment for 'Not known' to be last instead of 'Asian' as is currently the case.

Let's try setting <code>'sort'</code> to <code>False</code> and see what changes:


```python
fig['data'][0].update({'sort' : False})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(2)%20-%20Making%20our%20first%20pie%20chart/pyo.iplot-1.png)``





So this has changed the order in which the segments appear, but not satisfactorily. The segments now appear in the same order that they do in the data.

Let's change <code>'sort'</code> back to <code>True</code> and look at the <code>'direction'</code> parameter...

The default <code>direction</code> for how the segments follow each other is <code>'counterclockwise'</code>. Let's set <code>direction</code> to <code>'clockwise'</code> to fix this:


```python
fig['data'][0].update({'direction' : 'clockwise',
                      'sort' : True})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(2)%20-%20Making%20our%20first%20pie%20chart/pyo.iplot-2.png)`





That's much better! Let's push this chart to the Plotly cloud:


```python
py.plot(fig, filename="Ethnicity of UK students", fileopt="overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(2)%20-%20Making%20our%20first%20pie%20chart/py.plot-0.png)




    'https://plot.ly/~rmuir/263'



