# What is the difference between CLASS and OBJECT?
# CLASS = is the blueprint / the plan

# OBJECT = is the product made from the blueprint / plan


#METHOD = 

class Dog:
    genus = 'Canis' #shared information for everypne
    count = 0 #every objects gets a count 

    def __init__(self,name)
        self.name = name

    @classmethod
    def sayhi(): 
        print('hi')

# @classmethod A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance,


d1 = Dog('Lessie')
d2 = Dog('Rex')

d1 is the OBJECT (created from class Dog)
Dog is te CLASS 

self.name - belongs to specific object
genus - belongs to ALL objects


INSTANCE: d1 = Dog('Lessie') <- inside () is instance of the class 


CLASSMETHOD / staticmethod - SEE PAPER!!!!!



PROPERTY
@property
def bark(self):
    print(bark)


makes function behave like variable =
c3 = Dog('Bob')
allows to print:
c3.bark INSTEAD OF c3.bark()

