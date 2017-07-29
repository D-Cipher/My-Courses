
# Pie Charts (1) - Introduction to pie charts

In this lesson we're going to learn about pie charts. We'll find out what kind of data they are used to represent and in what situations they should be used. We'll also learn about some of the things we should and shouldn't do when making pie charts.

We'll then briefly look at some of the topics we'll cover in this section.

## What is a pie chart?

A pie chart is a circular chart which is used to display categorical data where the different categories comprise parts of a whole. The area of the circle is divided into segments that each represent a proportion of a whole.

Pie charts have a bad reputation in some circles (pun intended), and you can find several articles which recommend against using them. The two most common (and strong) arguments are that:

1. You cannot easily compare the size of two sections
2. They are only useful for showing limited numbers of categories

The ONS has <a href="https://style.ons.gov.uk/category/data-visualisation/charts/">excellent guidelines</a> on how to produce clear and meaningful visualisations, and I'll take you through some of their examples on pie charts. I would however highly recommend reading the article in its entirety.

## Making clear pie charts

A pie chart should be used when there are very few categories; any more than 6 and it will become difficult to read. They should also only be used when there is a large distinction between one of the categories. For example, it is quite difficult to tell which category is the largest in this pie chart without conciously comparing the numbers:

<img src="http://www.neighbourhood.statistics.gov.uk/HTMLDocs/style/Chart66.svg" height="400px" width="400px"/>

But this bar chart (which shows the same data) shows it in a much clearer way:
<img src="http://www.neighbourhood.statistics.gov.uk/HTMLDocs/style/Chart67.svg" height="400px" width="400px"/>

You should also rank the categories from smallest to largest and make sure that the first segment starts at the 12 o'clock position.

Pie charts have also gotten a bad reputation through people's unscrupulous use of 3D pie charts. These are highly misleading and should never be used!

Take these examples from the ONS guidelines. Categories A and B look to be almost equal when plotted in 3D, but are in fact very different. This is clear when they are plotted in 2D:

3D pie chart:
<img src="http://www.neighbourhood.statistics.gov.uk/HTMLDocs/style/Chart32.png"  height="400px" width="400px"/>

Data plotted in 2D:
<img src="http://www.neighbourhood.statistics.gov.uk/HTMLDocs/style/Chart33.svg"  height="400px" width="400px"/>


## What are we going to learn in this section?

In this section we're going to find out how to style a pie chart and use this styling to highlight individual sections. We'll  also learn how to display text and labels on a pie chart. We'll also see how to include a pie chart on a sub plots object. Finally, we'll learn how to create a donut chart.