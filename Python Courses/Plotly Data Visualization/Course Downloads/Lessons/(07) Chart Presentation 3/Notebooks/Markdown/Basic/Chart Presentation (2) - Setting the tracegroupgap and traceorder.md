
# Chart Presentation (2) - Setting the tracegroupgap and traceorder

In this lesson we're going to look at different ways of displaying the traces in the legend. In the final lesson of the previous section we saw how to set a <code>legendgroup</code> for our traces, and that we can increase the space between the different legend groups. In this lesson we're going to look at different values for tracegroupgap, and we're also going to find out how to change the order of the traces in the legend by changing the <code>traceorder</code> parameter.






 






## Applying a tracegroup to the data items

Let's get the chart we styled in the previous legend. We'll need to loop through the data items and set a <code>legendgroup</code> to each depending on if the trace is a bar or a scatter type. I've plotted the chart before the changes to <code>legendgroup</code> so you can compare them:


```python
stacked = py.get_figure("rmuir", 255)
pyo.iplot(stacked)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-0.png)
for d in stacked['data']:
    if d['type'] == 'bar':
        d.update({'legendgroup' : 'continent'})
    else:
        d.update({'legendgroup' : 'weight'})
```





Now, when we plot the chart after the changes, you can see that there is now some space between the bar traces and the line trace in the legend. The order of the traces has also changed.


```python
pyo.iplot(stacked)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-1.png)``





## Changing the <code>tracegroupgap</code>

In the last section we set <code>tracegroupgap</code> to a large number in order to move the traces near the correct part of our dashboard. Here we'll supply a much smaller number with the aim of distinguishing better between the traces:


```python
stacked['layout']['legend'].update({'tracegroupgap' : 20})
pyo.iplot(stacked)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-2.png)`





## Changing the <code>traceorder</code>

The <code>traceorder</code> parameter accepts any of the following inputs. These inputs can also be combined with a <code>'+'</code> symbol:

- <code>'reversed'</code> - reverses the order of the traces
- <code>'normal'</code> - puts the traces in the same order as the input data
- <code>'grouped'</code> - displays the items in groups if a <code>'legendgroup'</code> is provided

Let's see how these work in practise.

We can remove the grouping by setting <code>traceorder</code> to <code>'normal'</code>:


The <code>traceorder</code> parameter accepts any of the following inputs. These inputs can also be combined with a <code>'+'</code> symbol:

- <code>'reversed'</code> - reverses the order of the traces
- <code>'normal'</code> - puts the traces in the same order as the input data
- <code>'grouped'</code> - displays the items in groups if a <code>'legendgroup'</code> is providedstacked['layout']['legend'].update({'traceorder' : 'normal'})
pyo.iplot(stacked)

We
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-3.png) can reverse the order by setting <code>traceorder</code> to <code>'reversed'</code>:


```python
stacked['layout']['legend'].update({'traceorder' : 'reversed'})
pyo.iplot(stacked)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-4.png)




We can reinstate the tracegrouping by setting <code>traceorder</code> to <code>'grouped'</code>. Note that at the time of writing, one cannot set the traceorder to be <code>'reversed+grouped'</code> (well you can, but it doesn't work).


```python
stacked['layout']['legend'].update({'traceorder' : 'grouped'})
pyo.iplot(stacked)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/pyo.iplot-5.png)




```python
py.plot(stacked, filename="Meteorites by continent and weight (styled legend)", fileopt="overwrite")
```



![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(2)%20-%20Setting%20the%20tracegroupgap%20and%20traceorder/py.plot-0.png)

    'https://plot.ly/~rmuir/255'



