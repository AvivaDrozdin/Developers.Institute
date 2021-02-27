#DICTIONARY

#Basic
phonebook = {
    'name': {
        'fname': 'Aviva',
        'lname': 'Drozd'
    },
    'phone': 111111
}

#we grab items from dictionaries via KEYS!!!! NOT position
print(phonebook['name']['lname']) = Drozd
print(phonebook['phone']) = 11111



#More Complex
phonebook = {
    'person1': {'name': {'fname': 'adam', 'lname': 'adamson'}, 'phone': 1234},
    'person2': {'name': {'fname': 'bob', 'lname': 'boo'}, 'phone': 5678},
    'person1': {'name': {'fname': 'cindy', 'lname': 'chin'}, 'phone': 9123},
}

print(phonebook['person2']['phone']) # = prints person 2 phone number
print(phonebook['person1']['name']['fname']) # = prints person1 first name

#reassigning values 
phonebook['person2']['phone'] = 1111 #= reassigns phone nr to 1111
phonebook['person1']['name']['fname'] = 'Tom' # = ressigns person 1 fist name to Tom


#adding to dictionary
phonebook['person5'] = {
    'name': {'fname': 'Dan', 'lname': 'Danielson'},
    'phone': 2222
}
#adds dan to dictionary



#KEY, VALUE, ITEMS
phonebook.key() = returns all the keys in dictionary ([person1, name, fname, lname, phone])

phonebook.values() = returns all the values ([adam, adamson, 1234])

phonebook.items() =  returns a view object (with key+values)as tuples in a list.



#UPDATE 
#adds new key with value
phonebook.update({'school': 'DI'}) = adds key school with value DI to phonebook


#Remove from dictionary
phonebook.pop('person1') = removes person 1 
phonebook.pop('person2'['phone']) = removes person2 phone nr

