#INHERITANCE 
# (taking similar classes and building them further)

#e.g. class

class Person: #Parent Class / Base Class / Sup Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'{self.name} is {self.age} years old. ')
    
    def birthday(self):
        self.age += 1
        print('Happy Birthday')
    

#inheritance class e.g.

class Man(Person): #Child class / sub class
    #class Man(Person)= inherits everything from Person
                    #means = have to define NAME and AGE line in Person
    def __init__(self, name, age, fav_beer): #overriding innit
        super().__init__(name, age) #calls parent for name & age parameters
        self.fav_beer = fav_beer #our own parameter
        self.gender = 'Male' #our own parameter

    
    def birthday(self):
        self.age += 1
        print('Happy bday, lets go out for a beer with the boys') #OVERRIDES Person def birthday method in class Man 

        super().birthday() #calls parents method (uses parent method - add age, sappy happy bday)
        print('Lets drink') #add let drink 

    
    def drink_beer(self): #extendeds /adds own method in addition to doing everything that Person does
        print('glug glug glug')


#Inheritance
#class SubClass(SuperClass)

#IF YOU WANT TO REMOVE AN INHERITED METHOD - OVERRIDE IT


#ENCAPSULATION
#puting data & method is together

class Account:
    def __init__(self, acc_nr):
        self.acc_nr = acc_nr
        self.__balance = 0 #makes balance not accessible outside class
        self.__transaction = [] #list, because lists are ordered!

    def depost(self, amount):
        if amount > 0 and amount <= 100000:
            self.__balance += amount #allows to add to private balance
        self.__transaction.append(f'Deposited: {amount}')


    def withdraw(self):
        if amount <= self.__balance: #if amout smaller than balance
            self.__balance -= amount #allows to deduct from private balance the amount specified
            self.__transaction.append(f'Withdrawn: {amount}')
        return amount

    def info(self):
        print(f'Account {self.acc_nr} has a balance of ${self.__balance}' )
        pass


    def transaction_history(self): 
        for transaction in self.__transaction:
            print(transaction)




# leumi = Account('1234')
# leumi.deposti(300)
# leumi.withdraw(100)
# leumi.info() #show acc nr and balance


#PYTHON:
#self._thing = DOESN'T CHANGE ANYTHING, just lets other developers know it should be treated LIKE private

#self.__thing = MAKES PRIVATE! (Wont show in terminal). can ONLY be used in class (like with print())




# OTHER LANGUAGES:
# private self.withdraw
# public self.info
# protected self.balance

#[Public = Accessible anywhere
#Protected = accessible in parent & child classes
#Private = Accessible ONLY in parent class]