
# Chart presentation (2) -  Setting the tickformat

In the last lesson we learnt how to use the <code>plotly.get_figure()</code> function to retrieve a chart from the Plotly cloud and the <code>plotly.plot()</code> function with <code>fileopt = 'overwrite')</code> to push it back to the Plotly cloud and overwrite the original.

In this lesson we'll use this knowledge to update the format which we apply to the ticklabels.

Applying a format to a number does not change the value of that number, merely how it's displayed. We'll learn how to format a number as a currency and a percentage with differing levels of decimal precision. We'll also learn how apply datetime formats to the ticklabels.






 






## Getting a chart:

We'll get the same chart as in the last lesson; there's still a few tweaks that we need to make to it before it's ready to be published:


```python
stocks = py.get_figure("https://plot.ly/~rmuir/162/stock-closing-prices-for-apple-in-2012/")
```

Let's just confirm that we've got the right chart:


```python
pyo.iplot(stocks)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-0.png)```





First of all let's format the ticks on the y-axis to show the dollar amount rather than just a number. We can then remove the dollar sign from the axis label.

## Changing the tickformat

Now we'll change the <code>'tickformat'</code> for the y-axis. We can specify the <a href="https://docs.python.org/3/library/string.html#format-string-syntax">Python</a> or <a href="https://github.com/d3/d3-format/blob/master/README.md#format">D3</a> number formats.

The string formatting language can be quite dense and difficult to interpret, but there are some great resources which can really help you. <a href="https://mkaz.tech/python-string-format.html">Marcus Kazmierczak</a> has some nice examples for the Python number formats, and <a href="http://bl.ocks.org/zanarmstrong/05c1e95bf7aa16c4768e">this</a> bl.ock by Zan has some examples in D3.

This said, there are some occasions when you won't be able to format the ticks exactly as you wish - I've had difficulty applying a '£' format for example. We'll learn how to work around this problem in the next lesson.

The <code>'tickformat'</code> option is contained within each of the x- and y-axis objects within the layout:
````python
layout = {'xaxis' : {'tickformat' : <format string>},
          'yaxis' : {'tickformat' : <format string>}}
````
To change the tick format, we can pass different format string as the value for this option.

Here are some common string format values we can pass:
- Percentage with 2 decimal places: <code>".2%"</code>
- Percentage with 0 decimal places: <code>".0%"</code>
- Currency with 2 decimal places: <code>"&#36;.2f"</code>
- Currency with 0 decimal places: <code>"&#36;.0"</code>
- Currency with 0 decimal places and thousand separator: <code>"&#36;,"</code>

Let's apply each of these to the chart to see what happens:

Here, applying the 2 decimal place percentage format has mulitplied the number by 100, and added a decimal point, two 0s and a percentage (%) sign to the number. This isn't what we need for this chart, but we will update the stacked area charts with a similar format later in the lesson.


```python
stocks['layout']['yaxis'].update({'tickformat' : '.2%'})
pyo.iplot(stocks)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-1.png)``





This is the same format but without the decimal places:


```python
stocks['layout']['yaxis'].update({'tickformat' : '.0%'})
pyo.iplot(stocks)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-2.png)`





This format gives us the dollar amount and two decimal places:


```python
stocks['layout']['yaxis'].update({'tickformat' : '$.2f'})
pyo.iplot(stocks)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-3.png)





This gives us the dollar amount with 0 decimal places:


```python
stocks['layout']['yaxis'].update({'tickformat' : '$.0'})
pyo.iplot(stocks)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-4.png)




And this format gives us the dollar amount, but with a ',' separating each thousand. I've had to update the range on this chart to show this in action:


```python
stocks['layout']['yaxis'].update({'range' : [0, 1500], 'tickformat' : '$,'})
pyo.iplot(stocks)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-5.png)



Let's change the tickformat to something sensible and update the y-axis title then update our chart.


```python
stocks['layout'].update({'yaxis' : {'range' : [0, max(stocks['data'][0]['y']) * 1.05],
                                    'title' : 'Closing Price', 'tickformat' : "$.0"}})
pyo.iplot(stocks)
```



![pyo.iplot-6](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-6.png)


## Datetime

Datetime formats work in the same way as number formats; they themselves a form of number format.

Plotly has a builtin datetime formatter which chooses what it thinks are is the most suitable datetime format to use based on your data. Obviously we can change that! Let's find out how . . .

A datetime object is made of two parts; a date and a time. Plotly does not recognise a time without a date. 

- A date object:  31/12/95 - 31st December 1995
- A time object:  12:35:59.99 - Almost 12:36pm (This is not valid on its own)
- A datetime object:  31/12/95 12:35:59.99 - Almost 12:36pm on 31st December 1995


### Common date formats:

Here we'll implement a few different date formats to give you some easy ones to work with. You can see the <a href="https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">Python documentation</a> to find out how to build your own datetime formats.

- UK date: <code>"%d/%m/%y"</code>
- UK date with 4 digit year:  <code>"%d/%m/%Y"</code>
- American date with hyphens: <code>"%m-%d-%Y"</code>
- Abbreviated weekday and month names: <code>"%a %d %b %Y"</code>
- Unabbreviated weekday and month names: <code>"%A %d %B %Y"</code>

### Common time formats:

We don't have any time data stored in this chart, but the datetime objects have a default time of 00:00:00.00:
- 24 hour clock with microseconds: <code>"%H:%M:%S.%f"</code>
- 12 hour clock: <code>"%H%p %M:%S"</code>

If you have date and time data that you need to display, you can combined these formats:
- American date with hyphens and 24 hour clock: <code>"%m-%d-%Y %H:%M:%S"</code>

Let's try a few of these out. I'm going to write a function to make this a little easier:


```python
def updateDT(dt):
    stocks['layout'].update({'xaxis' : {'tickformat' : dt}})
    pyo.iplot(stocks)
```

UK
![pyo.iplot-7](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-7.png) date with a two digit year:


```python
updateDT("%d/%m/%y")
```





American date with hyphens:


```python
updateDT("%m-%d-%Y")
```





Abbreviated weekday and month names:


```python
updateDT("%a %d %b %Y")
```





I think that after all of that, I actually prefer the default datetime format for this use case! It seems that adding the day of the month gives a bit too much accuracy for the level of data we're showing:


```python
updateDT("%b %Y")
```





Let's push this fully updated chart to the cloud. Don't forget to overwrite it and remember to spell the filename correctly!


```python
py.plot(stocks, filename="Stock closing prices for Apple in 2012 (Savitzy-Golay Smoothing)", fileopt = 'overwrite')
```





![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/py.plot-0.png)    'https://plot.ly/~rmuir/162'



### Review and practice

It's time for you to practise what we've learnt; get the stacked proportional area plots that we previously created and set the y-axis format to a percentage format.


```python
stackedArea = py.get_figure('rmuir', 168)
stackedArea
```




    {'data': [{'fill': 'tonexty',
       'mode': 'lines',
       'name': 'United Arab Emirates',
       'type': 'scatter',
       'x': [1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011],
       'xsrc': 'rmuir:169:b02e8b',
       'y': [2.5137586389505222e-06,
        2.649614922631244e-06,
        4.4027804439059355e-06,
        5.100310353885034e-06,
        4.118429560440012e-06,
        4.726013316330187e-06,
        5.26541054029882e-06,
        0.00018729762491627794,
        0.00024394701960067528,
        0.003771380364294993,
        0.0025565807976064797,
        0.0034607341165363422,
        0.0036725588766425596,
        0.004603489790260972,
        0.00484383823859603,
        0.0048254703737304885,
        0.005907832782052164,
        0.005531498739632035,
        0.006121380754290752,
        0.0049402400690436036,
        0.0051577590602874595,
        0.005295699845359874,
        0.0053664160026471825,
        0.005032892916038731,
        0.0063442174203224575,
        0.006604558430817068,
        0.006129346775609568,
        0.005903180755067927,
        0.005698931374755937,
        0.006289893881587107,
        0.006059692003752967,
        0.006501712936012473,
        0.006456002954759521,
        0.007066192785752153,
        0.00758511046960517,
        0.007073337036945923,
        0.003979320469813565,
        0.003982472492290687,
        0.007820656964744755,
        0.007406339588276407,
        0.010281502004986676,
        0.009269988412514486,
        0.00757533769923427,
        0.008806841624659155,
        0.008675763936961152,
        0.008505969002115615,
        0.00866988899123515,
        0.009377634036943675,
        0.010503640116431378,
        0.01044463544707925,
        0.010296794327481044,
        0.010482925751344907],
       'ysrc': 'rmuir:169:02f16e'},
      {'fill': 'tonexty',
       'mode': 'lines',
       'name': 'United Kingdom',
       'type': 'scatter',
       'x': [1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011],
       'xsrc': 'rmuir:169:b02e8b',
       'y': [0.13351661426876435,
        0.1418497844979863,
        0.1424880640622166,
        0.13997801766237475,
        0.13665361124496006,
        0.13374302617660008,
        0.12688962420764974,
        0.1212422477513047,
        0.11935485728019941,
        0.11932574699879786,
        0.11205792457041387,
        0.11142162069227861,
        0.10521571115634498,
        0.10380089644876007,
        0.10033883620875396,
        0.09857559495435651,
        0.09514271571266067,
        0.09177832167100736,
        0.08877229275036377,
        0.0919692272975605,
        0.08611879143209299,
        0.08587558714511144,
        0.08519979292198818,
        0.08274821645094889,
        0.07872756620636158,
        0.08066584038943367,
        0.07993608463171338,
        0.07668597629196192,
        0.07291391675585199,
        0.07344178133655271,
        0.07082913915886364,
        0.07114204655706552,
        0.06822049444984911,
        0.0654933532310955,
        0.06427889534198225,
        0.06094070535828046,
        0.05739219993482117,
        0.054379667754421324,
        0.05886043765978523,
        0.057573175418285084,
        0.05976977152664362,
        0.05916589545252366,
        0.05471434329309268,
        0.05319621308228273,
        0.04998095214549638,
        0.048234596526393635,
        0.046560134730911605,
        0.044917475784435786,
        0.04496920908137619,
        0.04084271262789921,
        0.04053608034671701,
        0.03680923457175139],
       'ysrc': 'rmuir:169:66be97'},
      {'fill': 'tonexty',
       'mode': 'lines',
       'name': 'United States',
       'type': 'scatter',
       'x': [1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011],
       'xsrc': 'rmuir:169:b02e8b',
       'y': [0.79404859263033,
        0.8356258390447255,
        0.8598057845490584,
        0.8630507166361073,
        0.8680191589343151,
        0.8621106848072061,
        0.8575277693990888,
        0.8762981598382946,
        0.8712154030594842,
        0.8588848789007539,
        0.8378999883791781,
        0.8231587031442539,
        0.8200176278232509,
        0.8207196169949403,
        0.8113613323021585,
        0.7829102148140176,
        0.7824706793816472,
        0.7681069377765226,
        0.7568347738104482,
        0.7534714799243054,
        0.7462294393038256,
        0.737589668880453,
        0.712016929161174,
        0.7010457430331667,
        0.6906827956477024,
        0.6749698635187282,
        0.6632846846272404,
        0.6569873444264961,
        0.6493761636038331,
        0.6454386099330289,
        0.6328325674158359,
        0.621103237850533,
        0.6135927082268634,
        0.6044974178726412,
        0.5930903724664636,
        0.5754128836516103,
        0.5672388590932466,
        0.5683945905420749,
        0.5781159550340378,
        0.5783033373056975,
        0.5805782909448023,
        0.5711728700663106,
        0.5598971152455515,
        0.5213280871930519,
        0.49153971842888344,
        0.4726347557212671,
        0.4457687292161734,
        0.4347370594397841,
        0.41654438431370455,
        0.3796229972302001,
        0.3728460574727119,
        0.34842218754213267],
       'ysrc': 'rmuir:169:9f252f'},
      {'fill': 'tonexty',
       'mode': 'lines',
       'name': 'China',
       'type': 'scatter',
       'x': [1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011],
       'xsrc': 'rmuir:169:b02e8b',
       'y': [0.9724466915584633,
        0.9685923479121035,
        0.9655491235825249,
        0.9642816765400175,
        0.9661613353596006,
        0.9643493185482631,
        0.9647661292688376,
        0.9648105222307296,
        0.9632374000284964,
        0.9649538566861983,
        0.9672797008837357,
        0.9663685175633603,
        0.9658881523227671,
        0.9662831435558034,
        0.9641290616686435,
        0.9608312816683953,
        0.9606973133101893,
        0.9549787149476503,
        0.9565582823468717,
        0.9552043001813186,
        0.9512826491939721,
        0.9461446662328664,
        0.9420128196233102,
        0.9384360956280987,
        0.9388604377469905,
        0.9351181568358271,
        0.9317620646681535,
        0.9304930649200104,
        0.9285628798657489,
        0.9234718995107014,
        0.9195393557406214,
        0.915852854781835,
        0.9129783414009617,
        0.9127924283778741,
        0.9102897045903173,
        0.9078751459077712,
        0.9028682595084152,
        0.9001716842944638,
        0.8971346427584849,
        0.89185628381462,
        0.89160946905702,
        0.8899604510437956,
        0.8902843563816129,
        0.8943333161041331,
        0.8966847743025899,
        0.8966581429735389,
        0.8947109339770797,
        0.8916160014761092,
        0.8814999785526245,
        0.8737268966439937,
        0.8801375549348982,
        0.8781671366857389],
       'ysrc': 'rmuir:169:254efa'},
      {'fill': 'tonexty',
       'mode': 'lines',
       'name': 'India',
       'type': 'scatter',
       'x': [1960,
        1961,
        1962,
        1963,
        1964,
        1965,
        1966,
        1967,
        1968,
        1969,
        1970,
        1971,
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1984,
        1985,
        1986,
        1987,
        1988,
        1989,
        1990,
        1991,
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011],
       'xsrc': 'rmuir:169:b02e8b',
       'y': [1.0,
        1.0,
        1.0,
        1.0,
        0.9999999999999999,
        0.9999999999999999,
        1.0,
        0.9999999999999999,
        1.0,
        0.9999999999999998,
        0.9999999999999999,
        0.9999999999999999,
        1.0,
        1.0000000000000002,
        1.0,
        1.0000000000000002,
        0.9999999999999999,
        1.0,
        1.0000000000000002,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0000000000000002,
        1.0,
        1.0,
        1.0,
        1.0000000000000002,
        1.0,
        1.0,
        1.0,
        1.0000000000000002,
        1.0,
        0.9999999999999999,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.9999999999999999,
        1.0000000000000002,
        1.0000000000000002,
        1.0,
        0.9999999999999999,
        0.9999999999999998,
        0.9999999999999999,
        1.0,
        1.0000000000000002,
        1.0,
        1.0,
        1.0,
        1.0],
       'ysrc': 'rmuir:169:68c0c0'}],
     'layout': {'title': 'Proportion of C02 Emissions, 1960 - 2011',
      'xaxis': {'title': 'Year'},
      'yaxis': {'title': 'Proportion of C02 Emissions'}}}




```python
stackedArea['layout']['yaxis'].update({'tickformat' : ".0%", 'title' : 'Percentage of C02 Emissions'})
stackedArea['layout'].update({'title' : 'C02 Emissions, 1960 - 2011'})
pyo.iplot(stackedArea)
```






![pyo.iplot-8](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/pyo.iplot-8.png)
```python
py.plot(stackedArea, filename="Proportion of total Co2 Emissions 1960 - 2011", fileopt = 'overwrite')
```




  
![py.plot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Chart%20presentation%20(2)%20-%20%20Setting%20the%20tickformat/py.plot-1.png)  'https://plot.ly/~rmuir/158'



