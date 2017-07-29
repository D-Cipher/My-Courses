
# Chart presentation (8) - Changing hovertext (1)

In the last lessons we learnt how to use Pandas' <code>df.apply()</code> in conjunction with a user-defined or a <code>lambda</code> function to create a column in our DataFrame to store the value for the hovertext.

In this lesson we'll apply what we've learnt to the  stacked quantity C02 emissions area plot, and in the next we'll update the stacked proportional C02 emissions area plot.

We will get the data and rewrite the code which creates the chart rather than reloading the charts as we need to manipulate the DataFrames from which they were created in order to make the hovertext field.






 






### Stacked quantity area plot

Let's get the emissions data again:


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



### Writing a function

Seeing as we have to rewrite the code for this chart, let's try to do it as programmatically as we can. In lesson 13 of the Lineplot section we used a very long-winded way of making this chart, however in the subsequent lessons we found that we could reduce the amount of code by using the <code>df.cumsum()</code> method. We then further generalised the code by writing a function to create a stacked proportional area plot; we'll use the ideas from that function as a base to write one for a stacked quantity area plot.

If you'd like a challenge, go ahead and write a function which makes a stacked quantity area plot (you can base this code on the stacked proportional area), alternatively you can code along with me!

This function will have six arguments (the same five as for creating the stacked proportional area plot), plus one more which will define some of the text that goes in the hovertext field. As before, I'll write the explanation here and only include it in the finished function to save on space. We'll also test the function as we go.


```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked quantity area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text common to every hoverlabel
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
```

We need to reduce the input DataFrame down to only the columns which we need. You can also reuse this bit of code from the stacked proportional area function:


```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
        
    return stackedAreaDF
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
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



We don't need to create a 'Total' column because we're not calculating proportions, but we do need to calculate the cumulative sum of only the country columns:


```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
        
    return cumulative
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'],  'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
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
      <td>11.001</td>
      <td>584310.781</td>
      <td>3475006.881</td>
      <td>4255733.183</td>
      <td>4376315.144</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.001</td>
      <td>588949.536</td>
      <td>3469455.043</td>
      <td>4021521.893</td>
      <td>4151924.080</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.335</td>
      <td>593379.272</td>
      <td>3580587.145</td>
      <td>4020946.174</td>
      <td>4164413.882</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22.002</td>
      <td>603844.890</td>
      <td>3723075.764</td>
      <td>4159771.460</td>
      <td>4313855.133</td>
    </tr>
    <tr>
      <th>4</th>
      <td>18.335</td>
      <td>608373.635</td>
      <td>3864368.941</td>
      <td>4301291.991</td>
      <td>4451939.685</td>
    </tr>
  </tbody>
</table>
</div>



In order to create the hovertext column, we need the original values for the emissions. I'm going to merge the two DataFrames by their index. Because they both have the same number of rows, this is not a problem - each row in one DataFrame will map correctly to its counterpart in the other.

I also need to create a suffix for the column names for each DataFrame - because both have the same names, we need to know how to refer to the correct column:



```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulativeAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
        
    return cumulativeAndOrig
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'],  'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>United Arab Emirates | ARE_c</th>
      <th>United Kingdom | GBR_c</th>
      <th>United States | USA_c</th>
      <th>China | CHN_c</th>
      <th>India | IND_c</th>
      <th>Year</th>
      <th>United Arab Emirates | ARE_o</th>
      <th>United Kingdom | GBR_o</th>
      <th>United States | USA_o</th>
      <th>China | CHN_o</th>
      <th>India | IND_o</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.001</td>
      <td>584310.781</td>
      <td>3475006.881</td>
      <td>4255733.183</td>
      <td>4376315.144</td>
      <td>1960</td>
      <td>11.001</td>
      <td>584299.780</td>
      <td>2890696.100</td>
      <td>780726.302</td>
      <td>120581.961</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.001</td>
      <td>588949.536</td>
      <td>3469455.043</td>
      <td>4021521.893</td>
      <td>4151924.080</td>
      <td>1961</td>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.335</td>
      <td>593379.272</td>
      <td>3580587.145</td>
      <td>4020946.174</td>
      <td>4164413.882</td>
      <td>1962</td>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22.002</td>
      <td>603844.890</td>
      <td>3723075.764</td>
      <td>4159771.460</td>
      <td>4313855.133</td>
      <td>1963</td>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>18.335</td>
      <td>608373.635</td>
      <td>3864368.941</td>
      <td>4301291.991</td>
      <td>4451939.685</td>
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



Now we can use the Pandas' <code>df.apply(lambda x : x)</code> construction that we learnt in the previous lesson to create a text column for each country. This will also use the <code>hover</code> variable that we pass to the function:


```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
    
    for col in cols:
        cumulAndOrig[col + '_t'] = "<b>" + str(col)[:-6] + "</b><br>" + str(hover) + cumulAndOrig[col + "_o"].apply(lambda x:
            "{:,}Kt".format(int(round(x, 0))))
        
    return cumulAndOrig
   
test = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
test.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>United Arab Emirates | ARE_c</th>
      <th>United Kingdom | GBR_c</th>
      <th>United States | USA_c</th>
      <th>China | CHN_c</th>
      <th>India | IND_c</th>
      <th>Year</th>
      <th>United Arab Emirates | ARE_o</th>
      <th>United Kingdom | GBR_o</th>
      <th>United States | USA_o</th>
      <th>China | CHN_o</th>
      <th>India | IND_o</th>
      <th>United Arab Emirates | ARE_t</th>
      <th>United Kingdom | GBR_t</th>
      <th>United States | USA_t</th>
      <th>China | CHN_t</th>
      <th>India | IND_t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.001</td>
      <td>584310.781</td>
      <td>3475006.881</td>
      <td>4255733.183</td>
      <td>4376315.144</td>
      <td>1960</td>
      <td>11.001</td>
      <td>584299.78</td>
      <td>2890696.1</td>
      <td>780726.302</td>
      <td>120581.961</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Total C02 Emiss...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Total C02 Emissions: ...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Total C02 Emissions: 2...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Total C02 Emissions: 780,726Kt</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Total C02 Emissions: 120,582Kt</td>
    </tr>
  </tbody>
</table>
</div>



Now we can create our traces inside the same loop which creates the text, then create our Data, Layout and Figure objects before plotting the chart! I'm also going to return the Figure object so we can send it to the Plotly cloud:


```python
def createStackedQuantArea(df, time, cols, hover, title, yaxisTitle):
    """
    A function which manipulates the data into the correct format to produce a stacked quantity area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    title - the title of the chart
    yaxisTitle - the yaxis title of the chart (the xaxis title comes from the time variable)
    """
    traces = []
    stackedAreaDF = df.loc[:, ([time] + cols)]
    stackedAreaDF.fillna(0, inplace=True)
    
    cumulative = stackedAreaDF[cols].cumsum(axis = 1)
    
    cumulAndOrig = cumulative.merge(stackedAreaDF, 
                                         left_index = True,
                                         right_index = True,
                                        suffixes = ('_c','_o'))
    
    for col in cols:
        cumulAndOrig[col + '_t'] = "<b>" + str(col)[:-6]  + "</b><br>" + str(hover) + cumulAndOrig[col + "_o"].apply(lambda x:
            "{:,}Kt".format(int(round(x, 0))))
        
        traces.append({'type' : 'scatter',
                      'x' : cumulAndOrig[time],
                      'y' : cumulAndOrig[col + "_c"],
                       'text' : cumulAndOrig[col + "_t"],
                       'hoverinfo' : 'text+x',
                      'name' : col[:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
        
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle,
                       'ticksuffix' : ' Kt'},
             'hovermode' : 'closest'}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(8)%20-%20Changing%20hovertext%20(1)/pyo.iplot-0.png)    return fig
    
    
C02Quant = createStackedQuantArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND'], 'Total C02 Emissions: ',
                            "Quantity of Co2 Emissions, 1960-2011", 'Quantity of Co2 Emissions')
```





Let's push this chart to the Plotly cloud:


```python
py.plot(C02Quant, "C02 Emissions for UAE, USA, UK, India & China 1960 - 2011", fileopt = 'overwrite')
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(8)%20-%20Changing%20hovertext%20(1)/py.plot-0.png)``




    'https://plot.ly/~rmuir/124'



