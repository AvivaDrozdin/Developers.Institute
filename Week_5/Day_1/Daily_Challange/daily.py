# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!

#Step 1 create Farm Class

#Step 2 Initiate it with only name parameters & empty dictionary for animals (to store multiple keys & values)

#Step 3 create method to add animals. Parameters animal + how many
# check if animal is not yet in dictionary: if not - add to dictionary with either amount, or if unspecified +1



class Farm:

    def __init__(self, name):
        self.name = name
        self.zoo_dict = {}

    #add animal + amount. if amount not specified automatically add 1
    def add_animal(self, name, amount=1): 
        if new_animal not in self.zoo_dict: #if animal not in dictionary
            self.zoo_dict[new_animal] = amount #add new animal by amount
        else:
            self.zoo_dict[new_animal] += amount #if no amount supplied +1
    
    #prints out name of farm + type of animal with amount + EIEIO
    def get_info(self):
        print(f'{self.name}s Zoo ') #print zoo name
        for item in self.zoo_dict: #for each animal in zoo dict
            print(f'{item[0]} : {item[1]}') #print out key(animal) : value(amount)
        print('E-I-E-I-O')

#Expand the farm
    def get_animal_types(self):
        sorted_list = [] #empty list to add alphabetical ordered animals
        for key in self.zoo_dict.keys(): #for each key (animals) in zoo dicts keys
            sorted_list.append(key) #append key to list
        sorted_list.sort() #sort list alphabetically
        return sorted_list #get sorted list
    
    def get_short_info(self):
        items_in_list = self.get_animal_types
        animal_str = ','.join(items_in_list)
        print(f'{self.name}s Farm has {self.animal_str}')


    
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)

# print(macdonald.get_info())

# macdonald.get_animal_types()

# macdonald.get_short_info()


