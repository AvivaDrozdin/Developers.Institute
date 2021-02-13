#EX 1
import random
#Description: We will create a program that will generate a random sentence and display it to the user. We will allow the user to choose how long the sentence will be.

#Hint : The random sentences do not need to make sense or to be grammatically correct

#1. Download this word list
#2. Save it in your development directory.

def get_words():
    with open ('text.txt', 'r') as f:
        data = f.readlines()
        return data


def get_random_sentence(length):
    data = get_words()

    # sent_length = int(input('How many words should the sentence be?'))

    sentence = random.sample(data, length)

    sentence_string = '' += join.(sentence)


    print(sentence_string)







