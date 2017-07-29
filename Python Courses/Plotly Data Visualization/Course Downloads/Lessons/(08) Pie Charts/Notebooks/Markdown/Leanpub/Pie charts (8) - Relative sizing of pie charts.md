
# Pie charts (8) - Relative sizing of pie charts

In this lesson we're going to practise placing pie charts in a plotly subplot. We're also going to employ the <code>'scalegroup'</code> parameter to size these linked pie charts by their totals, relative to each other.





from plotly.tools import make_subplots



```python

 
```





## Getting the data

We're going to again use publically available data from HESA. This data shows, for each subject area, how many students who graduated in 2014-15 are in work, further study or are unemployed.

We'll choose a four different subject areas to compare using pie charts:


```python
outcomes = pd.read_csv("http://richard-muir.com/data/public/csv/StudentOutcomes201415BySubjectArea.csv", index_col = 0)
outcomes.head(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Work</th>
      <th>Work and further study</th>
      <th>Further study</th>
      <th>Unemployed</th>
      <th>Other</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Medicine &amp; dentistry</th>
      <td>6855.0</td>
      <td>135.0</td>
      <td>345.0</td>
      <td>15.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>Subjects allied to medicine</th>
      <td>22135.0</td>
      <td>935.0</td>
      <td>1825.0</td>
      <td>620.0</td>
      <td>630.0</td>
    </tr>
    <tr>
      <th>Biological sciences</th>
      <td>15725.0</td>
      <td>1800.0</td>
      <td>6045.0</td>
      <td>1520.0</td>
      <td>1335.0</td>
    </tr>
    <tr>
      <th>Veterinary science</th>
      <td>550.0</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>5.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>Agriculture &amp; related subjects</th>
      <td>1265.0</td>
      <td>120.0</td>
      <td>195.0</td>
      <td>120.0</td>
      <td>145.0</td>
    </tr>
    <tr>
      <th>Physical sciences</th>
      <td>6510.0</td>
      <td>555.0</td>
      <td>3410.0</td>
      <td>920.0</td>
      <td>620.0</td>
    </tr>
    <tr>
      <th>Mathematical sciences</th>
      <td>2910.0</td>
      <td>360.0</td>
      <td>1230.0</td>
      <td>385.0</td>
      <td>265.0</td>
    </tr>
    <tr>
      <th>Computer science</th>
      <td>7220.0</td>
      <td>225.0</td>
      <td>810.0</td>
      <td>925.0</td>
      <td>310.0</td>
    </tr>
    <tr>
      <th>Engineering &amp; technology</th>
      <td>9420.0</td>
      <td>405.0</td>
      <td>1740.0</td>
      <td>1010.0</td>
      <td>580.0</td>
    </tr>
    <tr>
      <th>Architecture, building &amp; planning</th>
      <td>3345.0</td>
      <td>230.0</td>
      <td>380.0</td>
      <td>270.0</td>
      <td>170.0</td>
    </tr>
  </tbody>
</table>
</div>



## Making the subplots object

We're going to make a subplots object with four cells, one for each subject which we're going to compare. We'll also set the width and height to make the figure a square.

Finally, we'll add a dummy data item so we can see the plotting area and make sure that we have removed all the visible legend components.


```python
fig = make_subplots(rows = 2, cols = 2,
                   subplot_titles = ["Medicine & Dentistry",
                                   "Biological Sciences",
                                   "Computer Science",
                                   "Engineering & Technology"])

fig['layout'].update({'height' : 900, 'width' : 900})

fig['data'].append({'type' : 'scatter'})
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(8)%20-%20Relative%20sizing%20of%20pie%20charts/pyo.iplot-0.png)```

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
    
    





Let's now remove the axis components by looping through the items in the layout, and for each axis object, applying the hideAxis parameters that we created in the previous lesson.


```python
hideAxis = {'zeroline' : False,
            'showgrid' : False,
            'showticklabels' : False,
            'showline' : False}

for key, axis in fig['layout'].items():
    if 'axis' in key:
        axis.update(hideAxis)
        
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(8)%20-%20Relative%20sizing%20of%20pie%20charts/pyo.iplot-1.png)``





The final thing to do before we start putting the pie charts in the subplots object is to get the domains of the axes. We need to create a lookup between the subject area and the domain.

To do this, we need to order the list of subjects to match their order on the subplots object; "Medicine & Dentistry" first in the list, and "Engineering & technology" last:


```python
subjects = ['Medicine & dentistry','Biological sciences','Computer science','Engineering & technology']

for key, axis in fig['layout'].items():
    if 'axis' in key:
        print(key, axis['domain'])
```

    yaxis1 [0.625, 1.0]
    yaxis4 [0.0, 0.375]
    xaxis1 [0.0, 0.45]
    xaxis4 [0.55, 1.0]
    xaxis3 [0.0, 0.45]
    yaxis3 [0.0, 0.375]
    xaxis2 [0.55, 1.0]
    yaxis2 [0.625, 1.0]
    

Using the helpful plot grid format, we can now assign each x- and y-axis domain to a subject, and create a lookup dictionary between the subject and that domain:
````
This is the format of your plot grid:
[ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
[ (2,1) x3,y3 ]  [ (2,2) x4,y4 ]
````

Remember that lists and 0-indexed, but the axis objects start from 1!


```python
subjLookup = {}
for i, sub in enumerate(subjects):
    axisPos = i + 1
    subjLookup[sub] = {'x' : fig['layout']['xaxis{}'.format(axisPos)]['domain'],
                       'y' : fig['layout']['yaxis{}'.format(axisPos)]['domain']}
    
subjLookup
```




    {'Biological sciences': {'x': [0.55, 1.0], 'y': [0.625, 1.0]},
     'Computer science': {'x': [0.0, 0.45], 'y': [0.0, 0.375]},
     'Engineering & technology': {'x': [0.55, 1.0], 'y': [0.0, 0.375]},
     'Medicine & dentistry': {'x': [0.0, 0.45], 'y': [0.625, 1.0]}}



## Making the pie charts

Let's now select the data for each subject area of interest and make a pie trace for each one.

We'll use the lookup to set the domain for this pie trace, and then append that trace to the list of data items in the fig:


```python
for s in subjects:
    fig['data'].append({'type' : 'pie',
                       'labels' : outcomes.columns.tolist(),
                       'values' : outcomes.loc[s],
                      'domain' : subjLookup[s],
                       'direction' : 'clockwise',
                       'name' : s})
    
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(8)%20-%20Relative%20sizing%20of%20pie%20charts/pyo.iplot-2.png)`





So there's some overlap between the labels on the pie charts and the subplot titles. The easiest way of fixing this is to move the titles up, but before we do this, let's scale the pie charts relative to each other.

The total number of students in each subject area is different, so we expect the pie charts to be different sizes. This may fix our problem!

## Linking the pie charts together

It's super easy to link the pie charts together! All we have to do is set a value for the <code>'scalegroup'</code> parameter, much as we would for a <code>'legendgroup'</code>.

Let's delete the traces from our figure, and re-add them with a <code>'scalegroup'</code> of <code>'subjects'</code>. We'll also suppress the pie chart name from the hoverinfo, as this doesn't add any information.


```python
fig['data'] = []

for s in subjects:
    fig['data'].append({'type' : 'pie',
                       'labels' : outcomes.columns.tolist(),
                       'values' : outcomes.loc[s],
                      'domain' : subjLookup[s],
                       'direction' : 'clockwise',
                       'scalegroup' : 'subjects',
                       'name' : s,
                       'hoverinfo' : 'label+value+percent'})
    
pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(8)%20-%20Relative%20sizing%20of%20pie%20charts/pyo.iplot-3.png)





We've got this chart looking really good! Let's send it to the Plotly cloud:


```python
py.plot(fig, filename="Student outcomes by subject area", fileopt = "overwrite")
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(8)%20-%20Relative%20sizing%20of%20pie%20charts/py.plot-0.png)



    'https://plot.ly/~rmuir/273'



