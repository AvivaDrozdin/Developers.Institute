#EXCEPTIONS (unexpected error)

animals = ['dog', 'cat']

sheep = animals[2] #crash because no postion 2 in list

num = int(input('which animal nr do u want?')) # if 0 or 1 - ok. 2,3,4... CRASHES

#How to prevent crashing WITHOUT conditionals?
# eg if we try access 5:

try: #code will TRY accessing nr 5, will crash
    print(animal[num])
except: #will catch crashing code and print instead:
    print('that nr is not available')

print('The End')

# catch crashing code! 
print(animal[num])


pets = ['dog', 'mouse']

user_inp = input('which animal nr do u want?')

try: 
    index = int(user_inp)
    print(animal[index])
except ValueError: #will ONLY catch value error (e.g. string instead int)
    print('Your input must be a nr')
except IndexError: #Will ONly catch index error (e.g. if int too big)
    print('This nr is too big')
except Exception: # will catch ALL errors

except IOError: # Input / output error (e.g. trying to read file that either that doesn't exist or you have no access too)

print('The end')

# try = try this, hope this works
# except = it didn't work, run this
#finally = always run this next (will run either way if code successful or not )




my_list = [2, 3, 'four', 1, None]

def summ(mylist):
    total = 0 
    for num in mylist:
        try: #try add num to total
            total += num
        except TypeError: # if get type error
            continue #ignore it & continue
    return total



#!!!! CAREFUL - If input to often invalid, can cause stack overflow (memory overflow)
def get_age():
    try: 
        age = int(input('How old are you? ')) #try asking for age
    except Exception:
        print('Invalid input. Try again') # if you get any type of error (e.g. not and int) ask to re-enter
        get_age() # repeat function until you get the age
    print('You are old')



# IMPORT

#How to import random nr?

#option 1
#import module from library (that is pre-installed in python. Can instal additional libraries)
#used if need many methods from random
import random 
random.randint(1,10) #random int between 1-10

#option 2
#used if needs only few specific function from random
from random import randint
randit(1,10)

#can change name of function if
import random as ran #changes name  of function to ran
from random import randit as randi #change name of method


#allows to automatically run in terminal
# &
#allows to import this code to different file
if __name__ == '__main__':
    print('hi')