
# Tables (5) - Styling the text in a table

In this lesson we're going to learn how to style the text in a table.

We're going to focus on three specific styling options:
1. Changing the font family, size and color
2. Thousand-separating numbers
3. Right-aligning numbers

Doing these three things will allow us to more closely follow the recommendations set out in the first lesson in this section. We want to make our tables as easy as possible to read, and by changing these parameters we can hopefully achieve this.



#### New Modules:

Figure Factory:



from plotly.tools import FigureFactory as FF



```python

 
```





## Changing the font:

Let's get the table we worked on in the last lesson:


```python
table = py.get_figure("rmuir", 313)
pyo.iplot(table)

![pyo.iplot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-0.png)```





As we learnt previously, the text in the tables is stored as annotations in the layout section of the figure.

We can therefore loop through the list of annotations and apply the styling options as necessary. We'll probably want to style the header/index annotations differently to the those which show data, however there is no direct way to identify which annotation is a header/index and which belongs in a row. 

We can see that the header and index items are shown in bold in the table. To find out which items are in the header/index, let's loop through the annotations and look for <code>'&lt;b&gt;'</code>:


```python
for ann in table['layout']['annotations']:
    if '<b>' in ann['text']:
        print('HEADER/INDEX: {}'.format(ann['text']))
    else:
        print('ROW DATA: {}'.format(ann['text']))
```

    HEADER/INDEX: <b>Country</b>
    HEADER/INDEX: <b> </b>
    HEADER/INDEX: <b>Population (2011)</b>
    HEADER/INDEX: <b>  </b>
    HEADER/INDEX: <b>Area</b>
    HEADER/INDEX: <b>   </b>
    HEADER/INDEX: <b>England</b>
    ROW DATA: 
    ROW DATA: 53012456
    ROW DATA: 
    ROW DATA: 130,395 km²
    ROW DATA: 
    HEADER/INDEX: <b>Scotland</b>
    ROW DATA: 
    ROW DATA: 5295000
    ROW DATA: 
    ROW DATA: 78,772 km²
    ROW DATA: 
    HEADER/INDEX: <b>Wales</b>
    ROW DATA: 
    ROW DATA: 3063456
    ROW DATA: 
    ROW DATA: 20,779 km²
    ROW DATA: 
    HEADER/INDEX: <b>Northern Ireland</b>
    ROW DATA: 
    ROW DATA: 1810863
    ROW DATA: 
    ROW DATA: 13,843 km²
    ROW DATA: 
    

We've previously learnt how to format text in annotations, so let's just make a small change as proof that it works. I'll change the colour of the data items from black to a dark grey, and the colour of the header/index from white to a light grey:


```python
for ann in table['layout']['annotations']:
    if '<b>' in ann['text']:
        ann['font']['color'] = '#f1f1f1'
    else:
        ann['font']['color'] = '#333'
pyo.iplot(table)
`
![pyo.iplot-1](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-1.png)``





## Formatting numbers with a thousand-separator

To improve readability, one of the simplest and most effective things you can do is to add in a thousand-separator between numbers.

The reason this is so effective is because it separates the number into smaller, more readable chunks.

For example:

53,865,800

is much easier to read than:

53865800

Let's add in thousand separators to the numbers in the Population column. We need to loop through the annotations again, and by checking if we can successfully convert the text of that annotation to an integer (or float), we can extract only the numbers from the table.

We'll do this in a <code>try-except</code> statement. This statement tries to execute some code, but if it code produces an error of the stated type, it simply carries on, rather than breaking:


```python
for ann in table['layout']['annotations']:
    try:
        print(int(ann['text']))
    except: 
        ValueError
```

    53012456
    5295000
    3063456
    1810863
    

Now that we've used this statement to isolate only the numbers, let's format them with a thousand separator:


```python
for ann in table['layout']['annotations']:
    try:
        ann['text'] = "{:,}".format(int(ann['text']))
    except: 
        ValueError
```


```python
pyo.iplot(table)
``
![pyo.iplot-2](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-2.png)`





Much better! The population numbers are much easier to compare now.

## Right-aligning numbers

Another way to make our tables easier to read is by right-aligning the numbers. This makes it much easier to visually compare the size of a number because all of the digits line up.

For left-aligned numbers, this is more difficult. Compare this:  
10,000  
100  

With this:  
<p style="text-align : right;">10,000<br>100</p>  

The digits in the 1, 10 and 100 position all line up with right-aligned numbers.

Let's right-align the text in our table. This is not as straightforward as adding a thousand-separator. First of all, we have to find the columns with numbers in.

Here is a quick function to check if a string has a number in:


```python
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
```

Let's loop through the data in our table and check which cells have numbers in.

We want to right align the column headings and data for the Population and Area columns. We know that the Area column title doesn't contain any numbers, so we can specify that directly:


```python
for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        print(ann['text'])
```

    <b>Population (2011)</b>
    <b>Area</b>
    53,012,456
    130,395 km²
    5,295,000
    78,772 km²
    3,063,456
    20,779 km²
    1,810,863
    13,843 km²
    

Let's now change the <code>'xanchor'</code> property of those annotations and see how that changes the alignment. We'll definitely have to move the annotation as well, but this is a good start:


```python
for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['xanchor'] = 'right'
        
pyo.iplot(table)
```
![pyo.iplot-3](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-3.png)





This has moved all the annotations to the left, because the right-hand side of the annotation is now anchored to the position of the annotation. We now need to move the annotations to the right. 

From looking at the annotations, the x-values for the position have a spacing of 1. Let's try adding 1 to each x-position and see how that moves the annotations:


```python
for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['x'] = ann['x'] + 1
pyo.iplot(table)
```

![pyo.iplot-4](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-4.png)




That's moved them a bit too far to the right; we can see some faint lines behind the numbers. Let's move them left by 0.1 for a total movement of 0.9 to the right.

Remember that this will likely be different for every table that you make. Try out some different values until it looks right to you.


```python
for ann in table['layout']['annotations']:
    if hasNumbers(ann['text']) or 'Area' in ann['text']:
        ann['x'] = ann['x'] - 0.1
pyo.iplot(table)
```


![pyo.iplot-5](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/pyo.iplot-5.png)



That's much better! Let's send this to the Plotly cloud:


```python
py.plot(table, filename="UK Population Table (right-align)", fileopt = 'overwrite')
```



![py.plot-0](http://www.richard-muir.com/images/courses/data-viz-plotly-python/testSection/Tables%20(5)%20-%20Styling%20the%20text%20in%20a%20table/py.plot-0.png)

    'https://plot.ly/~rmuir/309'



