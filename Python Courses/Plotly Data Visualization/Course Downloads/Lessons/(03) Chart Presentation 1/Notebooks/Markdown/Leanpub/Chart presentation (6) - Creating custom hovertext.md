
# Chart presentation (6) - Creating custom hovertext

In the last lesson we found out how to control what, how and where the hover information is displayed on a chart.

In this lesson we'll learn how to create a custom text field in a Pandas DataFrame using the <code>apply()</code> and <code>lambda</code> functions. We'll also learn how to style this custom field using some HTML tags.

Setting custom hovertext gives you very fine control over how the contextual information in your chart is displayed. Doing this correctly will really make your charts stand out.

This lesson has a strong focus on manipulating data in a Pandas DataFrame. We'll learn several different data manipulation techniques, but if you get stuck or don't understand something, you can ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>.






 






### Getting the data

We'll load the house price and ranks dataset from my website. This contains the average house price data for each region on the first day of each year from 1995 - 2016, as well as the rank of each region (1 being the most expensive).

We're going to create a text column for each Region which will contain the hovertext that will be displayed on the chart. This text field will contain the Region's name in bold, then on the next line, the average price for that year (formatted as £), and on the final line, the region's rank of house price in italics.


```python
housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/RegionalHousePricesAndRanksJan16.csv")
housePrices.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>South West_rank</th>
      <th>South East_rank</th>
      <th>London_rank</th>
      <th>East of England_rank</th>
      <th>West Midlands_rank</th>
      <th>East Midlands_rank</th>
      <th>Yorkshire and The Humber_rank</th>
      <th>North West_rank</th>
      <th>North East_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.15790</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.59610</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1996-01-01</td>
      <td>53373.21941</td>
      <td>64057.17813</td>
      <td>75341.92348</td>
      <td>55033.23782</td>
      <td>44886.62926</td>
      <td>44618.55057</td>
      <td>43460.63343</td>
      <td>42599.17133</td>
      <td>40789.94219</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997-01-01</td>
      <td>57751.25499</td>
      <td>69007.75473</td>
      <td>83065.73641</td>
      <td>59081.19696</td>
      <td>47535.66472</td>
      <td>46775.09426</td>
      <td>44984.36803</td>
      <td>44094.92509</td>
      <td>42353.48494</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1998-01-01</td>
      <td>64148.08628</td>
      <td>79976.21086</td>
      <td>97913.84288</td>
      <td>66899.05828</td>
      <td>50368.36040</td>
      <td>50771.31393</td>
      <td>46763.00972</td>
      <td>46308.63234</td>
      <td>44245.70109</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1999-01-01</td>
      <td>69447.64997</td>
      <td>87345.54483</td>
      <td>105695.32480</td>
      <td>71965.72065</td>
      <td>52640.75590</td>
      <td>53061.77692</td>
      <td>47586.11332</td>
      <td>47592.93309</td>
      <td>45466.77004</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



### Using the <code>df.apply()</code> method

The Pandas DataFrame <code>apply()</code> method applies a function to each row or column in the DataFrame. We're going to create a dummy DataFrame to see its behaviour:


```python
df = DataFrame.from_dict({'num1' : [1,2,3,4,5], 
                          'num2' : [5,10,15,20,25], 
                          'num3' : [10,20,30,40,50], 
                                    'letter' : ['a','b','c','d','e']})
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>letter</th>
      <th>num1</th>
      <th>num2</th>
      <th>num3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



Now, we're going to define a simple function which we will apply to the DataFrame. This function must take only one argument. Apply will pass the value of each cell in turn to the function, this value will be passed as the value for the function argument:


```python
def simpleFunction(x):
    return x * 5
```

Let's apply this function to the DataFrame:


```python
df.apply(simpleFunction)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>letter</th>
      <th>num1</th>
      <th>num2</th>
      <th>num3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aaaaa</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bbbbb</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ccccc</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ddddd</td>
      <td>20</td>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>eeeee</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



We can define a function that is intended to work along the rows:


```python
def rowFunction(x):
    return x[0] + str(x[2]) + str(x[3])
```


```python
df.apply(rowFunction, axis = 1)
```




    0    a11
    1    b22
    2    c33
    3    d44
    4    e55
    dtype: object



And we can use that function to create a new column:


```python
df['newcol'] = df.apply(rowFunction, axis = 1)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>letter</th>
      <th>num1</th>
      <th>num2</th>
      <th>num3</th>
      <th>newcol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>a11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>b22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>c33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>d44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>e55</td>
    </tr>
  </tbody>
</table>
</div>



We can also apply a function to a specific column:


```python
def multiple(x):
    return x * 5
df['newcol2'] = df['letter'].apply(multiple)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>letter</th>
      <th>num1</th>
      <th>num2</th>
      <th>num3</th>
      <th>newcol</th>
      <th>newcol2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>a11</td>
      <td>aaaaa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>b22</td>
      <td>bbbbb</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>c33</td>
      <td>ccccc</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>d44</td>
      <td>ddddd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>e55</td>
      <td>eeeee</td>
    </tr>
  </tbody>
</table>
</div>



## Using the </code>lambda</code> function

The lambda function is not bound to a function name, and only exists for the duration of its use. Lambda functions implicitly return a value. 

We can put a lambda function inside the <code>df.apply()</code> method to manipulate the values in a DataFrame:


```python
df['newcol3'] = df.apply(lambda x: x['newcol'] + x['newcol2'], axis = 1)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>letter</th>
      <th>num1</th>
      <th>num2</th>
      <th>num3</th>
      <th>newcol</th>
      <th>newcol2</th>
      <th>newcol3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>a11</td>
      <td>aaaaa</td>
      <td>a11aaaaa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>b22</td>
      <td>bbbbb</td>
      <td>b22bbbbb</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>c33</td>
      <td>ccccc</td>
      <td>c33ccccc</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>d44</td>
      <td>ddddd</td>
      <td>d44ddddd</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>e55</td>
      <td>eeeee</td>
      <td>e55eeeee</td>
    </tr>
  </tbody>
</table>
</div>



We'll now use the lambda function to build our text column.

We need to make this column for every region, so I'll first make a list of regions:


```python
regions = ['South West','South East','London', 
           'East of England','West Midlands','East Midlands',
           'Yorkshire and The Humber','North West','North East']
```

Next, we'll loop through each region and create a new column which contains the name of the region. This will form the basis of our text column:


```python
for r in regions:
    housePrices[r + "_text"] = r
    
housePrices.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>...</th>
      <th>North East_rank</th>
      <th>South West</th>
      <th>South East</th>
      <th>London</th>
      <th>East of England</th>
      <th>West Midlands</th>
      <th>East Midlands</th>
      <th>Yorkshire and The Humber</th>
      <th>North West</th>
      <th>North East</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.1579</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.5961</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>...</td>
      <td>9.0</td>
      <td>South West</td>
      <td>South East</td>
      <td>London</td>
      <td>East of England</td>
      <td>West Midlands</td>
      <td>East Midlands</td>
      <td>Yorkshire and The Humber</td>
      <td>North West</td>
      <td>North East</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 28 columns</p>
</div>



Now, we can add the HTML bold and line break tags. &lt;b&gt;...&lt;/b&gt; creates bold text and &lt;br&gt; inserts a line break.

These look odd in the table, but Plotly displays them as they are intended:


```python
for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>"
    
housePrices.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>...</th>
      <th>North East_rank</th>
      <th>South West</th>
      <th>South East</th>
      <th>London</th>
      <th>East of England</th>
      <th>West Midlands</th>
      <th>East Midlands</th>
      <th>Yorkshire and The Humber</th>
      <th>North West</th>
      <th>North East</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.1579</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.5961</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>...</td>
      <td>9.0</td>
      <td>&lt;b&gt;South West&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 28 columns</p>
</div>



Next we'll use the <code>df.apply()</code> method and a lambda function to add the average price to this text field.

We're selecting the column which has the average price for each region with <code>housePrices[r + "_avg"]</code>. Next, we'll take the value that we get for that particular column, round it, convert it to an integer and format it with a thousand separator, and return it by applying the lambda function: <code>apply(lambda x: "£{:,}".format(int(x.round(0))))</code>:


```python
for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(x.round(0)))) + "<br>"
housePrices.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>...</th>
      <th>North East_rank</th>
      <th>South West</th>
      <th>South East</th>
      <th>London</th>
      <th>East of England</th>
      <th>West Midlands</th>
      <th>East Midlands</th>
      <th>Yorkshire and The Humber</th>
      <th>North West</th>
      <th>North East</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.1579</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.5961</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>...</td>
      <td>9.0</td>
      <td>&lt;b&gt;South West&lt;/b&gt;&lt;br&gt;Average Price: £54,705&lt;br&gt;</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;Average Price: £64,019&lt;br&gt;</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;Average Price: £74,436&lt;br&gt;</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;Average Price: £56,7...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,091...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,545...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;Average Pri...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;Average Price: £43,958&lt;br&gt;</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;Average Price: £42,076&lt;br&gt;</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 28 columns</p>
</div>



Now we can add the rank to our text column in the same way, just specfing that the rank should be an integer rather than a float. The &lt;i&gt;...&lt;/i&gt; tags make this text italicised.


```python
for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(x.round(0)))) + "<br><i>Rank of average price: " + housePrices[r + "_rank"].apply(lambda x: 
                                                                                                             str(int(x))) + "</i>"
housePrices.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>South West_avg</th>
      <th>South East_avg</th>
      <th>London_avg</th>
      <th>East of England_avg</th>
      <th>West Midlands_avg</th>
      <th>East Midlands_avg</th>
      <th>Yorkshire and The Humber_avg</th>
      <th>North West_avg</th>
      <th>North East_avg</th>
      <th>...</th>
      <th>North East</th>
      <th>South West_text</th>
      <th>South East_text</th>
      <th>London_text</th>
      <th>East of England_text</th>
      <th>West Midlands_text</th>
      <th>East Midlands_text</th>
      <th>Yorkshire and The Humber_text</th>
      <th>North West_text</th>
      <th>North East_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1995-01-01</td>
      <td>54705.1579</td>
      <td>64018.87894</td>
      <td>74435.76052</td>
      <td>56701.5961</td>
      <td>45090.91026</td>
      <td>45544.52227</td>
      <td>44803.42878</td>
      <td>43958.48001</td>
      <td>42076.35411</td>
      <td>...</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;Average Price: £42,076&lt;br...</td>
      <td>&lt;b&gt;South West&lt;/b&gt;&lt;br&gt;Average Price: £54,705&lt;br...</td>
      <td>&lt;b&gt;South East&lt;/b&gt;&lt;br&gt;Average Price: £64,019&lt;br...</td>
      <td>&lt;b&gt;London&lt;/b&gt;&lt;br&gt;Average Price: £74,436&lt;br&gt;&lt;i&gt;...</td>
      <td>&lt;b&gt;East of England&lt;/b&gt;&lt;br&gt;Average Price: £56,7...</td>
      <td>&lt;b&gt;West Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,091...</td>
      <td>&lt;b&gt;East Midlands&lt;/b&gt;&lt;br&gt;Average Price: £45,545...</td>
      <td>&lt;b&gt;Yorkshire and The Humber&lt;/b&gt;&lt;br&gt;Average Pri...</td>
      <td>&lt;b&gt;North West&lt;/b&gt;&lt;br&gt;Average Price: £43,958&lt;br...</td>
      <td>&lt;b&gt;North East&lt;/b&gt;&lt;br&gt;Average Price: £42,076&lt;br...</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 37 columns</p>
</div>



Let's look at the value in a cell to make sure that we have done what we intended:


```python
housePrices.loc[0, 'London']
```




    '<b>London</b><br>Average Price: £74,436<br>Rank of average price: 1'



