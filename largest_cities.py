#Kate Morris
#PA_5

#dictionary with states and their capitals 
sgame = {
    'North Dakota':'Fargo',
    'South Dakots':'Sioux Falls',
    'Nebraska':'Omaha',
    'Kansas':'Wichita',
    'Oklahoma':'Oklahoma City',
    'Texas':'Houston',
    'Minnesota':'Minneapolis',
    'Iowa':'Des Moines',
    'Missouri':'Kansas City',
    'Arkansas':'Little Rock'
    }

r = 0 #set to zero as a base since 1 will be added for each correct answer.

for i in sgame: #a for in loop to cycle through each question
    print('What is the capital of',i,end=': ') #prompt user to enter answer

    rstate = input() 
    if rstate == sgame[i]: #if user gets answer correct, this message displays
        print('You are CORRECT,',sgame[i],'is the capital of',i)
        r = r+1 #increase count of correct answers to display results at the end
    else: #if user gets the question wrong, this message displays
        print('You are INCORRECT,',sgame[i],'is the capital of',i)
    print() #creates a space between each question and answer for easy reading

def display_results(r): #define the variable display_results
    print('You got ',r,'questions correct.')
    if r>=9: #if 9 or more questions are answered correctly
        print('Your knoledge of state capitals is great!!')

    elif r>=7: #if 7 or more questions are answered correctly 
        print('Your knoledge of state capitals is above average!')

    elif r>=4: #if 4 or more questions are answered correctly 
        print('Your knowledge of state capitals is average.')

    elif r<4: #if less than four questions are answered correctly
        print('You better study more!!!')
        
display_results(r) #shows the number of questions right and the appropriate message 

