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


#EX 3 in dogcont.py

#EX 4
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
    
    







