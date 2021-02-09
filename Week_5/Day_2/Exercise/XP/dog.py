class Dog():
    def __init__(self, name, age, weight, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed


    def mate(self, other_dog):
        new_pup_name = self.name + other_dog.name
        new_pup_breed = self.breed + other_dog.breed

        return Dog(new_pup_name, 0.1, 1, new_pup_breed)


    def bark(self):
        return print('Bark Bark Bark')


    def run_speed(self):
        return (self.weight/self.age)*10


    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score =  other_dog.run_speed() * other_dog.weight
        
        winner = None
        if self_score > other_score:
            winner = self
        elif self_score < other_score:
            winner = other_dog

        if winner:
            print(f'{winner.name} wins!')
        else:
            print('Draw!')

d1 = Dog('Rex', 6, 45, 'Pitbul')
d2 = Dog('Fifi', 5, 20, 'Labrador')


d1 = Dog('Butch', 6, 45, 'Buldog') #self.
d2 = Dog('Fifi', 5, 3, 'Poodle') #other_dog = parameter in fight

# 3. Create 3 dogs and use some of your methods

d3 = Dog('Monty', 5, 3, 'Maltese')
d4 = Dog('Tyson', 7, 54, 'Cane Corso')
d5 = Dog('Bobby', 2, 1, 'Dachshund')

#EXERCISE CONTINUES IN dogcont.py