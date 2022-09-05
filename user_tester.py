#Kate Morris
#PA_9

import user_class as uc #import where the class file is stored and assign a variable to refer to it later on

print('User Input:') #prompt the user to enter the below data
firstName = input('Enter the first name: ') #prompt the user to enter the first name and store it in firstName
lastName = input('Enter the last name: ') #prompt the user to enter the last name and store it in lastName
userId = input('Enter the userID: ') #prompt the user to enter the userID and store it in userId
password = input('Enter password: ') #prompt the user to enter the password and store it in password

user = uc.User(firstName,lastName,userId,password) #create an object of the User class called user and reference the file that the User class is in and specify each data attribute so they can be called upon

print('\nUser information:') #access the information stored in User class
print('First name: ',user.firstName) #use the 'user' object and call upon the data attribute within the object and print it
print('Last name: ',user.lastName) #the following lines contain the 'user' object and having each data attribute being called upon and printed using the 'print' function
print('UserId:',user.userId)
print('Password:',user.password)

