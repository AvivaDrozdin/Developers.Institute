#EX 1

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1. Add another cat breed
class Scottish_Fold(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#2. Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
my_cats = [Bengal('Fluffy', 2), Chartreux('Tom', 6), Scottish_Fold('Bob', 3)]


#3. Instantiate the Pet class with all your cats. Use the variable my_pets
my_pets = Pets(my_cats)

#4. Output all of the cats walking using the my_pets instance
my_pets.walk()





#EX 2 

#1. Create a class named Dog with the attributes name, age, weight
from dog import Dog 

if __name__ == '__main__':



d1 = Dog('Butch', 6, 45) #self.
d2 = Dog('Fifi', 5, 3) #other_dog = parameter in fight

# 3. Create 3 dogs and use some of your methods

d3 = Dog('Monty', 5, 3)
d4 = Dog('Tyson', 7, 54)
d5 = Dog('Bobby', 2, 1)


#EX 3







