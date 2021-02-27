#EXERCISE 1
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

list1.extend(list2)

print(list1)

#EXERCISE 2
number = []

number.append(int(input('The first number is: ')))
number.append(int(input('The second number is: ')))
number.append(int(input('The third  number is: ')))

print(f'The biggest number is {max(number)}')


#EXERCISE 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range (len(alphabet)):
    if alphabet[i] in vowels:
        print(f'{alphabet[i]} is a vow')
    else:
        print(f'{alphabet[i]} is a const')

#EXERCISE 4
names = ['samus', 'cortana', 'v', 'link', 'mario', 'cortana', 'samus']

print(names)

for nam in names:
    nam = str(input('Give me a name: '))
    if nam in names:
        print(names.index(nam))
        continue 
    elif nam == 'exit':
        break
    else:
        names.append(nam)


#EXERCISE 5
words = []

while len(words) != 7:
    words.append(str(input('Give me a word: ')))
print(words)
    

for i in range (len(words)):
    letter = input('give me a single letter: ')
    if letter in words:
        print(f'the letter {letter} is at the index {words.index(letter)}')
    else:
        print('Sorry, no letter found')


#EXERCISE 6

million = [] # we want to create list - empty for now

for i in range(1, 1000001):
    million.append(i)

print(million)

print(min(million))
print(max(million))
print(sum(million))

#ex 6 - LIST COMPREHENSION
million = [i for i in range(1, 1000001)] #makes loop run in the list