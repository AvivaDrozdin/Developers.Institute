#  Exercise_1
#/ If you want to call your program, python will check if there are any executable programs in you computer.
#/ If the file is in your path, it can be executed from this place.

# Exercise_2
# alias / second name of data (eg. python = py)


#Exercise 3
3 <= 3 < 9 # expected outcome false // actual outcome true
3 == 3 == 3 # expected outcome true // actual outcome true
bool(0) # expected outcome false // actual outcome false
bool(5 == "5") #expected outcome true // actual outcome false (int != str)
bool(4 == 4) == bool("4" == "4") # expected outcome true // actual outcome true
bool(bool(None)) #expected outcome false // actual outcome false


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) #expected true // actual true
print("y is", y) # expected false // actual false
print("a:", a) # expected 5 (because True (which is 1) + a (4) = 5) // actual 5
print("b:", b)  #expected 10 (because 1 is false, so nothin gets added to b) // actual 10


#Execise 4
my_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

print(len(my_text)) #445 characters 

#Exercise 5

length = 0

while True:
    sentence = input('What is the longest sentence you know, without A? ')

    if 'a' in sentence or 'A' in sentence:
        print:('Oops, there was an A!')
    
    elif len(sentence)<length:
        print(f'The sentence was shorter than {length} charackters')
    
    else:
        length = len(sentence)
        print(f'Well done, your sentence is {length} charecters long')
    
