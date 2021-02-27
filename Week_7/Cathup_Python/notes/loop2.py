#LOOPS

#For Loop
# for num in range (50, 251):
#     if num % 3 == 0:
#         print (num)


#
#if name starts with A B C
# names = ['alec', 'ben', 'charlie', 'daniel', 'Freddy']
# a_list = []
# b_list = []
# c_list = []

# for name in names:
#     if name.startswith('a'):
#         a_list.append(name)
#     elif name.startswith('b'):
#         b_list.append(name)
#     elif name.startswith('c'):
#         c_list.append(name)

# print(a_list)
# print(b_list)
# print(c_list)

# #If name contains A B C
# names = ['alec', 'ben', 'charlie', 'daniel', 'Freddy']
# a_list = []
# b_list = []
# c_list = []

# for name in names:
#     if 'a' in name:
#         a_list.append(name)
#     elif 'b' in name:
#         b_list.append(name)
#     elif 'c' in name:
#         c_list.append(name)

# print(a_list)
# print(b_list)
# print(c_list)

# While Loop
# runs until condition is met

counter = 50
while counter < 60:
    if counter % 3 == 0:
        print(counter)
    counter += 1


#while active is true - input name
# as long as name is not exit, append entered names to list
#else make active false - leave loop

active = True
name_list = []
while active:
    name = input('What is your name? \n')
    if name != 'exit':
        name_list.append(name)
    else:
        active = False
print(name_list)


#create a while loop with a flag that asks the user the name of a city theyd like to visit when finishe entering all the cities input exit the finish the loop and print all the cities


visit = []

while True:
    cities = input('Which cities would you like to visit? \n')
    if cities != 'exit':
        visit.append(cities)
    else:
        break
print(visit)




