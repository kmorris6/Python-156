# CHAPTER 6 EXERCISES

my_string = 'Hi Jessica, I said Hello'

# Print the length of my_string (1 pt.).
print(len(my_string))

# Use slicing on my_string to print out I said (1 pt.).
a = my_string[12:19]
print(a)

# Use slicing on my_string to print out sica, (1 pt.).
print(my_string[6],my_string[7],my_string[8],my_string[9])

# Write an if statement to determine if my_string starts with Hello.
# If my_string starts with Hello print out: my_string starts with Hello.
#  If it does not print out:  my_string does not start with Hello. (2 pts.).
if my_string .startswith('Hello'):
    print('my_string starts with Hello.')
else:
    print('my_string does not start with Hello.')

# Write a loop that counts the number of space characters that appear in string_one. Print the count (3 pts.).
string_one = 'My name is George, what is your name.' # DO NOT DELETE THIS LINE OF CODE
count = 0 # USE THIS VARIABLE IN YOUR LOOP
for ch in string_one:
    if ch ==' ':
        count+=1
print(count)

# Write a loop that counts the number of digits that appear in string_two. Print the count (3 pts.).
string_two = '520-826-6752-mijbog' # DO NOT DELETE THIS LINE OF CODE
count = 0 # USE THIS VARIABLE IN YOUR LOOP
for ch in string_two:
    if ch.isnumeric():
        count+=1
print(count)

# Write a loop that counts the number of lowercase characters that appear in string_three. Print the count (3 pts.).
string_three = 'AbcdeFGhIjklMNOPqRstUvWXYz' # DO NOT DELETE THIS LINE OF CODE
count = 0 # USE THIS VARIABLE IN YOUR LOOP
for ch in string_three:
    if ch.islower():
        count+=1
print(count)

# Write a statement that splits split_string, creating the list ['cookies', 'milk', 'fudge', 'cake', 'ice cream'], save the list
# in a variable called split_list.  Print split_list (3 pts.).
split_string = 'cookies>milk>fudge>cake>ice cream' # DO NOT DELETE THIS LINE OF CODE
print(split_string.split('>'))

# Write an if-else statement that will check that the entered user name and password match the stored user
# name and password defined below.  While the password should be case sensitive, users should be able to log in even
# if their entered user name has the wrong capitalization.  If the user name and password match, print
# 'You are logged in!'. Otherwise, print 'Please check your user name and password and try again.' (5 pts.).
entered_user_name = 'thefittest11' # DO NOT DELETE THIS LINE OF CODE
entered_password = 'a8h1luk91' # DO NOT DELETE THIS LINE OF CODE
stored_user_name = 'TheFittest11' # DO NOT DELETE THIS LINE OF CODE
stored_password = 'a8H1LuK91' # DO NOT DELETE THIS LINE OF CODE

u_name = {entered_user_name, stored_user_name}

username = input('Enter the username: ')
password = input('Enter the password: ')

if (password == stored_password) and (username in u_name):
    print('You are logged in!')
else:
    print('Please check your user name and password and try again.')

# Write an if statement that will check if text_to_search_through contains text_to_search_for. If it does,
# print 'I found it!'.  Be sure to make this funtionality case insensitive (3pts.).
text_to_search_through = 'To be, or Not to Be--that is the question' # DO NOT DELETE THIS LINE OF CODE
text_to_search_for = 'Or not To be' # DO NOT DELETE THIS LINE OF CODE
if text_to_search_for.lower() in text_to_search_through.lower():
    print('I found it!')



