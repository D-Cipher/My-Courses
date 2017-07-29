
# Lineplots (15) - Creating a stacked proportional area plot with a function

In the last lesson we saw how to prepare the data to allow us to easily make a stacked proportional area plot. 

In this lesson we're going to wrap the code we wrote in a function which will allow us to choose which countries are displayed in what order on the chart.

This will be the most difficult piece of code we'll have written so far - it's meant to be challenging. If you don't understand or get stuck along the way, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>.



We'll also import the <code>random</code> library which we'll use at the end of this lesson to help us test our function.



import random



```python

 
```





## Getting the data

I'll get the data in the same way as the previous lesson:


```python
emissions = pd.read_csv("http://richard-muir.com/data/public/csv/TotalCo2EmissionsByCountry.csv", index_col=0)
emissions.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Afghanistan | AFG</th>
      <th>Albania | ALB</th>
      <th>Algeria | DZA</th>
      <th>American Samoa | ASM</th>
      <th>Andorra | AND</th>
      <th>Angola | AGO</th>
      <th>Antigua and Barbuda | ATG</th>
      <th>Arab World | ARB</th>
      <th>Argentina | ARG</th>
      <th>...</th>
      <th>Uzbekistan | UZB</th>
      <th>Vanuatu | VUT</th>
      <th>Venezuela, RB | VEN</th>
      <th>Vietnam | VNM</th>
      <th>Virgin Islands (U.S.) | VIR</th>
      <th>West Bank and Gaza | PSE</th>
      <th>World | WLD</th>
      <th>Yemen, Rep. | YEM</th>
      <th>Zambia | ZMB</th>
      <th>Zimbabwe | ZWE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>414.371</td>
      <td>2024.184</td>
      <td>6160.560</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>550.050</td>
      <td>36.670</td>
      <td>59563.98922</td>
      <td>48815.104</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57069.521</td>
      <td>7491.681</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.396706e+06</td>
      <td>3633.997</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>491.378</td>
      <td>2280.874</td>
      <td>6065.218</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>454.708</td>
      <td>47.671</td>
      <td>65151.09581</td>
      <td>51180.319</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>51928.387</td>
      <td>7986.726</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.434403e+06</td>
      <td>2665.909</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>689.396</td>
      <td>2464.224</td>
      <td>5669.182</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1180.774</td>
      <td>102.676</td>
      <td>74357.70773</td>
      <td>53695.881</td>
      <td>...</td>
      <td>NaN</td>
      <td>40.337</td>
      <td>54106.585</td>
      <td>9347.183</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.818840e+06</td>
      <td>3887.020</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>707.731</td>
      <td>2082.856</td>
      <td>5427.160</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1151.438</td>
      <td>84.341</td>
      <td>87895.97916</td>
      <td>50083.886</td>
      <td>...</td>
      <td>NaN</td>
      <td>33.003</td>
      <td>56204.109</td>
      <td>9119.829</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.035575e+07</td>
      <td>2918.932</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>839.743</td>
      <td>2016.850</td>
      <td>5650.847</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1224.778</td>
      <td>91.675</td>
      <td>103196.28160</td>
      <td>55727.399</td>
      <td>...</td>
      <td>NaN</td>
      <td>62.339</td>
      <td>56603.812</td>
      <td>11800.406</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.094701e+07</td>
      <td>3633.997</td>
      <td>3278.298</td>
      <td>4473.74</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 249 columns</p>
</div>



### Writing the function

The function we're going to write will not only plot the chart, but will also do all of the data manipulation and calculation. The function will take 5 arguments:
- a DataFrame
- the column name of the time element in the data as a string
- a list of columns which contain the variables we want to include in the chart (the columns must be present in the DataFrame)
- The title of the chart
- The y-axis title (the x-axis title will be the time element of the DataFrame)

At each stage of making this function we're going to return an object that will allow us to check if the code we've written works as expected.

Before we begin writing the function, it's important to write a docstring, especially for a large function such as this. Writing a docstring means that when you come back to use the function, you don't have to figure out what each variable does and what type of variable you need to pass to the function. I'll write this now, and then include it in the finished version to save on space.


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame as a string
    cols - the name of the columns in the DataFrame which you want to include in the area plot as list
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
```

The first step in the function is to create a DataFrame which contains only the columns that we want to keep. 

In this section, I'm going to include Andorra to make sure that the <code>fillna()</code> function has worked. In the rest of the lesson I'm going to test the function as we go by using the same countries as in the previous lesson. This will assure me that the function is right! 


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    return stackedAreaDF
   
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND', 'Andorra | AND'],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>United Arab Emirates | ARE</th>
      <th>United Kingdom | GBR</th>
      <th>United States | USA</th>
      <th>China | CHN</th>
      <th>India | IND</th>
      <th>Andorra | AND</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>11.001</td>
      <td>584299.780</td>
      <td>2890696.100</td>
      <td>780726.302</td>
      <td>120581.961</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>18.335</td>
      <td>608355.300</td>
      <td>3255995.306</td>
      <td>436923.050</td>
      <td>150647.694</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



The next step is to create the <code>'Total'</code> column:


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    return stackedAreaDF
    
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>United Arab Emirates | ARE</th>
      <th>United Kingdom | GBR</th>
      <th>United States | USA</th>
      <th>China | CHN</th>
      <th>India | IND</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>11.001</td>
      <td>584299.780</td>
      <td>2890696.100</td>
      <td>780726.302</td>
      <td>120581.961</td>
      <td>4376315.144</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
      <td>4151924.080</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
      <td>4164413.882</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
      <td>4313855.133</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>18.335</td>
      <td>608355.300</td>
      <td>3255995.306</td>
      <td>436923.050</td>
      <td>150647.694</td>
      <td>4451939.685</td>
    </tr>
  </tbody>
</table>
</div>



Now we'll calculate the percentage for each country using the <code>'Total'</code> column. I also want to create a list of all the column names which hold percentages. I'll use that hlist to help me calculate the cumulative sum.


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):
    PCcols = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)

    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
    
    return stackedAreaDF
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>United Arab Emirates | ARE</th>
      <th>United Kingdom | GBR</th>
      <th>United States | USA</th>
      <th>China | CHN</th>
      <th>India | IND</th>
      <th>Total</th>
      <th>pc_United Arab Emirates | ARE</th>
      <th>pc_United Kingdom | GBR</th>
      <th>pc_United States | USA</th>
      <th>pc_China | CHN</th>
      <th>pc_India | IND</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>11.001</td>
      <td>584299.780</td>
      <td>2890696.100</td>
      <td>780726.302</td>
      <td>120581.961</td>
      <td>4376315.144</td>
      <td>0.000003</td>
      <td>0.133514</td>
      <td>0.660532</td>
      <td>0.178398</td>
      <td>0.027553</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
      <td>4151924.080</td>
      <td>0.000003</td>
      <td>0.141847</td>
      <td>0.693776</td>
      <td>0.132967</td>
      <td>0.031408</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
      <td>4164413.882</td>
      <td>0.000004</td>
      <td>0.142484</td>
      <td>0.717318</td>
      <td>0.105743</td>
      <td>0.034451</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
      <td>4313855.133</td>
      <td>0.000005</td>
      <td>0.139973</td>
      <td>0.723073</td>
      <td>0.101231</td>
      <td>0.035718</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>18.335</td>
      <td>608355.300</td>
      <td>3255995.306</td>
      <td>436923.050</td>
      <td>150647.694</td>
      <td>4451939.685</td>
      <td>0.000004</td>
      <td>0.136649</td>
      <td>0.731366</td>
      <td>0.098142</td>
      <td>0.033839</td>
    </tr>
  </tbody>
</table>
</div>



We'll now create a new DataFrame which will be the cumulative sum of the percentages for the countries of interest. We'll also need to concatenate the time element variable:


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):
    PCcols = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    
    
    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]
    
    
    return stackedPCAreaDF
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pc_United Arab Emirates | ARE</th>
      <th>pc_United Kingdom | GBR</th>
      <th>pc_United States | USA</th>
      <th>pc_China | CHN</th>
      <th>pc_India | IND</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000003</td>
      <td>0.133517</td>
      <td>0.794049</td>
      <td>0.972447</td>
      <td>1.0</td>
      <td>1960</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000003</td>
      <td>0.141850</td>
      <td>0.835626</td>
      <td>0.968592</td>
      <td>1.0</td>
      <td>1961</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.000004</td>
      <td>0.142488</td>
      <td>0.859806</td>
      <td>0.965549</td>
      <td>1.0</td>
      <td>1962</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.000005</td>
      <td>0.139978</td>
      <td>0.863051</td>
      <td>0.964282</td>
      <td>1.0</td>
      <td>1963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000004</td>
      <td>0.136654</td>
      <td>0.868019</td>
      <td>0.966161</td>
      <td>1.0</td>
      <td>1964</td>
    </tr>
  </tbody>
</table>
</div>



Now we'll create the traces in the same way as we did in the previous lesson:


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle):  
    
    PCcols = []
    traces = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    stackedAreaDF.fillna(0, inplace=True)

    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]

    for col in PCcols:
        traces.append({'type' : 'scatter',
                     'x' : stackedPCAreaDF[time],
                     'y' : stackedPCAreaDF[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    return traces
  
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
test
```




    [{'fill': 'tonexty',
      'mode': 'lines',
      'name': 'United Arab Emirates',
      'type': 'scatter',
      'x': 0     1960
      1     1961
      2     1962
      3     1963
      4     1964
      5     1965
      6     1966
      7     1967
      8     1968
      9     1969
      10    1970
      11    1971
      12    1972
      13    1973
      14    1974
      15    1975
      16    1976
      17    1977
      18    1978
      19    1979
      20    1980
      21    1981
      22    1982
      23    1983
      24    1984
      25    1985
      26    1986
      27    1987
      28    1988
      29    1989
      30    1990
      31    1991
      32    1992
      33    1993
      34    1994
      35    1995
      36    1996
      37    1997
      38    1998
      39    1999
      40    2000
      41    2001
      42    2002
      43    2003
      44    2004
      45    2005
      46    2006
      47    2007
      48    2008
      49    2009
      50    2010
      51    2011
      Name: Year, dtype: int64,
      'y': 0     0.000003
      1     0.000003
      2     0.000004
      3     0.000005
      4     0.000004
      5     0.000005
      6     0.000005
      7     0.000187
      8     0.000244
      9     0.003771
      10    0.002557
      11    0.003461
      12    0.003673
      13    0.004603
      14    0.004844
      15    0.004825
      16    0.005908
      17    0.005531
      18    0.006121
      19    0.004940
      20    0.005158
      21    0.005296
      22    0.005366
      23    0.005033
      24    0.006344
      25    0.006605
      26    0.006129
      27    0.005903
      28    0.005699
      29    0.006290
      30    0.006060
      31    0.006502
      32    0.006456
      33    0.007066
      34    0.007585
      35    0.007073
      36    0.003979
      37    0.003982
      38    0.007821
      39    0.007406
      40    0.010282
      41    0.009270
      42    0.007575
      43    0.008807
      44    0.008676
      45    0.008506
      46    0.008670
      47    0.009378
      48    0.010504
      49    0.010445
      50    0.010297
      51    0.010483
      Name: pc_United Arab Emirates | ARE, dtype: float64},
     {'fill': 'tonexty',
      'mode': 'lines',
      'name': 'United Kingdom',
      'type': 'scatter',
      'x': 0     1960
      1     1961
      2     1962
      3     1963
      4     1964
      5     1965
      6     1966
      7     1967
      8     1968
      9     1969
      10    1970
      11    1971
      12    1972
      13    1973
      14    1974
      15    1975
      16    1976
      17    1977
      18    1978
      19    1979
      20    1980
      21    1981
      22    1982
      23    1983
      24    1984
      25    1985
      26    1986
      27    1987
      28    1988
      29    1989
      30    1990
      31    1991
      32    1992
      33    1993
      34    1994
      35    1995
      36    1996
      37    1997
      38    1998
      39    1999
      40    2000
      41    2001
      42    2002
      43    2003
      44    2004
      45    2005
      46    2006
      47    2007
      48    2008
      49    2009
      50    2010
      51    2011
      Name: Year, dtype: int64,
      'y': 0     0.133517
      1     0.141850
      2     0.142488
      3     0.139978
      4     0.136654
      5     0.133743
      6     0.126890
      7     0.121242
      8     0.119355
      9     0.119326
      10    0.112058
      11    0.111422
      12    0.105216
      13    0.103801
      14    0.100339
      15    0.098576
      16    0.095143
      17    0.091778
      18    0.088772
      19    0.091969
      20    0.086119
      21    0.085876
      22    0.085200
      23    0.082748
      24    0.078728
      25    0.080666
      26    0.079936
      27    0.076686
      28    0.072914
      29    0.073442
      30    0.070829
      31    0.071142
      32    0.068220
      33    0.065493
      34    0.064279
      35    0.060941
      36    0.057392
      37    0.054380
      38    0.058860
      39    0.057573
      40    0.059770
      41    0.059166
      42    0.054714
      43    0.053196
      44    0.049981
      45    0.048235
      46    0.046560
      47    0.044917
      48    0.044969
      49    0.040843
      50    0.040536
      51    0.036809
      Name: pc_United Kingdom | GBR, dtype: float64},
     {'fill': 'tonexty',
      'mode': 'lines',
      'name': 'United States',
      'type': 'scatter',
      'x': 0     1960
      1     1961
      2     1962
      3     1963
      4     1964
      5     1965
      6     1966
      7     1967
      8     1968
      9     1969
      10    1970
      11    1971
      12    1972
      13    1973
      14    1974
      15    1975
      16    1976
      17    1977
      18    1978
      19    1979
      20    1980
      21    1981
      22    1982
      23    1983
      24    1984
      25    1985
      26    1986
      27    1987
      28    1988
      29    1989
      30    1990
      31    1991
      32    1992
      33    1993
      34    1994
      35    1995
      36    1996
      37    1997
      38    1998
      39    1999
      40    2000
      41    2001
      42    2002
      43    2003
      44    2004
      45    2005
      46    2006
      47    2007
      48    2008
      49    2009
      50    2010
      51    2011
      Name: Year, dtype: int64,
      'y': 0     0.794049
      1     0.835626
      2     0.859806
      3     0.863051
      4     0.868019
      5     0.862111
      6     0.857528
      7     0.876298
      8     0.871215
      9     0.858885
      10    0.837900
      11    0.823159
      12    0.820018
      13    0.820720
      14    0.811361
      15    0.782910
      16    0.782471
      17    0.768107
      18    0.756835
      19    0.753471
      20    0.746229
      21    0.737590
      22    0.712017
      23    0.701046
      24    0.690683
      25    0.674970
      26    0.663285
      27    0.656987
      28    0.649376
      29    0.645439
      30    0.632833
      31    0.621103
      32    0.613593
      33    0.604497
      34    0.593090
      35    0.575413
      36    0.567239
      37    0.568395
      38    0.578116
      39    0.578303
      40    0.580578
      41    0.571173
      42    0.559897
      43    0.521328
      44    0.491540
      45    0.472635
      46    0.445769
      47    0.434737
      48    0.416544
      49    0.379623
      50    0.372846
      51    0.348422
      Name: pc_United States | USA, dtype: float64},
     {'fill': 'tonexty',
      'mode': 'lines',
      'name': 'China',
      'type': 'scatter',
      'x': 0     1960
      1     1961
      2     1962
      3     1963
      4     1964
      5     1965
      6     1966
      7     1967
      8     1968
      9     1969
      10    1970
      11    1971
      12    1972
      13    1973
      14    1974
      15    1975
      16    1976
      17    1977
      18    1978
      19    1979
      20    1980
      21    1981
      22    1982
      23    1983
      24    1984
      25    1985
      26    1986
      27    1987
      28    1988
      29    1989
      30    1990
      31    1991
      32    1992
      33    1993
      34    1994
      35    1995
      36    1996
      37    1997
      38    1998
      39    1999
      40    2000
      41    2001
      42    2002
      43    2003
      44    2004
      45    2005
      46    2006
      47    2007
      48    2008
      49    2009
      50    2010
      51    2011
      Name: Year, dtype: int64,
      'y': 0     0.972447
      1     0.968592
      2     0.965549
      3     0.964282
      4     0.966161
      5     0.964349
      6     0.964766
      7     0.964811
      8     0.963237
      9     0.964954
      10    0.967280
      11    0.966369
      12    0.965888
      13    0.966283
      14    0.964129
      15    0.960831
      16    0.960697
      17    0.954979
      18    0.956558
      19    0.955204
      20    0.951283
      21    0.946145
      22    0.942013
      23    0.938436
      24    0.938860
      25    0.935118
      26    0.931762
      27    0.930493
      28    0.928563
      29    0.923472
      30    0.919539
      31    0.915853
      32    0.912978
      33    0.912792
      34    0.910290
      35    0.907875
      36    0.902868
      37    0.900172
      38    0.897135
      39    0.891856
      40    0.891609
      41    0.889960
      42    0.890284
      43    0.894333
      44    0.896685
      45    0.896658
      46    0.894711
      47    0.891616
      48    0.881500
      49    0.873727
      50    0.880138
      51    0.878167
      Name: pc_China | CHN, dtype: float64},
     {'fill': 'tonexty',
      'mode': 'lines',
      'name': 'India',
      'type': 'scatter',
      'x': 0     1960
      1     1961
      2     1962
      3     1963
      4     1964
      5     1965
      6     1966
      7     1967
      8     1968
      9     1969
      10    1970
      11    1971
      12    1972
      13    1973
      14    1974
      15    1975
      16    1976
      17    1977
      18    1978
      19    1979
      20    1980
      21    1981
      22    1982
      23    1983
      24    1984
      25    1985
      26    1986
      27    1987
      28    1988
      29    1989
      30    1990
      31    1991
      32    1992
      33    1993
      34    1994
      35    1995
      36    1996
      37    1997
      38    1998
      39    1999
      40    2000
      41    2001
      42    2002
      43    2003
      44    2004
      45    2005
      46    2006
      47    2007
      48    2008
      49    2009
      50    2010
      51    2011
      Name: Year, dtype: int64,
      'y': 0     1.0
      1     1.0
      2     1.0
      3     1.0
      4     1.0
      5     1.0
      6     1.0
      7     1.0
      8     1.0
      9     1.0
      10    1.0
      11    1.0
      12    1.0
      13    1.0
      14    1.0
      15    1.0
      16    1.0
      17    1.0
      18    1.0
      19    1.0
      20    1.0
      21    1.0
      22    1.0
      23    1.0
      24    1.0
      25    1.0
      26    1.0
      27    1.0
      28    1.0
      29    1.0
      30    1.0
      31    1.0
      32    1.0
      33    1.0
      34    1.0
      35    1.0
      36    1.0
      37    1.0
      38    1.0
      39    1.0
      40    1.0
      41    1.0
      42    1.0
      43    1.0
      44    1.0
      45    1.0
      46    1.0
      47    1.0
      48    1.0
      49    1.0
      50    1.0
      51    1.0
      Name: pc_India | IND, dtype: float64}]



Finally, we'll create the Data, Layout and Figure objects and plot the chart. We're not going to return anything this time, as we'll be able to see the plot and diagnose any problems:


```python
def createStackedPropArea(df, time, cols, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
    PCcols = []
    traces = []
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    stackedAreaDF['Total'] = stackedAreaDF[cols].sum(axis =1)
    
    for col in cols:
        stackedAreaDF["pc_"+str(col)] = stackedAreaDF[col] / stackedAreaDF['Total']
        PCcols.append("pc_"+str(col))
        
    stackedPCAreaDF = stackedAreaDF[PCcols].cumsum(axis=1)
    stackedPCAreaDF[time] = stackedAreaDF[time]

    for col in PCcols:
        traces.append({'type' : 'scatter',
                      'x' : stackedPCAreaDF[time],
                      'y' : stackedPCAreaDF[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(15)%20-%20Creating%20a%20stacked%20proportional%20area%20plot%20with%20a%20function/pyo.iplot-0.png)    return fig
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',],
                            "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')

```





OK, so that looks like it worked! Let's try passing the countries in a different order:


```python
test2 = createStackedPropArea(emissions, 'Year', ['China | CHN', 
                                          'United States | USA', 
                                          'India | IND',
                                          'United Arab Emirates | ARE',
                                          'United Kingdom | GBR', 
                                          ],
                      "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
```





Finally, we'll try passing a totally new list of countries. I'll pick these at random using the <code>random.choice()</code> function from the <code>random</code> library, but feel free to have a look at the list of countries and choose some interesting comparisons!


```python
countries = []
for i in range(10):
    countries.append(random.choice(emissions.columns.tolist()))
countries
```




    ['Pacific island small states | PSS',
     'South Africa | ZAF',
     'Sweden | SWE',
     'Cuba | CUB',
     'Ghana | GHA',
     'Hungary | HUN',
     'Denmark | DNK',
     'Estonia | EST',
     'Singapore | SGP',
     'El Salvador | SLV']




```python
test3 = createStackedPropArea(emissions, 'Year', countries,  
                              "Proportion of Co2 Emissions, 1960-2015", 'Proprtion of Co2 Emissions')
```





### Creating a stacked proportional area plot with a function - What have we learnt?

In this lesson we've learnt how to take code that we've previously written and wrap it in a function, making it more generalisable and reusable. We've written a function that we can use to create a stacked proportional area plot from any suitable input DataFrame, learning how to build a function step by step, checking the output each time.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>