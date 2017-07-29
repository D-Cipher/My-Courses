
# Tables (7) - Adding hovertext

At the start of this section we learnt that the <code>create_table()</code> function actually uses the Plotly heatmap to create a table. We also learnt that we can use some of the instructions for creating a heatmap to modify our table.

In this lesson we're going to learn how to add hovertext to a table by passing data through the <code>create_table()</code> function into the heatmap.

Adding hovertext to a table may seem a little redundant because the table itself is made of text, however we can consider the hovertext in this case as a kind of sophisticated annotation. In the section on bar charts we added an annotation which we though explained the large number of meteorites in a a particular year. In this lesson we'll add some hovertext that fills a similar role.





from plotly.tools import FigureFactory as FF



```python

 
```





## How does hovertext work on a heatmap/table?

We can add hovertext by amending the figure which is returned by the create_table function.

First, let's look at how hovertext is displayed on a table. Let's get our table object and tell it to display <code>'hoverinfo' : 'all'</code>:


```python
table = py.get_figure("rmuir", 309)
table['data'][0].update({'hoverinfo' : 'all'})
pyo.iplot(table)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(7)%20-%20Adding%20hovertext/pyo.iplot-0.png)```





This is quite unhelpful. The standard hoverinfo doesn't convey any interesting or helpful information.

In order to make the hoverinfo relevant, we have to include some text to display.

A heatmap expects the <code>'text'</code> parameter to be of the same shape as the <code>'z'</code> parameter, with each item in the text corresponding to an item in <code>'z'</code>.

Let's see what shape our text item must take:


```python
table['data'][0]['z']
```




    [[0, 0, 0, 0, 0, 0],
     [0, 0.5, 0.5, 0.5, 0.5, 0.5],
     [0, 1, 1, 1, 1, 1],
     [0, 0.5, 0.5, 0.5, 0.5, 0.5],
     [0, 1, 1, 1, 1, 1]]



We therefore have to add a specific text item to be displayed over each cell in the table. 

## Adding a text parameter

As a useful piece of contextual information, let's add the population of the capital city of each country.

This information will be attached to the third item in every row (but the first).

Let's add some holding text to make sure we have got the right place. We will pass in an empty string for the items for which we don't want text displayed, and tell Plotly to only display text on hover:


```python
text = [['','','','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],
       ['','','HOLDING','','',''],]

table['data'][0].update({'text' : text,
                        'hoverinfo' : 'text'})
pyo.iplot(table)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(7)%20-%20Adding%20hovertext/pyo.iplot-1.png)``





Now let's add the info:


```python
text = [['','','','','',''],
       ['','','<b>London</b><br>Population: 8,630,100','','',''],
       ['','','<b>Edinburgh</b><br>Population: 492,680','','',''],
       ['','','<b>Cardiff</b><br>Population: 346,100','','',''],
       ['','','<b>Belfast</b><br>Population: 333,870','','',''],]

table['data'][0].update({'text' : text})
pyo.iplot(table)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(7)%20-%20Adding%20hovertext/pyo.iplot-2.png)`





I'm really happy with how that's turned out! Let's push this to the Plotly cloud:


```python
py.plot(table, filename="Population of UK Countries (hoverinfo)", fileopt="overwrite")
```
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(7)%20-%20Adding%20hovertext/py.plot-0.png)




    'https://plot.ly/~rmuir/311'



