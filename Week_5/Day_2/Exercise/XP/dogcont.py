#EX 2 (continued)

#1. Create a class named Dog with the attributes name, age, weight
from dog import Dog #part 1
import random #part 4.4

#2. create class perdog inherits from dog
#3. add attribute trained (bool) that starts with false
class PetDog(Dog):
    super().__init__(name, age, weight, breed):
        self.trained = False 

    def train(self):
        self.bark()
        return self.trained = True

    def play(self, *dog_names):
        dogs = ','.join(dog_names.name)
        print(f'The dogs: {dogs} are playing together ')
        return dog_names.trained = false
    
    def do_a_trick(self, *dog_names):
        sentence = random.randint(0,3) #4 sentences
        if self.trained = True:
            if sentence == 0:
                print(f'{dog_names} does a barrel roll')
                dog_names.trained = False
        elif:
            if sentence == 1:
                print(f'{dog_name} stands on their back legs')
                dog_names.trained = False
        elif:
            if sentence == 2:
                print(f'{dog_names} Shakes your hand')
                dog_names.trained = False
        else:
            print(f'{dog_names} plays dead')
            dog_names.trained = False





