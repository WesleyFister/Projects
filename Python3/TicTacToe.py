import os
game_move =[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Prints Tic Tac Toe board on screen.
def game_board():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("          |          |")
	print("     " + str(game_move[0]) + "    |     " + str(game_move[1]) + "    |     " + str(game_move[2]) + "     ")
	print("          |          |")
	print("__________|__________|__________")
	print("          |          |")
	print("          |          |")
	print("     " + str(game_move[3]) + "    |     " + str(game_move[4]) + "    |     " + str(game_move[5]) + "     ")
	print("          |          |")
	print("__________|__________|__________")
	print("          |          |")
	print("          |          |")
	print("     " + str(game_move[6]) + "    |     " + str(game_move[7]) + "    |     " + str(game_move[8]) + "     ")
	print("          |          |")

def player1():
	game_board()

# Determines if input from user is an integer and is 1-9. Also if slot on board is taken by an "X" or an "O".
	try:
		global action0
		action0 = int(input("\nWhat is your move player 1? (1-9) "))
	except ValueError:
		action0 = None
		pass
	if action0 is not None:
		if int(action0) >= 0 and int(action0) <= 10:
			if type(game_move[action0 - 1]) == int:
				game_move[int(action0) - 1] = "X"
			else:
				game_board()
				player1()
		else:
			game_board()
			player1()
	else:
		game_board()
		player1()

# Win condition for player 1.
	if game_move[0] == "X" and game_move[1] == "X" and game_move[2] == "X" or game_move[3] == "X" and game_move[4] == "X" and game_move[5] == "X" or game_move[6] == "X" and game_move[7] == "X" and game_move[8] == "X" or game_move[0] == "X" and game_move[3] == "X" and game_move[6] == "X" or game_move[1] == "X" and game_move[4] == "X" and game_move[7] == "X" or game_move[2] == "X" and game_move[5] == "X" and game_move[8] == "X" or game_move[0] == "X" and game_move[4] == "X" and game_move[8] == "X" or game_move[2] == "X" and game_move[4] == "X" and game_move[6] == "X":
		game_board()
		print("Player 1 wins!")
		exit()

	game_board()

def player2():
	game_board()

# Determines if input from user is an integer and is 1-9. Also if slot on board is taken by an "X" or an "O".
	try:
		global action1
		action1 = int(input("\nWhat is your move player 2? (1-9) "))
	except ValueError:
		action1 = None
		pass
	if action1 is not None:
		if int(action1) >= 0 and int(action1) <= 10:
			if type(game_move[int(action1) - 1]) == int:
				game_move[int(action1) - 1] = "O"
			else:
				game_board()
				player2()
		else:
			game_board()
			player2()
	else:
		game_board()
		player2()

# Win condition for player 2.
	if game_move[0] == "O" and game_move[1] == "O" and game_move[2] == "O" or game_move[3] == "O" and game_move[4] == "O" and game_move[5] == "O" or game_move[6] == "O" and game_move[7] == "O" and game_move[8] == "O" or game_move[0] == "O" and game_move[3] == "O" and game_move[6] == "O" or game_move[1] == "O" and game_move[4] == "O" and game_move[7] == "O" or game_move[2] == "O" and game_move[5] == "O" and game_move[8] == "O" or game_move[0] == "O" and game_move[4] == "O" and game_move[8] == "O" or game_move[2] == "O" and game_move[4] == "O" and game_move[6] == "O":
		game_board()
		print("Player 2 wins!")
		exit()



# Game start.
while type(game_move[0]) == int or type(game_move[1]) == int or type(game_move[2]) == int or type(game_move[3]) == int or type(game_move[4]) == int or type(game_move[5]) == int or type(game_move[6]) == int or type(game_move[7]) == int or type(game_move[8]) == int:
  player1()
  if type(game_move[0]) == int or type(game_move[1]) == int or type(game_move[2]) == int or type(game_move[3]) == int or type(game_move[4]) == int or type(game_move[5]) == int or type(game_move[6]) == int or type(game_move[7]) == int or type(game_move[8]) == int:
    player2()
print("\nNobody wins!")