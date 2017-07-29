
# Lineplots (14) - Stacked proportional area plots

In the last lesson, we saw how to make a stacked area plot using the <code>'tonexty'</code> option for the <code>'fill'</code> option. This allowed us to compare the change in total emissions, as well as the change in each individual country's emissions over a period of time.

In this lesson we're going to create a stacked area plot which shows the percentage of total emissions that each country produced. The code for the chart will be almost identical to the previous lesson; the novelty in this lesson will be learning how to do a little data manipulation to get the data into percentages of total emissions, rather than just the raw figures. 

We'll also prepare the data in a way that allows us to create the traces using a loop, rather than the long-form way we learnt in the previous lesson, and in doing so we'll learn how to use the <code>pandas.cumsum()</code> function to get a cumulative sum over several traces.






 






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



### Preparing the data

The next step is to select from the DataFrame the columns which we want to include in our chart. I'm going to include the same five countries as in the previous lesson - I suggest you do the same so you can check your code is working properly. 

To make life a little easier in the future, I'm going to select the columns in two stages. First of all I'm going to get a list of the countries that will be included in the chart. This list will serve two purposes:
- Select the countries that we want to include
- Provide a list of country columns which we can use to create the row totals (we don't want to add the year column to the total)
Then, I also need to pass the <code>'Year'</code> column to the selection to make sure that's included in the new DataFrame:


```python
sumColumnSelection = ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',]

stackedAreaData = emissions.loc[:,(['Year'] + sumColumnSelection)]
stackedAreaData.head()
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
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>18.335</td>
      <td>608355.300</td>
      <td>3255995.306</td>
      <td>436923.050</td>
      <td>150647.694</td>
    </tr>
  </tbody>
</table>
</div>



The next step is to calculate the row totals for each year; we'll need these in order to calculate each country's share of the total emissions each year. We'll do this with the <code>df.sum()</code> method and the list of countries that we've just created.


```python
stackedAreaData['Total'] = stackedAreaData[sumColumnSelection].sum(axis = 1)
stackedAreaData.head()
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



Now, I'll calculate each country's percentage of total emissions for the year. I'll write a loop to go through the columns to make this easier:


```python
for country in sumColumnSelection:
    stackedAreaData["pc_"+str(country)] = stackedAreaData[country] / stackedAreaData['Total']
    
stackedAreaData.head()
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



We can now use the <code>pandas.DataFrame.cumsum()</code> method to get a cumulative row total of the percentages. This will allow us to create the traces much more easily. 

First of all I'll make a new list of the percentage columns:


```python
sumColumnSelectionPC = ['pc_United Arab Emirates | ARE','pc_United Kingdom | GBR', 
                   'pc_United States | USA','pc_China | CHN', 'pc_India | IND',]
```

Now, I'll use that list to only select the percentage columns for cumulative summing. I'm also going to create a new object:


```python
PCAreaData = stackedAreaData[sumColumnSelectionPC].cumsum(axis=1)
PCAreaData.head()
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
    </tr>
    <tr>
      <th>1</th>
      <td>0.000003</td>
      <td>0.141850</td>
      <td>0.835626</td>
      <td>0.968592</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.000004</td>
      <td>0.142488</td>
      <td>0.859806</td>
      <td>0.965549</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.000005</td>
      <td>0.139978</td>
      <td>0.863051</td>
      <td>0.964282</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000004</td>
      <td>0.136654</td>
      <td>0.868019</td>
      <td>0.966161</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



We can check if this worked by using a calculator on a couple of rows. However it does seem likely that it worked because the cumulative total for India is 1 in every case.

Next we need to add the <code>'Year'</code> column to the DataFrame - we'll take this straight from the <code>stackedAreaData</code> DataFrame.


```python
PCAreaData['Year'] = stackedAreaData['Year']

PCAreaData.head()
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



### Plotting the chart

Now, we can loop through the columns in the DataFrame and create our traces. 

I'm using a string slice to remove the <code>'pc_'</code> and the country code from the column name to create a meaningful name for the trace.


```python
traces = []

for col in PCAreaData.columns.tolist():
    if col != 'Year':
        traces.append({'type' : 'scatter',
                      'x' : PCAreaData['Year'],
                      'y' : PCAreaData[col],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
traces
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



Let's create the Data, Layout and Figure objects and plot the chart!


```python
data = Data(traces)
layout = {'title' : "Proportion of Co2 Emissions, 1960-2011",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Proprtion of Co2 Emissions'}}
fig = Figure(data = data, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(14)%20-%20Stacked%20proportional%20area%20plots/pyo.iplot-0.png)```





This chart, whilst showing the same data as the previous chart, paints a very different picture. We can see that the United Arab Emirates' proportion of total emissions has risen slightly, the UK's had fallen to about a third of the 1960 levels by 2010. America's share of total emissions has dropped even more dramatically, whilst China and India's share of emissions has rise, with China's share rising much more dramatically.

When taken in conjunction with the previous chart, which showed how the total emissions has rises, both of these charts present a very powerful message.

On a more critical note, this chart isn't quite there yet. The hoverinfo shows the cumulative sum of emissions, rather than each country's individual emissions and it would also be nice to display the proportions as percentages. We will return to both of these in a future lesson, but for now I'm really happy with this chart; let's push it to the Plotly cloud!


```python
py.plot(fig, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = "overwrite")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(14)%20-%20Stacked%20proportional%20area%20plots/py.plot-0.png)``




    'https://plot.ly/~rmuir/158'



### Stacked proportional area plots - what have we learnt?

This class focussed more on data manipulation that on actually charting. We saw that with a few simple functions and methods, we can make our life much easier!

We learnt how to use label-based indexing to select certain columns from a DataFrame. We used the <code>df.sum(axis = 1)</code> method to get a total for each row in the DataFrame to allow us to calculate the percentage of total.

We calculated the percentage of total emissions for each country in a list using a loop, and then used <code>df.cumsum(axis=1)</code> to give us a cumulative total over the columns.

Finally, we plotted this data using a For loop, specifying <code>'fill' : 'tonexty'</code> in the trace.

In the next lesson we're going to wrap all of this in a function which will let us create a stacked area plot for as many countries as we wish.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>