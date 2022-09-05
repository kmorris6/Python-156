#Kate Morris
#exercise_assignment_4

# CHAPTER 4 EXERCISES

# Set registeration_list = to an empty list (1 pt.).
registration_list =[]

# Add Sara to the list using the append function, print the list (2 pts.).
registration_list.append('Sara')
print(registration_list)

# Add Adam to the list using the append function, print the list (2 pts.).
registration_list.append('Adam')
print(registration_list)

# Add Jaqueline, Seth and Juan to the list using the += augmented assignment
# operator using 1 line of code (2 pts.).
registration_list+='Jaqueline','Seth','Juan'

# Replace Jaqueline with Salma in the list using a single line of code (1 pt.).
registration_list[2] = 'Salma'

# Use a for in loop to print the names in the list (2 pts.).
for registration in range(1):
    print(registration_list)
    
# Write an if statement using in to determine if Seth is in the list.  If Seth is in the list,
# print out: Seth is registered. (2 pts.).
if 'Seth' in registration_list:
	print('Seth is registered.')

# Use indexing to print the name Sara (1 pt.).
print(registration_list[0])

# Use slicing to print the names Salma, Seth (2 pts.).
print(registration_list[2:4])

# Use slicing to print the names Seth, Juan (2 pts.).
print(registration_list[3:5])

# Use negative indexing and slicing to print the names Adam, Salma (2 pts.).
print(registration_list[-4:-2])

# Print the length of the list (1 pt.).
len(registration_list)

# Remove Seth from the list using the del statement (1 pt.).
del registration_list[3]

# Insert Penelope into the list as the second element, print the list (2 pts.).
registration_list.insert(1, 'Penelope')
print(registration_list)

# Print the index of Adam in the list (1 pt.).
registration_list.index('Adam')

# Remove Sara from the list using the remove method (1 pt.).
registration_list.remove('Sara')

# Sort the values in the list in reverse order, print the list (2 pts.).
registration_list.reverse()
print(registration_list)

# Create a tuple that contains the days of the week, eg. Monday, Tuesday, etc (3 pts.).
days_of_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

# Print the length of the tuple (1 pt.).
print(len(days_of_week))

# Use indexing to print Wednesday (1 pt.).
print(days_of_week[2])

# Use slicing to print Friday, Saturday, Sunday) (2 pts.).
print(days_of_week[4:7])

# Can Tuples have their values modified, appended, or removed (1 pt.)?
# Enter yes or not here: not here

