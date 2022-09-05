#Kate Morris
#PA_7

#Part 1 (20 points):
import random #import keyword and name of module to use the random function 
try: 
    str1=input('Enter the path to the file you wish to create:') #prompt user to enter the path to the file they want to create
    str2=input('Enter the file name: ')#prompt the user to enter the file name
    if str1[len(str1)-1]=='\\': 
        str1=str1+str2
    else:
        str1=str1+'\\'+str2
    f=open(str1,'w') #open the file created in write mode
    for i in range(50): #put in the random 50 integers between 1 and 1000 in created file
        f.write(str(random.randint(1,1000))+'\n') #use \n to put each integer on separate lines
    f.close() #close the file
    print('The 50 random numbers have been written to the file successfully.')
except(IOError,PermissionError):
    print('You do not have permission to access the folder')
    print('The program has ended')

#Part 2 (30 points)
try:
    str1=input('Enter the path to the file you wish to read:') #prompt the user to enter the path to the file to read
    str2=input('Enter the file name:') #prompt the user to enter the file name
    if str1[len(str1)-1]=='\\':
        str1=str1+str2
    else:
        str1=str1+'\\'+str2
    f=open(str1) #open the created file in read mode
    l=f.readlines() #read the created file in the form of lines
    l=list(map(int,l))
    print('The lowest number is:',min(l)) #use the min function to get the lowest number 
    print('The highest number is:',max(l)) #use the max function to get the highest number
    print('The sum of the numbers in the list is:',sum(l)) #use the sum function to get the sum of all the numbers
    print('The average of the numbers in the list is:',sum(l)/len(l)) #take the sum divided by the number of characters to get the average
except(FileNotFoundError,IOError):
    print('The',str1,'does not exist')
    print('The program has ended')

