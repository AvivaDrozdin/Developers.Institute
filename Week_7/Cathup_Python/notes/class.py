import random
#XP

#cats
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest (self, other, other2):
        oldest = 0
        if self.age > other.age and self.age > other2.age:
            oldest = self.age
        elif other.age > other2.age and other.age > self.age:
            oldest = other.age
        else:
            oldest = other2.age
        
        print (f'The oldest cat is {oldest} years old')

cat1 = Cat('Fluffy', 2)
cat2 = Cat('Clawford', 8)
cat3 = Cat('Mittens', 5)

#dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print('bark bark')

    def jump(self):
        print(f'{self.name} jumps {self.height*2}cm high!')

david_dog = Dog('Rex', 50)
sarah_dog = Dog('Teacup', 20)

# if david_dog > sarah_dog:
#     print(f'{david_dog} is larger')
# elif david_dog < sarah_dog:
#     print(f'{sarah_dog} is larger')
# else:
#     print('Both dogs are the same size')

#song producer
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing(self):
        for text in self.lyrics:
            print(text)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

#zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add(self, new_animals):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        print(self.animal)

    def get(self, animals):
        for each in self.animals:
            print(each)
        
    def sell(self, animals):
        if sold in self.animals:
            self.animals.remove(sold)
        else:
            print('There is no such animal at the zoo')
        print(self.animals)

    def sort(self, animals):
        self.animals.sort()
        print(f'The animals in alphabetical order are: {self.animals}')
        
        #HELP WITH GROUPING PLS
    

#GOLD
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    
    def area(self):
        Pi = 3.141
        area = Pi * self.radius * self.radius
        print(f'The area of the circle is {area}cm²')


    def perimeter(self):
        Pi = 3.141
        p = 2 * Pi * self.radius
        print(f'The perimeter of the circle is {p}')

cir1 = Circle(3)


#2
class MyList:
    def __init__(self, list):
        self.list = list
    
    def check(self):
        if type (self.list) != list:
            return False
        else:
            return True
    
    def reverse(self):
        reverse = self.list.reverse()
        print(reverse)
    
    def sort(self):
        sort = self.list.sort()
        print(self.list)

    def new_list(self):
        new_list = []
        random_nr = random.randrange(1,100) 
        
        for random_nr in range(len(self.list)):
            new_list.append(random_nr)

        print(new_list)


mylist = [1, 3, 5, 7, 12, 47]

#3 






