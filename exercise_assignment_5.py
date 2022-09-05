#Kate Morris
#Exercise Assignment 5

# CHAPTER 5 EXERCISES

# Create a dictionary called days_of_month, that includes the month as the key and days in the month
# as the value (3 pts.). The days in the month must be an int.
# The dictionary should contain: January - 31, February - 28, March - 31, April - 30, May - 31, June - 30

days_of_month = {'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31} 

# Print the dictionary (1 pt.).
print(days_of_month)

# Write a for in loop that prints the keys in the dictionary. Use the keys() method (2 pts.).
for k in days_of_month.keys():
    print(k)

# Write a for in loop that prints the values in the dictionary. Use the values() method (2 pts.).
for v in days_of_month.values():
    print(v)

# Write a for in loop that prints the items in the dictionary AS A TUPLE (2 pts.).
for i in days_of_month.items():
    print(i)

# Write a for in loop that assigns the keys and values to seperate variables and prints the following
# line for each dictionary item: "There are 'number of days' days in the month of 'month'."
# eg. There are 31 days in the month of January. (3 pts.)
for val, dom_count in days_of_month.items():
    print('There are '+ str(dom_count)+' days in the month of'+ ' '+val)
    
# Write an if statement using not in to determine if September is in the dictionary.  If September is not in the dictionary,
# print out: September is not in the dictionary (2 pts.).
if 'September' not in days_of_month:
    print('September is not in the dictionary.')

# Update the number of days for February to 29 using one line of code, print the dictionary (2 pts.).
days_of_month['February']=29
print(days_of_month)

# Add the month of July with 31 days to the dictionary (1 pt.).
days_of_month['July']=31

# Print the length of the dictionary (1 pt.).
n_items = len(days_of_month)
print(n_items)

# Remove the month of March from the list.  Print the dictionary (2 pts.).
del days_of_month['March']
print(days_of_month)

# Write code to create a set name set1 with the following integers as members: 10, 20, 30, 40, and 50 (2 pts.).
set1 = set([10,20,30,40,50])

# Write code to create a set name set 2 with the following integers as members: 40, 50, 60 and 70 (2 pts.).
set2 = set([40,50,60,70])

# Write code that creates another set containing all the elements of set1 and set2, and assigns the
# resulting set to the variable set3. Print set3 (2 pts.).
set3 = set1.union(set2)
print(set3)

# Write code that creates another set containing only the elements that are found in both set1 and set2,
# and assigns the resulting set to the variable set4.  Print set4 (2 pts.).
set4 = set1.intersection(set2)
print(set4)

# Write code that creates another set containing the elements that appear in set1 but not in set2,
# and assigns the resulting set to the variable set5. Print set5 (2 pts.).
set5 = set1.difference(set2)
print(set5)

# Write code that creates another set containing the elements that appear in set2 but not in set1,
# and assigns the resulting set to the variable set6. Print set6 (2 pts.).
set6 = set2.difference(set1)
print(set6)

# Write code that creates another set containing the elements that are not shared by set1 and set2,
# and assigns the resulting set to the variable set7. Print set7 (2 pts.).
set7 = set1.symmetric_difference(set2)
print(set7)
