
# Pie charts (9) - Donut charts

In this lesson we're going to learn how to make a special kind of pie chart called a donut chart.

A donut chart is like a pie chart, except the centre of the pie has been removed to leave a space, causing it to look like a donut.

There is a lot of controversy over whether or not we should use donut charts; many people believe they are even harder to understand than a pie chart because you can't see where the segments meet in the middle. Regardless, I believe that it's better to know how to create something and then have the option not to, rather than not knowing. 

I've also seen some donut charts which I though were particularly effective, especially from a design point of view.

Donut charts can be used when the information that we need to convey is very simple and the differences between the categories are stark. They can be used when seeing the general trend in the data is more important than knowing the exact figures.

Donut charts are most useful when you need to display contextual information about your data, and that contextual information must be inextricably linked to that bit of data - by using a donut chart, you can put the information in the hole. You don't need to link it to a single chart with a line, a figure reference or a footnote; the contextual info becomes part of the data.






 






## Getting the data

We're going to use the same data as in the previous lesson. In this lesson we'll make a single donut chart and learn how to change the size of the hole. We'll also practise placing text effectively within the hole.


```python
outcomes = pd.read_csv("http://richard-muir.com/data/public/csv/StudentOutcomes201415BySubjectArea.csv", index_col = 0)
outcomes
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
    <tr>
      <th>Total - Science subject areas</th>
      <td>75930.0</td>
      <td>4770.0</td>
      <td>15995.0</td>
      <td>5780.0</td>
      <td>4110.0</td>
    </tr>
    <tr>
      <th>Social studies</th>
      <td>14925.0</td>
      <td>1355.0</td>
      <td>3795.0</td>
      <td>1465.0</td>
      <td>1380.0</td>
    </tr>
    <tr>
      <th>Law</th>
      <td>4470.0</td>
      <td>995.0</td>
      <td>2870.0</td>
      <td>485.0</td>
      <td>425.0</td>
    </tr>
    <tr>
      <th>Business &amp; administrative studies</th>
      <td>20150.0</td>
      <td>1500.0</td>
      <td>2295.0</td>
      <td>1790.0</td>
      <td>1375.0</td>
    </tr>
    <tr>
      <th>Mass communications &amp; documentation</th>
      <td>5210.0</td>
      <td>165.0</td>
      <td>455.0</td>
      <td>520.0</td>
      <td>355.0</td>
    </tr>
    <tr>
      <th>Languages</th>
      <td>9340.0</td>
      <td>940.0</td>
      <td>3165.0</td>
      <td>975.0</td>
      <td>870.0</td>
    </tr>
    <tr>
      <th>Historical &amp; philosophical studies</th>
      <td>6140.0</td>
      <td>715.0</td>
      <td>2640.0</td>
      <td>705.0</td>
      <td>635.0</td>
    </tr>
    <tr>
      <th>Creative arts &amp; design</th>
      <td>19925.0</td>
      <td>920.0</td>
      <td>2170.0</td>
      <td>1865.0</td>
      <td>1290.0</td>
    </tr>
    <tr>
      <th>Education</th>
      <td>9590.0</td>
      <td>370.0</td>
      <td>1485.0</td>
      <td>285.0</td>
      <td>400.0</td>
    </tr>
    <tr>
      <th>Combined</th>
      <td>245.0</td>
      <td>40.0</td>
      <td>80.0</td>
      <td>25.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>165930.0</td>
      <td>11765.0</td>
      <td>34950.0</td>
      <td>13900.0</td>
      <td>10875.0</td>
    </tr>
  </tbody>
</table>
</div>



## Making a pie chart
We'll take the data for a single subject and make a pie chart:


```python
fig = {'data' : [{'type' : 'pie',
          'labels' : outcomes.columns.tolist(),
          'values' : outcomes.loc['Medicine & dentistry'],
          'name' : 'Medicine & dentistry',
          'direction' : 'clockwise'}],
       'layout' : {'title' : 'Outcomes for medicine and dentistry students'}}

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-0.png)```





## Turning a pie chart into a donut chart

To make a donut chart, we simply set a value between 0 and 1 for the <code>'hole'</code> parameter. The default is 0. Let's try a large value:


```python
fig['data'][0].update({'hole' : 0.9})
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-1.png)``





That's not particularly clear. Let's use a slightly smaller value:


```python
fig['data'][0].update({'hole' : 0.5})
pyo.iplot(fig)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-2.png)`





## Providing contextual info with an annotation

As I mentioned in the introduction, donut charts are most useful when you need to link some contextual info to your data. Let's add some information about Medicine and Dentistry students in the form of an annotation and place it in the hole.

Adding an annotation in this way requires some trial and error; you will certainly need to play with the text size, the line breaks, the wording and the size of the donut hole in order for the information to fit and to look good.

Let's have a go!

We need to set the <code>'xref'</code> and <code>'yref'</code> to <code>'paper'</code> because there is no idea of x- and y-coordinates on a pie chart.

Let's start by positioning the annotation dead centre:


```python
info = "Medicine & Dentistry students are more likely to be employed than students from any other subject area"

fig['layout'].update({'annotations' : [{'text' : info,
                                       'xref' : 'paper',
                                       'yref' : 'paper',
                                       'x' : 0.5,
                                       'y' : 0.5,
                                       'showarrow' : False}]})

pyo.iplot(fig)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-3.png)





Let's add some line breaks into the text, and make the font slightly bigger and bold.

It's worth saying that it took me a while to get the line breaks right here! When you're making your own chart, don't be put off if it takes a few minutes!


```python
info = "<b>Medicine &<br>Dentistry students<br>are more likely to<br>be employed than<br>students from any<br>other subject<br>area</b>"

fig['layout'].update({'annotations' : [{'text' : info,
                                       'xref' : 'paper',
                                       'yref' : 'paper',
                                       'x' : 0.5,
                                       'y' : 0.5,
                                       'showarrow' : False,
                                       'font' : {'size' : 16}}]})

pyo.iplot(fig)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-4.png)




Finally, let's increase the size of the hole to accomodate the text:


```python
fig['data'][0].update({'hole' : 0.55})
pyo.iplot(fig)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/pyo.iplot-5.png)



I'm happy with this! Let's send it to the Plotly cloud:


```python
py.plot(fig, filename="Outcomes for Medicine & Dentistry students (donut chart)", fileopt = "overwrite")
```



![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Pie%20charts%20(9)%20-%20Donut%20charts/py.plot-0.png)

    'https://plot.ly/~rmuir/275'



