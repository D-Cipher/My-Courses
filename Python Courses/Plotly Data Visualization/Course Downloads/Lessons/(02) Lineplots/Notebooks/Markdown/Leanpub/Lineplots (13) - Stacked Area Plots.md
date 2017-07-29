
# Lineplots (13) - Stacked Area Plots

In the last lesson we looked at how to use the <code>'fill'</code> option to fill the space between the trace and the axis.

In this lesson we're going to take this a step further and use this option to create a stacked area plot. A stacked area plot is similar to a multiple line plot, however the spaces between each trace are filled with colour.

We'll also learn how to prepare our data to allow it to be presented as a stacked area plot - the data for this type of chart must be in a specific format to prevent the chart from being misleading, or simply wrong.

# Module Imports



#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame



```python

 
```





### Getting the data

We'll now get the data to create a stacked area chart. This is the same dataset that we used in the previous lesson.


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



## Creating stacked area graphs

Stacked area graphs are great at displaying how the share between different categories and the total of all categories changes over time. One of the most effective and beautiful area charts I've seen is <a href="http://www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE_GRAPHIC.html">this one</a> by the New York Times:

<img src="https://i.kinja-img.com/gawker-media/image/upload/s--K9GtbazJ--/c_fit,fl_progressive,q_80,w_636/18s3l4g96exgapng.png"/>

It shows the box office revenues for films from 1986 to 2008, with the height of each section showing the revenue by week and the color showing the total revenue for a single film. 

I don't think we're quite at the stage to be producing something of this sohpistication, but let's take <a href="https://www.ec.gc.ca/indicateurs-indicators/default.asp?lang=en&n=64B9E95D-1">this</a> example as a starting point and use it to make something much nicer:

<img src="https://www.ec.gc.ca/indicateurs-indicators/64B9E95D-5B44-42A8-98E2-7FBFED3CD6D2/AirPollutantEmissions_VOC_Source_EN.gif"/>

This chart shows, for Canada, how the total emissions of volatile organic compounds have changed between 1990 and 2014. We can see that the overall amount has reduced, and that most of this reduction has come from Off-road vehicles.

We're now going to make a stacked area chart showing how total Co2 emissions have changed for 5 countries. There will be a little bit of data manipulation here; I'll try to keep it to a minimum but it is handy to be able to quickly make a few simple changes to the to try displaying it in a new way.

Doing the data manipulation here also makes it very clear how to construct this stacked area chart, as it is not quite as simple as just entering the data.

#### When making a stacked area chart, the values for each additional trace are cumulative. That is, if Country A has 100Kt emissions, and Country B has 50Kt of emissions, the line for Country B must be drawn at 150Kt of emissions.

The first thing to do is to select the countries we want from the emissions DataFrame. We've also got to select the 'Year' column. I'll create a new DataFrame which contains only these columns using the <code>df.loc[]</code> label-based selection. I want to select all rows, but only those columns in the list.


```python
ColumnSelection = ['United Arab Emirates | ARE','United Kingdom | GBR', 
                   'United States | USA','China | CHN', 'India | IND','Year']

stackedAreaData = emissions.loc[:,(ColumnSelection)]
stackedAreaData.head(5)
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
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.001</td>
      <td>584299.780</td>
      <td>2890696.100</td>
      <td>780726.302</td>
      <td>120581.961</td>
      <td>1960</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.001</td>
      <td>588938.535</td>
      <td>2880505.507</td>
      <td>552066.850</td>
      <td>130402.187</td>
      <td>1961</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.335</td>
      <td>593360.937</td>
      <td>2987207.873</td>
      <td>440359.029</td>
      <td>143467.708</td>
      <td>1962</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22.002</td>
      <td>603822.888</td>
      <td>3119230.874</td>
      <td>436695.696</td>
      <td>154083.673</td>
      <td>1963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>18.335</td>
      <td>608355.300</td>
      <td>3255995.306</td>
      <td>436923.050</td>
      <td>150647.694</td>
      <td>1964</td>
    </tr>
  </tbody>
</table>
</div>



The plan here is to create one trace for each country, and one for the total. The difference between this chart and other we have made so far, is that the y-values of one country need to be the sum of the y-values for that country and for all previous countries.

For example:

- In 1960 the trace for 'United Arab Emirates' will have a y-value of 11.001. 

- The trace for 'United Kingdom' will have a y-value of 11.001 + 584299.78.

- The trace for 'United States' will have a y-value of 11.001 + 584299.78 + 2890696.100, and so on. It might be easier to think of this as a running total for the emissions of each country.

I'll set the <code>'fill'</code> option to <code>'tonexty'</code>; this will fill the area from each trace down to the line of the previous one, or to y = zero if it is the first trace. I'll leave the <code>'fillcolour'</code> to the default, as I think the default colours are quite nice.

As the <code>'tonexty'</code> option for <code>'fill'</code> fills the vertical area between each trace, the <code>'tonextx'</code> option will fill the horizontal area between each trace. We won't use <code>'tonextx'</code> in this course, but if it interests you, then please share any charts you make with it!

This is quite a tedious way of making the traces this chart, however I think it really makes clear the fact that each trace is the cumulative total of itself and all the previous traces. In the next lesson we'll prepare the data in such a way that we can create the traces using a loop.


```python
UnitedArabEmirates = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'UAE Co2 Emissions'
                     }

UnitedKingdom = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'UK Co2 Emissions'
                     }

UnitedStates = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'USA Co2 Emissions'
                     }

China = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'] + stackedAreaData['China | CHN'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'China Co2 Emissions'
                     }

India = {'type' : 'scatter',
                      'x' : stackedAreaData['Year'],
                      'y' : stackedAreaData['United Arab Emirates | ARE'] + stackedAreaData['United Kingdom | GBR']
                            + stackedAreaData['United States | USA'] + stackedAreaData['China | CHN'] 
                             + stackedAreaData['India | IND'],
                      'mode' : 'lines',
                      'fill' : 'tonexty',
                      'name' : 'India Co2 Emissions'
                     }


layout = {'title' : "Co2 emissions in kilotons, 1960-2011",
         'xaxis' : {'title' : 'Year'},
         'yaxis' : {'title' : 'Co2 Emissions (kt)'}}

data = Data([UnitedArabEmirates, UnitedKingdom, UnitedStates, China, India])

fig = Figure(data=data, layout=layout)

pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(13)%20-%20Stacked%20Area%20Plots/pyo.iplot-0.png)```





This chart clearly shows how the total emissions have more than tripled since 1960, with China accounting for the majority of the increase. The UK and UAE's emissions have remained relatively flat. It's quite difficult to see how the proportions of total emissions for each country have changed though. 

In the next lesson we'll make a stacked proportional area chart. This will involve slightly more data manipulation, but it's a really effective and useful chart to create.

I'm pretty happy with this plot; I'll send it to the Plotly cloud:


```python
py.plot(fig, filename="Co2 Emissions for UK, USA, UAE, India & China 1960 - 2011", fileopt = "overwrite")
`
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Lineplots%20(13)%20-%20Stacked%20Area%20Plots/py.plot-0.png)``




    'https://plot.ly/~rmuir/156'



### Stacked Area Charts - What have we learnt?

In this lesson we've learnt how to organise our data into the format required for a stacked area chart; that is, the quantity presented for each trace should be a cumulative total including all previous traces.

We've also learnt how to implement to <code>'tonexty'</code> option for <code>'fill'</code> to actually make a stacked area chart.

In the next lesson, we're going to create a proportional stacked area chart - this will show each country's share of the total emissions as a percentage, and presents a very different view of the data.


I hope you've enjoyed this lesson!

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>