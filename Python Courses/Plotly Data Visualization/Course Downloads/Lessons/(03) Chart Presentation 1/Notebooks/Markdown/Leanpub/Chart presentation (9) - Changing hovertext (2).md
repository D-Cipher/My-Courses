
# Chart presentation (9) - Changing hovertext (2)

In the last lesson we applied what we had previously learnt about hovertext to the stacked quantity area plot which we previously made. In this lesson we're going to do the same for the stacked proportional area plot.






 






### Stacked proportional area plot

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



## Changing the proportional area plot

Now we can take the concepts that we applied to the stacked quantity area and inject them into the function that we wrote for the stacked proportional area plot. I suggest just copying and pasting this function from your notes from the previous lesson rather than writing it out. 

I'm going to add another variable <code>hover</code> to the function - this allows us to define which text appears on each hover label.


```python
def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(9)%20-%20Changing%20hovertext%20(2)/pyo.iplot-0.png)
    
    return fig
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
```





First of all we need to merge the cumulative percentage DataFrame with the original. I'll paste this bit of code over in just after we create the cumulative DataFrame. We can also remove the part where we assign the <code>time</code> column to the cumulative sum DataFrame:

````python
stackedAreaData = stackedAreaDF[[time] + PCcols].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))
````    

We also need to change the data source and column names that we pass to the trace to reflect the updated names from the merge function:
````python
'x' : stackedAreaData[time],
'y' : stackedAreaData[col + "_c"],
````

I'm not going to plot the chart, but I am going to return the <code>stackedAreaData</code> object to see that it has been made correctly:


```python
def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes six arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    
    
    ########################################################
    ################## NEW CODE GOES HERE ##################
    ########################################################
    stackedAreaData = stackedAreaDF[[time] + PCcols].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))
    
    for col in PCcols:
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                       ## CHANGE THE COLUMN REFERENCE ##
                      'y' : stackedAreaData[col + "_c"],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    #pyo.iplot(fig)


![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(9)%20-%20Changing%20hovertext%20(2)/pyo.iplot-1.png)    
    return stackedAreaData
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>pc_United Arab Emirates | ARE_o</th>
      <th>pc_United Kingdom | GBR_o</th>
      <th>pc_United States | USA_o</th>
      <th>pc_China | CHN_o</th>
      <th>pc_India | IND_o</th>
      <th>pc_United Arab Emirates | ARE_c</th>
      <th>pc_United Kingdom | GBR_c</th>
      <th>pc_United States | USA_c</th>
      <th>pc_China | CHN_c</th>
      <th>pc_India | IND_c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>0.000003</td>
      <td>0.133514</td>
      <td>0.660532</td>
      <td>0.178398</td>
      <td>0.027553</td>
      <td>0.000003</td>
      <td>0.133517</td>
      <td>0.794049</td>
      <td>0.972447</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>0.000003</td>
      <td>0.141847</td>
      <td>0.693776</td>
      <td>0.132967</td>
      <td>0.031408</td>
      <td>0.000003</td>
      <td>0.141850</td>
      <td>0.835626</td>
      <td>0.968592</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>0.000004</td>
      <td>0.142484</td>
      <td>0.717318</td>
      <td>0.105743</td>
      <td>0.034451</td>
      <td>0.000004</td>
      <td>0.142488</td>
      <td>0.859806</td>
      <td>0.965549</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>0.000005</td>
      <td>0.139973</td>
      <td>0.723073</td>
      <td>0.101231</td>
      <td>0.035718</td>
      <td>0.000005</td>
      <td>0.139978</td>
      <td>0.863051</td>
      <td>0.964282</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>0.000004</td>
      <td>0.136649</td>
      <td>0.731366</td>
      <td>0.098142</td>
      <td>0.033839</td>
      <td>0.000004</td>
      <td>0.136654</td>
      <td>0.868019</td>
      <td>0.966161</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



The DataFrame looks as it should.

Now we can create the text column. We can reuse most of the code from the previous function, but we just need to change the format and column references.

We need to change the string slice which we take from the <code>col</code> variable within the loop to account for the fact that each col is prefixed with <code>pc_</code>:
````python
stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" . . . 
````

The most important thing to do is to make sure that we are formatiing the raw value for x in the <code>lambda</code> function rather than the rounded, integer-ised version. We need to change the <code>lambda</code> to:
````python
.apply(lambda x: "{:.0%}".format(x))
````


```python
def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    stackedAreaData = stackedAreaDF[PCcols + [time]].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))

    for col in PCcols:
        
        ########################################################
        ################## NEW CODE GOES HERE ##################
        ########################################################        
        stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" + str(hover) + stackedAreaData[col + "_o"].apply(lambda x:
            "{:.0%}".format(x))
        
        
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                      'y' : stackedAreaData[col + "_c"],
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle}}
    fig = Figure(data = data, layout = layout)
    #pyo.iplot(fig)

 
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(9)%20-%20Changing%20hovertext%20(2)/pyo.iplot-2.png)   
    return stackedAreaData
    
test = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
test.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pc_United Arab Emirates | ARE_o</th>
      <th>pc_United Kingdom | GBR_o</th>
      <th>pc_United States | USA_o</th>
      <th>pc_China | CHN_o</th>
      <th>pc_India | IND_o</th>
      <th>Year</th>
      <th>pc_United Arab Emirates | ARE_c</th>
      <th>pc_United Kingdom | GBR_c</th>
      <th>pc_United States | USA_c</th>
      <th>pc_China | CHN_c</th>
      <th>pc_India | IND_c</th>
      <th>pc_United Arab Emirates | ARE_t</th>
      <th>pc_United Kingdom | GBR_t</th>
      <th>pc_United States | USA_t</th>
      <th>pc_China | CHN_t</th>
      <th>pc_India | IND_t</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000003</td>
      <td>0.133514</td>
      <td>0.660532</td>
      <td>0.178398</td>
      <td>0.027553</td>
      <td>1960</td>
      <td>0.000003</td>
      <td>0.133517</td>
      <td>0.794049</td>
      <td>0.972447</td>
      <td>1.0</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Proportion of t...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Proportion of total C...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Proportion of total C0...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.000003</td>
      <td>0.141847</td>
      <td>0.693776</td>
      <td>0.132967</td>
      <td>0.031408</td>
      <td>1961</td>
      <td>0.000003</td>
      <td>0.141850</td>
      <td>0.835626</td>
      <td>0.968592</td>
      <td>1.0</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Proportion of t...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Proportion of total C...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Proportion of total C0...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.000004</td>
      <td>0.142484</td>
      <td>0.717318</td>
      <td>0.105743</td>
      <td>0.034451</td>
      <td>1962</td>
      <td>0.000004</td>
      <td>0.142488</td>
      <td>0.859806</td>
      <td>0.965549</td>
      <td>1.0</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Proportion of t...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Proportion of total C...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Proportion of total C0...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.000005</td>
      <td>0.139973</td>
      <td>0.723073</td>
      <td>0.101231</td>
      <td>0.035718</td>
      <td>1963</td>
      <td>0.000005</td>
      <td>0.139978</td>
      <td>0.863051</td>
      <td>0.964282</td>
      <td>1.0</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Proportion of t...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Proportion of total C...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Proportion of total C0...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000004</td>
      <td>0.136649</td>
      <td>0.731366</td>
      <td>0.098142</td>
      <td>0.033839</td>
      <td>1964</td>
      <td>0.000004</td>
      <td>0.136654</td>
      <td>0.868019</td>
      <td>0.966161</td>
      <td>1.0</td>
      <td>&lt;b&gt;United Arab Emirates&lt;/b&gt;&lt;br&gt;Proportion of t...</td>
      <td>&lt;b&gt;United Kingdom&lt;/b&gt;&lt;br&gt;Proportion of total C...</td>
      <td>&lt;b&gt;United States&lt;/b&gt;&lt;br&gt;Proportion of total C0...</td>
      <td>&lt;b&gt;China&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
      <td>&lt;b&gt;India&lt;/b&gt;&lt;br&gt;Proportion of total C02 Emissi...</td>
    </tr>
  </tbody>
</table>
</div>



Now let's add the hovertext to the trace and update the <code>'hovermode'</code> and <code>'hoverinfo'</code> options, update the <code>'tickformat'</code>, plot the chart and return the Figure object for later use:


```python
def createStackedPropArea(df, time, cols, hover, title, yaxisTitle): 
    """
    A function which manipulates the data into the correct format to produce a stacked proportional area plot with Plotly.
    
    Takes five arguments:
    
    df - a pandas DataFrame
    time - the time element of the data, must be a column in the DataFrame
    cols - the name of the columns in the DataFrame which you want to include in the area plot
    hover - the text that you want to include on the hovertext
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
    stackedAreaData = stackedAreaDF[PCcols + [time]].merge(stackedPCAreaDF[PCcols], 
                                        left_index = True,
                                         right_index = True,
                                        suffixes = ('_o','_c'))

    for col in PCcols:       
        stackedAreaData[col + '_t'] = "<b>" + str(col)[3:-6]  + "</b><br>" + str(hover) + stackedAreaData[col + "_o"].apply(lambda x:
            "{:.0%}".format(x))
        
        
        traces.append({'type' : 'scatter',
                      'x' : stackedAreaData[time],
                      'y' : stackedAreaData[col + "_c"],
                       'text' : stackedAreaData[col + "_t"],
                       'hoverinfo' : 'text+x',
                      'name' : col[3:-6],
                      'mode' : 'lines',
                      'fill' : 'tonexty'})
    
    data = Data(traces)
    layout = {'title' : title,
             'xaxis' : {'title' : time},
             'yaxis' : {'title' : yaxisTitle,
                       'tickformat' : '%'},
              'hovermode' : 'closest'}
    fig = Figure(data = data, layout = layout)
    pyo.iplot(fig)

  
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(9)%20-%20Changing%20hovertext%20(2)/pyo.iplot-3.png)  return fig
    
    
C02Prop = createStackedPropArea(emissions, 'Year', ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND',], 'Proportion of total C02 Emissions: ',
                            "Proportion of Co2 Emissions, 1960-2011", 'Proprtion of Co2 Emissions')
```





Let's send this to the Plotly cloud:


```python
py.plot(C02Prop, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = 'overwrite')
```

![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(9)%20-%20Changing%20hovertext%20(2)/py.plot-0.png)



    'https://plot.ly/~rmuir/158'



