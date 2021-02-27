#1 get random words v
#2. split words into letters v
#3 make words into*
#4. make a list of stars
#4. let user guess letter
#5 if letter incorrect -1 life
#6 if letter correct, uncover / print
import random 

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)


word_split = list(word)
star_list = []

for i in range(len(word_split)):
    star_list.append("*")









