#Ex 1
def insert_word():
    item = input('What would you like to add? ')
    position = int(input('Where would you like to add it? '))
    my_list.insert(position, item) #WHY only this way round??


my_list = ['Hello', 'friend']
print(my_list)
insert_word()
print(my_list)

#Ex 2
text_sample = 'Hello world. I love Python'

def count_spaces(text):
    counter = text.count(' ')
    return counter

print(count_spaces(text_sample))

#Ex 3
some_text = input('Give me a sentence: ')

def count_upper_lower(text):
    upper = 0
    lower = 0
    for letter in text:
        if letter.isupper():
            upper +=1
        elif letter.islower():
            lower +=1
    
    print(f'There are {upper} uppercase letters, and {lower} lowercase letters in the sentence')

count_upper_lower(some_text)


#Ex 4
def find_maxi(numbers):
    maxi = numbers[0]
    for num in numbers:
        if num > maxi:
            maxi = num
    return maxi

numbers_list = [1, 14, 55, 32, 12]

print(find_maxi(numbers_list))


#Ex 5

#Ex 6
add_numbers = [1, 2, 3, 4]

def add_up(numbers):
    sum = 0
    for item in numbers:
        sum += item
    return sum

print(add_up(add_numbers))

#Ex 7

#Ex 8
more_numbers = [1, 2, 3]

def square_root(numbers):
    total = 0
    for n in numbers:
        total += n**2
    result = total**(1/2)
    return result

print(square_root(more_numbers))

#Ex 9

#Ex 10
word_list = ['hello', 'this', 'is', 'asuperduperlong', 'word']

def longest_word(text):
    longest = ''
    for word in text:
        if len(longest) < len(word):
            longest = word
    return longest

print(longest_word(word_list))

#Ex 11
sentence = ['This', 'is', 10, 'a', 12, 15, 'word', 43, 'maybe']

def split_types(list):
    number = []
    strings = []
    for item in list:
        if type(item) == str:
            strings.append(item)
        else:
            number.append(item)
    return numbers, strings
    
print(split_types(sentence))