
#  Variable Types - Strings (1)

In the last class we learnt about <code>integers</code> and <code>floats</code> in Python. We also learnt how to do different mathematical operations, some of which you may not have come across before, such as the modulus function.

In this lesson we're going to learn about <code>strings</code>. A string is another name for a variable which contains text, rather than numbers. We're going to learn how to create string variables, how to convert between string, integer and float, and finally how to use mathematical operators on strings.

### Strings

A string is several characters enclosed by single or double quotation marks:



'This is a string'





    'This is a string'




```python
"This is also a string"
```




    'This is also a string'



Strings which contain a single quotation mark must be enclosed by double quotation marks:


```python
'This doesn't work'
```


      File "<ipython-input-3-dee2dc12bc4d>", line 1
        'This doesn't work'
                    ^
    SyntaxError: invalid syntax
    



```python
"It didn't work, anyway"
```




    "It didn't work, anyway"



Likewise, strings which contain a double quotation mark must be enclosed by single quotation marks:


```python
'He said "I never wanted that to happen"'
```




    'He said "I never wanted that to happen"'



Strings which contain both types of quotation mark must be enclosed by 3 single quotation marks:


```python
'''He said "I didn't want that to happen"'''
```




    'He said "I didn\'t want that to happen"'



You can see that Python has converted our triple quotation marks into just single quotation marks, and included a <code>\</code>. This is called an 'escape character'; Python uses this to decide whether or not to process the following character as text string or as code. 

In this case, the escape character tells Python to process the apostrophe as a text string.

## Converting between strings, integers and floats

As with integers and floats, we can convert strings into other data types. This is slightly more complex than converting between integers and floats.

Some strings can be converted into integers and floats:


```python
string1 = "5"

testVarInt1 = int(string1)

print(testVarInt1)
```

    5
    


```python
testVarFloat1 = float(string1)

print(testVarFloat1)
```

    5.0
    

And others can't, even though they look like they can:


```python
string2 = "5.0"

testVarInt2 = int(string2)

print(testVarInt2)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-47cbf35cdb73> in <module>()
          1 string2 = "5.0"
          2 
    ----> 3 testVarInt2 = int(string2)
          4 
          5 print(testVarInt2)
    

    ValueError: invalid literal for int() with base 10: '5.0'



```python
testVarFloat2 = int(string2)

print(testVarFloat2)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-10-23c1894ef386> in <module>()
    ----> 1 testVarFloat2 = int(string2)
          2 
          3 print(testVarFloat2)
    

    ValueError: invalid literal for int() with base 10: '5.0'


And some can't, and definitely shouldn't:


```python
string3 = 'Hello World!'

print(int(string3))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-a852bd737cc4> in <module>()
          1 string3 = 'Hello World!'
          2 
    ----> 3 print(int(string3))
    

    ValueError: invalid literal for int() with base 10: 'Hello World!'


We can also convert integers and floats into strings using the <code>str()</code> function:


```python
int1 = 5

string4 = str(int1)

print(type(string4))
```

    <class 'str'>
    


```python
float1 = 6.77779

string5 = str(float1)

print(type(string5))
```

    <class 'str'>
    

## Mathematical operators and strings

We can also use mathematical operators on strings. This might seem counterintuitive at first...


```python
string1 = "This is a test"

string2 = string1 + '. ' + string1

print(string2)
```

    This is a test. This is a test
    


```python
string3 = 'Hi'
string4 = 'Ho'

print((string3 + string4 + ', ') * 2 + "it's off to work we go.")
```

    HiHo, HiHo, it's off to work we go.
    

But not all of the mathematical operators make sense:


```python
print(string3 - 5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-a04a62121e8e> in <module>()
    ----> 1 print(string3 - 5)
    

    TypeError: unsupported operand type(s) for -: 'str' and 'int'



```python
print(string3 ** 5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-17-64ee776f3f99> in <module>()
    ----> 1 print(string3 ** 5)
    

    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'



```python
print(string3 / 5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-461b4b4d33df> in <module>()
    ----> 1 print(string3 / 5)
    

    TypeError: unsupported operand type(s) for /: 'str' and 'int'


## What have we learnt in this lesson?
In this lesson we've learnt about strings in Python. We've seen how to create strings and when to use single quotes and double quotes and we've learnt a little bit about escape characters. 

We've also learnt how to change between strings, integers and floats, but that this doesn't always work. We've seen how to apply mathematical operators to strings, but that this is only possible with addition and multiplication.

In the next lesson we'll learn how to index and slice strings, as well as how to implement some common functions, such as the <code>len()</code> function.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>