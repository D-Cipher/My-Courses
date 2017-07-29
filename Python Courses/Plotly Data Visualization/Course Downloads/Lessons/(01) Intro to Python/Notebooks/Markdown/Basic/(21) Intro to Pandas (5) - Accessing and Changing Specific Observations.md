
# Intro to Pandas (5) - Accessing and Changing Specific Observations

In the last lesson we saw how to rename and drop columns, and to set the index in a DataFrame.

In this lesson we'll learn about positional and label-based selection and how to use this to make changes to specific observations.



## Positional and Label-based Selection

First of all, I'm going to read some data into a DataFrame. I also need to make another DataFrame which has a label-based index rather than a positional index.



baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData_r = baseRateData.rename(columns = {'VALUE' : 'Value', 'DATE' : 'Date'})
baseRateData_r.set_index(baseRateData_r['Date'], inplace=True)
baseRateData_r.drop(['Date'], axis = 1, inplace = True)


Let's have a look at these DataFrames:


```python
baseRateData.head()
```




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




```python
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



#### Selecting observations in a DataFrame

We can select observations from a DataFrame by using <code>df.loc</code> and <code>df.iloc</code>.

- <code>df.loc</code> selects the observations by their index label
- <code>df.iloc</code> selects the observations by their position

Here, I'm using <code>df.loc</code> to select the first 10 rows from <code>baseRateData</code>. Note that <code>df.loc</code> doesn't work like a list slice in Python; rather than stopping before the specified number, we include that observation:


```python
baseRateData.loc[:9]
```




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
    <tr>
      <th>5</th>
      <td>11.5</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11.5</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11.5</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11.5</td>
      <td>14/01/1975</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11.5</td>
      <td>15/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



If I try to use <code>df.loc</code> on <code>baseRateData_r</code>, this won't work because we have changed the index label:


```python
baseRateData_r.loc[:9]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-3206989f6fbb> in <module>()
    ----> 1 baseRateData_r.loc[:9]
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       1310             return self._getitem_tuple(key)
       1311         else:
    -> 1312             return self._getitem_axis(key, axis=0)
       1313 
       1314     def _getitem_axis(self, key, axis=0):
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\core\indexing.py in _getitem_axis(self, key, axis)
       1451         if isinstance(key, slice):
       1452             self._has_valid_type(key, axis)
    -> 1453             return self._get_slice_axis(key, axis=axis)
       1454         elif is_bool_indexer(key):
       1455             return self._getbool_axis(key, axis=axis)
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\core\indexing.py in _get_slice_axis(self, slice_obj, axis)
       1332         labels = obj._get_axis(axis)
       1333         indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop,
    -> 1334                                        slice_obj.step, kind=self.name)
       1335 
       1336         if isinstance(indexer, slice):
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\indexes\base.py in slice_indexer(self, start, end, step, kind)
       2995         """
       2996         start_slice, end_slice = self.slice_locs(start, end, step=step,
    -> 2997                                                  kind=kind)
       2998 
       2999         # return a slice
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\indexes\base.py in slice_locs(self, start, end, step, kind)
       3180         end_slice = None
       3181         if end is not None:
    -> 3182             end_slice = self.get_slice_bound(end, 'right', kind)
       3183         if end_slice is None:
       3184             end_slice = len(self)
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\indexes\base.py in get_slice_bound(self, label, side, kind)
       3113         # For datetime indices label may be a string that has to be converted
       3114         # to datetime boundary according to its resolution.
    -> 3115         label = self._maybe_cast_slice_bound(label, side, kind)
       3116 
       3117         # we need to look up the label
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\indexes\base.py in _maybe_cast_slice_bound(self, label, side, kind)
       3071         # this is rejected (generally .loc gets you here)
       3072         elif is_integer(label):
    -> 3073             self._invalid_indexer('slice', label)
       3074 
       3075         return label
    

    C:\Users\Rytch\Anaconda3\lib\site-packages\pandas\indexes\base.py in _invalid_indexer(self, form, key)
       1282                         "indexers [{key}] of {kind}".format(
       1283                             form=form, klass=type(self), key=key,
    -> 1284                             kind=type(key)))
       1285 
       1286     def get_duplicates(self):
    

    TypeError: cannot do slice indexing on <class 'pandas.indexes.base.Index'> with these indexers [9] of <class 'int'>


Instead I have to pass the row index label which I want:


```python
baseRateData_r.loc[:'15/01/1975']
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
    <tr>
      <th>09/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>10/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>13/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>14/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>15/01/1975</th>
      <td>11.5</td>
    </tr>
  </tbody>
</table>
</div>



But <code>df.iloc</code> works the same on both DataFrames because in <code>baseRateData</code>, the index is equal to the position - <code>df.iloc</code> works on the ordinal position of the rows.

Confusingly, <code>df.iloc</code> works in the same way as list and string slicing, stopping just before the specified position:


```python
baseRateData.iloc[:9]
```




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
    <tr>
      <th>5</th>
      <td>11.5</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11.5</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11.5</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11.5</td>
      <td>14/01/1975</td>
    </tr>
  </tbody>
</table>
</div>




```python
baseRateData_r.iloc[:9]
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
    <tr>
      <th>09/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>10/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>13/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>14/01/1975</th>
      <td>11.5</td>
    </tr>
  </tbody>
</table>
</div>



For both <code>df.loc</code> and <code>df.iloc</code>, we can take a slice from the middle of the DataFrame:


```python
baseRateData_r.loc['06/01/1975':'13/01/1975']
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
    <tr>
      <th>09/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>10/01/1975</th>
      <td>11.5</td>
    </tr>
    <tr>
      <th>13/01/1975</th>
      <td>11.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
baseRateData.iloc[4:6]
```




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
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.5</td>
      <td>09/01/1975</td>
    </tr>
  </tbody>
</table>
</div>



We can also combine the column names with <code>df.loc</code> and <code>df.iloc</code> to get 2D slices of a DataFrame.

Remember that <code>df.loc</code> works on the labels:


```python
baseRateData.loc[5:13, 'DATE']
```




    5     09/01/1975
    6     10/01/1975
    7     13/01/1975
    8     14/01/1975
    9     15/01/1975
    10    16/01/1975
    11    17/01/1975
    12    20/01/1975
    13    21/01/1975
    Name: DATE, dtype: object



But <code>df.iloc</code> operates on the index; the columns are numerically indexed (in the same way as the rows):


```python
baseRateData.iloc[5:13, 0]
```




    5     11.50
    6     11.50
    7     11.50
    8     11.50
    9     11.50
    10    11.50
    11    11.50
    12    11.25
    Name: VALUE, dtype: float64



### Changing Data in a DataFrame

So now we can select individual rows and columns in a DataFrame by the index label or position. We can use this knowledge to make changes to specific observations within the DataFrame.

Imagine that we were told that the first twenty rows of our data were incorrect; they should have been 1.15 instead of 11.5. Let's make some changes!

First of all, I'm using <code>df.loc</code> to select the first 20 rows by label and only the 'VALUE' column. It's just a simple matter of setting the value which we want these observations to take:


```python
baseRateData.loc[:19, 'VALUE'] = 1.15

baseRateData.head(25)
```




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
      <td>1.15</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.15</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.15</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.15</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.15</td>
      <td>08/01/1975</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.15</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.15</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.15</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.15</td>
      <td>14/01/1975</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.15</td>
      <td>15/01/1975</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.15</td>
      <td>16/01/1975</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.15</td>
      <td>17/01/1975</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.15</td>
      <td>20/01/1975</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.15</td>
      <td>21/01/1975</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.15</td>
      <td>22/01/1975</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1.15</td>
      <td>23/01/1975</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1.15</td>
      <td>24/01/1975</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.15</td>
      <td>27/01/1975</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.15</td>
      <td>28/01/1975</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.15</td>
      <td>29/01/1975</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11.00</td>
      <td>30/01/1975</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11.00</td>
      <td>31/01/1975</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11.00</td>
      <td>03/02/1975</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11.00</td>
      <td>04/02/1975</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11.00</td>
      <td>05/02/1975</td>
    </tr>
  </tbody>
</table>
</div>



We can also do it with <code>df.iloc</code>. Remember that the slicing is slightly different...

I'll change it instead to 2.15 so we can prove it works:


```python
baseRateData.iloc[:20, 0] = 2.15

baseRateData.head(25)
```




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
      <td>2.15</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.15</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.15</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.15</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.15</td>
      <td>08/01/1975</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.15</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.15</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.15</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.15</td>
      <td>14/01/1975</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.15</td>
      <td>15/01/1975</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2.15</td>
      <td>16/01/1975</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2.15</td>
      <td>17/01/1975</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2.15</td>
      <td>20/01/1975</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2.15</td>
      <td>21/01/1975</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2.15</td>
      <td>22/01/1975</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2.15</td>
      <td>23/01/1975</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2.15</td>
      <td>24/01/1975</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2.15</td>
      <td>27/01/1975</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2.15</td>
      <td>28/01/1975</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2.15</td>
      <td>29/01/1975</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11.00</td>
      <td>30/01/1975</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11.00</td>
      <td>31/01/1975</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11.00</td>
      <td>03/02/1975</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11.00</td>
      <td>04/02/1975</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11.00</td>
      <td>05/02/1975</td>
    </tr>
  </tbody>
</table>
</div>



