#Kate Morris
#PA_1


#A car's miles-per-gallon (MPG) can be calculated with the following formula:
#MPG = Miles driven / Gallons of gas used.

#Write the program that prompts the user for the number of miles driven and the gallons of gas used.
#It should calculate the car's MPG and display the result with 2 places to the right decimal point.
#The miles driven and gallons of gas used should be floats.


#Make a variable for the number of miles driven with a floating point number.
MDriven=float(input('Enter the miles driven: ')) #prompts user to enter miles driven

#Make a variable for the number of gallons of fuel used with a floating point number. 
GFuel=float(input('Enter gallons of fuel used: ')) #prompts user to enter gallons of fuel used.

#Calculate the miles per gallon using the equation: MPG: Miles Driven / Gallons of fuel used
MPG=MDriven/GFuel

#Print the MPG to two decimal places.
print(f'Your mpg was: {MPG:.2f}')


