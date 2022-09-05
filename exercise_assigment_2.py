#Kate Morris
#EA_2

# CHAPTER 2 EXERCISES

# Set x equal to an integer value (1 pt.).
x =76

# Write an if statement that assigns 15 to the variable y,
# and assigns 25 to the variable z if the variable x is greater than 75
# Print y and z (3 pts.).
if x>75:
    y=15
    z=25
    print(y, z)

# Set a equal to an integer value (1 pt.).
a =50

# Write an if-else statement that assigns 5 to the variable b if the variable a is less than 20.
# Otherwise, it should assign 99 to the variable b.
# Print b (4 pts.).
if a<20:
    b1=5
    print(int(b1))
else:
    b2=99
    print(int(b2))

# Set speed equal to an integer value (1 pt.)
speed =55

# Write an if-else statement that prints 'Speed is normal' if the speed variable is within the range of 45 to 65 (Hint: use and). If the speed variable’s
# value is outside this range, print 'Speed is abnormal' (4 pts.).
if speed>=45 and speed<=65:
    print('Speed is normal')
else:
    print('Speed is abnormal')

# Set points equal to an integer value (1 pt.)
points =105

# Write an if-else statement that determines whether the points variable is outside the range of 5 to 46 (Hint: use or). If the variable’s value is
# outside this range it should print 'Invalid points.' Otherwise, it should print 'Valid points.' (4 pts.)
if points<5 or points>46:
    print('Invalid points.')
else:
    print('Valid points.')

# Write a while loop that prompts the user with text to enter a whole number. The number should be multiplied by 10, and the result
# added to a variable named product. The loop should iterate as long as product is less than 100. Print product after exiting the while loop (6 pts.).
product = 0 # DO NOT DELETE THIS LINE OF CODE, USE THE VARIABLE IN THE WHILE LOOP
nProduct = 'y'
while nProduct == 'y':
    num1 = int(input('Enter a whole number: '))
    nProduct = num1*10+product
    StopLoop = input('Do you want to enter another whole number (Enter y for yes): ')
    print('The end product is ' + str(nProduct))

# Write a for loop that prints the following set of numbers: 0 10 20 30 40 50 . . . 100 on one line (3 pts.).
for num in range(0, 110, 10):
    print(num)

# Write a for loop that prints the numbers 1 through 5, each on a seperate line (2 pts.).
print() # DO NOT DELETE THIS LINE OF CODE, ADD YOUR ANSWER AFTER THE PRINT STATEMENT
for a in range(1,6):
    print(str(a))
