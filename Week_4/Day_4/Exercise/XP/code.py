# #Exer. 1
# def display_message(text):
#     print('I am learning about functions today')

# #Exer 2
# def favorite_book(title):
#     print(f'One of my favorite books is {title}')

# favorite_book('21 lessons for the 21st century')

# #Exer 3
# def describe_city(city, country = 'Lithuania'):
#     print(f'{city} is in {country}. ')

# describe_city('Vilnius')
# describe_city('Moscow', 'Russia')
# describe_city('Cartagena', 'Colombia')

# #Exer 4

# inputNr = int(input('Number between 1 - 100: '))

# def comparison(number):
#     random == inputNr.randint(1, 102)
#     if random == number:
#         print('Correct')
#     else:
#         print(f'{random} is not equal to {number}')

# #Exer 5
# def make_shirt(size = 'L', message):
#     default = 'I <3 Python'
#     if size == 'L' or size == 'M':
#         print(f'You have chosen a T-Shirt sized {size} with the message "{python}"')
#     else:
#         print(f'You have chosen a T-Shirt sized {size} with the message "{message}" ')


# #postitional
# make_shirt('S', 'Hello Shirt')
# #keyword
# make_shirt(message='Bye Shirt', size='S')

# #Exer 6
# magicians = ['Shin Lim', 'Houdini', 'Copperfield']

# def show_magicians(list):
#     for name in list:
#         print(f'There is a magician named {name}')

# show_magicians(magicians)

# def make_great(list):
#     addition = []
#     for name in list:
#         addition.append(f'The Great {name}')
#     return addition

# great = make_great(magicians)
# show_magicians(great)

# #Exer 7

# #Exer 8 ?
select = int(input('Give me a number between 1 and 9: '))

def calc(select):
    total = int(select) + int(2*select) + int(3*select) + (4*select)
    return total

