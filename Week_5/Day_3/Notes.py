INHERITANCE 
 is a type of
 (is language a type of person - NO)
 (is superman a type of person - YES) - Superman inherits from person


COMPOSITION
 has a type of
 (has Person a language - YES)
 (has Superman a language - YES)  



 class Person:
    def __init__(self, name, age)

 class Language:
    def __init__(self, name, region)

 class Superman(Person):
    def __init__(self, name, age, power)


language = Language('English'. 'UK', '850BC')

p1 = Person('Bob', 6, Language('greek', 'greece', '400BC'))



DUNDLER METHODS:

REPR & STR 
Methods that start with double underscore like:

__init__: called when an object is instatiated 
(e.g. d1 = Dog() )

__repr__: Called when you dump (type) a variable on screen
(e.g. d1 = Dog() / just type: d1 INSTEAD OF print(d1)) # more formal

__str__: Called when you print a variable #more informal than repr

repr / str: 
class person:
    str return 'Hi im bob, im 21' #more informal
    repr return 'Name: Bob. Age: 21' # more formal






GT 

p1 = Person(20, 1, 100)
p2 = Person(505, 2, 90)

p1 > p2 #epected return true as takes first value
Actual return - ERROR!
Why? The computer doesnt understand what class Person is.

Need to use __gt__ (greater than)


class Person:
    def __init__(self, weigh, height, fb_friend):
        self.weight = weight
        self.height = height 
        self.fb_friend = fb_friend

    def __gt__(self, other): #Literlly say that we ONLY care whos fb friends are greater
        if self.fb_friends > other.fb_friends:
            return True
        else:
            return False


p2 > p1 (p2 is greater than p1?) = FALSE - because p1 has more fb friends, with __gt__ specified thats the only comparison argument we care about


ADD 
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def woof(self):
        print(f'Hi I am a {self.breed}, my name is {self.name} and I am {self.age} years old')

    def __add__(self, other):
        puppy_name = (self.name + other.name).capitalize()
        puppy_age = 0.1
        puppy_breed = self.breed if self.breed == other.breed else self.br

with __add__ we can call d3 = d1 + d2 INSTEAD d3 = d1.mate(d2)


d1 = Dog('Lessie', 4, 'Collie')
d2 = Dog('Rex', 3, 'Shepard')




#file names in the terminal will be renamed in memory to main! 

#if this file was loaded from the terminal
if __name__ == '__main__':




DATETIME MODULE: 

import datetime 

datetime.datetime.now() - shows current date and time


