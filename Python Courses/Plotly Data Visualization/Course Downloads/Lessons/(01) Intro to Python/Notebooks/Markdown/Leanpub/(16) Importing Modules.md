
# Importing Modules

In this lesson we're going to learn how to import different code libraries and how to use functions from those libraries. This is vital knowledge for this course; Plotly itself is an external code library and there are many different functions which we'll need to use.

## How to import a module

We'll start by importing the Python builtin library called `random` - this library allows us to create different random numbers. 

It's as easy as typing `import`, then the module name into the cell. When the Python interpreter finds an `import` statement, it searches through a list of directories in which it expects to find modules to be imported.



import random


When we try to import a module that doesn't yet exist, we get an `ImportError`:



		~~~~~~~~
import bananas
~~~~~~~~


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-2-e67d4964b26e> in <module>()
    ----> 1 import bananas
    

    ImportError: No module named 'bananas'


We can test to see that the module has been imported by typing the module name, then a ` . `, then pressing `tab` to see what functions are available to us from the module. We can scroll through these options using the arrow keys:



		~~~~~~~~
random.
~~~~~~~~


      File "<ipython-input-3-4bd0ffe0ca6b>", line 1
        random.
               ^
    SyntaxError: invalid syntax
    


We're going to use the `random.randint` function to get a random integer. Remember to press `shift + tab` after opening the brackets to see what arguments the function takes.



		~~~~~~~~
random.randint(5, 10)
~~~~~~~~




    7



But imagine that we had to use `random.randint()` a lot in whatever program we are writing. It would become very time consuming to write `random.randint()` every time.

Luckily, we can create a shorthand to reference the `random` module:



		~~~~~~~~
import random as r
~~~~~~~~

We can now use `random.randint()` by typing `r.randint()`:



		~~~~~~~~
r.randint(5, 10)
~~~~~~~~




    10



We could go one step further, and import the `randint` module directly from `random`. This will let us use `randint` without having to reference the `random` module at all:



		~~~~~~~~
from random import randint

randint(5, 10)
~~~~~~~~




    7



You can also import multiple modules at the same time. In this example, `random()` creates a random number between 0 and 1:



		~~~~~~~~
from random import randint, random

print(random())
~~~~~~~~

    0.736779117754959
    

Finally, we can choose to import all of the functions in a module:



		~~~~~~~~
from random import *
~~~~~~~~

This option should be used sparingly. Python uses 'namespaces' to keep track of object and function names; if you had created your own function called `randint`, and then imported the `random.randint()` function, you might experience some unwanted and unexpected behaviour in your program.

## Importing the modules we'll use in the course

From now on, we'll use the same modules in almost every lesson - we may add a few more modules, or utilise some different functions from these libraries, but we will always use at least these imports.

`plotly.offline` allows us to use plotly's `plot` function to create our charts without pushing them to the Plotly cloud. This is handy when we develop a chart and don't want multiple beta versions being displayed publicly. I've imported this as `pyo`,

The `plotly.graph_objs` library contains many functions which help us to create different kinds of charts; I've decided to import them all throughout the course.

On the other hand, `plotly.plotly` makes the chart and pushes it to your plotly account in the cloud. We'll use this when we're happy with the chart we've made. I've imported this as `py`

`pandas` is a great library for data analysis and manipulation. It's very powerful and very complex; a full tutorial on how to use it is far beyond the scope of this course, but there are a few functions that we'll use repeatedly, one of these being a Pandas DataFrame, which I've imported separately as we'll use it that often! We'll learn about Pandas very soon!



		~~~~~~~~
#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
#allows us to create the Data and Figure objects
from plotly.graph_objs import *
#plotly.plotly pushes your charts to the cloud  
import plotly.plotly as py

#pandas is a data analysis library
import pandas as pd
from pandas import DataFrame
~~~~~~~~
