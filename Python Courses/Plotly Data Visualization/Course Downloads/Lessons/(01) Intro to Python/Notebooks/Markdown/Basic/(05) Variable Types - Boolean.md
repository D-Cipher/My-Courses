
# Variable Types - Boolean

In the last lesson we learnt how to index and slice strings. We also learnt how to use some common string functions such as the <code>len()</code> function.

In this lesson, we'll learn about Boolean values. Boolean values evaluate to either True or False and are commonly used for comparisons of equality and inequality, as well as controlling the flow of a program.

## Boolean Values

Boolean values evaluate to True or False. You can see how Jupyter highlights these keywords:



boolTrue = True
boolFalse = False


Integers, floats and strings can be evaluated to a boolean value by using the <code>bool()</code> function.

All non-zero numbers evaluate to <code>True</code> whilst 0 evaluates to <code>False</code>:


```python
bool(0)
```




    False




```python
bool(0.00000000001)
```




    True




```python
bool(10)
```




    True



All non-empty strings evaluate to <code>True</code>, whilst an empty string evaluates to <code>False</code>:


```python
bool("hi")
```




    True




```python
bool(' ')
```




    True




```python
bool('')
```




    False



## And, Or and Not

You can also create more complex boolean expressions by using <code>and</code>, <code>or</code> and <code>not</code> to compare multiple expressions.

<code>and</code> only returns <code>True</code> if all the boolean expressions evaluate to <code>True</code>:


```python
print(True and True)
```

    True
    


```python
print(True and False)
```

    False
    


```python
print(True and True and True and True and False)
```

    False
    

<code>or</code> returns <code>True</code> if at least one expression evalutes to <code>True</code>:


```python
print(True or False)
```

    True
    


```python
print(False or False)
```

    False
    


```python
print(False or False or False or False or True)
```

    True
    

<code>not</code> inverts the boolean expression; <code>True</code> becomes <code>False</code> and vice versa:


```python
print(not True)
```

    False
    


```python
print(not False)
```

    True
    


```python
print(not(True and True))
```

    False
    

You can use brackets to create complex expressions. What do you think this evaluates to?


```python
print(not (True or False) and not(False and True))
```

    False
    

## Logical comparisons

We've just seen the basics of boolean values, however comparing <code>True</code> and <code>False</code> isn't particularly useful. The power of boolean values lies in how we can use them to compare values.

In Python, we can test for equality by using the <code>==</code> symbol; this test for equality returns a boolean value:


```python
5 == 5
```




    True




```python
5 == 10
```




    False



We can also test for inequality using <code>!=</code>; this also returns a boolean value:


```python
1 != 2
```




    True




```python
1 != 1
```




    False



<code>==</code> and <code>!=</code> both work on strings:


```python
'hi' == 'hi'
```




    True




```python
'hi' != 'ho'
```




    True



We can test if a number is greater than another number using <code>></code>:


```python
5 > 4
```




    True




```python
5 > 10
```




    False



We can test if a number is greater than or equal to another number by using <code>>=</code>


```python
5 >= 4
```




    True




```python
5 >= 5
```




    True




```python
5 >= 6
```




    False



We can also test if a number is less than another number by using <code>&lt;</code>:


```python
5 < 4
```




    False




```python
10 < 100
```




    True



An we can test if a number is less than or equal to another number by using <code>&lt;=</code>:


```python
5 <= 7
```




    True




```python
5 <= 5
```




    True




```python
5 <= 4
```




    False



We can also do these comparisons on strings. Python compares the first two items in the string and if they differ, this determines the outcome of the comparison. If they're the same, the next two items are compared:


```python
'a' < 'b'
```




    True




```python
'hi' < 'ho'
```




    True




```python
'z' < 'x'
```




    False



### Combining comparisons with And, Or and Not

We now know how to create complex comparisons of strings and numbers. For the following examples, try to figure out what the answer will be before you run the cell.


```python
1 != 3 and 2 == 5
```




    False




```python
"test" != "testing" and 5 == 5
```




    True




```python
"one" == 1
```




    False




```python
not (True and False)
```




    True




```python
not (4 == 4 and 0 != 10)
```




    False



