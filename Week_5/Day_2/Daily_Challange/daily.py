# Gene 1 0

# Chromosome [1 0 1 0 1 0 1 0 1 0]

# DNA: [
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
#     [1 0 1 0 1 0 1 0 1 0]
# ]

#Bool - 0 = false , 1 = True

from random import randint

class Gene:
    def __init__(self): #when create gene it will get a random nr
        self.value = randint(0,1)
    
    #mutate - beginner code
    def mutate(self):
        if self.value == 1:
            self.value ==0
        else:
            self value = 1
        
    def __repr__(self):
        return f'{self.value}'

    #Ternary Statement =
    # IF statement that sets a variable - in one line
        self.value = 1 if self.value == else 0
    
class Chromosome:
    def __init__(self):
        self.value = [Gene() for _ in range(10)] #_ will often see when variable is just thre to loop and has no value / need for loop but not value

        #option 2: - same as above
        # for gene in range(10):
        #     self.value,append(gene)
    
    def mutate(self):
        for gene in self.value:
            if random() > 0.5:
                gene.mutate()

    def __repr__(self):
        return f'{self.value}'

class DNA:
    def __init__(self):
        self.value = [Chromosome() for _ in range(10)]

    def __repr__(self):
        return f'{self.value}'

    def mutate(self):
        while gene = 1
