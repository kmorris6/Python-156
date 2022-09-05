# Kate Morris
# PA_11

import matplotlib.pyplot as pyp #import matplotlib to plot graphs
import math #import the math library for finding base 2 numbers

oddnums=[i for i in range(1,100,2)] #find the odd numbers for range 1 to 100 in increments of 2 and label it the variable oddnums
base2_odd = [math.log2(i) for i in oddnums] #for each value that comes from oddnums, this will find the base 2 log
colors = [i for i in range(50,len(oddnums)+50)] #create a color map list of the 50 numbers
limit = [int(min(oddnums)) , int(max(oddnums))+1, math.floor(int(min(base2_odd))),math.ceil((max(base2_odd)))] #make a list of values which has min, max values for X and Y
#using math.floor will show the lowest number and math.ceil will show the maximum number

pyp.scatter(oddnums,base2_odd ,c=colors,cmap='Greens') #scatter plot with the x and y using the list of odd numbers and assigning the color green for the plot
pyp.axis(limit) #set the axis limits
pyp.xlabel('Value') #apply the x axis label
pyp.ylabel('base-2 logarithm Value') #apply the y axis label
pyp.title('Plot showing the base-2 lagarithm of odd numbers 1 through 100') #apply the plot title
pyp.show() #print the plot

