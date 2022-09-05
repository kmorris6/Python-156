#Kate Morris
#PA_9

class User: #Define the name of the class using the keyword 'class'
    def __init__(self,firstName,lastName,userId,password): #Define the init method and initialize the object
        self.firstName = firstName #Setting the attributes (firstName, lastName, userId, and password) to be passed into the User class
        self.lastName = lastName
        self.userId = userId
        self.password = password

    @property #Define property decorator for the attributes passed into the object (firstName, lastName, userId, and password)
    def firstName(self): #Define the attribute
        return self.__firstName #Return the name stored in the data attribute

    @firstName.setter #Create a setter by setting the name for that object for the User class
    def firstName(self,firstName): #Define the attribute
        self.__firstName = firstName 

#The rest of the code are the property decorators and setters for each data attribute that is assigned to the User class  
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self,lastName):
        self.__lastName = lastName

    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self,userId):
        self.__userId = userId

    @property
    def password (self):
        return self.__password

    @password.setter
    def password(self,password):
        self.__password = password
#Run the program and this compiles the class
    
