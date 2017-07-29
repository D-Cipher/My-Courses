
# Variable Types - Lists (2)

In the last lesson we learnt that a list can hold any number of  variables and that these variables can be of any type, even other lists. We also saw that we can index and slice lists in the same way that we can with strings.

In this lesson we'll learn how to add items to a list using the <code>list.append()</code> function, how to delete an item from a list by its index using the <code>del</code> keyword, and how to create and access nested lists.

## Adding items to a list

When Plotly interprets data, it expects each particular piece (or trace) of data to be an item in a list, for example Plotly would expect the x-values and y-values of a chart to be in two separate lists, and there are many occasions where we would want to create the dynamically.

To do this, we use the <code>list.append()</code> function.

First, we start with an empty list which will eventually contain our x-values:



xVals = []

print(xVals)


    []
    

Then, we might decide that we want to add some observations to our list of x-values. To do this, we can use <code>list.append()</code> to add them one by one (we'll learn a faster way to do this in a future lesson):


```python
xVals.append(2)

print(xVals)

xVals.append(4)

print(xVals)

xVals.append(6)

print(xVals)

xVals.append(8)

print(xVals)

xVals.append(10)

print(xVals)
```

    [2]
    [2, 4]
    [2, 4, 6]
    [2, 4, 6, 8]
    [2, 4, 6, 8, 10]
    

## Deleting items from a list

After creating our list of x-values, we might then want to delete items from that list. To do this, we use the <code>del</code> keyword in conjunction with the list index to select the item which we want to remove.

Here I'm taking a copy of the x-vals because I want to use this list later on in this lesson:


```python
xValsDel = xVals
```

If we wanted to delete the first (or zeroeth) item in the list we would use the <code>del</code> keyword, and select the item at index 0:


```python
print("Before:", xValsDel)

del xValsDel[0]

print("After:", xValsDel)
```

    Before: [2, 4, 6, 8, 10]
    After: [4, 6, 8, 10]
    

We might also want to delete the last item in the list. We can select the last item by choosing the item at index -1:


```python
print("Before:", xValsDel)

del xValsDel[-1]

print("After:", xValsDel)
```

    Before: [4, 6, 8, 10]
    After: [4, 6, 8]
    

## Creating and accessing nested lists

So, now we've created our x-values and y-values and seen how to delete items from them as we wish, we'll now learn how to create a nested list and how to access the items in that list.

First, I'll create a list which contains our x-values and y-values:


```python
yVals = [1,2,3]
allData = [xVals, yVals]
print(allData)
```

    [[4, 6, 8], [1, 2, 3]]
    

We can then access the item in the zeroeth position by using index 0:


```python
print(allData[0])
```

    [4, 6, 8]
    

We can then access the items inside the list at index 0 in allData by adding another square bracket:


```python
print(allData[0][1])
```

    6
    

We can continue this process indefinitely, with nested lists inside nested lists. This list is three levels deep:


```python
allData2 = [allData, allData]
allData2
```




    [[[4, 6, 8], [1, 2, 3]], [[4, 6, 8], [1, 2, 3]]]



We can access the list at index 0:


```python
allData2[0]
```




    [[4, 6, 8], [1, 2, 3]]



We can access the nested list at index 1:


```python
allData2[0][1]
```




    [1, 2, 3]



And we can access the item at index 2 in that list:


```python
allData2[0][1][2]
```




    3



