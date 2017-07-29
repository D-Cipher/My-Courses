
# coding: utf-8

# # Chart presentation (6) - Creating custom hovertext

# In the last lesson we found out how to control what, how and where the hover information is displayed on a chart.
# 
# In this lesson we'll learn how to create a custom text field in a Pandas DataFrame using the <code>apply()</code> and <code>lambda</code> functions. We'll also learn how to style this custom field using some HTML tags.
# 
# Setting custom hovertext gives you very fine control over how the contextual information in your chart is displayed. Doing this correctly will really make your charts stand out.
# 
# This lesson has a strong focus on manipulating data in a Pandas DataFrame. We'll learn several different data manipulation techniques, but if you get stuck or don't understand something, you can ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>.

# ## Module Imports

# In[2]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ### Getting the data
# 
# We'll load the house price and ranks dataset from my website. This contains the average house price data for each region on the first day of each year from 1995 - 2016, as well as the rank of each region (1 being the most expensive).
# 
# We're going to create a text column for each Region which will contain the hovertext that will be displayed on the chart. This text field will contain the Region's name in bold, then on the next line, the average price for that year (formatted as £), and on the final line, the region's rank of house price in italics.

# In[38]:

housePrices = pd.read_csv("http://www.richard-muir.com/data/public/csv/RegionalHousePricesAndRanksJan16.csv")
housePrices.head()


# ### Using the <code>df.apply()</code> method
# 
# The Pandas DataFrame <code>apply()</code> method applies a function to each row or column in the DataFrame. We're going to create a dummy DataFrame to see its behaviour:

# In[39]:

df = DataFrame.from_dict({'num1' : [1,2,3,4,5], 
                          'num2' : [5,10,15,20,25], 
                          'num3' : [10,20,30,40,50], 
                                    'letter' : ['a','b','c','d','e']})
df


# Now, we're going to define a simple function which we will apply to the DataFrame. This function must take only one argument. Apply will pass the value of each cell in turn to the function, this value will be passed as the value for the function argument:

# In[40]:

def simpleFunction(x):
    return x * 5


# Let's apply this function to the DataFrame:

# In[41]:

df.apply(simpleFunction)


# We can define a function that is intended to work along the rows:

# In[42]:

def rowFunction(x):
    return x[0] + str(x[2]) + str(x[3])


# In[43]:

df.apply(rowFunction, axis = 1)


# And we can use that function to create a new column:

# In[44]:

df['newcol'] = df.apply(rowFunction, axis = 1)
df


# We can also apply a function to a specific column:

# In[45]:

def multiple(x):
    return x * 5
df['newcol2'] = df['letter'].apply(multiple)
df


# ## Using the </code>lambda</code> function
# 
# The lambda function is not bound to a function name, and only exists for the duration of its use. Lambda functions implicitly return a value. 
# 
# We can put a lambda function inside the <code>df.apply()</code> method to manipulate the values in a DataFrame:

# In[46]:

df['newcol3'] = df.apply(lambda x: x['newcol'] + x['newcol2'], axis = 1)
df


# We'll now use the lambda function to build our text column.
# 
# We need to make this column for every region, so I'll first make a list of regions:

# In[47]:

regions = ['South West','South East','London', 
           'East of England','West Midlands','East Midlands',
           'Yorkshire and The Humber','North West','North East']


# Next, we'll loop through each region and create a new column which contains the name of the region. This will form the basis of our text column:

# In[48]:

for r in regions:
    housePrices[r + "_text"] = r
    
housePrices.head(1)


# Now, we can add the HTML bold and line break tags. &lt;b&gt;...&lt;/b&gt; creates bold text and &lt;br&gt; inserts a line break.
# 
# These look odd in the table, but Plotly displays them as they are intended:

# In[49]:

for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>"
    
housePrices.head(1)


# Next we'll use the <code>df.apply()</code> method and a lambda function to add the average price to this text field.
# 
# We're selecting the column which has the average price for each region with <code>housePrices[r + "_avg"]</code>. Next, we'll take the value that we get for that particular column, round it, convert it to an integer and format it with a thousand separator, and return it by applying the lambda function: <code>apply(lambda x: "£{:,}".format(int(x.round(0))))</code>:

# In[68]:

for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(x.round(0)))) + "<br>"
housePrices.head(1)


# Now we can add the rank to our text column in the same way, just specfing that the rank should be an integer rather than a float. The &lt;i&gt;...&lt;/i&gt; tags make this text italicised.

# In[91]:

for r in regions:
    housePrices[r + "_text"] = "<b>" + r +"</b><br>Average Price: " + housePrices[r + "_avg"].apply(lambda x: 
        "£{:,}".format(int(x.round(0)))) + "<br><i>Rank of average price: " + housePrices[r + "_rank"].apply(lambda x: 
                                                                                                             str(int(x))) + "</i>"
housePrices.head(1)


# Let's look at the value in a cell to make sure that we have done what we intended:

# In[92]:

housePrices.loc[0, 'London']


# ### What have we learnt this lesson?

# In this lesson we've seen how to use Pandas' <code>df.apply()</code> method in conjunction with a user-defined function, or the <code>lambda</code> anonymous function to make a column in the DataFrame which contains the text that we want Plotly to show on hover.
# 
# We've seen how to style this text with the &lt;b&gt;...&lt;/b&gt; tags to create bold text, the &lt;i&gt;...&lt;/i&gt; for italicised text, and the &lt;br&gt; tag to insert a line break.
# 
# In the next lesson we'll create a chart which uses this custom hovertext field.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
