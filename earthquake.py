#Kate Morris
#PA_2

#Scale1=input('Please enter the Richter scale value (between 0 and 10) for the earthquake: ') #prompts the user to enter a value
#Scale2=float(Scale1) #Need to allow the integer to be a floating decimal number

#if Scale2 > 10.0:
    #print('An invalid Richter scale value was entered.') #necessary boundary in case value added not on scale


#elif Scale2 >= 8.0:
    #print('Most structures fail.') 

#elif Scale2 >= 7.0:

#print('Many buildings destroyed.')

#elif Scale2 >= 6.0:
    #print('Many buildings considerably damaged, some collapse.')

#elif Scale2 >= 4.5:
    #print('Damage to poorly constructed buildings.')

#else:
    #print('No destruction of buildings.')

# if the word ends in 'ed', 'ly', or 'ing', remove the suffic
# if the resulting word is longer than 8 letters, keep the first 8 

# def stemmer(text): 
# if __name__ =='__main__':


from string import ascii_lowercase

def cryptogram(message, rotation=4):
    rotated = ascii_lowercase[rotation:] + ascii_lowercase[:rotation]
    cipher = {o: n for o, n in zip(ascii_lowercase, rotated)}

    encoded = []
    for char in message.lower():
        if char in cipher:
            encoded.append(cipher[char])
        else:
            encoded.append(char)

    return ''.join(encoded)
print(cryptogram("SUPER"))
