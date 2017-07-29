
# For Loops (1) - Looping through a range of values

In the last lesson we learnt how to use if-else statements to control which code is run in a program. We saw that we could run different blocks of code depending on the outcome of a condition. We also saw how to create complex decision trees usinh nested if statements.

In this lesson, we'll learn how to use For Loops to run the same piece of code a number of times. Normally code is run sequentially, with each line being executed after the previous line. By using loops, we can reduce the amount of code we have to write.

For loops are essential for creating charts in Plotly, for example we might want to create a different data item for every year in a range of years, or create a chart which shows data about a list of countries. Using a loop to run this code prevents us from having to write the same piece of code many times, but it also allows us to write the code without having to know how many times it will run.

## Different types of For Loops

There are two different types of for loops which we'll use. The first (which we'll cover in this lesson) allows us to run the same piece of code a specified number of times, whilst the second (which we'll learn about in the next lesson) allows us to run the same piece of code for each item in a sequence (a list for example). They differ in that the first type will always run the same number of times, whilst the second will run as many times as there are items in the sequence.

### Looping through a specified range of values

We'll first look at using a For Loop to run a piece of code a specified number of times. To do this, we need to use Python's <code>range()</code> function to set the range in which the loop will operate. We also need to create a variable which exists only within the loop to keep track of where we are in the range. The syntax for this is as follows:

`
for <variable name> in range(<set the range>):
    <code to run>
`

First we'll look at some simple examples of how to create these loops, you'll then get a chance to practise how they work before we see how we can apply what we've learnt when making charts.

## Our First For Loop

In the cell below I've created a for loop. If we compare what I've written to the syntax above, we can see that the variable which keeps track of our position within the loop is called <code>i</code> - this is a convention in programming. 

I've set the loop to run in the range of <code>0-5</code>. Python starts counting from 0 (which is implicit in the <code>range()</code> function), and you'll remember from the lesson on slicing lists that we stop at the position before the end of the slice. This means that the loop will run 5 times, but that <code>i</code> will take the values 0-4 inclusive throughout the duration of the loop.

Finally I've asked Python to simply print the value of <code>i</code> in each iteration of the loop. Doing this confirms how the loop works; that <code>i</code> increases by 1 each time the loop is run.


```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4
    

We can change the range in which the loop operates by passing other arguments to the <code>range()</code> function. Remember that after opening the brackets of a function, you can press <code>shift + tab</code> to see which arguments the function takes.

In the cell below, I've set the loop to start at the year 2002 and finish just before the year 2016. We could use this construct to create a chart for each year in the range of years.


```python
for i in range(2002, 2016):
    print(i)
```

    2002
    2003
    2004
    2005
    2006
    2007
    2008
    2009
    2010
    2011
    2012
    2013
    2014
    2015
    

We can also pass a third argument to the <code>range()</code> function. This argument allows us to specify the step that  the loop variable (in this case, <code>i</code>) takes. In this case, I'm asking the loop to print out every other year. The loop doesn't print out the year 2016 because we have told it to stop just before 2016.


```python
for i in range(2002, 2016, 2):
    print(i)
```

    2002
    2004
    2006
    2008
    2010
    2012
    2014
    

##  Running more interesting code

We're not limited to simply printing out the value of <code>i</code> each time we run through the loop. We can implement conditional programming to do different things depending on which value <code>i</code> takes on a specific iteration of the loop.

For example, say that we wanted to run a piece of code that manipulates data for every year between 2005 and 2015 inclusive, but we know that the data needed to be processed differently for 2009. We could use an if statement to run a different piece of code only when <code>i</code> is equal to 2009:


```python
for i in range(2005, 2016):
    if i == 2009:
        print("Process the data differently for: " + str(i))
    else:
        print("Process the data as normal for: " + str(i))
```

    Process the data as normal for: 2005
    Process the data as normal for: 2006
    Process the data as normal for: 2007
    Process the data as normal for: 2008
    Process the data differently for: 2009
    Process the data as normal for: 2010
    Process the data as normal for: 2011
    Process the data as normal for: 2012
    Process the data as normal for: 2013
    Process the data as normal for: 2014
    Process the data as normal for: 2015
    

## Practise

This is the chance for you to practise what you've learnt. For each problem, try and solve it before scrolling down to see the solution.

### 1

Write a loop which prints out the values from 2 to 13 inclusive.

````
2
3
4
5
6
7
8
9
10
11
12
13
````

### 2

Write a loop which prints out the values from 6 to 21 inclusive, but only even numbers:

````
6
8
10
12
14
16
18
20
````

### 3

Write a loop which gives the following output:

````
i = 5, i is odd
i = 8, i is even
i = 11, i is odd
i = 14, i is even
i = 17, i is odd
i = 20, i is even
````


## Answers

### 1


```python
for i in range(2, 14):
    print(i)
```

    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    

### 2


```python
for i in range(6, 21,2):
    print(i)
```

    6
    8
    10
    12
    14
    16
    18
    20
    


```python
#or

for i in range(6, 21):
    if i %2 == 0:
        print(i)
```

    6
    8
    10
    12
    14
    16
    18
    20
    

### 3


```python
for i in range(5, 21,3):
    if i %2 == 0:
        print("i = " + str(i) + ", i is even")
    else:
        print("i = " + str(i) + ", i is odd")
```

    i = 5, i is odd
    i = 8, i is even
    i = 11, i is odd
    i = 14, i is even
    i = 17, i is odd
    i = 20, i is even
    

