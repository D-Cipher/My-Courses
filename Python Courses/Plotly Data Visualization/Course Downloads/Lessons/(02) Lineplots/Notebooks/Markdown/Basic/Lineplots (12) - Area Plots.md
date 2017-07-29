
# Lineplots (12) - Area Plots

In this lesson I'm going to introduce the <code>'fill'</code> option and how we can use it to create an area plot. An area plot is basically a line chart with the colour filled in between the trace and the axis. 

Although an area plot shows the same information as a line plot, the way the data is presented means that they are particularly suited to presenting a quantity of data, such as the amount of oil, money or pollution. The fact that the chart is filled in with colour really helps the reader understand that we are representing a quantity, rather than just a number.

## What is an area plot?

This <a href="https://conceptdraw.com/a2540c3/p1/preview/640/pict--area-graph-us-incarceration-timeline-clean-area-graph">example</a> shows the power of an area graph (although I do not love everything about it, particularly the font). The upward trend in total numbers of encarcerated people would be evident from the line alone, but adding in the red fill undernear really helps to convey the shock of the message. Of course, this plot doesn't take population growth into account, but the author's message is still clear.

This is another occasion when you have to think about the message that you want to send with your chart - an area plot is another tool for you to use.

<img src="https://conceptdraw.com/a2540c3/p1/preview/640/pict--area-graph-us-incarceration-timeline-clean-area-graph"/>






 






### Creating an area plot

Let's create an area plot which shows how the total Co2 emissions changed for Great Britain between 1960 and 2015.

I downloaded the data from <a href="http://data.worldbank.org/indicator/EN.ATM.CO2E.PC?page=2">The World Bank</a> and have already fiddled it into a usable format, available <a href="http://richard-muir/com/data/public/csv/TotalCo2EmissionsByCountry.csv">here</a> (click to download). I'm going to load it straight from my website into Pandas as a DataFrame.

I'm specifying the <code>index_col</code>, because the index is already contained within the .csv and I don't want to repeat it.


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



I'll get a list of the column names so I can know what column name to pass to the DataFrame to get the data I want. 

When I made this .csv from the data at the World Bank, the country code was contained within a separate column - this didn't fit into the shape of the data that I wanted and so I concatenated the country code to the country name with a <code>'|'</code> separator. This way I can extract the country code from the name at some point in the future.


```python
columnNames = emissions.columns.tolist()
columnNames
```




    ['Year',
     'Afghanistan | AFG',
     'Albania | ALB',
     'Algeria | DZA',
     'American Samoa | ASM',
     'Andorra | AND',
     'Angola | AGO',
     'Antigua and Barbuda | ATG',
     'Arab World | ARB',
     'Argentina | ARG',
     'Armenia | ARM',
     'Aruba | ABW',
     'Australia | AUS',
     'Austria | AUT',
     'Azerbaijan | AZE',
     'Bahamas, The | BHS',
     'Bahrain | BHR',
     'Bangladesh | BGD',
     'Barbados | BRB',
     'Belarus | BLR',
     'Belgium | BEL',
     'Belize | BLZ',
     'Benin | BEN',
     'Bermuda | BMU',
     'Bhutan | BTN',
     'Bolivia | BOL',
     'Bosnia and Herzegovina | BIH',
     'Botswana | BWA',
     'Brazil | BRA',
     'Brunei Darussalam | BRN',
     'Bulgaria | BGR',
     'Burkina Faso | BFA',
     'Burundi | BDI',
     'Cabo Verde | CPV',
     'Cambodia | KHM',
     'Cameroon | CMR',
     'Canada | CAN',
     'Caribbean small states | CSS',
     'Cayman Islands | CYM',
     'Central African Republic | CAF',
     'Central Europe and the Baltics | CEB',
     'Chad | TCD',
     'Channel Islands | CHI',
     'Chile | CHL',
     'China | CHN',
     'Colombia | COL',
     'Comoros | COM',
     'Congo, Dem. Rep. | COD',
     'Congo, Rep. | COG',
     'Costa Rica | CRI',
     "Cote d'Ivoire | CIV",
     'Croatia | HRV',
     'Cuba | CUB',
     'Curacao | CUW',
     'Cyprus | CYP',
     'Czech Republic | CZE',
     'Denmark | DNK',
     'Djibouti | DJI',
     'Dominica | DMA',
     'Dominican Republic | DOM',
     'East Asia & Pacific (all income levels) | EAS',
     'East Asia & Pacific (developing only) | EAP',
     'Ecuador | ECU',
     'Egypt, Arab Rep. | EGY',
     'El Salvador | SLV',
     'Equatorial Guinea | GNQ',
     'Eritrea | ERI',
     'Estonia | EST',
     'Ethiopia | ETH',
     'Euro area | EMU',
     'Europe & Central Asia (all income levels) | ECS',
     'Europe & Central Asia (developing only) | ECA',
     'European Union | EUU',
     'Faroe Islands | FRO',
     'Fiji | FJI',
     'Finland | FIN',
     'Fragile and conflict affected situations | FCS',
     'France | FRA',
     'French Polynesia | PYF',
     'Gabon | GAB',
     'Gambia, The | GMB',
     'Georgia | GEO',
     'Germany | DEU',
     'Ghana | GHA',
     'Greece | GRC',
     'Greenland | GRL',
     'Grenada | GRD',
     'Guam | GUM',
     'Guatemala | GTM',
     'Guinea | GIN',
     'Guinea-Bissau | GNB',
     'Guyana | GUY',
     'Haiti | HTI',
     'Heavily indebted poor countries (HIPC) | HPC',
     'High income | HIC',
     'High income: OECD | OEC',
     'High income: nonOECD | NOC',
     'Honduras | HND',
     'Hong Kong SAR, China | HKG',
     'Hungary | HUN',
     'Iceland | ISL',
     'India | IND',
     'Indonesia | IDN',
     'Iran, Islamic Rep. | IRN',
     'Iraq | IRQ',
     'Ireland | IRL',
     'Isle of Man | IMN',
     'Israel | ISR',
     'Italy | ITA',
     'Jamaica | JAM',
     'Japan | JPN',
     'Jordan | JOR',
     'Kazakhstan | KAZ',
     'Kenya | KEN',
     'Kiribati | KIR',
     'Korea, Dem. People?s Rep. | PRK',
     'Korea, Rep. | KOR',
     'Kosovo | KSV',
     'Kuwait | KWT',
     'Kyrgyz Republic | KGZ',
     'Lao PDR | LAO',
     'Latin America & Caribbean (all income levels) | LCN',
     'Latin America & Caribbean (developing only) | LAC',
     'Latvia | LVA',
     'Least developed countries: UN classification | LDC',
     'Lebanon | LBN',
     'Lesotho | LSO',
     'Liberia | LBR',
     'Libya | LBY',
     'Liechtenstein | LIE',
     'Lithuania | LTU',
     'Low & middle income | LMY',
     'Low income | LIC',
     'Lower middle income | LMC',
     'Luxembourg | LUX',
     'Macao SAR, China | MAC',
     'Macedonia, FYR | MKD',
     'Madagascar | MDG',
     'Malawi | MWI',
     'Malaysia | MYS',
     'Maldives | MDV',
     'Mali | MLI',
     'Malta | MLT',
     'Marshall Islands | MHL',
     'Mauritania | MRT',
     'Mauritius | MUS',
     'Mexico | MEX',
     'Micronesia, Fed. Sts. | FSM',
     'Middle East & North Africa (all income levels) | MEA',
     'Middle East & North Africa (developing only) | MNA',
     'Middle income | MIC',
     'Moldova | MDA',
     'Monaco | MCO',
     'Mongolia | MNG',
     'Montenegro | MNE',
     'Morocco | MAR',
     'Mozambique | MOZ',
     'Myanmar | MMR',
     'Namibia | NAM',
     'Nepal | NPL',
     'Netherlands | NLD',
     'New Caledonia | NCL',
     'New Zealand | NZL',
     'Nicaragua | NIC',
     'Niger | NER',
     'Nigeria | NGA',
     'North America | NAC',
     'Northern Mariana Islands | MNP',
     'Norway | NOR',
     'Not classified | INX',
     'OECD members | OED',
     'Oman | OMN',
     'Other small states | OSS',
     'Pacific island small states | PSS',
     'Pakistan | PAK',
     'Palau | PLW',
     'Panama | PAN',
     'Papua New Guinea | PNG',
     'Paraguay | PRY',
     'Peru | PER',
     'Philippines | PHL',
     'Poland | POL',
     'Portugal | PRT',
     'Puerto Rico | PRI',
     'Qatar | QAT',
     'Romania | ROU',
     'Russian Federation | RUS',
     'Rwanda | RWA',
     'Samoa | WSM',
     'San Marino | SMR',
     'Sao Tome and Principe | STP',
     'Saudi Arabia | SAU',
     'Senegal | SEN',
     'Serbia | SRB',
     'Seychelles | SYC',
     'Sierra Leone | SLE',
     'Singapore | SGP',
     'Sint Maarten (Dutch part) | SXM',
     'Slovak Republic | SVK',
     'Slovenia | SVN',
     'Small states | SST',
     'Solomon Islands | SLB',
     'Somalia | SOM',
     'South Africa | ZAF',
     'South Asia | SAS',
     'South Sudan | SSD',
     'Spain | ESP',
     'Sri Lanka | LKA',
     'St. Kitts and Nevis | KNA',
     'St. Lucia | LCA',
     'St. Martin (French part) | MAF',
     'St. Vincent and the Grenadines | VCT',
     'Sub-Saharan Africa (all income levels) | SSF',
     'Sub-Saharan Africa (developing only) | SSA',
     'Sudan | SDN',
     'Suriname | SUR',
     'Swaziland | SWZ',
     'Sweden | SWE',
     'Switzerland | CHE',
     'Syrian Arab Republic | SYR',
     'Tajikistan | TJK',
     'Tanzania | TZA',
     'Thailand | THA',
     'Timor-Leste | TLS',
     'Togo | TGO',
     'Tonga | TON',
     'Trinidad and Tobago | TTO',
     'Tunisia | TUN',
     'Turkey | TUR',
     'Turkmenistan | TKM',
     'Turks and Caicos Islands | TCA',
     'Tuvalu | TUV',
     'Uganda | UGA',
     'Ukraine | UKR',
     'United Arab Emirates | ARE',
     'United Kingdom | GBR',
     'United States | USA',
     'Upper middle income | UMC',
     'Uruguay | URY',
     'Uzbekistan | UZB',
     'Vanuatu | VUT',
     'Venezuela, RB | VEN',
     'Vietnam | VNM',
     'Virgin Islands (U.S.) | VIR',
     'West Bank and Gaza | PSE',
     'World | WLD',
     'Yemen, Rep. | YEM',
     'Zambia | ZMB',
     'Zimbabwe | ZWE']



The column for the UK is called <code>'United Kingdom | GBR'</code>.

I'll now start making the line chart. We'll see what it looks like without adding the area fill and then look at how that changes the presentation of the data.

First I'll create the trace. I'll put the year on the x-axis and the total emissions on the y-axis:


```python
UKEmissions = {'type' : 'scatter',
              'x' : emissions['Year'],
              'y' : emissions['United Kingdom | GBR'],
              'mode' : 'lines',
              'name' : 'UK Co2 Emissions'}

layout = {'title' : "Co2 emissions in kilotons for the UK, 1960-2015",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Co2 Emissions (kt)'}}

data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/pyo.iplot-0.png)```





Let's send this line plot to the Plotly cloud:


```python
py.plot(fig, filename="UK CO2 emissions in Kt, 1960-2015", fileopt="overwrite")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/py.plot-0.png)``




    'https://plot.ly/~rmuir/154'



So this chart shows quite a clear message; despite a few peaks, the total Co2 emissions for the UK has been steadily decreasing from its peak in the 1970's. 

Let's see what this looks like as an area graph.

The <code>'fill'</code> option is contained within the trace object. The possible values are:
<code>
    "none" - No fill
    "tozeroy" - Fills to y = 0 (vertical fill)
    "tozerox" - Fills to x = 0 (horizontal fill)
    "tonexty" - Fills between traces (vertically, to the trace before or to 0 if there is no previous trace)
    "tonextx" - Fills between traces (horizontally, to the trace before or to 0 if there is no previous trace)
    "toself"  - Connects the endpoints of a trace into a closed shape (useful for <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Synthetic_data_2D_KDE.png/500px-Synthetic_data_2D_KDE.png">Kernel Density Plots</a>)
    "tonext"  - Fills the space between two plots if one completely encloses the other (useful for Kernel Density Plots again)
</code>

We won't be looking at Kernel Density Plots in this course and therefore I won't go into any more detail about <code>'toself'</code> and <code>'tonext'</code>.

First of all, look at the effect of <code>'tozeroy'</code> and <code>'tozerox'</code>. 

In the next lesson however, we'll use <code>'tonexty'</code> and <code>'tonextx'</code> to make stacked area graphs.


```python
UKEmissions.update({'fill' : 'tozeroy'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)
``
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/pyo.iplot-1.png)`





You can see how the <code>fill</code> option has filled the area between the trace and the x-axis. This has had the effect of completely changing the message of the chart. In the its first incarnation it seemed like very good news; despite a couple of blips, Co2 has fallen dramatically in the last 40 years. However the chart now sends the message that we still have an awful lot of emissions, and whilst they have fallen, the fall is not a large proportion of the total.

You'll also notice how the colour under the trace is a much lighter shade (it's actually half-transparent) - this is one of the many things that Plotly does to help us out with the design of our charts, and another option which we can change:


```python
UKEmissions.update({'fillcolor' : 'rgba(89, 100, 212, 0.46)'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)
```
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/pyo.iplot-2.png)





Let's try changing the <code>'fill'</code> option to <code>'tozerox'</code>. The <code>'tozeroy'</code> option filled the chart down to the y=0 line. The <code>'tozerox'</code> option is going to do the same, but to x=0. Let's see how this affects the chart.


```python
UKEmissions.update({'fill' : 'tozerox'})
data = Data([UKEmissions])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)
```

![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/pyo.iplot-3.png)




This has produced a strange chart. By setting <code>'fill'</code> to <code>'tozerox'</code>, we have asked Plotly to fill in the area back to the year 0. Because the trace doesn't go back that far, Plotly has copied the y-value for the smallest value of year. 

The only reason this chart looks wrong is because we chose the wrong value for <code>'fill'</code> to fit our data. If you transpose the x- and y-values and keep the same <code>'fill'</code> option then the chart will make sense again.

Here's the chart with the x- and y-values switched:


```python
UKEmissions.update({'x' : emissions['United Kingdom | GBR'],
                   'y' : emissions['Year']})
data = Data([UKEmissions])

layout = {'title' : "Co2 emissions in kilotons for the UK, 1960-2015",
         'xaxis' : {'title' : 'Co2 Emissions (kt)'},
         'yaxis' : {'title' : 'Year'}}

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)
```


![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(12)%20-%20Area%20Plots/pyo.iplot-4.png)



Whilst this chart now makes sense, it doesn't necessarily display the data well - it's easier for us to understand time on a horizontal scale rather than a vertical, and easier for us to grasp a magnitude on a vertical scale than a horizontal. I much prefer the first version of this area chart and as such I won't push this to my Plotly cloud, but feel free to do it if you wish!

### Area charts - what have we learnt?

In this lesson we've seen how to create an area chart and how to implement the <code>'tozerox'</code> and <code>'tozeroy'</code> options for <code>'fill'</code>.

We've also found out how to change the <code>'fillcolor'</code> to have finer control over the style of our chart.

I hope you've enjoyed this lesson!

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>