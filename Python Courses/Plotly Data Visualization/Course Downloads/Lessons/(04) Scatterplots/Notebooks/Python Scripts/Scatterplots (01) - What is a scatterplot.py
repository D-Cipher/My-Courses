
# coding: utf-8

# # Scatterplots (01) - What is a scatterplot
# 
# Scatterplots are used to show the relationship between two quantitative (numeric) variables. This relationship can be positive or negative, and they may also show a strong or weak (or non-existent!) correlation.

# ## How are scatterplots created?
# 
# Scatterplots are created by placing a dot at the intersection of the x-value and the y-value of a data point. This is repeated once for each data point to build up a picture of the relationship between the two variables.
# 
# In the following example, the three points A, B & C are plotted at (1, 5), (2, 6), and (6, 3) respectively:
# 
# <table>
# <tr>
#     <th>Point</th><th>x-value</th><th>y-value</th>
# </tr>
# <tr>
# <td>A</td><td>1</td><td>5</td>
# </tr>
# <tr>
# <td>B</td><td>4</td><td>3</td>
# </tr>
# <tr>
# <td>C</td><td>6</td><td>4</td>
# </tr>
# </table>
# 
# <img src="http://www.richard-muir.com/images/xyvalues.png"/>

# ## What type of variables are plotted on a scatterplot?
# 
# #### Scatterplots generally show two types of relationships:
# 1. The relationship between a control or independent variable (plotted on the x-axis), with the dependent variable of interest plotted on the y-axis. For example a researcher may hypothesise that the selling price of a house is related to the floor space. The selling price is the variable of interest and is plotted on the y-axis, whlst the area is the independent variable and is plotted on the x-axis. <a href ="https://plot.ly/~bturnbull/106/california-housing-prices-and-size-scatter-plot/">This plot</a> by the Plotly user <a href="https://plot.ly/~bturnbull">@bturnbull</a> is a great example: 
# <img src="https://plot.ly/~bturnbull/106/california-housing-prices-and-size-scatter-plot.png"/>
# 
# 2. The relationship between two variables, neither of which is assumed to be dependent on the other. A famous example of this comes from the <a href="https://en.wikipedia.org/wiki/Iris_flower_data_set">Iris flower dataset</a> which is used as a test case for machine learning algorithms. <a href="https://plot.ly/~akandykeller/836/sepal-width-vs-petal-length.embed">This plot</a> by Plotly user <a href="https://plot.ly/~akandykeller/folder/home">@akandykeller</a> shows the relationship between two different kinds of petal for two subspecies of the same plant. Neither measurement can be thought to cause the other, but the relationship between the two, or the correlation, is interesting:
# <img src="https://plot.ly/~akandykeller/836/sepal-width-vs-petal-length.png"/>
# 
# In the second case, it's really important to remember that <a href="http://www.tylervigen.com/spurious-correlations">Correlation does not imply causation</a>.

# ## Correlations
# 
# The image below shows some perfect, strong and weak, positive and negative correlations:
# 
# <img src="http://www.richard-muir.com/images/correlations.png"/>

# ## How can we quantify the relationship between two variables?
# 
# Scatterplots are often displayed with a line of best fit, or regression line. In its simplest form this line is fitted to minimise the distances between each individual the point and this line, although there are many different types of regression. The equation of this line therefore describes the relationship between the variables.
# 
# <a href="https://plot.ly/~OLI_Stanford/268/infant-vocalization-and-iq-regression-line/">This chart</a> by Plotly user <a href="https://plot.ly/~OLI_Stanford/folder/home">@OLI_Stanford</a> shows data for the frequency of vocalisations by an infant plotted against his or her IQ. This data has been fitted with a regression line which quantifies the observed relationship between these variables:
# <img src="https://plot.ly/~OLI_Stanford/268/infant-vocalization-and-iq-regression-line.png"/>

# ## What will we learn in this section?
# 
# In this section we'll learn how to make a simple scatterplot to investigate the relationship between two variables. We'll plot this relationship for single and multiple categories and we'll also find out how to style the markers to distinguish the different categories.
# 
# We'll learn how to calculate and plot a regression line, as well as how to calculate and display different measures of fit for that line by adding annotations to the plot and making different use of the text option in the traces.
# 
# We'll learn how to display a third variable on a scatterplot by varying the size of the markers to create a bubble plot, and we'll also investigate the plotly subplots functionality to create a scatterplot matrix and investigate the relationships between many different variables.
# 
# Let's get started!

# In[ ]:



