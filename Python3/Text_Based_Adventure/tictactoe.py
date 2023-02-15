def start_tictactoe():
  import os
  import random
  global game_move
  game_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]


  
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
  		print("NOOOOO, How can I have been defeated? Here take my gold I can't go on.")
  		exit()
  
  	game_board()
  
  
  
  # Lord Faodsyhfuiashfuo's code to play Tictactoe.
  def player2():
    game_board()
    action2 = random.randint(0, 8)
    if type(game_move[action2]) == int:
      game_move[int(action2)] = "O"
    else:
      player2()
  
    # Win condition for Faodsyhfuiashfuo.
    if game_move[0] == "O" and game_move[1] == "O" and game_move[2] == "O" or game_move[3] == "O" and game_move[4] == "O" and game_move[5] == "O" or game_move[6] == "O" and game_move[7] == "O" and game_move[8] == "O" or game_move[0] == "O" and game_move[3] == "O" and game_move[6] == "O" or game_move[1] == "O" and game_move[4] == "O" and game_move[7] == "O" or game_move[2] == "O" and game_move[5] == "O" and game_move[8] == "O" or game_move[0] == "O" and game_move[4] == "O" and game_move[8] == "O" or game_move[2] == "O" and game_move[4] == "O" and game_move[6] == "O":
      game_board()
      print("HAHAHA, you lose hero and now you shall die!")
      exit()
  
  
  def start():
    while type(game_move[0]) == int or type(game_move[1]) == int or type(game_move[2]) == int or type(game_move[3]) == int or type(game_move[4]) == int or type(game_move[5]) == int or type(game_move[6]) == int or type(game_move[7]) == int or type(game_move[8]) == int:
      player1()
      if type(game_move[0]) == int or type(game_move[1]) == int or type(game_move[2]) == int or type(game_move[3]) == int or type(game_move[4]) == int or type(game_move[5]) == int or type(game_move[6]) == int or type(game_move[7]) == int or type(game_move[8]) == int:
        player2()
      print("\nNobody wins! And you decide to go home and take a nice hot shower. You wonder what those letters meant...")
  start()