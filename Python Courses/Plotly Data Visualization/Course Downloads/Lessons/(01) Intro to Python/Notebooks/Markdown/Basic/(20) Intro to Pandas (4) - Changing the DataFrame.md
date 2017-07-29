
# Intro to Pandas (4) - Changing the DataFrame

In the last lesson we saw how to create new columns in a DataFrame.

In this lesson we'll learn how to change the DataFrame itself; how to rename and drop columns, as well as how to set the index.



## Making Changes to a DataFrame

First of all, I'm going to read some data into a DataFrame:



baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData.head()





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VALUE</th>
      <th>DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.5</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.5</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



We can rename columns in a DataFrame by using the <code>df.rename()</code> function. To this function, we must pass a dictionary where the key is the old column name, and the value is the new column name.

We can choose to rename the columns in the DataFrame <code>inplace</code> - this modifies the original object. Here I'm changing the column names to be lowercase:


```python
baseRateData.rename(columns = {'VALUE' : 'value', 'DATE' : 'date'}, inplace=True)

baseRateData.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.5</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.5</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



If you're creating a new object from the DataFrame, you don't need to do it rename the columns <code>inplace</code>:


```python
baseRateData_r = baseRateData.rename(columns = {'value' : 'Value', 'date' : 'Date'})

baseRateData_r.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.5</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.5</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



We can also change the index of the DataFrame, this is helpful to do when we want to merge a DataFrame, or to use the index to select locations.

Here I'm changing the index to be the Date column using the <code>df.set_index()</code> method. I'm doing this <code>inplace</code> because I don't want to create a new object.


```python
baseRateData_r.set_index(baseRateData_r['Date'], inplace=True)

baseRateData_r.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
      <th>Date</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>02/01/1975</th>
      <td>11.5</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>03/01/1975</th>
      <td>11.5</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>06/01/1975</th>
      <td>11.5</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>07/01/1975</th>
      <td>11.5</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>08/01/1975</th>
      <td>11.5</td>
      <td>08/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



We can also drop columns by using the <code>df.drop()</code> method. 

Because we have the information about the Date contained in the index I'm now going to drop the Date column to save memory. I have to tell Pandas to drop a column by using <code>axis = 1</code> (<code>axis = 0</code> tells Pandas to drop a row).

Once again I don't want to create a new object, so I'll drop this column <code>inplace</code>:


```python
baseRateData_r.drop(['Date'], axis = 1, inplace = True)

baseRateData_r.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Value</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>02/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>03/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>06/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>07/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>08/01/1975</th>
      <td>11.5</td>
    </tr>
  </tbody>
</table>
</div>



