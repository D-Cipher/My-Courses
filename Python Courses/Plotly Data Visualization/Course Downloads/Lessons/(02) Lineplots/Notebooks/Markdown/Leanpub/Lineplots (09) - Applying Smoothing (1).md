
# Lineplots (9) - Applying Smoothing (1)

In this lesson I'm going to show you how we can change how the line for the lineplot is displayed. We'll investigate how to use Plotly's builtin <code>smoothing</code> option to allow us to smooth out some of the fluctuation in the line. 






 






## Smoothing a line

Before you apply smoothing to a line chart, you should consider very carefully why you are doing it, and what information you may lose by doing so. Essentially, when you smooth a line plot you are plotting data that doesn't exactly exist. For example, when you have a few points on a plot, a smoothed line will follow a different path to a straight line connecting these points. You can see this in the example below.

To smooth a line, we need to set the <code>'shape'</code> option to <code>'spline'</code> and pass a float value between 0 and 1.3 to the <code>'smoothing'</code> option. Both of these options are inside the <code>'line'</code> dictionary. Smoothing only works on scatterplots.
````python
trace = {'type' : 'scatter',
         'line' : {'smoothing' : <float between 0 and 1.3>,
                  'shape' : 'spline'}}
````

### Too much smoothing?

Here we have the same data plotted on two different traces. One trace has been smoothed to the maximum value in Plotly and the other has not. 

It's important to know that setting a value for smoothing only works when <code>'shape'</code> is set to <code>'spline'</code> (there are other options for <code>'shape'</code> that we'll explore in later lessons).

I haven't bothered setting the layout options for this chart as it's simply to demonstrate a point.


```python
xVals = [1,2,3,4,5,6,7,8,9,10]
yVals = [11,15,8,21,14,28,19,10,5,20]

unSmoothTrace = {'type' : 'scatter',
               'x' : xVals,
               'y' : yVals,
              'mode' : 'lines',
               'line' : {'smoothing' : 0,
                        'shape' : 'spline'},
                'name' : 'UnSmooth'}

smoothTrace = {'type' : 'scatter',
               'x' : xVals,
               'y' : yVals,
              'mode' : 'lines',
               'line' : {'smoothing' : 1.3,
                        'shape' : 'spline'},
              'name' : 'Smooth'}

data = Data([unSmoothTrace, smoothTrace])

pyo.iplot(data)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(09)%20-%20Applying%20Smoothing%20(1)/pyo.iplot-0.png)```





You can see how the smoothed line meets the unsmoothed line at the right points, but by showing a curve connecting the points, more accuracy is attributed to the data than is actually present in it.

Here is a slightly smaller value for <code>smoothing</code>:


```python
updateSmoothTrace = {'smoothing' : 0.8}

smoothTrace['line'].update(updateSmoothTrace)

data = Data([unSmoothTrace, smoothTrace])

fig = Figure(data = data)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(09)%20-%20Applying%20Smoothing%20(1)/pyo.iplot-1.png)``





The slightly less smoothed line even more closely follows the unsmoothed line. 

Here's an even smaller value for <code>smoothing</code>


```python
updateSmoothTrace = {'smoothing' : 0.3}

smoothTrace['line'].update(updateSmoothTrace)

data = Data([unSmoothTrace, smoothTrace])

fig = Figure(data = data)
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(09)%20-%20Applying%20Smoothing%20(1)/pyo.iplot-2.png)`





The smoothed line is now almost identical to the unsmoothed line.

## Smoothing data - what have we learnt?

So, we've seen that smoothing data can be misleading, but that this is especially so when they are few data points and the value for smoothing is high. We've seen that in order to smooth a line chart we need to set the <code>'shape'</code> to <code>'spline'</code> and give a value to the <code>'smoothing'</code> option.

In the next lesson we'll look at how smoothing affects real data. We'll get the stock prices for Apple for a few years and investigate what happens when we change the smoothing value. We'll also find out how to apply a 3rd party smoothing function to the data.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>