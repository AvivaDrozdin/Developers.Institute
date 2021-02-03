
# 1 Create a function that has 2 parameters:
# Your age, and your friends age.
# Return the older age
def oldest(myAge, friendAge):
    if myAge > friendAge:
        return myAge
    else:
        return friendAge



# 2. Create a function that takes 2 words
# It must return the lenght of the longer word
def longest(word1, word2):
    if len(word1) < len(word2):
        


# 3. Write the max() function yourself...
def maximum(numbers):  #defining function called maximum with parameter(numbers)
    maxi = numbers[0] #maxi = any given numbers - starting at first given number
    for num in numbers: #each loop num - in given numbers
        if num > maxi: #checks if num is larger than maxi
            maxi=num   # if yes, maxi becomes num
    return maxi 

nr_list = [4, -20, 95, -15, -2]

print(maximum(nr_list))