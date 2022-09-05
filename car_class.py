#Kate Morris
#PA_10

# Car class with a make, model and year

class Car:
    # init method for Car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Property Decorators
    @property
    def make(self):
        return self.__make

    @property    
    def model(self):
        return self.__model

    @property    
    def year(self):
        return self.__year

    # Setters
    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model

    @year.setter
    def year(self, year):
        self.__year = year
    
# Add the ElectricCar class below

class ElectricCar(Car): #Define an ElectricCar class that will have the Car class
    def __init__(self,make,model,year,battery,miles): #Use init to place the data attributes from the Car class and two new ones for ElectricCar class
        Car.__init__(self,make,model,year) #This places the Car class inside of ElectricCar class
        self.battery_size =  battery #Initialize the battery_size and miles_per_charge attributes
        self.miles_per_charge = miles

#Set property decorators for the two new data attributes being added
    @property
    def battery_size(self):
        return self.__battery_size
    @property
    def miles_per_charge(self):
        return self.__miles_per_charge

#Set setters for the two new data attributes being added
    @battery_size.setter
    def battery_size(self,battery):
        self.__battery_size = battery
    @miles_per_charge.setter
    def miles_per_charge(self,miles):
        self.__miles_per_charge = miles

#Run the program to compile the ElectricCar class
