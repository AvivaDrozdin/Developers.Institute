import json

#CAN'T CONVERT CLASSES TO JSON

#almost all data that is send or pulled via the internet  is send in JSON



#CONVERT FROM JSON

#load #read from json file and convert to python
#loads #s = string. convert json string to python object


#CONVERT FROM PYTHON TO JSON
#dump # convert from python to json and write file
#dumps #convert from python to json file


thing = [
    {
        'name': 'Bob',
        'age': 55,
        'stuff': True
    },
    {
        'nums': [1,2,3,4],
        'letters': ['a', 'b', 'c']
    }
]

#this will convert our python object to  json file & display in new txt file called jfile
with open('jfile.txt', 'w') as f:
    json.dump(thing, f, indent=4) #indets new line by 4 - makes it more readable


#load json file and convert to python
with open('jfile.txt', 'r') as f:
    thing2 = json.load(f)