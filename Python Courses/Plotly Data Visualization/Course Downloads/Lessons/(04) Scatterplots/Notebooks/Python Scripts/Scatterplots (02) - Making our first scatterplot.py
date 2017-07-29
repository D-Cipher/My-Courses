
# coding: utf-8

# # Scatterplots (02) - Making our first scatterplot

# In this lesson we're going to make our first scatterplot showing the relationship between revenue and number of employees for around 50 different companies. 
# 
# With Plotly, we make scatterplots and lineplots in very similar ways, so the next few lessons should not only teach you about scatterplots, but also serve as a handy revision guide for the Lineplots section.

# ## Module Imports

# In[1]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# In[2]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Getting the data
# 
# We'll get the data on company revenue and number of employees (which I've previously prepared) as a .csv from my website:

# In[3]:

companies = pd.read_csv("http://www.richard-muir.com/data/public/csv/CompaniesRevenueEmployees.csv", index_col = 0)
companies.head()


# ### Adding the hovertext
# Now we'll create the column which contains the text that will be shown when a user moves their mouse pointer over a data point. Scatterplots are used to show the relationship between two variables, but adding coherent hovertext is a great way of ensuring that the user can check and outlying points - those which may lie outside the general trend of the data.
# 
# We're going to have the hovertext show the company's name in bold and the industry in italics on the first line, then the revenue and number of employees on two further lines.
# 
# I'm using <code>df.apply(lambda x: . . .)</code> along with the Python <code>str.format()</code> method to create this text field, accessing each column in turn within the lambda function:

# In[18]:

companies['text'] = companies.apply(lambda x: 
                                    """<b>{}</b> (<i>{}</i>)<br>Revenue: ${} billion<br>Employees: {:,}""".format(x['Name'], 
                                                                                                                  x['Industry'], 
                                                                                                                  x['Revenue (USD billions)'],
                                                                                                                  x['Employees']),
                                    axis = 1)


# In[19]:

companies.head()


# Let's look at a specific cell to make sure the numbers have been formatted correctly:

# In[20]:

companies.loc[0, 'text']


# ## Making our scatter trace
# We can now make our scatter trace. We'll do this is a similar way to how we made the traces for our line charts in the previous section, however rather than specifying <code>'mode' : 'lines'</code>, we'll instead specify <code>'mode' : 'markers'</code>.
# 
# It's not clear from the data if there is a variable that we consider to be especially independent or dependent (an independent variable is conventionally plotted on the x-axis), so we can plot the variables on whichever axis:

# In[21]:

companiesTrace = {'type' : 'scatter',
                 'mode' : 'markers',
                 'x' : companies['Revenue (USD billions)'],
                  'y' : companies['Employees'],
                  'text' : companies['text'],
                  'hoverinfo' : 'text'}


# Now we'll set the chart and axis titles in the layout:

# In[22]:

layout = {'title' : 'Revenue by number of employees',
         'xaxis' : {'title' : 'Revenue (Billion $)'},
          'yaxis' : {'title' : 'Employees'}}


# Let's create the figure object and plot it!

# In[23]:

fig = Figure(data = [companiesTrace], layout = layout)
pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (02) - Making our first scatterplot\pyo.iplot-0.png") 
 #

# So you can clearly see the relationship between revenue and the number of employees for these companies. It looks like there's a slight upwards trend, but most of the data points are clustered around the bottom left corner.
# 
# Let's send this chart to the Plotly cloud.

# In[24]:

py.plot(fig, filename="Companies by revenue and number of employees", fileopt = 'overwrite')


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(04) Scatterplots\Notebooks\images\Scatterplots (02) - Making our first scatterplot\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to create a scatterplot by changing the <code>'mode'</code> option to <code>'markers'</code> rather than <code>'lines'</code>. We've also reviewed how to use the apply method and lambda function to create a column in the DataFrame to display the hovertext.
# 
# In the next lesson we'll look at how to style the marker points. We've touched upon this briefly in the lineplots section, but we'll investigate some extra options.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
