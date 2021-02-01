#get first / last letter of text
text = 'testing'
text[0] # = first letter
text[len(text)-1] # length of text 7
len(text)-1 #g
text[-1] #g - best was


#SLICING
text[2:5] # gets sti (start a letter 2 - ending at 5 - one letter after which we want tu cut off)
[start:stop:step] #start = inclusive (includes chosen letter)
                  #stop = exclusive (excludes chosen letter)
                  #step = takes every second letter

[:5] # will assume no beginning = starts from beginning
[0:] # will assume no given ending = ends at sentence end

#step:
text = 123456789 
test[1::2] #starts at position one and steps every second nr



#pyhon remembers forwars and backwards

 t  e  s  t  i  n  g
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1



text = "This is a test sentence"
text[10:14]


#EXERCISE  - Extract the name:
bob@gmail.com
#say 
hi bob...

email = input('Enter your email')

#SOLUTION 1
email[:-10] # starting at 0 and ending and -10 (because py can count backwards & @gmail.com would be -10 slice off)

#Better option
#split() - method of string
print(f'Hello {email.split('@')[0]}')




#LISTS (similar to array in JS)
my_hobbies = ['eat', 'sleep', 'code']
my_hobbies[1] #would get us sleep

my_hobbies[2] = 'Cats' # would get code and change to cats

my_hobbies[-2] # would give us sleep (going backwards)
my_hobbies[::2] #start at 0, stop at end and select every 2nd = eat & cats

#METHODS THAT BELONG TO LISTS: . = method
.append(item) #appends / adds to a list eg. my_hobbies.append('coffe') adds coffee at end
.remove(item) #removes from list eh. my_hobbies.remove('eat') removes eat from list
                                                    #either item name or postion nr
                        #remove() full removes an item

.pop([index]) #if () empty - removes last item, if (nr) removes item of given nr
                #.pop() gives item back = if assign variable, popped item gets stored in variable

my_hobbies.sort() # sorts alphabettically (unless otherwise specified) AUTOMATICALLY SORTS 


your_hobbies['cook', 'fish', 'dance']

your_hobbies + my_hobbies #combines two lists DOESN'T save

my_hobbies.extend(your_hobbies) # adds items from your list and ads to my list. AUTOMATICALLY SAVES


numbers = [66, 4, 12, -12, 1, 50, 0]

sum(numbers) #function = gives sum of list with numbers
sorted(numbers) #function = sorts from smalles to biggest - doesn't remember unless given new variable

numbers.sort() #method = unless specified will sort small to big = AUTOMATIVALLY STORES NEW LIST!




letters = ['a', 'b', 'd', 'e']
letter.insert(2, 'c') # inserts letter c at position 2




#FUNCTION!!!! if there is no . = function
len() # gets length of list
input() #user input
print() # print (same as console log)



#SETS (NOT ORDERED!!! unlike Lists)
#useful for combining & chopping data
#also useful to remove duplicates
myset = {'a', 'b', 'c', 'd', 'e', 'f'}

#Sets can't have duplicates
#can add things to it but it will be unordered (show up in random position)

#converting list to set
emails = ['bob@gmail.com', 'droz@outlook.com', 'mark@gmail.com', 'bob@gmail.com']
>>> uniqueMail = set(emails)
>>> print(uniqueMail)


#TUPLE (Can NOT be changed) 
#useful for things that never change. e.g. days of week
my_tuple = (5,6,7)
my_tuple[0] # shows 5
my_tuple[0]=1 # WON'T WORK

#tuple has only two methods
count()
my_tuple.index(7) #shows what index 7 has



#CHANGABLE = mutable
#UNCAHNGABLE = imutable

strings = IMUTABLE # we can REASSIGN but not change it
intergers = IMUTABLE # we can REASSIGN but not change it
floats = IMUTABLE # we can REASSIGN but not change it
tupple = IMUTABLE

#immutable when reasigned creates new string / interger / float


lists = MUTABLE #can be changed & reassigned 
sets = MUTABLE

#mutables access same exisiting list



#LOOPS

list_names = ['bob', 'mark', 'daniel', 'alex']

for name in list_names:
    print(name) #will print one name each loop



for allname in list_names:
    if name == 'bob':
        print('robert')
    else:
        print(name)




for i in range(100):
    print(i) #does not include last nr 100 = goes to 99
=
for (i = 0; i < 100; i++) in JS

range(start,stop,step)

#RANGE can ONLY be used in loops

#enumerate() gives index number of each charackter
for i, char in enumerate('Hello'):
    print(i, char)

#0 H
#1 e
#2 l
#3 l
#4 o

for i, nr in enumerate(list(range(100))):
    if nr == 50:
        print(f'index of 50 is {i}') #will five index of 50







#WHILE LOOP
num = 0
while num < 10:
    print(num)
    num += 1





== # is something equal to

is #used to test if two variables refer to the same object.
    # eg. x = 'Hello'
    #     y = x
    # print(x is y) = True





 

