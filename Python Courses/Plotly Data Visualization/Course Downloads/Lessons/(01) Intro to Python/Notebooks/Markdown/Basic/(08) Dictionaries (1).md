
# Dictionaries (1)

In the last two lessons we learnt how to create lists, as well as how to implement some common functions and methods on them to change their contents.

In this lesson we'll learn how to create dictionaries and how to access the different items inside them. Plotly expects the instructions it needs to create the chart to be in a dictionary of a particular form, it's therefore really important that we understand them well.

## What is a dictionary?

A dictionary is similar to a list in that it is a container which can hold many other objects. These objects can be of any type, even lists or other dictionaries. One important difference, is that the items within a dictionary are made of two elements; the key of that item and the value of that item. Whilst we access the items in a list by their index, we access the items in a dictionary by their key.

Dictionaries are contained within two curly brackets, with each key/value pair separated by a comma, and each key and value being separated by a colon. The key goes on the left, and the value goes on the right. Keys must be unique within a dictionary.

In the dictionary below, <code>key1</code> corresponds to the string <code>'Value 1'</code>, whilst <code>key2</code> corresponds to the value <code>5</code>:



dict1 = {'key1' : 'Value 1', 'key2': 5}


In the dictionary below, the dictionary keys are numbers rather than strings. There are some situations in which this could be helpful, however I generally prefer to use meaningful strings for the dictionary keys, as this will help us access them later.

In this dictionary, the key <code>5</code> refers to the string <code>'Value1'</code>, whilst the key <code>10</code> refers to the value <code>20</code>:


```python
dict2 = {5 : 'Value1', 10: 20}
```

The keys and values in a dictionary don't need to be set directly as strings or integers, we can instead set them to the value of an object.

In this example, I'm setting the keys of the dictionary as a slice from a string variable, whilst the values are items from a list. 

Whilst this example is not directly applicable, it functions as a proof of concept. We will see the real power of being able to use variables to set the keys and values of a dictionary when we learn about loops.


```python
testString = 'key1key2'
testList = [5,10]

dict3 = {testString[:4] : testList[0], testString[4:] : testList[1]}

print(dict3)
```

    {'key1': 5, 'key2': 10}
    

## Accessing items in a dictionary

In a previous lesson we have seen how to access the items in a list by their index. We access the individual values in a dictionary by referencing them with their key.

The example dictionary below contains test scores for four students:


```python
testScores = {'Alice' : 10, 'Bob' : 50, 'Petra' : 80, 'Andy' : 65}
```

In this cell, I can get Bob's test score by passing his name as a key to the dictionary:


```python
testScores['Bob']
```




    50



If we use a key which is not in the dictionary, we get an error:


```python
testScores['John']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-13-36f9679a8f84> in <module>()
    ----> 1 testScores['John']
    

    KeyError: 'John'


Just as we can create keys and items using variables, we can also access them in the same way.

Here, we have the students' names stored in a list. We can access their test scores in the dictionary by passing the item at a particular index of the list:


```python
students = ['Alice' ,'Bob' ,'Petra' ,'Andy']

testScores[students[3]]
```




    65



## Changing a dictionary

As well as accessing items in a dictionary, we can also create new items:


```python
testScores['Jeremy'] = 100

testScores
```




    {'Alice': 10, 'Andy': 65, 'Bob': 50, 'Jeremy': 100, 'Petra': 80}



We can also change the value of a specific key:


```python
testScores['Alice'] = 100
```

We can update more than one item at a time by using the <code>dict.update()</code> method.

We can pass a dictionary as an argument to this method:


```python
testScores.update({'Andy' : 90, 'Bob' : 25})

testScores
```




    {'Alice': 100, 'Andy': 90, 'Bob': 25, 'Jeremy': 100, 'Petra': 80}



We can also add more than one item at the same time:


```python
testScores.update({'Malcolm' : 64, 'Anthony' : 32, 'Bethany' : 99})

testScores
```




    {'Alice': 100,
     'Andy': 90,
     'Anthony': 32,
     'Bethany': 99,
     'Bob': 25,
     'Jeremy': 100,
     'Malcolm': 64,
     'Petra': 80}



We can delete items in a dictionary by using the <code>del</code> keyword:


```python
del testScores['Alice']

testScores
```




    {'Andy': 90,
     'Anthony': 32,
     'Bethany': 99,
     'Bob': 25,
     'Jeremy': 100,
     'Malcolm': 64,
     'Petra': 80}



And we can empty the dictionary of all its elements by using the <code>dict.clear()</code> method:


```python
testScores.clear()

testScores
```




    {}



