# OOP / Object Oriened Programing 

Abstraction:
- way to hide complexity by hiding unneccesary details from user.
e.g.:

string.upper() - 
instead of:
def upper():
    .
    .
    .

Encapsulation:
- data & methods are bundled.
e.g.
Data: string 
Methods: .upper(), .join() etc.



How to make your own class?
e.g. to store user information:

#Class ALWAYS capital letter

#what data does "Peron" have:
# Name 
# Age

#What objects can 'person' perform?
# sayHi()
# have_bday()

class Person:
    def __init__(self, name, age): #ALWAYS needed #define initiation
        self.myname = name
        self.myage = age 

    def say_hello(self):
        print(f'Hi my name is {self.myname}')

user = Person(name='Jon', age=15)

#RULE 1.
#ALL methods must have self as a first argument, INSIDE CLASS - Self is available everywhere inside class, including functions etc

#RULE 2.
#init  = attaches variables to self 


