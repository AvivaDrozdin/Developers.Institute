#EXERCISE 1
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

list1.extend(list2)

print(list1)

#EXERCISE 2
number = []

number.append(int(input('first number: ')))
number.append(int(input('second number: ')))
number.append(int(input('thrid number: ')))

number.sort()

print(f'the highest number is {number[len(number)-1]}')


#EXERCISE 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range (0, len(alphabet)):
    for e in range (0, len(vowels)):
        if vowels[e] in alphabet[i]:
            print(f'{vowels[e]} is a vowel')
        print(f'{alphabet[i]} is a consonant')

#EXERCISE 4
names = ['samus', 'cortana', 'v', 'link', 'mario', 'cortana', 'samus']

print(names)

askName = input('pick a name: ')

if askName in names:
    print(f'This name exists on index {names.index(askName)}')
else:
    print('This name is not in the list')


#EXERCISE 5
words = []
askWords = input('Give me 7 words: ')

words = askWords.split(',') #puts words in list 
while len(words) != 7:
    askWords = input('Give me 7 words: ')
    words = askWords.split(',')

letter = input('give me a single letter: ')

for j in range (0, len(words)):
    if letter in words(j):
        print(f'the letter {letter} is at the index {words[j].find(letter)}')
    else:
        print('Sorry, no letter found')


#EXERCISE 6

million = []

for i in range(1, 1000001):
    million.append(i)

print(million)

print(min(million))
print(max(million))
print(sum(million))