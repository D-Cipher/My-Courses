
# Intro to Pandas (3) - Accessing and Creating Columns

In the last lesson we saw how to implement some useful functions and methods to help us describe a DataFrame. 

In this lesson we'll learn how to access data in a DataFrame. We'll also learn how to create new columns from existing columns and from a list. These skills are essential to be able to plot data with Plotly as we'll often want to plot the data in different ways - being able to do some basic data manipulation will be really helpful. 

The content in the next few lessons is by no means an exhaustive list of what you can do with Pandas, and we will introduce some more functionality as we progress with the course, but the material presented here is enough to get us started.



## Accessing columns in a DataFrame

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



We access the data held in each column in the same way that we would access a dictionary's values by the key. This is the most common aspect of a DataFrame which we'll use in this course. 


```python
baseRateData['VALUE']
```




    0        11.50
    1        11.50
    2        11.50
    3        11.50
    4        11.50
    5        11.50
    6        11.50
    7        11.50
    8        11.50
    9        11.50
    10       11.50
    11       11.50
    12       11.25
    13       11.25
    14       11.25
    15       11.25
    16       11.25
    17       11.00
    18       11.00
    19       11.00
    20       11.00
    21       11.00
    22       11.00
    23       11.00
    24       11.00
    25       11.00
    26       11.00
    27       10.75
    28       10.75
    29       10.75
             ...  
    10456     0.50
    10457     0.50
    10458     0.50
    10459     0.50
    10460     0.50
    10461     0.50
    10462     0.50
    10463     0.50
    10464     0.50
    10465     0.50
    10466     0.50
    10467     0.50
    10468     0.50
    10469     0.50
    10470     0.50
    10471     0.50
    10472     0.50
    10473     0.50
    10474     0.50
    10475     0.50
    10476     0.50
    10477     0.50
    10478     0.50
    10479     0.50
    10480     0.50
    10481     0.50
    10482     0.50
    10483     0.50
    10484     0.50
    10485     0.50
    Name: VALUE, dtype: float64



We can also access these values by using a <code> . </code>. Which option to use is not important, I prefer using the dictionary-like option because it's familiar to me, and the syntax highlighting makes it obvious that I'm accessing a column rather than a method.


```python
baseRateData.VALUE
```




    0        11.50
    1        11.50
    2        11.50
    3        11.50
    4        11.50
    5        11.50
    6        11.50
    7        11.50
    8        11.50
    9        11.50
    10       11.50
    11       11.50
    12       11.25
    13       11.25
    14       11.25
    15       11.25
    16       11.25
    17       11.00
    18       11.00
    19       11.00
    20       11.00
    21       11.00
    22       11.00
    23       11.00
    24       11.00
    25       11.00
    26       11.00
    27       10.75
    28       10.75
    29       10.75
             ...  
    10456     0.50
    10457     0.50
    10458     0.50
    10459     0.50
    10460     0.50
    10461     0.50
    10462     0.50
    10463     0.50
    10464     0.50
    10465     0.50
    10466     0.50
    10467     0.50
    10468     0.50
    10469     0.50
    10470     0.50
    10471     0.50
    10472     0.50
    10473     0.50
    10474     0.50
    10475     0.50
    10476     0.50
    10477     0.50
    10478     0.50
    10479     0.50
    10480     0.50
    10481     0.50
    10482     0.50
    10483     0.50
    10484     0.50
    10485     0.50
    Name: VALUE, dtype: float64



We can get the minimum, maximum and mean values for a particular column:


```python
baseRateData['VALUE'].max()
```




    17.0




```python
baseRateData['VALUE'].min()
```




    0.5




```python
baseRateData['VALUE'].mean()
```




    7.135084884608049



## Creating New Columns in a DataFrame

We can create new columns in a DataFrame in the same way that we create new keys and values in a Dictionary.

Here, I'm creating a new column which stores the base rate data as a proportion rather than a percentage:


```python
baseRateData['VALUE_PROP'] = baseRateData['VALUE'] / 100

baseRateData.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VALUE</th>
      <th>DATE</th>
      <th>VALUE_PROP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.5</td>
      <td>02/01/1975</td>
      <td>0.115</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.5</td>
      <td>03/01/1975</td>
      <td>0.115</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>06/01/1975</td>
      <td>0.115</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>07/01/1975</td>
      <td>0.115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
      <td>0.115</td>
    </tr>
  </tbody>
</table>
</div>



We can also create a new column from a list. 

Imagine that we wanted to set the colour of the data point depending on the value of the base rate, for example if the base rate drops below 5, we could colour this green, otherwise it would be coloured red.

In the cell below, I'm looping through each value in the VALUE column, and appending a new item to the list <code>colours</code> depending on the value of VALUE:


```python
colours = []

for row in baseRateData['VALUE']:
    if row < 5:
        colours.append('Green')
    else:
        colours.append('Red')
```

I can now create a new column directly from the list:


```python
baseRateData['COLOUR'] = colours
```

Let's check that this has worked by looking at the top and bottom five rows:


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
      <th>VALUE_PROP</th>
      <th>COLOUR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.5</td>
      <td>02/01/1975</td>
      <td>0.115</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.5</td>
      <td>03/01/1975</td>
      <td>0.115</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>06/01/1975</td>
      <td>0.115</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.5</td>
      <td>07/01/1975</td>
      <td>0.115</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.5</td>
      <td>08/01/1975</td>
      <td>0.115</td>
      <td>Red</td>
    </tr>
  </tbody>
</table>
</div>




```python
baseRateData.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VALUE</th>
      <th>DATE</th>
      <th>VALUE_PROP</th>
      <th>COLOUR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10481</th>
      <td>0.5</td>
      <td>17/06/2016</td>
      <td>0.005</td>
      <td>Green</td>
    </tr>
    <tr>
      <th>10482</th>
      <td>0.5</td>
      <td>20/06/2016</td>
      <td>0.005</td>
      <td>Green</td>
    </tr>
    <tr>
      <th>10483</th>
      <td>0.5</td>
      <td>21/06/2016</td>
      <td>0.005</td>
      <td>Green</td>
    </tr>
    <tr>
      <th>10484</th>
      <td>0.5</td>
      <td>22/06/2016</td>
      <td>0.005</td>
      <td>Green</td>
    </tr>
    <tr>
      <th>10485</th>
      <td>0.5</td>
      <td>23/06/2016</td>
      <td>0.005</td>
      <td>Green</td>
    </tr>
  </tbody>
</table>
</div>



