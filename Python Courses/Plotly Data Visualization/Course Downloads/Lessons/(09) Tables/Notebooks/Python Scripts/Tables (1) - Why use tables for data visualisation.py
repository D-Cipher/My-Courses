
# coding: utf-8

# # Tables (1) - Why use tables for data visualisation?

# You might think that including tables in a course about data visualisation is a bit pointless.
# 
# Surely the whole point of displaying data in a visual way is to remove the need for clunky, ugly and hard-to-read tables?
# 
# This is not neccesarily true; presenting data in a table is a valid and useful way of communicating data to your audience.
# 
# The basic difference between tables and charts is that whilst charts interact with our visual system of understanding, tables interact with our verbal system - we read them, and therefore absorb information differently from them.
# 
# ### Why use a table?
# 
# Tables are actually a very effective form of data presentation for several reasons:
# 1. Familiarity - Almost everyone is familiar with tables and how to read and understand them. 
# 2. Granularity - Tables can show data at the lowest level of aggregation, and allow people to interrogate the raw numbers without having to interpret them through a chart or through hoverinfo.
# 3. Variety - Different people interact with data in different ways. Including a table in your dashboard will broaden its appeal to those who like seeing tabular data.
# 
# ##### Tables and charts complement each other because each serves a different function for presenting data.

# ## Designing effective tables

# Just as with charts and graphs it's important to consider how your audience will interpret the data you present in a table, and even more so to design your table in such a way that it's easy for the reader to understand.
# 
# There are a few basic design rules we can follow:

# #### Keep your table small and succint.
# 
# - It's very easy to be overwhelmed by a giant wall of tabular data. 
# - Tables should allow the user to interrogate the most important numbers behind the charts, not to display every piece of data that you used. That's what a .csv download is for!

# #### Make spacious and uncluttered tables.
# - Use space to delineate rows and columns. 
# - The numbers in adjacent columns should have enough space between them so that the reader doesn't confuse them for a single number. 
# - There should be vertical space between each row. 

# #### Help your reader understand the table.
# 
# - Set the header row to a different colour to the rest of the table; your reader will intuitively know it's not to be interpreted as data.   
# - Alternate colours for the rows in the table so your readers don't have to trace across the table with their finger.   
# - Use a monospace font (like Arial) so that the size of numbers can be easily compared.
# - Sort your table in a sensible order - Alphabetically or by Date are two common sorting methods that allow people to easily find the information they need.

# ## What will we learn in this section?

# In this section we'll learn how to create a table in Plotly from a list or a Pandas DataFrame.
# 
# We'll see how to set the colours and font for the table which will allow us to implement what we've just learnt about designing effective tables. We'll also see how to add hoverinfo to a table to capitalise on the interactivity that makes Plotly great.
# 
# Finally we'll see how to incorporate tables and charts together into the same figure. This will allow us to include tables in any dashboards that we make.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
