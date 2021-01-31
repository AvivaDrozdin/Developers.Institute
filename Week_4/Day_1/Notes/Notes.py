# print('hello')

# myAge = 25

# print(myAge + 123879) #in comand

# print('Hello \nmy name is Aviva') #\n new line

# name = 'aviva'
# name.upper() # = will make name aviva with uppercase = Aviva
# name.lower() # = will make name Aviva with lowecase = aviva

# name.title() # = capetalizes every single word in sentance
# name.capitalize() # capetilizes first word of sentance

# #How to convert string to interger? 
# number = '5'
# int(number) # converts string "5" to interger 5
# str(number) # converts interger to string (5 to "5")
# float(number) # changes interger 5 to float 5.0

# #Boolean
# bool(5) # = true
# bool(-5) # = true
# bool(0) # = false
# #WHY?
# # Computers run on binery (0 & 1)
# # no electricity = 0 electricity = 1
# # Same with boolean
# # if there is a value (5, -5, hello etc) is true
# # if there is NO value (0 or empty sting) = false

# otherName = 'mark'
# len(otherName) # =4 - gives yout the length of an array


# # How to get a variable into a sentance? e.g.
# "Hello Mark, you are 5 years old"

# #Option 1
# # print ('Hello ' + otherName + 'you are ' + str.number + 'years old')
# # #option 2
# # print ('Hello {} you are {} years old'.format(otherName, number))
# # #Option 3
# # print(f'Hello {name} you are {number} years old')


# #how to get user input? (equivalent to js)
# fname = input('What is your name? ')
# ageP = int(input('How old are you? ')) # makes string to interger

# print(fname)
# print(ageP) #computers read everything in strings

#              #makes name with capital
# print(f'Hello {fname.capitalize()} you are {ageP + 1} old') # have to convert age sting to int.


# # CONDITIONALS (if / else )

# newAge = int(input('How old are you')) # no{} required to to space in if/else block
# county = 'Israel'

# # NEEDS the spaceing in conditionals! Otherwise conditional not readable

# if newAge >= 18 and country == 'Israel':  # IF
#     print('Have a GoldStart') 

# elif age <= 18 or country =='USA': #ELSE IF
#     print('Have a soda')

# else: #ELSE
#     print('Have a soda') 

# print('Thanks for coming')

# && = and in py
#|| = or in py


email = input('Enter email address ')

if '@' not in email:
    print('invalid address')
else:
    print('added to spam')




