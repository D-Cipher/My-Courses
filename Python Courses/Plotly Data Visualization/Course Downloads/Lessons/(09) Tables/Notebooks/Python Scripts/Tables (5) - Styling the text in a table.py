
# coding: utf-8

# # Tables (5) - Styling the text in a table

# In this lesson we're going to learn how to style the text in a table.
# 
# We're going to focus on three specific styling options:
# 1. Changing the font family, size and color
# 2. Thousand-separating numbers
# 3. Right-aligning numbers
# 
# Doing these three things will allow us to more closely follow the recommendations set out in the first lesson in this section. We want to make our tables as easy as possible to read, and by changing these parameters we can hopefully achieve this.

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


# #### New Modules:
# 
# Figure Factory:

# In[2]:

from plotly.tools import FigureFactory as FF


# In[3]:

#lets us see the charts in an iPython Notebook
pyo.offline.init_notebook_mode() # run at the start of every ipython 


# ## Changing the font:

# Let's get the table we worked on in the last lesson:

# In[4]:

table = py.get_figure("rmuir", 313)
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-0.png") 
 #

# As we learnt previously, the text in the tables is stored as annotations in the layout section of the figure.
# 
# We can therefore loop through the list of annotations and apply the styling options as necessary. We'll probably want to style the header/index annotations differently to the those which show data, however there is no direct way to identify which annotation is a header/index and which belongs in a row. 
# 
# We can see that the header and index items are shown in bold in the table. To find out which items are in the header/index, let's loop through the annotations and look for <code>'&lt;b&gt;'</code>:

# In[5]:

for ann in table['layout']['annotations']:
    if '<b>' in ann['text']:
        print('HEADER/INDEX: {}'.format(ann['text']))
    else:
        print('ROW DATA: {}'.format(ann['text']))


# We've previously learnt how to format text in annotations, so let's just make a small change as proof that it works. I'll change the colour of the data items from black to a dark grey, and the colour of the header/index from white to a light grey:

# In[6]:

for ann in table['layout']['annotations']:
    if '<b>' in ann['text']:
        ann['font']['color'] = '#f1f1f1'
    else:
        ann['font']['color'] = '#333'
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-1.png") 
 #

# ## Formatting numbers with a thousand-separator
# 
# To improve readability, one of the simplest and most effective things you can do is to add in a thousand-separator between numbers.
# 
# The reason this is so effective is because it separates the number into smaller, more readable chunks.
# 
# For example:
# 
# 53,865,800
# 
# is much easier to read than:
# 
# 53865800
# 
# Let's add in thousand separators to the numbers in the Population column. We need to loop through the annotations again, and by checking if we can successfully convert the text of that annotation to an integer (or float), we can extract only the numbers from the table.
# 
# We'll do this in a <code>try-except</code> statement. This statement tries to execute some code, but if it code produces an error of the stated type, it simply carries on, rather than breaking:

# In[7]:

for ann in table['layout']['annotations']:
    try:
        print(int(ann['text']))
    except: 
        ValueError


# Now that we've used this statement to isolate only the numbers, let's format them with a thousand separator:

# In[8]:

for ann in table['layout']['annotations']:
    try:
        ann['text'] = "{:,}".format(int(ann['text']))
    except: 
        ValueError


# In[9]:

pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-2.png") 
 #

# Much better! The population numbers are much easier to compare now.

# ## Right-aligning numbers
# 
# Another way to make our tables easier to read is by right-aligning the numbers. This makes it much easier to visually compare the size of a number because all of the digits line up.
# 
# For left-aligned numbers, this is more difficult. Compare this:  
# 10,000  
# 100  
# 
# With this:  
# <p style="text-align : right;">10,000<br>100</p>  
# 
# The digits in the 1, 10 and 100 position all line up with right-aligned numbers.
# 
# Let's right-align the text in our table. This is not as straightforward as adding a thousand-separator. First of all, we have to find the columns with numbers in.
# 
# Here is a quick function to check if a string has a number in:

# In[10]:

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


# Let's loop through the data in our table and check which cells have numbers in.
# 
# We want to right align the column headings and data for the Population and Area columns. We know that the Area column title doesn't contain any numbers, so we can specify that directly:

# In[11]:

for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        print(ann['text'])


# Let's now change the <code>'xanchor'</code> property of those annotations and see how that changes the alignment. We'll definitely have to move the annotation as well, but this is a good start:

# In[12]:

for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['xanchor'] = 'right'
        
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-3.png") 
 #

# This has moved all the annotations to the left, because the right-hand side of the annotation is now anchored to the position of the annotation. We now need to move the annotations to the right. 
# 
# From looking at the annotations, the x-values for the position have a spacing of 1. Let's try adding 1 to each x-position and see how that moves the annotations:

# In[13]:

for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['x'] = ann['x'] + 1
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-4.png") 
 #

# That's moved them a bit too far to the right; we can see some faint lines behind the numbers. Let's move them left by 0.1 for a total movement of 0.9 to the right.
# 
# Remember that this will likely be different for every table that you make. Try out some different values until it looks right to you.

# In[14]:

for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['x'] = ann['x'] - 0.1
pyo.iplot(table)


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\pyo.iplot-5.png") 
 #

# That's much better! Let's send this to the Plotly cloud:

# In[15]:

py.plot(table, filename="UK Population Table (right-align)", fileopt = 'overwrite')


py.image.save_as(table, r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(09) Tables\Notebooks\images\Tables (5) - Styling the text in a table\py.plot-0.png") 
 #

# ### What have we learnt this lesson?

# In this lesson we've learnt how to style the data in the table to make our table as clear as possible.
# 
# We saw how to change the font size, colour and family to make the annotations contrast against the background colour. Plotly's default font family is a monospace font (where each number takes the same amount of horizontal space) so we didn't need to change that.
# 
# We saw how to identify which items in our table data need to have thousand separators added. We did this using a <code>try-except</code> statement and added the thousand separators using the string formatting method.
# 
# Finally, we saw how to right-align numeric data items in our table and why this might be a good idea.
# 
# In the next lesson we'll learn how to change the row height in our table to add some extra space to our table.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
