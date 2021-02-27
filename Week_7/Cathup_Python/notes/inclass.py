# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

# magicians = ['Houdini', 'Copperfield', 'Blaine']

# def show_magicians():
#     for name in magicians:
#         print(name)

# def make_great():
#     great = []
#     for name in magicians:
#         great.append(f'The great {name}')
#     print(great)

#create a a function called shopping list that asks the user for items untill the user decides to exit then prints out the list

def shopping():
    basket = []

    while True:
        item = str(input('add to basket: '))
        if item != 'exit':
            basket.append(item)
        else:
            print(basket)
            break


