#Cost Per Port Documentation

The following guide is a documentation of the assumptions, process, and modeling that went into NSI's cost per port analysis for 2016.

##Model Assumptions
Cost per port is an attempt to estimate the level of cost effeciency against delivering the most customer value. Cost per port is calculated by taking the total cost of a category item in a given time frame divided by the estimated total ports opened in that time frame. 

For example, in the East Coast the cost per port for labor in January is calculated by taking the total January labor cost and dividing by the estimated ports opened for January in the East Cost. This was \$43.80, meaning for each port we opened it cost us about \$43.80 in labor.

'''
Cost per port = Cost ($) / Est. Number of ports

'''

There are several key assumptions that we must make in order to determine cost per port. First, we are making the assumption that number of ports opened represent customer value delivery. Ports are an endpoint of communication and we uses the expanding of those connections as a benchmark. Secondly, the data that we have is financial data, which has limitations. The most important limitation is it cannot fully represent actual ports opened. We can only estimate the number of ports based on the type and number of cables purchased. Further, this presents another assumption that the number of cables purchased translates to port value. Again, from the data there is not a way to determine if all or a certain percentage of the cables purchased were used. Hence, the number of ports is an estimate based on purchases and not on direct observations. 

##Data Attributes
The data is a normal data frame extracted from our financials for 2016. Each observation represents a specific item in a purchase order that was executed in 2016. The key variables pulled include: 
1. The description of the item that was purchased (the specific cable, specific labor used, infrastructural purchases, etc).
2. The quantity of the item.
3. The total cost of the item.
4. If the item was a cable, then the total number of strands on that cable.
5. Location of the purchase, CAR.
6. Date of the purchase.

##Extrapolated Assumptions
There were several important varaibles that were extrapolated from these data pulls, including: 
1. The category of the item (Cable, Labor, Infrastructure, etc), derived from the item description.
2. If the item was a cable then the type of cable (Jumper, Trunking, MTP, Pigtail, etc), this was also derived from the item description.
3. If the item was a cable then the estimated number of ports.

The estimated number of ports is calculated by taking the cable's strand count and multiplying by the quantity for cables: LC-LC SMF Jumpers, LC-LC SMF Trunks, SC cables, Armored Trunks, and Armored Jumpers, and Fan-out Pigtails. For all MTP, QSFP, and other/unknown cables, the strand value is irrelevant so port value is just the quantity. For Copper, Power Cables, and Non-Fan-out Pigtails, they do not provide additional port value.

