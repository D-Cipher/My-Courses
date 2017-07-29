
# Scatterplots (04) - Plotting different traces

In this lesson we're going to plot the famous <a href="https://en.wikipedia.org/wiki/Iris_flower_data_set">Iris flower dataset</a> which is often used as a test case for machine learning models. This dataset contains 50 samples from each of 3 species of the Iris flower (<i>setosa, virginica</i> and <i>versicolor</i>), and each flower had four measurements taken from it; the length and the width of the <a href="https://en.wikipedia.org/wiki/Sepal">sepals</a> and the <a href="https://en.wikipedia.org/wiki/Petal">petals</a>.

We're going to create a scatterplot from this dataset, and in doing so apply the marker styling options that we learnt in the previous lesson. 

We're also going to find out how to use Pandas to get a dataset straight from table in a webpage - this is a really useful tool which will allow you access many different data sources. 

Finally, we'll learn how to use the Python functions <code>dict()</code> and <code>zip()</code> to create a lookup dictionary which we'll use to style the marker symbols and colours for each species.






 






## Getting the data

We're going to use the Pandas <code>read_html()</code> function to get the Iris dataset from Wikipedia. This function takes a url as an argument, and returns a list of objects from the webpage which could contain data. This particular functionality relies on a few different Python libraries (lxml, html5lilb and BeautifulSoup4), all of which are included in the Anaconda distribution which we downloaded. However if you're having trouble using this function for whatever reason, you can download the .csv from my website by passing this url: http://www.richard-muir.com/data/public/csv/irisDataset.csv to the <code>pd.read_csv()</code> function.

We're going to set <code>header = 0</code> to make sure that the table headings are set as the column titles:


```python
url = "https://en.wikipedia.org/wiki/Iris_flower_data_set"
returnObject = pd.read_html(url, header=0)
```

<code>pd.read_html()</code> returns a list. Let's have a look at the first item in that list:


```python
returnObject[0]  #it works!
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal length</th>
      <th>Sepal width</th>
      <th>Petal length</th>
      <th>Petal width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.7</td>
      <td>0.4</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.6</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>2.9</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.4</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.8</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.1</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.3</td>
      <td>3.0</td>
      <td>1.1</td>
      <td>0.1</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5.8</td>
      <td>4.0</td>
      <td>1.2</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5.7</td>
      <td>4.4</td>
      <td>1.5</td>
      <td>0.4</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>16</th>
      <td>5.4</td>
      <td>3.9</td>
      <td>1.3</td>
      <td>0.4</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.3</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>18</th>
      <td>5.7</td>
      <td>3.8</td>
      <td>1.7</td>
      <td>0.3</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>19</th>
      <td>5.1</td>
      <td>3.8</td>
      <td>1.5</td>
      <td>0.3</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>20</th>
      <td>5.4</td>
      <td>3.4</td>
      <td>1.7</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>21</th>
      <td>5.1</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.4</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>22</th>
      <td>4.6</td>
      <td>3.6</td>
      <td>1.0</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>23</th>
      <td>5.1</td>
      <td>3.3</td>
      <td>1.7</td>
      <td>0.5</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>24</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.9</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>25</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>26</th>
      <td>5.0</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>0.4</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>27</th>
      <td>5.2</td>
      <td>3.5</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>28</th>
      <td>5.2</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>29</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>I. setosa</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>120</th>
      <td>6.9</td>
      <td>3.2</td>
      <td>5.7</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>121</th>
      <td>5.6</td>
      <td>2.8</td>
      <td>4.9</td>
      <td>2.0</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>122</th>
      <td>7.7</td>
      <td>2.8</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>123</th>
      <td>6.3</td>
      <td>2.7</td>
      <td>4.9</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>124</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.1</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7.2</td>
      <td>3.2</td>
      <td>6.0</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>126</th>
      <td>6.2</td>
      <td>2.8</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>127</th>
      <td>6.1</td>
      <td>3.0</td>
      <td>4.9</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>128</th>
      <td>6.4</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>2.1</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>129</th>
      <td>7.2</td>
      <td>3.0</td>
      <td>5.8</td>
      <td>1.6</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>130</th>
      <td>7.4</td>
      <td>2.8</td>
      <td>6.1</td>
      <td>1.9</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>131</th>
      <td>7.9</td>
      <td>3.8</td>
      <td>6.4</td>
      <td>2.0</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>132</th>
      <td>6.4</td>
      <td>2.8</td>
      <td>5.6</td>
      <td>2.2</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>133</th>
      <td>6.3</td>
      <td>2.8</td>
      <td>5.1</td>
      <td>1.5</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>134</th>
      <td>6.1</td>
      <td>2.6</td>
      <td>5.6</td>
      <td>1.4</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>135</th>
      <td>7.7</td>
      <td>3.0</td>
      <td>6.1</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>136</th>
      <td>6.3</td>
      <td>3.4</td>
      <td>5.6</td>
      <td>2.4</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>137</th>
      <td>6.4</td>
      <td>3.1</td>
      <td>5.5</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>138</th>
      <td>6.0</td>
      <td>3.0</td>
      <td>4.8</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>139</th>
      <td>6.9</td>
      <td>3.1</td>
      <td>5.4</td>
      <td>2.1</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>140</th>
      <td>6.7</td>
      <td>3.1</td>
      <td>5.6</td>
      <td>2.4</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>141</th>
      <td>6.9</td>
      <td>3.1</td>
      <td>5.1</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>142</th>
      <td>5.8</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.9</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>143</th>
      <td>6.8</td>
      <td>3.2</td>
      <td>5.9</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>144</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.5</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>I. virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>I. virginica</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 5 columns</p>
</div>



I'll now create a new object called <code>iris</code> and set it to the output of <code>pd.read_html()</code>:


```python
iris = returnObject[0]
```

### Preparing the data for plotting 
Because we have the three different data traces contained within the same DataFrame, we need to find a way of splitting them so we can plot them separately in Plotly. 

I'm going to use <code>pd.Series.unique()</code> to get the unique items in the Species column:


```python
irisSpeciesUnique = list(iris['Species'].unique())
irisSpeciesUnique
```




    ['I.\xa0setosa', 'I.\xa0versicolor', 'I.\xa0virginica']



Those strange characters ("\xa0") have snuck in as a consequence of reading the HTML and converting the output to a string. We don't have to worry about them affecting the way the chart is displayed because Plotly also displays HTML.

### Plotting the data
We can now use the <code>irisSpecies</code> list to select each species in turn from the DataFrame by using <code>df.loc[]</code>. We're going to create the traces directly from this loop, only plotting the Sepal length and Sepal width for each species.

The x-values are set using this code which tells pandas to select only the rows where the Species column is equal to the current value of sp in the loop, and then to take only the 'Sepal length' column:
````python
iris.loc[iris['Species'] == species,'Sepal length']
````

The y-values are set in the same way, but we only want the 'Sepal width' column:


```python
traces = []
for sp in irisSpeciesUnique:
    traces.append({'type' : 'scatter',
                  'mode' : 'markers',
                  'x' : iris.loc[iris['Species'] == sp,'Sepal length'],
                  'y' : iris.loc[iris['Species'] == sp,'Sepal width'],
                  'name' : sp})
```

Now I'll create the layout and Figure object and plot the data. 

I want to set the range for each axis so that the chart doesn't resize when we show and hide the different traces:


```python
layout = {'title' : "Sepal length and width for Iris setosa, versicolor and virginica",
         'xaxis' : {'title' : 'Sepal length (cm)',
                   'range' : [iris['Sepal length'].min() * 0.95, iris['Sepal length'].max() * 1.05]},
         'yaxis' : {'title' : 'Sepal width (cm)',
                   'range' : [iris['Sepal width'].min() * 0.95, iris['Sepal width'].max() * 1.05]}}

fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(04)%20-%20Plotting%20different%20traces/pyo.iplot-0.png)```





So that plot has come out looking OK. It's great that Plotly's default colour system looks so good! 

It's now time to apply our own styling to the traces. First we need to create a lookup dictionary which contains the marker symbol information which we want to attach to each trace.

We'll first create a list of dictionaries which contain the marker symbols and colours:


```python
symbolsAndColours = [{'color' : "#663399", 'symbol' : 'circle'},
                    {'color' : '#FF6347', 'symbol' : 'square'}, 
                    {'color' : '#2E8B57', 'symbol' : 'diamond'}]
```

We'll now take our list of species and <code>zip()</code> the two lists together, then turn the resulting output into a dictionary. You can see how <code>zip()</code> combines the two lists into one object:


```python
markerSymbolInfo = dict(zip(irisSpeciesUnique, symbolsAndColours))
markerSymbolInfo
```




    {'I.\xa0setosa': {'color': '#663399', 'symbol': 'circle'},
     'I.\xa0versicolor': {'color': '#FF6347', 'symbol': 'square'},
     'I.\xa0virginica': {'color': '#2E8B57', 'symbol': 'diamond'}}



We can now copy our previous loop and add in the marker styling options. It is only the colour and symbol which will change for each species.

For each trace I will set the marker size to 8, the opacity to 0.7 and the marker line to width = 1.25 and color = black.


```python
traces = []
for sp in irisSpeciesUnique:
    traces.append({'type' : 'scatter',
                  'mode' : 'markers',
                  'x' : iris.loc[iris['Species'] == sp,'Sepal length'],
                  'y' : iris.loc[iris['Species'] == sp,'Sepal width'],
                  'name' : sp,
                  
                  'marker' : {'color' : markerSymbolInfo[sp]['color'],
                             'symbol' : markerSymbolInfo[sp]['symbol'],
                             'size' : 8,
                             'opacity' : 0.7,
                             'line' : {'width' : 1.25,
                                      'color' : 'black'}}})
```

Let's refresh the Figure object and replot the chart:


```python
fig = Figure(data = traces, layout = layout)
pyo.iplot(fig)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(04)%20-%20Plotting%20different%20traces/pyo.iplot-1.png)``





In my opinion this is a great improvement on the chart. By changing the marker opacity we have made clear that there is some overplotting within the species groups (look at the darker purple dots), and by changing the marker symbol we have made clear that there is overplotting between the species groups.

Let's send this chart to the Plotly cloud:


```python
py.plot(fig, filename="Iris dataset", fileopt = "overwrite")
``
![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Scatterplots%20(04)%20-%20Plotting%20different%20traces/py.plot-0.png)`




    'https://plot.ly/~rmuir/204'



