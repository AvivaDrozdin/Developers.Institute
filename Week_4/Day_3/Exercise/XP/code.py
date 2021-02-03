#EXERCISE 1
keys = ['Ten', 'Twenty', 'Thrirty'] #list 1
values = [10, 20, 30] #list 2

dictionary = dict(zip(keys, values)) #create a dictionary with dict by zipping keys & values together
print(dictionary)



#EXERCISE 2

#part of yesterday

family_dict = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

price_list = [0, 10, 15]
price = 0

for name, age in family_dict.items():
    if age < 3:
        print(f'{name} would be paying ${price_list[0]}')
    elif age >= 3 and age < 12:
        print(f'{name} would be paying ${price_list[1]}')
        price += price_list[1]
    else:
        print(f'{name} would be paying ${price_list[2]}')
        price += price_list[2]

print(f'The total for the family is ${price}')

#EXERCISE 3

#part 1
brand = {
    'name': 'Zara',
    'creation_date': 1972,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'Red',
        'US': ['Pink', 'Green']
    },
}

#part 2
brand["number_stores"] = 2

#part 3
for customer in brand['type_of_clothes'][:3] #start at beginning at start of list stopping at index 3 (to get kinds in list)
print('The clients of Zara are', ','.join(brand['type_of_clothes'][:3]))


#part 4
brand['country_creation '] = 'Spain'

#part 5
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

#part 6
del(brand['creation_date'])

#part 7
print(brand['international_competitors'][-1])

#part 8
UScolors = brand['major_color']['US']

print(f'Zaras major colors in the US are {UScolors}') #?

#part9 (Not sure about this)
# total_pairs = brand.items()
# print(total_pairs)

#part 10
for keys in brand.keys():
    print(keys)

#part 11
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000,
}

#part 11.1
brand.update(more_on_zara)
print(brand)

#part 11.2
print(brand['number_stores']) #number of stores gets overwritten with a new value


#EXERCISE 4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

#part 1
disney_users_A = {users[j]: j for j in range(0, len(users))} #assigns j to each users via loop that runs length of users list
print(disney_users_A)

#part 2
disney_users_B = dict(enumerate(users)) #gives the number of each user
print(disney_users_B)

#part 3
users = sorted(users) #sort users alphabetically
disney_users_C = {users[k]: k for k in range (0, len(users))} #use same loop as A
print(disney_users_C)

#part 4
disney_users_D = {users[l]: l for l in range(0, len(users)) if "i" in users[l]}
print(disney_users_D)

#part 5
disney_users_F = {users[m]: m for m in range(0, len(users)) if "M" and "P" in users[m][0]}
print(disney_users_F)


