# # DICTIONARY (MUTABLE)

# #sets hold single items.
# #dictionaries hold keys  & values like name: John
# # is similar to JS objects
# #You can store ANYTHING in a dictionary (strings, intergers, sets, list, tuples, dictionaries etc.)

# #dictionaries are NOT ordered! CAN'T LOOP

# #dictionary = {
# # key : value
# # }

# #Keys have to be unique AND IMMUTABLE (strings, tuples etc)


# person = {
#     'name': 'Aviva',
#     'surname': 'Drozdin',
#     'job:' : 'student',
#     'pets' : 0,
#     'citizenships': ['Lithuanian', 'German', 'Israeli'],
#     'work_experience' : {
#         'bizDev_manager' : 'IATI',
#         'Software_Sales' : 'Voxsmart',
#     },
#     'parents' : ('Mom', 'Dad'),
#     99: 'Red Balloons',
#     ('A', 'B') : 'The alphabet',
# }




# #print(person['surname']) # would get Drozdin

# person['middlename'] = 'Eva' # adds middle name
# person['middlename'] = 'Ieva' #reassigns middle name

# print(('A', 'B'))


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict['marks'[1]])



#Accessing dict.

#option 1
sampleDict('class') #shows class
sampleDict('age') # CRASHES because doesn't exist

#option 2 (BETTER)
sampleDict.get('class') # will show class
sampleDict.get('age') # will show nothing as doesn't exst

#other:
my_keys = sampleDict.keys() 
print(my_keys) #shows the keys


#to know what type of datastructure smthg is: 
type(sampleDict) #explains that it is a dictionary

my_keys = sampleDict.keys() 
print(my_keys) #shows it is type of dict keys


#this gives you new data structure:
dict_keys # special type of list, that you can't change

# IN lets you know if key exists in distionary



#GET VALUES (e.g Aviva)
inventory = {
    'apples': 100,
    'pears': 200,
}

mykey = inventory.keys() #get key
myvalue = inventory.values() #get value
myitems = inventory.items() #get both
#gives:
dict_items([('apples': 100), ('pears': 200)]) #dict gives you tuples - means imutable

myitems = list1 #convert myitems to a list
list1[1][1] #access value of pears (100) access index1 item and index 1 value



#UPDATE / Change in list / dict
inventory['apples'] = 1000 #changes value of apples otion1
inventory.update['apples', 1000] # changes value of apples option2




#LIST COMPRAHENSION

#THIS :
number = []

for i in range (1, 11):
    number.append(i*i)

#IS THE SAME AS:
number = [i*i for i in range(1, 11)]
print (number)



#make dictionary from 100 to 110 where key is a number and the value is half of the key

# other = {}
# for e in range(100, 111}:
#     other[e] = e/2 
# print(other)

# someother = {f/2 for e in range(100, 111)}


#ask 3 users for their name, put names in list

#option 1
names = []
for i in range(3):
    name = input('What ur name? ')
    name.append(name)
print(name)
#SAME AS:
othername = [input('whats ur name? ') for i in range(3)]

print(othername)



#generate a list between 1 & 100.
#if nr is divisible by 7 add to list

#OPTION 1
numbers = []
for i in range (1, 101):
    if i % 7 == 0:
        number.append(i)
    else:
        print(':) ')
print(number)

#OPTION 2 - List comprahension
numb = [e for e if e % 7 == 0 else ':)' in range(1, 101)]
print(numb)



#LIST FUNCTION
map() = #function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

= <map object at 0x034244F0>
['appleorange', 'bananalemon', 'cherrypineapple']


