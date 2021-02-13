# w = write (if repeated, it overwrites the previous text)
# r = read
# a = append
# w+ = write + read
# a+ = append + read

#Reading:
#f.read() = Reads the entire file into a single string
#f.readline() = Reads a single line (if repeated - reads 2nd and so on)
#f.readlines() = Reads the entire file into a list of strings


#f.tell() = tells you where cursor is
#f.seek() = changes position of cursor





# with open('name.txt', 'w') as f:
#     f.write('Hi \n')

# with open('name.txt', 'a') as f:
#     f.write('hi again')

# with open('name.txt', 'w') as f: #overwrites the first w and a
#     f.write('Hello \n')

# with open('name.txt', 'a') as f:
#     f.write('Bye')

# with open('name.txt', 'r') as f:
#     data = f.readline() #reads first line - if repeated - reads 2nd and so on


# with open('name.txt', 'r') as f:
#     text = f.read()

# with open('name.txt', 'r') as f:
#     emails = f.readlines()



# with open ('name.txt', 'r') as f:
#     data = f.readlines()

# for person in data:
#     person = person.strip('\n')
#     print(f'sending email to {person}')

with open('name.txt', 'r') as f:
    print(f.seek(5)) #starts of at index 5
    data = f.readlines()
    print(f.tell()) #tells me where we are in txt file

