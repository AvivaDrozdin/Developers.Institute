board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0

#print board
def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()

#function to exit game
def quit(user_input):
  if user_input.lower() == "exit": 
    print("Thanks for playing")
    return True
  else: return False



def check_input(user_input):
  #1 - check if its a number
  if not isnumber(user_input): return False
  user_input = int(user_input)
  #2 - check if its 1 - 9
  if not from_to_nr(user_input): return False

  return True

#1) function to check in input is nr
def isnumber(user_input):
  if not user_input.isnumeric(): 
    print("This is not a valid character")
    return False
  else: return True

#2)  function to check if nr is within 1-9 rage
def from_to_nr(user_input):
  if user_input > 9 or user_input < 1: 
    print("This is number is is invalid")
    return False
  else: return True

def istaken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] != "-":
    print("This position is already taken.")
    return True
  else: return False

def coordinates(user_input):
  row = int(user_input / 3)
  col = user_input
  if col > 2: col = int(col % 3)
  return (row,col)

def add_to_board(coords, board, player):
  row = coords[0]
  col = coords[1]
  board[row][col] = player

def current_user(user):
  if user: return "x"
  else: return "o"

def winning(user, board):
  if check_row(user, board): return True
  if check_col(user, board): return True
  if check_diag(user, board): return True
  return False

def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False 

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  #top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False

while turns < 9:
  player = current_user(user)
  print_board(board)
  user_input = input("Please enter a position 1 through 9 or enter \"exit\" to quit: ")
  if quit(user_input): break
  if not check_input(user_input):
    print("Please try again.")
    continue
  user_input = int(user_input) - 1
  coords = coordinates(user_input)
  if istaken(coords, board):
    print("Please try again.")
    continue
  add_to_board(coords, board, player)
  if winning(player, board): 
    print(f"{player.upper()} won!")
    break
  
  turns += 1
  if turns == 9: print("Tie!")
  user = not user

