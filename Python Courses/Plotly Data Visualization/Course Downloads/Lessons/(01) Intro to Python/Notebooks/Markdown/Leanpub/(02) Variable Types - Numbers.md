
#  Variable Types - Numbers

In the last class we saw how to assign values to variables using the `=` symbol. We also learnt what a valid variable name is. 

In this lesson we'll look at two of the different types of value which can be assigned to a variable; `integers` and `floats`. We'll also see how the different mathematical operators work.

Python supports three different types of number; integer, float and complex. We won't concern ourselves with complex numbers in this course.

### Integers

An integer is a whole number, without a decimal point. We can use the `type()` function to see what type a variable is:



integer1 = 10

print(type(integer1))


    <class 'int'>
    

### Floats

A floating point number is a number with a decimal point:



		~~~~~~~~
float1 = 0.5

print(type(float1))
~~~~~~~~

    <class 'float'>
    

You can convert integers to floats, and vice versa.

Here, I'll convert an integer to a float using the `int()` function:



		~~~~~~~~
integer2 = int(2.1)

print(integer2)
~~~~~~~~

    2
    

It looks like the `int()` function rounded down; what happens when the first decimal number is greater than 5?



		~~~~~~~~
integer3 = int(2.9)

print(integer3)
~~~~~~~~

    2
    

So, we now know that the `int()` function chops off the decimal part of the number and doesn't round the part before the decimal.

Let's convert an integer to a float and see what happens:



		~~~~~~~~
float2 = float(5)

print(float2)
~~~~~~~~

    5.0
    

Using the `float()` function adds a decimal place to an integer.

### Addition, Subtraction, Division, Multiplication... and a couple more

We can do maths really easily in Python.

#### Addition
Here, I'm going to add two numbers together:



		~~~~~~~~
subTotal = 5 + 5
print(subTotal)
~~~~~~~~

    10
    

I can also add a number to a variable:



		~~~~~~~~
total = subTotal + 20
print(total)
~~~~~~~~

    30
    

#### Subtraction
We can subtract numbers:



		~~~~~~~~
stockToday  = 100 - 20
print(stockToday)
~~~~~~~~

    80
    

And we can also subtract numbers from variables:



		~~~~~~~~
salesToday = 40

stockTomorrow = stockToday - salesToday

print(stockTomorrow)
~~~~~~~~

    40
    

#### Multiplication
We can do multiplication:



		~~~~~~~~
avgLenOfWord = 9

avgLenOfSentence = 12

avgLettersInASentence =  avgLenOfWord * avgLenOfSentence

print(avgLettersInASentence)
~~~~~~~~

    108
    

#### Division
And we can do division:

(division always results in a floating point number)



		~~~~~~~~
amountOfSpaghetti = 1000

numberOfPeople = 10

spaghettiPerPerson = amountOfSpaghetti / numberOfPeople

print(spaghettiPerPerson)
~~~~~~~~

    100.0
    

#### Modulus
We can also get the remainder of a number when it is divided by another number:



		~~~~~~~~
remainder = 10 % 3

print(remainder)
~~~~~~~~

    1
    

#### Exponents
We can raise a number by a power:



		~~~~~~~~
startingRabbits = 2

numberOfDays = 3

finalRabbits = startingRabbits ** numberOfDays

print(finalRabbits)

~~~~~~~~

    8
    

#### Floor division

We can remove the decimal points when a division is not exact:



		~~~~~~~~
print(11 / 3)
~~~~~~~~

    3.6666666666666665
    



		~~~~~~~~
print(11 // 3)
~~~~~~~~

    3
    

## What have we learnt in this lesson?
In this lesson we've learnt about integers and floats in Python, and how to convert between the two. Finally, we learnt how to use mathematical operators to manipulate numbers and variables.

If you have any questions, please ask in the comments section or email <a href="mailto:me@richard-muir.com">me@richard-muir.com</a>