
# Chart Presentation (4) - Creating ticklabels

In the last lesson we saw how to use the <code>'tickprefix'</code> and <code>'ticksuffix'</code> parameters to modify the existing ticklabels. We also saw that we can gain some control over the number of ticks by specifying a value for <code>'nticks'</code>.

In this lesson we'll find out how to set the text and position of our own ticklabels using the <code>'tickmode'</code>, <code>'tickvals'</code> and <code>'ticktext'</code> parameters.






 






## Getting a chart to modify:

We'll import the MPs expense claims chart and set the tickvalues individually:


```python
expenses = py.get_figure('rmuir', 148)
pyo.iplot(expenses)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/pyo.iplot-0.png)```





## Setting the tickvalues

In order to set the tickvalues, we need to manipulate three different parameters within the axis object. First of all, we need to set <code>'tickmode'</code> to <code>'array'</code> to tell Plotly to expect a list of ticks.

Next, we need to set the <code>'tickvals'</code> to be a list of numbers where each tick will be displayed.

Finally, we specify the <code>'ticktext'</code> to place at each of the <code>'tickvals'</code>:
````python
layout = {'xaxis' : {'tickmode' :  'array',
                       'tickvals' : <list of values>,
                       'ticktext' : <list of values>}}
````

The values that we specify in <code>'tickvals'</code> must be contained within the data that relates to the axis. For example, we couldn't have <code>'tickvals' : [5, 10]</code> when the axis is categorical, for example <code>'x' : ['UK','USA']</code>.

Both lists of <code>'ticktext'</code> and <code>'tickvals'</code> must have the same length otherwise your text will not display properly.

Let's specify some practise tickvalues:


```python
expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [3, 6, 9], 'ticktext' : ['three',' six','nine']})
pyo.iplot(expenses)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/pyo.iplot-1.png)``





You can see how the <code>'ticktext'</code> and <code>'tickvals'</code> have been placed on the x-axis.


```python
expenses['layout']['xaxis'].update({'tickmode' : 'array', 
                                    'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['three',' six','nine']})
pyo.iplot(expenses)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/pyo.iplot-2.png)`





You can see that whilst we have specified 12 values for the position of the ticklabels, we have only specified 3 values for the <code>'ticktext'</code>. Plotly will use each value of <code>'ticktext'</code> once and then revert to using the <code>'tickvals'</code> when they have run out.


Let's specify the values to be something more relevant, the month names for example:


```python
expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']})
pyo.iplot(expenses)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/pyo.iplot-3.png)





Great, that seems to have worked. But we can acheive the same outcome by using a date format. Let's try something a little more complex.

We'll use the <code>'ticktext'</code> to add some contextual information to the tick labels. For example, the number of expense claims is so low in August because the MPs go on a summer recess. 

Let's encode this information into the <code>'ticktext'</code>:


```python
expenses['layout']['xaxis'].update({'tickmode' : 'array', 'tickvals' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                                    'ticktext' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug<br>(Summer Recess)','Sep','Oct','Nov','Dec']})
pyo.iplot(expenses)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/pyo.iplot-4.png)




Great, that helps to clarify one of the main trends in the chart. Let's push it back to the Plotly cloud:


```python
py.plot(expenses, filename="MP Expense claims by month 2010-2015", fileopt = "overwrite")
```


![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(4)%20-%20Creating%20ticklabels/py.plot-0.png)


    'https://plot.ly/~rmuir/148'



