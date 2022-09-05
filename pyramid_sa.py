#Kate Morris
#PA_3

from math import sqrt #Import sqrt from math for surface area calculation
def calculate_area(l,w,h): #Define a variable to later input values
    Area = l*w +l*sqrt((w/2)*(w/2) +h*h) + w*sqrt((l/2)*(l/2) +h*h) 
    return Area 

l = float(input("Enter the pyramid's length: ")) #Prompts user to enter pyramids length
w = float(input("Enter the pyramid's width: ")) #Prompts user to enter pyramids width
h = float(input("Enter the pyramid's height: ")) #Prompts user to enter pyramids height

sa = calculate_area(l,w,h) #Assign surface area to the variable 'sa' 
print(f'The surface area of the right rectangular pyramid is {sa:.2f}') #Print the surface area of the right rectangular pyramid to two decimal places
