
# coding: utf-8

# # Barcharts (1) - What is a barchart?
# 
# In this section we're going to learn how to create barcharts with Plotly. A barchart is used to display categorical data, with the size of the bar representing the quantity (or sometimes proportion) in that particular category. Barcharts make it easy to compare different categories because we can easily assess which bars are longer than others.
# 
# Barcharts can be horizontal or vertical. The example below from Plotly user <a href="https://plot.ly/~elliotk">elliotk</a> shows the reasons people reject an employment offer:

# In[7]:

import plotly.plotly as py
import plotly.offline as pyo
pyo.init_notebook_mode()
pyo.iplot(py.get_figure("elliotk", 21))


py.image.save_as(py.get_figure("elliotk", 21), r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (01) - What is a barchart\pyo.iplot-0.png") 
 #

# 
# ### Stacked bar charts
# 
# We can also use bar charts to show more complex categorical data, by stacking the bars, as in this example from the Higher Education Funding Council for England which shows the proportion of staff by gender and job type:

# In[6]:

pyo.iplot(py.get_figure("hefceplots", 33))


py.image.save_as(py.get_figure("hefceplots", 33), r"C:\Users\Rytch\Google Drive\Financial\Passive Income\Online courses\Plotly\Course Content\Lessons\(06) Barcharts\Notebooks\images\Barcharts (01) - What is a barchart\pyo.iplot-1.png") 
 #

# ### Grouped bar charts
# Bar charts can also be grouped, as in this example from the ONS which shows people's feelings about financial debt:
# <img src="http://visual.ons.gov.uk/wp-content/uploads/2016/01/Debt-Week_FINAL-051.png"/>
# 
# It's also conceptually possible to create a stacked, grouped bar chart. However, at the time of writing, Plotly does not have this functionality.
# 
# 
# ### What will I learn in this section?
# 
# In this section you'll learn how to create vertical and horizontal bar charts as well as how to create stacked and grouped bar charts, as well as stacked proportional bar charts. You'll also learn about the different styling options available for bar charts. You'll also find out how to combine different types of traces on the same plot; we'll combine a Bar Chart with a Scatterplot. Finally, we'll use the Plotly <code>make_subplots()</code> function to create our first dashboard. Throughout this section we'll be using data from NASA on the number of meteroites that have been found across the world.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
