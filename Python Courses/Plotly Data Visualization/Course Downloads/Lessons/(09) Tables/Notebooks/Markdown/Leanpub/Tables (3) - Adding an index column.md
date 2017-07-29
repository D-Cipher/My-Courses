
# Tables (3) - Adding an index column

In this lesson we're going to learn how to add an index column to the left of our table. Using an index column can help people to find data more easily in the table.

Which column to include as an index column is a matter of preference, but it's a good idea to set the index column so that the data contained in that row describes the item named in the column.

For example, in a table of countries by population, you would probably choose the Country as the index column, rather than the population. Likewise, in a table displaying stock prices, you might put the date or the company as the index column, rather than the closing price.



#### New Modules:

Let's import the FigureFactory again:



from plotly.tools import FigureFactory as FF



```python

 
```





## Setting an index column

Throughout this course we have generally used DataFrames to store the data for our charts. A Pandas DataFrame already has an index and we can leverage this property to create an index in a Plotly table.

In order to set the index column in a DataFrame as the index column in a Plotly table, we specify <code>index = True</code> when calling the <code>create_table()</code> function.

Let's get some data and try this out. This is the same data we used in the previous lesson:


```python
df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)

df = df[['Name','Population (2011)', 'Area (km2)']]
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Population (2011)</th>
      <th>Area (km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>England</td>
      <td>53107169</td>
      <td>130395</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Scotland</td>
      <td>5299900</td>
      <td>78772</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wales</td>
      <td>3063758</td>
      <td>20779</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Northern Ireland</td>
      <td>1814318</td>
      <td>13843</td>
    </tr>
  </tbody>
</table>
</div>



Let's now plot this with <code>index = True</code> and see what the index column looks like:


```python
UKCountryInfo = FF.create_table(df, index='True')
pyo.iplot(UKCountryInfo)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/pyo.iplot-0.png)```





So we definitely have an index column; it's the same colour as the column titles, but this index column doesn't really add much to the table. Let's try changing the index column in the Pandas DataFrame.

We'll use the <code>DataFrame.set_index()</code> function to do this. We need to tell this function which column to use as the index. We also want to drop that column from the table, and do all of this in place:


```python
df.set_index('Name', drop=True, inplace = True)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population (2011)</th>
      <th>Area (km2)</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>England</th>
      <td>53107169</td>
      <td>130395</td>
    </tr>
    <tr>
      <th>Scotland</th>
      <td>5299900</td>
      <td>78772</td>
    </tr>
    <tr>
      <th>Wales</th>
      <td>3063758</td>
      <td>20779</td>
    </tr>
    <tr>
      <th>Northern Ireland</th>
      <td>1814318</td>
      <td>13843</td>
    </tr>
  </tbody>
</table>
</div>



Let's try creating a Plotly table from this DataFrame:


```python
UKCountryInfo = FF.create_table(df, index=True)
pyo.iplot(UKCountryInfo)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/pyo.iplot-1.png)``





## Adding a title to the index column

We can also specify a title for the index column by specifying an <code>index_title = ''</code> in the function call. A title on the index is not necessary in every table (certainly not in this example), but is definitely useful to know:


```python
UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
pyo.iplot(UKCountryInfo)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/pyo.iplot-2.png)`





Explain option 2

## Changing the size of the index column

You might notice that, especially in a table with as few columns as this one, the index column dominates the table somewhat. Whilst we have no direct way of setting the width of the columns, we can trick Plotly into reducing the width of all of this columns together by passing in some empty columns.

Let's add in three empty columns to our DataFrame; one between the index and the Population column, and another between Population and Area, and a final one after Area.

We'll set the column names to be spaces; 1 space, 2 spaces and 3 spaces respectively to ensure that all the columns have different names. The data held in each column will be an empty string:


```python
df[" "] = ""
df["  "] = ""
df["   "] = ""
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Population (2011)</th>
      <th>Area (km2)</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>England</th>
      <td>53107169</td>
      <td>130395</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Scotland</th>
      <td>5299900</td>
      <td>78772</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Wales</th>
      <td>3063758</td>
      <td>20779</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Northern Ireland</th>
      <td>1814318</td>
      <td>13843</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



Let's now reorder the columns:


```python
df = df[[' ', 'Population (2011)', '  ', 'Area (km2)', '   ']]
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Population (2011)</th>
      <th></th>
      <th>Area (km2)</th>
      <th></th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>England</th>
      <td></td>
      <td>53107169</td>
      <td></td>
      <td>130395</td>
      <td></td>
    </tr>
    <tr>
      <th>Scotland</th>
      <td></td>
      <td>5299900</td>
      <td></td>
      <td>78772</td>
      <td></td>
    </tr>
    <tr>
      <th>Wales</th>
      <td></td>
      <td>3063758</td>
      <td></td>
      <td>20779</td>
      <td></td>
    </tr>
    <tr>
      <th>Northern Ireland</th>
      <td></td>
      <td>1814318</td>
      <td></td>
      <td>13843</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



And plot our new table:


```python
UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
pyo.iplot(UKCountryInfo)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/pyo.iplot-3.png)





And sent it to the Plotly cloud:


```python
py.plot(UKCountryInfo, filename='UK Country Population Info', fileopt = 'Overwrite')
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/py.plot-0.png)



    'https://plot.ly/~rmuir/331'



## Changing the size of the columns by changing the size of the table

As well as adding more columns to the table in order to spread out the existing columns and reduce the size of the index, we can also change the width of the table itself.

Adding new columns is useful when the table must fill a particular space, however if the table is standalone, or does not have to fill a particular width, we can reduce the width to reduce the size of all the columns.


```python
df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df = df[['Name','Population (2011)', 'Area (km2)']]
df.set_index('Name', drop=True, inplace = True)

UKCountryInfo = FF.create_table(df, index=True, index_title='Country')
UKCountryInfo['layout'].update({'width' : 500})
pyo.iplot(UKCountryInfo)
```


![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/pyo.iplot-4.png)




```python
py.plot(UKCountryInfo, filename='UK Country Population Info (Small)', fileopt = 'Overwrite')
```



![py.plot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(3)%20-%20Adding%20an%20index%20column/py.plot-1.png)

    'https://plot.ly/~rmuir/333'



