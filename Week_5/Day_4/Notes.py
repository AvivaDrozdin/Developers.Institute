#JSON, API, I/O 

#(JSON is not a way of sending data - is  a format of data)

# Python File I/O:
# Python file operations: opening a file / reading it / closing it

with open('name.txt', 'w') as f: #f = file
    #open (text file 'name', write) as file
	f.write('hello')
    #file write 'hello'

#once you get out of the block, file closes

w = write
r = read
a = append
