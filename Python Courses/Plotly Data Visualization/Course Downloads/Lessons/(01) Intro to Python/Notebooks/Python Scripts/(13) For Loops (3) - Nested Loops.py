
# coding: utf-8

# # For Loops (3) - Nested Loops

# In the last lesson we learnt how to write a loop which applies the same piece of code to every item in a sequence. We saw that we could use this to loop through the items in a list and create a new list from these items. We also learnt how to loop through the keys or values (or both) in a dictionary and how we might use this feature when creating charts.
# 
# In this lesson we're going to look at nested loops and how to implement them in our code. 
# 
# ## Nested Loops
# 
# Nested loops are a very powerful construct; they allow us to loop through a sequence of sequences and apply the same operation to each sequence and sub-sequence. This is easier to explain with an example.
# 
# In the previous lesson we saw how to create a new list from the items in a list; we took a list of proportions and multiplied each proportion by 100 to get its percentage equivalent. We also saw how to loop through the keys and values in a dictionary. In this lesson we're going to combine these two concepts.
# 
# Imagine that we have a data structure that contains, for each year, a list of the proportions of total sales each quarter that came from a particular product:

# In[1]:

dataProp = {2009 : [0.12,0.22,0.35,0.41],
       2010 : [0.15, 0.36, 0.47, 0.62],
       2011 : [0.07, 0.14, 0.27, 0.29],
       2012 : [0.05, 0.13, 0.15, 0.26]}


# We saw in the last lesson that we could loop through the items in a list and do an operation to each item. In the cell below, I loop through each value in the list of proportions for 2009 and create a new list with the percentages:

# In[2]:

perc2009 = []

for prop in dataProp[2009]:
    perc2009.append(prop * 100)
    
perc2009


# We also saw how to loop through the items in a dictionary. Here, I'm looping through the items in the <code>dataProp</code> dictionary and creating a new list with the proportions of sales from that product over all the years:

# In[3]:

allSales = []

for year in dataProp.values():
    allSales = allSales + year
    
allSales


# But what if we wanted to do both of these things? What if we wanted a list of all the percentages of the total sales which are attirbuted to that item?
# 
# We could do it in two steps:
# 
# (I'm converting to an integer because of the way <a href="https://docs.python.org/3.1/tutorial/floatingpoint.html">floats are represented by Python</a> - try it without <code>int()</code>)

# In[4]:

allSales = []

for year in dataProp.values():
    allSales = allSales + year
    
salePercentages = []

for sale in allSales:
    salePercentages.append(int(sale * 100))
    
salePercentages


# But we can also achieve the same result by using a nested loop.
# 
# ## How do nested loops work?
# 
# When we nest one loop inside another we aren't creating two loops which run one after the other, we are actually creating a hierarchy of loops, with one loop running inside the other.
# 
# The syntax is as follows, note that we must give a different name to the variable which records our position in each loop:
# ````python
# for item1 in outerloop:
#     <do something>
#     for item2 in innerloop:
#         <do something>
# ````
# 
# For each item in the outer loop, the inner loop will run through all the items in a sequence. This means that the inner loop will run many times. For examaple, if we have 5 items in the outer loop and 5 in the inner loop, the inner loop will run 25 times. With ten in each loop, the inner loop will run 100 times. It's therefore really important to consider how many loops will run!
# 
# The code in the cell below shows you how the loops operate; before you run it, consider what you expect the loop to do:

# In[5]:

outerLoop = [1, 2, 3, 4, 5]
innerLoop = ['a', 'b', 'c', 'd', 'e']

for item1 in outerLoop:
    for item2 in innerLoop:
        print(item1, item2)


# So, the outer loop counts up from 1 to 5, whilst the inner loop goes through the alphabet from a to e. For every number in the outer loop, the inner loop counts through the five letters. This behaviour is consistent in all nested loops.

# ## Using Nested Loops
# 
# So let's apply what we've learnt to the problem I posed earlier:
# 
# ##### How can we make a list of the percentages of sales for each quarter over all of the years?
# 
# Well, first we know that we need to create an empty list and loop through the data dictionary:

# In[6]:

percentages = []

for d in dataProp.values():
    print(d)


# Next, within the loop that cycles through the lists in the dictionary, we need to create a loop which cycles through each item in the list:

# In[7]:

for d in dataProp.values():
    for item in d:
        print(item)


# Now, we can append each item in turn to the <code>percentages</code> list (and multiply by 100 to get the percentage):

# In[8]:

for d in dataProp.values():
    for item in d:
        percentages.append(int(item * 100))
        
percentages


# ### What have we learnt this lesson?

# In this lesson we reviewed how to loop through the items in a dictionary or a list. We learnt how to create a nested loop, and what behaviour to expect from the inner and outer loops. We then applied this knowledge to loop through the items in a dictionary of lists of data and append these items to a master list of percentages.

# If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>
