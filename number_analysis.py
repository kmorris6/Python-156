#Kate Morris
#PA_4

import random #Import keyword and name of module to use the random function
fir_ran = list(range(-100,101)) #Name a list that has a range from -100 to 100
#Need to type a range from -100 to 101 to include 100
sec_ran = random.sample(fir_ran,k=20) #Set a new variable to display a random sample of 20 integers within the range of -100 and 100
print('The list contains: ',sec_ran) #Print the list of 20 random integers

mini_num = min(sec_ran) #Print the minimum value of the random sample list
print('The lowest number is: ',mini_num)

maxi_num = max(sec_ran) #Print the maximum value of the random sample list
print('The highest number is: ',maxi_num)

total = sum(sec_ran) #Print the sum up the numbers of the random sample list
print('The sum of the numbers in the list is: ',total)

average = total / len(sec_ran) #Print the average of the random sample list
print('The average of the numbers in the list is: ',average)








    









 


