from pprint import pprint

# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: France -> blue, Spain -> red, US -> pink, green 

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator': 'Amanctio Ortega Gaona',
    'type_clothing': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'HM', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'Blue',
        'Spain': 'Red',
        'US': ['Pink', 'Green']
    }
}

#2.
brand['number_stores'] = 2
#pprint(brand)

#3
print('The clients of Zara are', ','.join(brand['type_clothing'][:3]))


#4
brand.update({'country_creation': 'Spain'})
#pprint(brand)

#5
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')


#6
brand.pop('creation_date')
pprint(brand)

#7.
print(brand['international_competitors'][-1])

#8
print('The major colors in the US are', ','.join(brand['major_color']['US']))

#9.
print(len(brand.items()))

#10.
print(brand.keys())

#11.
more_zara = {
    'creation_date': 1975,
    'number_stores': 10000,
}

#11.1
brand.update(more_zara)
pprint(brand)

#11.2
print(brand['number_stores'])



