
# Intro to Pandas (2) - Useful DataFrame Functions

In the last lesson we saw how to read data into a Pandas DataFrame from a .csv file on the internet or on your local machine and we also saw how to account for escape characters when reading a .csv file from a different folder in your local machine.

In this lesson we're going to look at some useful DataFrame functions and methods. Whilst we won't use these directly to plot data, utilising these will make your life a lot easier!



## Using DataFrames

Before we can learn about some useful DataFrame functions, we first need to create one. This time I'm going to assign the DataFrame to an object, rather than just display it.

We can see the DataFrame by typing the object name on its own line:



baseRateData = pd.read_csv("http://www.richard-muir.com/data/public/csv/BoEBaseRate.csv")

baseRateData





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
      <td>11.50</td>
      <td>02/01/1975</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.50</td>
      <td>03/01/1975</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.50</td>
      <td>06/01/1975</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.50</td>
      <td>07/01/1975</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11.50</td>
      <td>08/01/1975</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.50</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11.50</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11.50</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11.50</td>
      <td>14/01/1975</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11.50</td>
      <td>15/01/1975</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11.50</td>
      <td>16/01/1975</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11.50</td>
      <td>17/01/1975</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11.25</td>
      <td>20/01/1975</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11.25</td>
      <td>21/01/1975</td>
    </tr>
    <tr>
      <th>14</th>
      <td>11.25</td>
      <td>22/01/1975</td>
    </tr>
    <tr>
      <th>15</th>
      <td>11.25</td>
      <td>23/01/1975</td>
    </tr>
    <tr>
      <th>16</th>
      <td>11.25</td>
      <td>24/01/1975</td>
    </tr>
    <tr>
      <th>17</th>
      <td>11.00</td>
      <td>27/01/1975</td>
    </tr>
    <tr>
      <th>18</th>
      <td>11.00</td>
      <td>28/01/1975</td>
    </tr>
    <tr>
      <th>19</th>
      <td>11.00</td>
      <td>29/01/1975</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11.00</td>
      <td>30/01/1975</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11.00</td>
      <td>31/01/1975</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11.00</td>
      <td>03/02/1975</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11.00</td>
      <td>04/02/1975</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11.00</td>
      <td>05/02/1975</td>
    </tr>
    <tr>
      <th>25</th>
      <td>11.00</td>
      <td>06/02/1975</td>
    </tr>
    <tr>
      <th>26</th>
      <td>11.00</td>
      <td>07/02/1975</td>
    </tr>
    <tr>
      <th>27</th>
      <td>10.75</td>
      <td>10/02/1975</td>
    </tr>
    <tr>
      <th>28</th>
      <td>10.75</td>
      <td>11/02/1975</td>
    </tr>
    <tr>
      <th>29</th>
      <td>10.75</td>
      <td>12/02/1975</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10456</th>
      <td>0.50</td>
      <td>12/05/2016</td>
    </tr>
    <tr>
      <th>10457</th>
      <td>0.50</td>
      <td>13/05/2016</td>
    </tr>
    <tr>
      <th>10458</th>
      <td>0.50</td>
      <td>16/05/2016</td>
    </tr>
    <tr>
      <th>10459</th>
      <td>0.50</td>
      <td>17/05/2016</td>
    </tr>
    <tr>
      <th>10460</th>
      <td>0.50</td>
      <td>18/05/2016</td>
    </tr>
    <tr>
      <th>10461</th>
      <td>0.50</td>
      <td>19/05/2016</td>
    </tr>
    <tr>
      <th>10462</th>
      <td>0.50</td>
      <td>20/05/2016</td>
    </tr>
    <tr>
      <th>10463</th>
      <td>0.50</td>
      <td>23/05/2016</td>
    </tr>
    <tr>
      <th>10464</th>
      <td>0.50</td>
      <td>24/05/2016</td>
    </tr>
    <tr>
      <th>10465</th>
      <td>0.50</td>
      <td>25/05/2016</td>
    </tr>
    <tr>
      <th>10466</th>
      <td>0.50</td>
      <td>26/05/2016</td>
    </tr>
    <tr>
      <th>10467</th>
      <td>0.50</td>
      <td>27/05/2016</td>
    </tr>
    <tr>
      <th>10468</th>
      <td>0.50</td>
      <td>31/05/2016</td>
    </tr>
    <tr>
      <th>10469</th>
      <td>0.50</td>
      <td>01/06/2016</td>
    </tr>
    <tr>
      <th>10470</th>
      <td>0.50</td>
      <td>02/06/2016</td>
    </tr>
    <tr>
      <th>10471</th>
      <td>0.50</td>
      <td>03/06/2016</td>
    </tr>
    <tr>
      <th>10472</th>
      <td>0.50</td>
      <td>06/06/2016</td>
    </tr>
    <tr>
      <th>10473</th>
      <td>0.50</td>
      <td>07/06/2016</td>
    </tr>
    <tr>
      <th>10474</th>
      <td>0.50</td>
      <td>08/06/2016</td>
    </tr>
    <tr>
      <th>10475</th>
      <td>0.50</td>
      <td>09/06/2016</td>
    </tr>
    <tr>
      <th>10476</th>
      <td>0.50</td>
      <td>10/06/2016</td>
    </tr>
    <tr>
      <th>10477</th>
      <td>0.50</td>
      <td>13/06/2016</td>
    </tr>
    <tr>
      <th>10478</th>
      <td>0.50</td>
      <td>14/06/2016</td>
    </tr>
    <tr>
      <th>10479</th>
      <td>0.50</td>
      <td>15/06/2016</td>
    </tr>
    <tr>
      <th>10480</th>
      <td>0.50</td>
      <td>16/06/2016</td>
    </tr>
    <tr>
      <th>10481</th>
      <td>0.50</td>
      <td>17/06/2016</td>
    </tr>
    <tr>
      <th>10482</th>
      <td>0.50</td>
      <td>20/06/2016</td>
    </tr>
    <tr>
      <th>10483</th>
      <td>0.50</td>
      <td>21/06/2016</td>
    </tr>
    <tr>
      <th>10484</th>
      <td>0.50</td>
      <td>22/06/2016</td>
    </tr>
    <tr>
      <th>10485</th>
      <td>0.50</td>
      <td>23/06/2016</td>
    </tr>
  </tbody>
</table>
<p>10486 rows Ã— 2 columns</p>
</div>



This DataFrame is really long, and it's a pain to keep scrolling up to see the column names. We can use `df.head(x)` to see the top x rows (df is the conventional abbreviation for DataFrame, which I'll use throughout the course). 

The default number of rows is 5. Note that this doesn't change the DataFrame, merely how it is displayed on the screen.



		~~~~~~~~
baseRateData.head(10)
~~~~~~~~




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
    <tr>
      <th>5</th>
      <td>11.5</td>
      <td>09/01/1975</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11.5</td>
      <td>10/01/1975</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11.5</td>
      <td>13/01/1975</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11.5</td>
      <td>14/01/1975</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11.5</td>
      <td>15/01/1975</td>
    </tr>
  </tbody>
</table>
</div>





		~~~~~~~~
baseRateData.head()
~~~~~~~~




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



We can also see the bottom x rows using `df.tail(x)`. Once again, the default is 5.



		~~~~~~~~
baseRateData.tail(5)
~~~~~~~~




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
      <th>10481</th>
      <td>0.5</td>
      <td>17/06/2016</td>
    </tr>
    <tr>
      <th>10482</th>
      <td>0.5</td>
      <td>20/06/2016</td>
    </tr>
    <tr>
      <th>10483</th>
      <td>0.5</td>
      <td>21/06/2016</td>
    </tr>
    <tr>
      <th>10484</th>
      <td>0.5</td>
      <td>22/06/2016</td>
    </tr>
    <tr>
      <th>10485</th>
      <td>0.5</td>
      <td>23/06/2016</td>
    </tr>
  </tbody>
</table>
</div>



That's much more manageable!

Before we start looking at more useful functions, let's take a quick tour of a DataFrame.

You can see that this DataFrame has 10,486 rows (remember, Python is zero-indexed!) and 3 columns. The left-most column (in bold) is called the index. The index of the DataFrame doesn't necessarily hold any data; instead it allows us to access the data by its location.

We can also see the column names of the DataFrame. Used in conjunction with the index, we can reference an exact cell within the DataFrame.

We can get some more information about the DataFrame by using the `df.info()` method.



		~~~~~~~~
baseRateData.info()
~~~~~~~~

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10486 entries, 0 to 10485
    Data columns (total 2 columns):
    VALUE    10486 non-null float64
    DATE     10486 non-null object
    dtypes: float64(1), object(1)
    memory usage: 163.9+ KB
    

This tells us that we are inspecting a DataFrame and that the DataFrame has 10,486 rows (indexed from 0-10,485), and 2 data columns (the index doesn't hold data). It also gives us some information about the type of data stored in each column, as well as the approximate amount of RAM used to hold it.

We can get some statistical information on numeric columns by using the `df.describe()` method:



		~~~~~~~~
baseRateData.describe()
~~~~~~~~




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>VALUE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10486.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>7.135085</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.515003</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.125000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10.562500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>17.000000</td>
    </tr>
  </tbody>
</table>
</div>



This has given us some summary statistics for the `VALUE` column, for example we can see that the average base rate for the time period is 7.14%. This is useful to allow you to get an idea of the shape of your data - if it does not look as you expect after plotting it, something may have gone wrong along the way!

Finally, we can get the column names in a DataFrame and store it in a list. This is helpful when we want to plot different data columns on the same chart - we can loop through the column names.



		~~~~~~~~
baseRateData.columns.tolist()
~~~~~~~~




    ['VALUE', 'DATE']


