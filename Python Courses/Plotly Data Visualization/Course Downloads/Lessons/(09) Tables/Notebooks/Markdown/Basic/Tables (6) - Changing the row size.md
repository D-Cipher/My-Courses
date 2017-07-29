
# Tables (6) - Changing the row size

We saw at the start of this section how important it is to add space to our table. Adding space can stop our readers from becoming overwhelmed by the amount of data and aids in their understanding of the table, but adding too much can make the table difficult to read as the rows and columns seem unconnected.

We've previously seen how to change the amount of horizontal spacing by adding and removing columns. Here we'll learn how to change the amount of vertical space.



#### New Modules:

FigureFactory:



from plotly.tools import FigureFactory as FF



```python

 
```





## Increasing the amount of vertical space

Because we have to specify the amount of vertical spacing when we create the table, we have to remake the table from the previous lesson:


```python
df = pd.read_csv('http://richard-muir.com/data/public/csv/UKCountryPopulation.csv', index_col = 0)
df = df[['Name','Population (2011)', 'Area (km2)']]
df.set_index('Name', drop = True, inplace = True)
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



When we make the table we can change the <code>height_constant</code> from its default value of 30 to increase or decrease the amount of space in the table.

Reducing it to 10 gives us a very compact table:


```python
pyo.iplot(FF.create_table(df, index=True, index_title='Country',height_constant = 10))

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(6)%20-%20Changing%20the%20row%20size/pyo.iplot-0.png)```





Whilst increasing it to 50 gives us a more spacious table:


```python
pyo.iplot(FF.create_table(df, index=True, index_title='Country',height_constant = 50))
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(6)%20-%20Changing%20the%20row%20size/pyo.iplot-1.png)``





It's best for you to decide on the right amount of spacing for your table and tailor that to each specific use case.

