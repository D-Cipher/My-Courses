
# coding: utf-8

# # Lineplots (10) - Applying Smoothing (2)

# In the last lesson we saw how to implement smoothing on a line chart of dummy data. 
# 
# In this lesson we'll apply Plotly's built in smoothing function to stock market data to see how this technique works on real data. We'll also see how to apply  a smoothing function imported from the <code>scipy</code> scientific computing library.

# ## Module Imports

# In[8]:

#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame


# ### Additional modules
# We'll also use the <code>pandas_datareader</code> module to get the stock market data. First of all we have to install this module.
# 
# 1. Open a command window somewhere in your computer
# 2. Type <code>conda install pandas-datareader</code>
# 3. Press <code>y</code> to confirm the installation
# 
# Then we'll import it.
# 
# We'll also import the <code>signal</code> module from the scientific computing library <code>scipy</code> - this will help us to achieve greater smoothing that is possible with Plotly's built in smoothing option.

# In[10]:

from pandas_datareader import data
from scipy import signal


# In[11]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Using smoothing with real data

# So first thing's first, I'll get the stockmarket data we'll be using directly from Yahoo Finance using Pandas' <code>get_data_yahoo()</code> function. 
# 
# I'll pass the name of the stock (or ticker) to the function, followed by the start date and end date of the range for which I want data.

# In[12]:

appleVals = data.get_data_yahoo('AAPL','1/1/2012','1/1/2013')
appleVals.head()


# I'll create two traces; a smoothed trace and an unsmoothed trace.
# 
# I'm setting the x-values to <code>appleVals.index</code> - this is the left-most column (in bold), and contains the dates. The y-values are set to the closing price, however for the unsmoothed trace I'm adding $50 to each value to separate the traces.

# In[13]:

unSmoothApple = {'type' : 'scatter',
               'x' : appleVals.index,
               'y' : appleVals['Close']+50,
              'mode' : 'lines',
               'line' : {'smoothing' : 0,
                        'shape' : 'spline'},
                'name' : 'Apple (UnSmooth)'}

smoothApple = {'type' : 'scatter',
               'x' : appleVals.index,
               'y' : appleVals['Close'],
              'mode' : 'lines',
               'line' : {'smoothing' : 1.3,
                        'shape' : 'spline'},
              'name' : 'Apple (Smooth)'}

layout = {'title' : 'Stock closing prices for Apple in 2012',
         'xaxis' : {'title' : 'Date'},
         'yaxis' : {'title' : 'Closing Price ($)'}}

data = Data([unSmoothApple, smoothApple])

fig = Figure(data = data, layout = layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (10) - Applying Smoothing (2)\pyo.iplot-0.png") 
 #

# Let's push this chart to the cloud:

# In[14]:

py.plot(fig, filename = "Stock closing prices for Apple in 2012 (Plotly smoothing)", fileopt="overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (10) - Applying Smoothing (2)\py.plot-0.png") 
 #

# The effect of the smoothing is subtle, but noticeable. After zooming in, the effect of the smoothing is more obvious. By clicking and dragging a box around a section of the graph, you can see that the smoothed trace is a little less spiky.
# 
# A higher <code>smoothing</code> value would have a better result in  this situation, but this is not yet possible with Plotly (at the time of writing).
# 
# We can however apply our own smoothing to the data using the <code>signal</code> libary in the <code>scipy</code> module.
# 
# There are many different smoothing options in this library, however we're going to implement the <a href=
# "http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_filter.html#scipy.signal.savgol_filter">Savitzky-Golay</a> filter. This filter basically calculates a moving average of the  5 points closest to the point in question. The actual operation of the algorithm is far more complex, but this is the general idea.
# 
# The Savitzy-Golay function accepts the following arguments:
# - x - an array (list) of data to be filtered
# - window_length - The length of the window in which the filter operates, must be an odd number
# - polyorder - the order of the polynomial used to fit the samples, must be less than window_length
# 
# There are other arguments which you can manipulate, however using these three will enable you to apply enough smoothing to your data.

# We can now incorporate this into our charting function. I'm setting the <code>window_length</code> to 51 and the <code>polyorder</code> to 3. 
# 
# I'm also replotting the un-smoothed trace so that it has it's original values - it's easier to compare the two this way.
# 
# I recommend experimenting with other values for these numbers.

# In[7]:

smoothApple.update({'y' : signal.savgol_filter(appleVals['Close'], 51, 3),})
unSmoothApple.update({'y' : appleVals['Close']})

data = Data([ smoothApple, unSmoothApple ])

fig = Figure(data = data, layout = layout)

pyo.iplot(fig)


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (10) - Applying Smoothing (2)\pyo.iplot-1.png") 
 #

# You can see how this smoothing function has smoothed out a lot of the variability of the data - it has dramatically changed the shape of the line! It's for this reason that we must be careful when using smoothing.
# 
# You could try changing some of the parameters to get a different result.
# 
# You could also try out other smoothing functions; this is not the only one available. 

# I'm going to push this smooted chart to the cloud as well:

# In[8]:

py.plot(fig, filename="Stock closing prices for Apple in 2012 (Savitzy-Golay smoothing)", fileopt = "overwrite")


py.image.save_as(fig, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(02) Lineplots\Notebooks\images\Lineplots (10) - Applying Smoothing (2)\py.plot-1.png") 
 #

# ### Smoothing real data - what have we learnt?

# In this lesson we've seen how to use Plotly's built in smoothing options to smooth some stock market data.
# 
# We've also seen how to use the <code>scipy</code> library to provide an additional smoothing function.
# 
# Just remember that it's not always necessary or even desirable to smooth data; think carefully about what message your chart displays before and after smoothing, and whether this is the message you want it to send.
# 
# In the next lesson we'll look at stepwise line shapes.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
