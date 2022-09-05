#Kate Morris
#PA_11

import random #import random to generate the random list of integers below
input_list = [] #list for the random input values
for i in range(200): 
    i = random.randint(50,120) #random values will be found between 50 and 120
    input_list.append(i) #add value to the list using .append

import matplotlib.pyplot as pyp #import matplotlib to show the plot

print(f'The input list: {input_list}') #print the input list values

s_val = [] #list the values that are above 100
for i in input_list:
    if(i>=100): #set the parameter that if the value is greater than 100, add the value to the list labeled s_val
        s_val.append(i)

x_val = []
y_val = []

x_val = list(set(s_val)) #store the values greater than 100 in a list, using set() will remove duplicate values

pyp.hist(s_val,len(x_val),align='mid',rwidth=0.8,color='Blue') #create histogram plot with the list of values
pyp.xlabel('Temperature') #set the x axis label
pyp.ylabel('Number of days') #set the y axis label
pyp.xticks(x_val)
pyp.title('High Temperature >= 100 degrees in East Mesa for 2020') #set the title for the plot
pyp.show() #print the histogram

