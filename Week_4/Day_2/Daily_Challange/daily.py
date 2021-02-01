birthday = input("When is your birthday? DD MM YYYY: ")

candles = int(birthday[-1])
day, month, year = birthday.split(' ')
year = int(year) # checks for birthyear
top = int((11-candles)/2)
topRight = top
if candles%2 == 0:
    topRight += 1    # if there is an even number of candle, add another line to the right, so the lenght will stay the same

# Defining symbols

line = "_"
candle = "i"
space = " "
frostTop = "^"
frostBottom = "~"

# Cake-function

def cake():
    print(f"{4*space}{top*line}{candles*candle}{topRight*line}")
    print(f"{3*space}|:H:a:p:p:y:|")
    print(f"{1*space}{2*line}|{11*line}|{2*line}")
    print(f"|{17*frostTop}|")
    print(f"|:B:i:r:t:h:d:a:y:|")
    print(f"|{17*space}|")
    print(f"{19*frostBottom}")

# Print
if year%4 == 0: # if leap year -> 2 cakes
    cake()
    print("")
    cake()
else:
    cake()