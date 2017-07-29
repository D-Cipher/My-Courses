
# Chart Presentation (6) - Adding a source annotation

In this lesson we'll put into practise what we've learnt so far about creating and positioning annotations and increasing the margins of our charts to add a source annotation to some charts that we've previously created. 

Citing and referencing your sources is a vital part of producing any data visualisation as it's important for people to be able to replicate your work.






 






## Getting the charts

We're going to add source annotations to two charts that we've previously produced; the Gapminder plot, and the plot which shows Life Expectancy against cigarette prices.


```python
gapMinder = py.get_figure("rmuir", 225)
lifeExp = py.get_figure("rmuir", 223)
```

### Setting the source for the Gapminder plot

Let's add the source as an annotation to the Gapminder plot, remembering to set the <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code> to allow us to position this annotation outside of the plotting area.

I'm going to position this annotation at the bottom-right of the chart, in italics, and in a small, light grey font.


```python
gapMinder['layout'].update({'annotations' : [{'text' : "<i>Source: https://www.gapminder.org/data/</i>",
                                             'xref' : 'paper',
                                             'yref' : 'paper',
                                             'x' : 0,
                                             'y' : -0.4,
                                             'font' : {'size' : 12,
                                                      'color' : 'grey'},
                                              'xanchor' : 'left',
                                             'showarrow' : False}]})
pyo.iplot(gapMinder)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(6)%20-%20Adding%20a%20source%20annotation/pyo.iplot-0.png)```





## Changing the source for the Life Expectancy plot

I sourced the data for this plot from the WHO. Let's add this to the chart, keeping the same parameters for the annotation:


```python
lifeExp['layout'].update({'annotations' : [{'text' : "<i>Source: The World Health Organisation (WHO)</i>",
                                             'xref' : 'paper',
                                             'yref' : 'paper',
                                             'x' : 0,
                                             'y' : -0.4,
                                             'font' : {'size' : 12,
                                                      'color' : 'grey'},
                                              'xanchor' : 'left',
                                             'showarrow' : False}]})
pyo.iplot(lifeExp)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(6)%20-%20Adding%20a%20source%20annotation/pyo.iplot-1.png)``





Let's increase the height and bottom margin of the chart so we can see the source:


```python
lifeExp['layout'].update({'height' : 500,
                         'margin' : {'b' : 130}})
pyo.iplot(lifeExp)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(6)%20-%20Adding%20a%20source%20annotation/pyo.iplot-2.png)`





Great, these two plots are looking much better. Let's send them to the PLotly cloud:


```python
py.plot(gapMinder, filename="Life expectancy and GPD per capita", fileopt="overwrite")

py
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(6)%20-%20Adding%20a%20source%20annotation/py.plot-0.png).plot(lifeExp, filename="Life expectancy against cost of cigarettes (Male & Female regressions)", fileopt="overwrite")
```

![py.plot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20Presentation%20(6)%20-%20Adding%20a%20source%20annotation/py.plot-1.png)



    'https://plot.ly/~rmuir/223'



