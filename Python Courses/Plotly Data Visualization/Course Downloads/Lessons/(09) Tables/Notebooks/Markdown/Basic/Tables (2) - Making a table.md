
# Tables (2) - Making a table

In this lesson we're going to learn how make a table in Plotly.

We'll learn how to make one from a list and a Pandas DataFrame.



#### New Modules:

In order to make a table in Plotly, we have to use a different library called the <code>'FigureFactory'</code>. This is an in-development part of the Plotly codebase and is liable to change without notice.

The <code>'FigureFactory'</code> gives options for creating many different types of chart . . . I suggest trying a few of them out if you're curious!



from plotly.tools import FigureFactory as FF



```python

 
```





## Making a table from a list

We can use the <code>FigureFactory.create_table()</code> function to create a table. This function actually uses the Heatmap chart type (which we won't cover in this course) to create a table, and we'll use different aspects of the Heatmap chart to make stylistic changes to our tables.

It's very simple to create a table from a list, provided that the list is in the correct format.

The list must be comprised of several sublists. Each sublist will be a row in the table, and the first sublist will be the column titles.

Let's try this out and create a table showing the population and area of the different countries in the United Kingdom. I sourced this data from <a href = "https://en.wikipedia.org/wiki/Population_of_the_countries_of_the_United_Kingdom">Wikipedia</a>.

Here's our table data with the row for the column headings and space for the data:


```python
tableData = [['Country','Population','Area (km2)'],
             [],
             [],
             [],
             []]
```

Here's the table data with the values completed:


```python
tableData = [['Country','Population','Area (km2)'],
             ['England',53865800, 130395],
             ['Scotland',5327700, 78772],
             ['Wales',3082400,20779],
             ['Northern Ireland', 1829700, 13843]]
```

We can now pass this into the <code>FF.create_table()</code> function and create an object to plot:


```python
UKCountries = FF.create_table(tableData)
pyo.iplot(UKCountries)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(2)%20-%20Making%20a%20table/pyo.iplot-0.png)```





You can see that Plotly follows many of the recommendations for designing clear tables. The header row is a different colour, the row colours alternate, and the font allows for comparisons between the numbers.

There are still improvements to make which we will look at later in this section.

#### The structure of a table object

Let's have a look at the structure of our table object.

You can see that the data displayed in the table is not contained within the data element of the figure. The data element actually contains the instructions for colouring the rows and header.

The data displayed in the table is stored as annotations which are positioned by the <code>FF.create_table()</code> function. We will use this knowledge later to allow us to style the data in the table.


```python
UKCountries
```




    {'data': [{'colorscale': [[0, '#00083e'], [0.5, '#ededee'], [1, '#ffffff']],
       'hoverinfo': 'none',
       'opacity': 0.75,
       'showscale': False,
       'type': 'heatmap',
       'z': [[0, 0, 0], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5], [1, 1, 1]]}],
     'layout': {'annotations': [{'align': 'left',
        'font': {'color': '#ffffff'},
        'showarrow': False,
        'text': '<b>Country</b>',
        'x': -0.45,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 0,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#ffffff'},
        'showarrow': False,
        'text': '<b>Population</b>',
        'x': 0.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 0,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#ffffff'},
        'showarrow': False,
        'text': '<b>Area (km2)</b>',
        'x': 1.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 0,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': 'England',
        'x': -0.45,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 1,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '53865800',
        'x': 0.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 1,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '130395',
        'x': 1.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 1,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': 'Scotland',
        'x': -0.45,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 2,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '5327700',
        'x': 0.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 2,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '78772',
        'x': 1.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 2,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': 'Wales',
        'x': -0.45,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 3,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '3082400',
        'x': 0.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 3,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '20779',
        'x': 1.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 3,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': 'Northern Ireland',
        'x': -0.45,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 4,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '1829700',
        'x': 0.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 4,
        'yref': 'y1'},
       {'align': 'left',
        'font': {'color': '#000000'},
        'showarrow': False,
        'text': '13843',
        'x': 1.55,
        'xanchor': 'left',
        'xref': 'x1',
        'y': 4,
        'yref': 'y1'}],
      'height': 200,
      'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0},
      'xaxis': {'dtick': 1,
       'gridwidth': 2,
       'showticklabels': False,
       'tick0': -0.5,
       'ticks': '',
       'zeroline': False},
      'yaxis': {'autorange': 'reversed',
       'dtick': 1,
       'gridwidth': 2,
       'showticklabels': False,
       'tick0': 0.5,
       'ticks': '',
       'zeroline': False}}}



## Making a table from a DataFrame

Let's get the same data that we used earlier, but rather than writing it out in a dictionary, we'll get it as a csv:


```python
df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Name</th>
      <th>Population (2015)</th>
      <th>Percent of UK (2015)</th>
      <th>Area (km2)</th>
      <th>Pop.density (2011, km2)</th>
      <th>Population (2011)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>England</td>
      <td>54786327</td>
      <td>84.1%</td>
      <td>130395</td>
      <td>40655</td>
      <td>53107169</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>Scotland</td>
      <td>5373000</td>
      <td>8.3%</td>
      <td>78772</td>
      <td>6722</td>
      <td>5299900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>Wales</td>
      <td>3099086</td>
      <td>4.8%</td>
      <td>20779</td>
      <td>14743</td>
      <td>3063758</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>Northern Ireland</td>
      <td>1851621</td>
      <td>2.8%</td>
      <td>13843</td>
      <td>13081</td>
      <td>1814318</td>
    </tr>
  </tbody>
</table>
</div>



We can now pass this DataFrame directly into the <code>create_table()</code> function:


```python
UKCountryInfo = FF.create_table(df)
pyo.iplot(UKCountryInfo)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(2)%20-%20Making%20a%20table/pyo.iplot-1.png)``





So you can see that the entire DataFrame gets translated into a Plotly table, but it looks a bit cramped. We could increase the size of the table to include all the information, but for now, let's reduce the number of columns. We'll take the column for 2011 because we'll use data from another source for 2011 in a later lesson in this section.


```python
df = df[['Name','Population (2011)', 'Area (km2)']]
UKCountryInfo = FF.create_table(df)
pyo.iplot(UKCountryInfo)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(2)%20-%20Making%20a%20table/pyo.iplot-2.png)`





