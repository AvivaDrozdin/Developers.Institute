#CONDITIONALS
#1. 
month = int(input('Which month is it? (1-12) '))

if month >= 3 and month <=5:
    print('Spring runs between March and May')
elif month >=6 and month <=8:
    print('Summer runs between June and August')
elif month >=9 and month <=11:
    print('Autumn runs between September and November')
elif month <= 12 and month >= 1:
    print('Winter runs between December to February')
elif month == 0 or month >12:
    print('Invalid Input')


#2. 
#ask the user for their name if the name begins with the letter a print a if b print b if c print c if none of the above print does not start with a b or c
#.startswith()

#option 1
name = input('What is your name? ').lower()

if name.startswith('a'):
    print('a')
elif name.startswith('b'):
    print('b')
elif name.startswith('c'):
    print('c')
else:
    print("Your name doesn't start with A B or C")

#option 2
initial = name[0].lower()

if initial == 'a': 
    print('a')
elif initial == 'b': 
    print('b')
elif initial == 'c': 
    print('c')
else: 
    print('I dont know')


#LIST & DICTIONARY
#List:
#Ordered. To grab items use index
names = ['Chaim', 'Esther', 'Sam', 'Aviva']

#get name at position x
print(name[0]) = Chaim
print(name[1]) = Esther

#get length of list
print(len(name)) = 4 (gives length of list)

#remove from list
names.pop() = removes last item in list 
names.pop(0) = removes item at position 0
names.remove('Esther') = removes Esther

#add to list
names.append('Lisa') = adds item to end of list 
names.insert(2, 'Josh') = adds josh to position 2

#how to split ONE word?
name = 'chaim'
print(list(name)) = makes name into list and splits by letter
#split () does not work as there are no dividors between (, or ' ' etc.)

#3 
# 3. Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove('Banana')
#print(basket)

basket.pop(2)
#print(basket)

basket.append('Kiwi')
#print(basket)

basket.insert(0, 'Apples')
#print(basket)

count = basket.count('Apples')
#print(count)


basket.clear()
print(basket)


#DICTIONARY





