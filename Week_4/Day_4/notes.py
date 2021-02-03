#Something than can be looped is called 'INTERABLE'

#List / key  = Interable
# Strings = Interable


#FUNCTIONS
#benefits:
#1. makes code faster
#2. makes code neater

#some functions have OPTIONAL input

def say_hi():  #def = defining function + functionName() - ()<- optional but almost always used
    print('Hi everyone')



nums = [1, 2, 3, 4]
sum(nums)
#The sum function takes a list of numbers as input

print()
#print takes variables, list, intergers, string etc as input


def sum(list of nr) #eg 123
    return total   #returns total


def my_function(input1, input2, input3):
    return whatever

def sayHello(name): #name = given name
    print(f'Hello{name}') # prints name

    #IN terminal write: sayHello('bob')


#capitalizing
def capitalize(text):
    output = text[0].upper() + text[1:] #capitalizes letter of index 0 + remaining text.
    #without  + text[1:] will only show first capital letter
    return output

#capitalizing faster:
def capitalize(text):
    return text[0].upper() + text[1:]


    function_name(parameter)
        # =
    in terminal function_name(argument)

#Lets pretend sum() doesn't exist:
# sum() = TO THIS FUNCTION (what's happening in background)
def get_total(numbers):
    total = 0 
    for i in numbers:
        total += i
    return total

print(get_total([1, 2, 3]))


#FUNCTIONS CAN RETURN LISTS, TUPLES, DICT, ETC


#DEFAULT ARGUMENTS
def sayhi(name='stranger'):
    print(f'hello{name}')

IF we give argument john: sayhi('John')
will say "hello John"

IF we dont give an argument with name, will say "hello stranger"


def gettotal(numbers=[]):
    tot = 0
    for num in numbers:
        tot += num
    return tot

IF there are nr in list, will add them up
OTHERWISE just add up empty list


#CAN ADD AS MANY PARAMETERS AS REQUIRED
#parameters are ordered - what comes first, shows first etc. = postional arguments

def happyBday(name, age):
    print(f'Happy birthday {name}, you are {age} years old')
#postional arguments
happyBday('fred', 25)
#keyword arguments
happyBday(age=25, name="bob")



y = 10 #global - can be called with print

def something(name): #variables that are defined in a function - ONLY exist in funcion = local
    x = 5 #local. doesn't exist outside function. CAN'T be called in print
    name = name.upper()
    print(x)
    print(name)
    return x #makes local variable available in global scope. can be called!!!

x_value = something('whatever')
#will give us bob and 5
#will RETURN 5 and safe it in x_value!!!

x_value -> 5





z = 10
print (z)

def someelse(name):
    z = 5
    print(z)
   #return z 

someelse('bob') #call function
print(z)

#ON TERMINAL
will show:
10 #from z global
5 # z local
10# z global

IF we return & store local z we can print it 

y = something('bob')
will return:
10 # global z
5 # y (which stores local z)
10 #global z



# 1) create function that has 2 param:
    #your age & friend age
#return older age

# 2) create function that takes list as argument
#list contain 2 items




# 1 Create a function that has 2 parameters:
# Your age, and your friends age.
# Return the older age


# 2. Create a function that takes 2 words
# It must return the lenght of the longer word


# 3. Write the max() function yourself...


# 4.  Create a function that takes a list as an argument
# The list should contain any number of entries.
# each entry should have a name and grade
# return the name of the person with the highest grade


# Exer. 3
def maximum(numbers):  #defining function called maximum with parameter(numbers)
    maxi = numbers[0] #maxi = any given numbers - starting at first given number
    for num in numbers: #each loop num - in given numbers
        if num > maxi: #checks if num is larger than maxi
            maxi=num   # if yes, maxi becomes num
    return maxi 

nr_list = [4, -20, -95, -15, -2]
print(maximum(nr_list))


#exer 1
# 1 Create a function that has 2 parameters:
# Your age, and your friends age.
# Return the older age

def oldest(my_age, friend_age): #definind function oldest with my age & friends age
    if my_age > friend_age: # enters if statement: if my age is larger than friens age - return my age
        return my_age 
    else: #othrwise return friends age
        return friend_age









