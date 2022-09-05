#Kate Morris
#PA_6

def cv(string): #define a variable to keep the user string in to count vowels
    vowels = 'aeiou' #specify the letters and/or vowels to count in the user string
    count_vowels = 0 #set to 0 so the vowels can be added to a base of 0
    for ch in string:
        if ch.lower() in vowels: #if statement to evaluate the user string for vowels
            count_vowels += 1 #as each vowel is counted, it adds 1 to total
    return count_vowels #return the total number of vowels in the user string

def cc(string): #define a variable to keep the user string in to count consonants, as it was done for vowels
    consonants = 'bcdfghjklmnpqrstvwxyz' #specify the consonants to count in the user string
    count_consonants = 0 #set to 0 so the consonants can be added to a base of 0
    for ch in string:
        if ch.lower() in consonants: #if statement to evaluate the user string for consonants
            count_consonants += 1 #as each consonant is counted, it adds 1 to total
    return count_consonants #return the total number of consonants in the user string

user = input('Enter a string: ') #Prompt the user to enter a string

vowels = cv(user) #total number of vowels in the user's string
consonants = cc(user) #total number of consonants in the user's string

print('The string you entered includes ', vowels, 'vowels and ', consonants, 'consonants.') 
    



