
# Variable Types - Lists (1)

In the last few lessons we have looked at four types of variable; integers, floats, strings and boolean. These are all what I like to call 'simple' variable types; each of them is comprised of only one object.

Python allows for many different types of what I call 'complex' variable types; these are variables which contain 1 or more separate objects. In this course we will only look at lists and dictionaries as these are the primary data structures which Plotly uses to create charts. In the next couple of lessons we'll learn about lists.


## What is a list?

A list, whilst being an object in its own right, is also a container for other objects.

A list can contain any number of elements (you are limited by your computer's memory), and can contain elements of any type, even other lists.

A list is comprised of different items, separated by commas, between two square brackets.

This is a list of numbers:



list1 = [0, 1, 2, 3, 4]


This is a list of strings:



		~~~~~~~~
list2 = ['a', 'b', 'c', 'd', 'e']
~~~~~~~~

And this is a list of lists:



		~~~~~~~~
list3 = [list1, list2]

print(list3)
~~~~~~~~

    [[0, 1, 2, 3, 4], ['a', 'b', 'c', 'd', 'e']]
    

## Mathematical Operators and Common Functions/Methods

We can do addition on lists:



		~~~~~~~~
list4 = list1 + list2

print(list4)
~~~~~~~~

    [0, 1, 2, 3, 4, 'a', 'b', 'c', 'd', 'e']
    

And we can also do multiplication:



		~~~~~~~~
print(list1 * 4)
~~~~~~~~

    [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    

We can get the number of items in a list by using the `len()` function:



		~~~~~~~~
print(len(list1))
~~~~~~~~

    5
    

Many of the same functions that work on strings also work on lists because they are both 'sequences'; bear in mind that some functions will only work on lists, and others only on strings.

We can check which functions can be applied to an object by typing the object's name, followed by a ` . ` and then pressing `tab`:



		~~~~~~~~
list1.  #put the cursor on the right of the dot and press tab
~~~~~~~~


      File "<ipython-input-7-5a8c7cb8fa05>", line 1
        list1.  #put the cursor on the right of the dot and press tab
                                                                     ^
    SyntaxError: invalid syntax
    


## Indexing and Slicing Lists

In a previous lesson we learnt how to select different items within a string by using the index of that item:



		~~~~~~~~
string1 = 'abcdefg'

print(string1[4])
~~~~~~~~

    e
    

And we also learnt how to take slices of a string by passing two indices separated by a colon (remember that the slice starts from the first index and stops just before the second):



		~~~~~~~~
print(string1[2:5])
~~~~~~~~

    cde
    

The same method that we use to index and slice strings can be directly applied to lists. Here, I'm taking a particular item from list 1:



		~~~~~~~~
print(list1[0])
~~~~~~~~

    0
    

And a different item from list 2. Notice how taking a single item returns just that item:



		~~~~~~~~
print(list2[3])
~~~~~~~~

    d
    

We can also change a value in a list by accessing it by the index:



		~~~~~~~~
list2[3] = 'zzzz'

print(list2)
~~~~~~~~

    ['a', 'b', 'c', 'zzzz', 'e']
    

We can also take a slice from a list; this returns a list of items:



		~~~~~~~~
print(list1[2:5])
~~~~~~~~

    [2, 3, 4]
    

To change all of the items in a slice, you must set them equal to a new list of the same length as the slice:



		~~~~~~~~
list1[2:5] = [10,10,10]

print(list1)
~~~~~~~~

    [0, 1, 10, 10, 10]
    
