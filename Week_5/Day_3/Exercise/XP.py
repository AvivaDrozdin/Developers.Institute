# #EX 1

# #Python has a built-in document function for every built-in functions.
#     #1. Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
#     #2. And add documentation for your own function
    
# print (abs.__doc__)
# def abs(x):
#     """Return the absolute value of the argument."""
#     pass
# print(abs)

# print (int.__doc__)
# def int(x):
#     """Convert a number or string to an integer, or return 0 if no arguments are given.  If x is a number, return x.__int__().  For floating point numbers, this truncates towards zero."""
#     pass
# print(int)    


# print (raw_input.__doc__) #not working in terminal / can't find 
# def raw_input(item):
#     """raw_input is a form of input that takes the argument in the form of a string whereas the input function takes the value depending upon your input. Say, a=input(5) returns a as an integer with value 5 whereas  a=raw_input(5) returns a as a string of "5" """
# print(raw_input)

# #EX 2
# #Recreate results from DI XP EX2 
# #Hint : When you add 2 currencies, if they don’t have the same label raise an error

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c4 = Currency('shekel', 1)
# c3 = Currency('shekel', 10)

# class Currency:
#     def __init__(self, currency, amount):
#         self.value = amount
#         if amount >1:
#             self.currency = currency + 's'
#         else:
#             self.currency = currency
        
#     def __str__(self):
#         return f'{self.value} {self.currency}'

#     def __int__(self):
#         return f'{self.value}'

#     def __repr__(self):
#         return f'{self.value} {self.currency}'
    
#     def __add__(self, other):
#         try:
#             if type(other) == int or self.currency == other.currency:
#                return self.value + other.value
#         except TypeError:
#             print(f'TypeError: Cannot add {self.currency} and {other.currency')


#     def __iadd__(self, other):
#         if type(other) == int:
#             self.value == self.value += other
#             return self
#         elif self.currency == other.currency:
#             self.value = self.value + other.value
        
#         else:
#             print(f'TypeError: Cannot add {self.currency} and {other.currency}')


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 10)
# c4 = Currency('shekel', 1)

#EX3
import datetime 

def january(): #function
    print(f'The 1 of April is in {datetime.datetime(2021, 4, 1)-datetime.datetime.today().replace(microsecond=0)}')

january()


#EX 4
def holiday():
    today = datetime.datetime.now()
    purim = datetime.datetime(2021, 2, 25)
   # print(f'Today is the: {today.strftime(%d/%m/%y)}') #Syntax Error?
    print(f'Purim is in {purim - today.replace(microsecond=0)}')

holiday()

#EX 5
def calculate_age(seconds):
    minute = seconds/60
    hour = minute/60
    day = hour/24
    earth_year = day/365.25

    mercury_year = earth_year/0.2408467
    venus_year = earth_year/0.61519726
    mars_year = earth_year/1.8808158
    jupiter_year = earth_year/11.862615
    saturn_year = earth_year/29.447498
    uranus_year = earth_year/84.016846
    neptune_year = earth_year/164.79132

    print(f'Your are {earth_year} on Earth. \n Your age on other planets: Mercury: {mercury_year}, Venus: {venus_year}, Mars: {mars_year}, Jupiter: {jupiter_year}, Saturn: {saturn_year}, Uranus: {uranus_year}, Neptune: {neptune_year}')

calculate_age(878000000)


#EX 6
from faker import Faker

faker = Faker()

user = []
new_dict = {}

def faker_add(amount):
    for item in amount:
        new_dict['name'] = faker.name()
        new_dict['address'] = faker.address()
        new_dict['email'] = faker.email()
        #new_dict['language_spoken'] = faker.text()








