#Ex. 1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def oldest(self): #method = general / function = specific
        oldest = 0
        if self.age > oldest:
            oldest = self.age
        print(f'The oldest cat is {self.name} and is {self.age}' )    

cat_1 = ('Pebbles', 15)
cat_2 = ('Hati', 4)
cat_3 = ('Rhizi', 16)


#EX 2
class Dog:
    def __init__ (self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof')

    def jump(self):
        print(f'{self.name} jumps {self.height*2}cm')


davids_dog = Dog('Rex', 50)
sarahs_dog = Dog('Teacup', 20)


#EX 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for text_line in self.lyrics:
            print(text_line)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


#EX 4

class Zoo:
    def __init__(self, zoo_name='The Zoo'):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_animals(self, new_animal):
        print(input('Which animal would you like to add to the Zoo? '))
        if  new_animal not self.animals:
            self.animals.append(new_animal)
        print(self.animals)

    def get_animal(self, animals):
        for animal in self.animals:
            print(f'{animal}')

    def sell_animal(self, animals):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
        else:
            print('There is no such animal in the list')
        print(f'List of animals: {self.animals}')

    def sort_animals(self, animals):
        self.animals.sort():
        print(f'Animals sorted alphabetically: {self.animals}')
        for i in range(len(self.animals)):
            group = {i+1: self.animals[i]}
            self.new_dictionary.update(group)
        print(self.new_dictionary)

    def get_groups(self, animals):
        for items in self.new_dictionary.items():
            print(f'List of animals: {items}')


ramat_gan_safari = Zoo('Ramat Gan')

#add animals
ramat_gan_safari.add_animals('Lion')
ramat_gan_safari.add_animals('Ibex')
ramat_gan_safari.add_animals('Zebra')
ramat_gan_safari.add_animals('Monkey')

#Get animals
ramat_gan_safari.get_animal('Monkey')

#Remove animal
ramat_gan_safari.sell_animal('Lion')

#sort alphabetically
ramat_gan_safari.sort_animals()

#print different groups
ramat_gan_safari.get_groups()

