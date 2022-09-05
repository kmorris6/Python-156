#Kate Morris
#exercise_assignment_3

# CHAPTER 3 EXERCISES

# Write a function called greeting that prints the following: 'Hello, how are you today?' (3 pts.).
def greeting():
    print('Hello, how are you today?')

# Write a statement to call the greeting function (1 pt.)
greeting()

# Write a function named times_ten. The function should accept an argument and
# print the product of its argument multiplied times 10 (3 pts.).
def times_ten(num1):
    product = num1*10
    print('The product is',product)
    
# Write a statement to call the times_ten function passing in an argument of 15.3 (1 pt.).
times_ten(15.3)

# Write a statement to call the three_args function passing in an int value of 5 that will be assigned to parameter a,
# a float value of 13.2 that will be assigned to parameter b, and an int value of -8 that will be assigned
# to parameter c (3 pts.)
def three_args(a, b, c): # DO NOT DELETE OR UPDATE THIS FUNCTION
    answer = a + b * c
    print(answer)

a = int(5)
b = float(13.2)
c = int(-8)

three_args(5,13.2,-8)

# A program contains the cube function.
# Write a statement that passes the value 6 to the cube function and assigns its return value to the variable result (2 pts.).
def cube(num): # DO NOT DELETE OR UPDATE THIS FUNCTION
    return num * num * num
num = 6
result = cube(num)

# Write a statement to print the value of result (1 pt.)
print('The result is', result)

# Write a function named times_five that accepts a number as an argument. When the function is called,
# it should return the value of its argument multiplied times 5 (3 pts.).
def times_five(Nnum):
    return (Nnum*5)
Nnum = float(input('Enter a number: '))
Fnum = Nnum*5
print('The result is',Fnum)

# Write a statement that passes num1 to the times_five function and assigns its return value to the variable result_one (2 pts.).
num1 = 6 # DO NOT DELETE THIS LINE OF CODE, ADD YOUR ANSWER AFTER THIS LINE
result_one = times_five(num1)

# Write a statement to print the value of result_one (1 pt.)
print('The value of result_one is', result_one)

