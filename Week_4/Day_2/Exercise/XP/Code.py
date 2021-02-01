#EXERCISE 1

my_favorite_number = {3, 7, 8, 64}
my_favorite_number.add(9)
my_favorite_number.add(10)
my_favorite_number.pop()

print(my_favorite_number)

friend_favorite_number = {4, 1, 2, 11}

our_favorite_numbers = my_favorite_number.union(friend_favorite_number)

print(our_favorite_numbers)


#EXERCISE 2
#You can't add or remove anything to a tuple because of their immutable propertiy.


#EXERCISE 3
for i in range(21):
    print(i)


#EXERCISE 4
#intergers represent whole (positive or negative) numbers like 5 or -5
#floats represent real numbers like -2.5 or 3.141

#flots can be created either by float(int) function or by division of intergers

for i in range(1,5):
    print(i + 0.5)
    print(i + 1)


#EXERCISE 5
basket = ['banana', 'apples', 'oranges', 'blueberries']

basket.remove('banana') #removal option 1
basket.pop() #removal at end option 2 - blueberries
basket.append('kiwi') # add kiwi at the end
basket.insert(0, 'apples') #add apple at beggining
basket.count('apples') #count how many apples
basket.clear() #empties out basket

print(basket)


#EXERCISE 6

myname = 'Aviva'

name = input('What is the name? ')

while name != myname:
    name = input('What is the name? ')


#EXERCISE 7

#?

#EXERCISE 8
newList = []

for x in range(3, 31):
    newList += [x]

print(newList)


#EXERCISE 9

for y in range(1500, 2701):
    if y%7 == 0 and y%5 ==0:
        print(y)


#EXERCISE 10

fruit = input('What are your favorite fruits? (separated by space) ')

fruit_list = fruit.split() #makes strings into a list

new_fruit =('Add another fruit')

if new_fruit in fruit_list:
    print('You have chosen one of your favorite fruits. Enjoy!')
else:
    print('You have chosen a new fruit. Hope you enjoy it too!')


#EXERCIE 11
topping = []

while True:
    ask = input('What topping would you like on your pizza?QUIT to leave menu ')
    if ask == 'QUIT':
        break
    else:
        topping.append(ask)
        print(f'Following toppings added to your pizza: {ask} ')

print
toppingList = ', '.join(topping)

print(f'Your got following items on your pizzs {toppingList}. \n The total is ${10 + 2.5*len(topping)}. ')


#EXERCISE 12
people = input('How many people? ')
peopleAge = []
prices = [0, 10, 15]
ticketPrice = []

for z in range (0, people):
    askPerson = int(input(f'How old are you {z+1}? '))
    if askPerson < 3:
        ticketPrice.append(prices[0])
    elif askPerson >= 3 and askPerson <12:
        ticketPrice.append(prices[1])
    elif askPerson >= 16 and askPerson <= 21:
        print('People between 16 and 21 cannot see this movie')
    else:
        ticketPrice.append(prices[2])

final = 0
for a in range (0, len(ticketPrice)):
    final += ticketPrice[i]

print(f'Your final price is ${ticketPrice}')


#EXERCISE 13
user = []

amount = int(input('How many people? '))

for b in range (0, identifier):
    user_age = int(input('What is your age? '))
    user.append(user_age)

print(users)

new_list = []

for c in range (0, amount):
    if user[b] <= 16:
        continue
    else:
        new_list.append(user[b])

print(new_list)


#EXERCISE 14

family_list = []

while True:
    print("1. Name \n 2. Remove existing name \n 3. View Family Members \n 4. Exit")

    c = int(input('Choose your option 1. 2. 3. or 4.'))
    if c <1 and x >4:
        c = int(input('Choose your option 1. 2. 3. or 4.'))
    elif c == 1:
        newName = input('Add your name: ')
        family_list.append(newName)
    elif c == 2:
        removeName = input('Which name should be removed? ')
        if no family_list:
            print('No names inside')
            break
        else:
            family_list.remove(removeName)
    elif c == 3:
        family_list = ', '.join(family_list)
        print(f'These names are currently in the list: {family_list}')
    else:
        break
    



