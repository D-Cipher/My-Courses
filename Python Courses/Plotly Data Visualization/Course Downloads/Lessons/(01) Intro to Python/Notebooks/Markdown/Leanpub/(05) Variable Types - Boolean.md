
# Variable Types - Boolean

In the last lesson we learnt how to index and slice strings. We also learnt how to use some common string functions such as the `len()` function.

In this lesson, we'll learn about Boolean values. Boolean values evaluate to either True or False and are commonly used for comparisons of equality and inequality, as well as controlling the flow of a program.

## Boolean Values

Boolean values evaluate to True or False. You can see how Jupyter highlights these keywords:



boolTrue = True
boolFalse = False


Integers, floats and strings can be evaluated to a boolean value by using the `bool()` function.

All non-zero numbers evaluate to `True` whilst 0 evaluates to `False`:



		~~~~~~~~
bool(0)
~~~~~~~~




    False





		~~~~~~~~
bool(0.00000000001)
~~~~~~~~




    True





		~~~~~~~~
bool(10)
~~~~~~~~




    True



All non-empty strings evaluate to `True`, whilst an empty string evaluates to `False`:



		~~~~~~~~
bool("hi")
~~~~~~~~




    True





		~~~~~~~~
bool(' ')
~~~~~~~~




    True





		~~~~~~~~
bool('')
~~~~~~~~




    False



## And, Or and Not

You can also create more complex boolean expressions by using `and`, `or` and `not` to compare multiple expressions.

`and` only returns `True` if all the boolean expressions evaluate to `True`:



		~~~~~~~~
print(True and True)
~~~~~~~~

    True
    



		~~~~~~~~
print(True and False)
~~~~~~~~

    False
    



		~~~~~~~~
print(True and True and True and True and False)
~~~~~~~~

    False
    

`or` returns `True` if at least one expression evalutes to `True`:



		~~~~~~~~
print(True or False)
~~~~~~~~

    True
    



		~~~~~~~~
print(False or False)
~~~~~~~~

    False
    



		~~~~~~~~
print(False or False or False or False or True)
~~~~~~~~

    True
    

`not` inverts the boolean expression; `True` becomes `False` and vice versa:



		~~~~~~~~
print(not True)
~~~~~~~~

    False
    



		~~~~~~~~
print(not False)
~~~~~~~~

    True
    



		~~~~~~~~
print(not(True and True))
~~~~~~~~

    False
    

You can use brackets to create complex expressions. What do you think this evaluates to?



		~~~~~~~~
print(not (True or False) and not(False and True))
~~~~~~~~

    False
    

## Logical comparisons

We've just seen the basics of boolean values, however comparing `True` and `False` isn't particularly useful. The power of boolean values lies in how we can use them to compare values.

In Python, we can test for equality by using the `==` symbol; this test for equality returns a boolean value:



		~~~~~~~~
5 == 5
~~~~~~~~




    True





		~~~~~~~~
5 == 10
~~~~~~~~




    False



We can also test for inequality using `!=`; this also returns a boolean value:



		~~~~~~~~
1 != 2
~~~~~~~~




    True





		~~~~~~~~
1 != 1
~~~~~~~~




    False



`==` and `!=` both work on strings:



		~~~~~~~~
'hi' == 'hi'
~~~~~~~~




    True





		~~~~~~~~
'hi' != 'ho'
~~~~~~~~




    True



We can test if a number is greater than another number using `>`:



		~~~~~~~~
5 > 4
~~~~~~~~




    True





		~~~~~~~~
5 > 10
~~~~~~~~




    False



We can test if a number is greater than or equal to another number by using `>=`



		~~~~~~~~
5 >= 4
~~~~~~~~




    True





		~~~~~~~~
5 >= 5
~~~~~~~~




    True





		~~~~~~~~
5 >= 6
~~~~~~~~




    False



We can also test if a number is less than another number by using `&lt;`:



		~~~~~~~~
5 < 4
~~~~~~~~




    False





		~~~~~~~~
10 < 100
~~~~~~~~




    True



An we can test if a number is less than or equal to another number by using `&lt;=`:



		~~~~~~~~
5 <= 7
~~~~~~~~




    True





		~~~~~~~~
5 <= 5
~~~~~~~~




    True





		~~~~~~~~
5 <= 4
~~~~~~~~




    False



We can also do these comparisons on strings. Python compares the first two items in the string and if they differ, this determines the outcome of the comparison. If they're the same, the next two items are compared:



		~~~~~~~~
'a' < 'b'
~~~~~~~~




    True





		~~~~~~~~
'hi' < 'ho'
~~~~~~~~




    True





		~~~~~~~~
'z' < 'x'
~~~~~~~~




    False



### Combining comparisons with And, Or and Not

We now know how to create complex comparisons of strings and numbers. For the following examples, try to figure out what the answer will be before you run the cell.



		~~~~~~~~
1 != 3 and 2 == 5
~~~~~~~~




    False





		~~~~~~~~
"test" != "testing" and 5 == 5
~~~~~~~~




    True





		~~~~~~~~
"one" == 1
~~~~~~~~




    False





		~~~~~~~~
not (True and False)
~~~~~~~~




    True





		~~~~~~~~
not (4 == 4 and 0 != 10)
~~~~~~~~




    False


