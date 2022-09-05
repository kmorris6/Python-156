#Kate Morris
#PA_10

import car_class as c #Import where the class file is stored and assign a variable to reference it later

print('Car Input:') #Prompt the user to enter the make, model, and year
make = input('Enter the make: ') #Prompt user to enter make and store it in make
model = input('Enter the model: ') #Prompt the user to enter model and store it in model
year = input('Enter the year: ') #Prompt the user to enter the year and store it in year

cars = c.Car(make,model,year) #Create an object of from Car class called cars reference the file that the Car class is in and specify each data attribute necessary so they can be called upon
print('\nCar Information:') #Access the information from Car class
print('Make:',cars.make) #Use the 'cars' object to call upon the data attribute and print it
print('Model:',cars.model) #Use the 'cars' object to call upon the data attribute and print it
print('Year:',cars.year) #Use the 'cars' object to call upon the data attribute and print it

print('\nElectric Car input:') #Prompt the user to enter the following
make = input('Enter the make:') #Prompt the user to enter the make and store it in make
model = input('Enter the model:') #Prompt the user to enter model and store it in model
year = input('Enter the year:') #Prompt the user to enter the year and store it in year
battery = input('Enter the battery size:') #Prompt the user to enter the battery size and store it in battery
miles = input('Enter the miles between charge:') #Prompt the user to enter the miles between charges and store it in miles

ec = c.ElectricCar(make,model,year,battery,miles) #Create an object of from ElectricCar class called cars reference the file that the Car class is in and specify each data attribute necessary so they can be called upon
print('\nCar Information:') #Access the information from ElectronicCar class
print('Make:',ec.make) #Use the 'ec' object to call upon the data attribute make and print it
print('Model:',ec.model) #Use the 'ec' object to call upon the data attribute model and print it
print('Year:',ec.year) #Use the 'ec' object to call upon the data attribute year and print it
print('Battery:',ec.battery_size) #Use the 'ec' object to call upon the data attribute battery and print it
print('Miles Between Charge:',ec.miles_per_charge) #Use the 'ec' object to call upon the data attribute miles and print it
