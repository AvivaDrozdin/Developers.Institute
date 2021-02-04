
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
def longest_length(word1, word2):
    return max(len(word1), len(word2)) #return max of len of word 1 or 2
        


# 3. Write the max() function yourself...
def maximum(numbers):  #defining function called maximum with parameter(numbers)
    maxi = numbers[0] #maxi = any given numbers - starting at first given number
    for num in numbers: #each loop num - in given numbers
        if num > maxi: #checks if num is larger than maxi
            maxi=num   # if yes, maxi becomes num
    return maxi 

nr_list = [4, -20, 95, -15, -2]

print(maximum(nr_list))

# 4. Create a function that makes a list as an argument 
# the list should ontain any nr of entries
# each entry should have a name and grade
# return the name of the person with the highest grade

students = [
    {'Name': 'Adam', 'Grade' : 80},
    {'Name': 'Bob', 'Grade': 72},
    {'Name': 'Charlie', 'Grade': 81}
]

def top_student(students):
    top = students[0]
    for student in students:
        if student['grade'] > top['grade']:
            top = student
            
    return biggest