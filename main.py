
#Tic Tac Toe GAME

#Global Variables

#board
board= ["_", "_", "_", 
        "_", "_", "_", 
        "_", "_", "_" ]
#if game still going
game_still_going= True
#who won or tie?
winner=None
#whose turn it is
current_player = "X"

def display_board():
  print(board[0]+ " | "+board[1]+ " | "+board[2])
  print(board[3]+ " | "+board[4]+ " | "+board[5])
  print(board[6]+ " | "+board[7]+ " | "+board[8])

def play_game():

  #display initial board
  display_board()

  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()

    #Flip to the other player
    flip_player()
  
  #Ending
  if winner == "X" or winner =="O":
    print("Oooohhhoo "+ winner+" WON")
    print("LET's CELEBRATE")
  elif winner==None:
    print("Tie")


def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a VALID position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "_":
      valid = True
    else:
      print("You can't go there. Go again.")

      
  board[position]=player
  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():

  global winner

  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner= check_diagonals()

  if row_winner:
    winner=row_winner

  elif column_winner:
    winner= column_winner

  elif diagonal_winner:
    winner=diagonal_winner

  else:
    winner=None
  return


def check_rows():
  global game_still_going

  row_1 = board[0]==board[1]==board[2] != "_"
  row_2 = board[3]==board[4]==board[5] != "_"
  row_3 = board[6]==board[7]==board[8] != "_"
  
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return




def check_columns():
  global game_still_going

  column_1 = board[0]==board[3]==board[6] != "_"
  column_2 = board[1]==board[4]==board[7] != "_"
  column_3 = board[2]==board[5]==board[8] != "_"
  
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[4]
  elif column_3:
    return board[8]
  return



def check_diagonals():
  global game_still_going

  diagonals_1 = board[0]==board[4]==board[8] != "_"
  diagonals_2 = board[6]==board[4]==board[2] != "_"
  
  
  if diagonals_1 or diagonals_2 :
    game_still_going = False
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  
  return


def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going = False
  return


def flip_player():
  global current_player

  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"

  return

play_game()


