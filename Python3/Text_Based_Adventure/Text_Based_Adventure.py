import os
from tictactoe import start_tictactoe

# Declaring variables.
rooms = ["0", "1", "2", "3", "X", "5"]
player_pos = 4

dog_free0 = False
dog_free1 = False
cat_free0 = False
sword0 = False
sword1 = False
floor0 = True
floor1 = False



# Map of the floors.
def map():
  print("----------------------------------")
  print("|          |          |          |")
  print("|     "+ rooms[0] +"    |     "+ rooms[1] +"    |     "+ rooms[2] +"    |")
  print("|          |          |          |")
  print("|          |          |          |")
  print("|----------+----------+----------|")
  print("|          |          |          |")
  print("|     "+ rooms[3] +"    |     "+ rooms[4] +"    |     "+ rooms[5] +"    |")
  print("|          |          |          |")
  print("|          |          |          |")
  print("------------|  |------------------")

# Redraws the rooms with updated "X" marker.
def draw_map():
  global player_pos, rooms
  print('\nRoom:', player_pos)
  rooms = ["0", "1", "2", "3", "4", "5"]
  rooms[player_pos] = "X"

# Code for player's movement.
def player_move():
  global player_pos, rooms, pos
  print('\nRoom:', player_pos)
  pos = input("Where do you want to go? (Up, Down, Left, Right) ")

  if pos.lower() == 'up':
    if player_pos <= 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    else:
      player_pos = int(rooms[player_pos - 3])
      draw_map()

  elif pos.lower() == 'down':
    if player_pos >= 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    else:
      player_pos = int(rooms[player_pos + 3])
      draw_map()

  elif pos.lower() == 'left':
    if player_pos == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    elif player_pos == 0:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    else:
      player_pos = int(rooms[player_pos - 1])
      draw_map()

  elif pos.lower() == 'right':
    if player_pos == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    elif player_pos == 5:
      os.system('cls' if os.name == 'nt' else 'clear')
      map()
      player_move()
    else:
      player_pos = int(rooms[player_pos + 1])
      map()
      draw_map()
  elif player_pos == int():
    os.system('cls' if os.name == 'nt' else 'clear')
    map()
    player_move()
  elif pos.lower() == 'open':
    pass
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    map()
    player_move()

# Floor0's code.
while floor0 == True:
  global pos

  map()
  player_move()
  os.system('cls' if os.name == 'nt' else 'clear')
  if player_pos == 0:
    if sword0 == True:
      print('Goblin Gaurd: "Halt! In the name of our lord Faodsyhfuiashfuo!" You are about to charge in but think better of it and throw the sword at the goblin killing him. You pull the sword out of his corpse.')
      input("\nPress enter to acsend: ")
      floor0 = False
      floor1 = True
    else:
      print("You entered the room. The guard turns toward you and charges you with his sword. You try to defend yourself but fail and die.")
      exit()
  elif player_pos == 1:
    if dog_free0 == True:
      print("The room is empty besides the cage.")
    else:
      print("You enter room 2. In the corner you see a cage with a pure white dog inside.\n\nWill you: OPEN?")
    if pos.lower() == 'open':
      dog_free0 = True
      if dog_free0 is True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('You set the dog free. The dog glances at you and runs out the door.      (!) Under the dog you see the letter "U"')
  elif player_pos == 2:
    if sword0 == True:
      print("There is nothing but an opened box.")
    else:
      print("In the center of the room there is a closed cardboard box.\n\nWill you: OPEN?")
    if pos.lower() == 'open':
      sword0 = True
      if sword0 is True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('You struggle with the packaging tape for a few moments. Wow you must really be a pathetic hero as that took far too long. Opening the box reveals a sword with a rubber handle. Whoever made this sword was an idiot, best to find a better one soon.')
  elif player_pos == 3:
    print("You see nothing. I mean literally nothing, it's just a black void. You feel around and touch something sticking out of the wall next to the door. It makes a clicking sound and a blinding light illuminates the room. There's still nothing..")
  elif player_pos == 4:
    pass
  elif player_pos == 5:
    print("You see nothing but a wooden table and chair.   (!)\nYou see the letter 'F' marked in table leg.")

# Floor1's code.
while floor1 == True:
  os.system('cls' if os.name == 'nt' else 'clear')

  if player_pos == 0:
    print('You walk up stairs to find your... Mom? She lunges at you with a belt. In that moment you trip, throwing your sword into the air and killing your Mom. She disapears into a puff of smoke. You say to yourself "Maybe I shouldn\'t of eaten those mushrooms outside the castle."')
  elif player_pos == 1:
    if dog_free1 == True:
      print("The room is empty besides the cage.")
    else:
      print("You see.. another caged dog? He sees you but doesn't make a sound.\n\nWill you: OPEN?")
    if pos.lower() == 'open':
      dog_free1 = True
      if dog_free1 is True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Setting the dog free he bolts out of the cage just as you unlock it.      (!) Under the dog you see the letter "C"')
  elif player_pos == 2:
    pass
  elif player_pos == 3:
    if sword1 == True:
      print("The old man absent mindly stares at you still thinking of a number.")
    else:
      print("A short fat old man is in the room with a rug laid out on the floor. He says, 'I'll give you this sword if you can guess my number else you die!!")
      num = input("I'm thinking of a number 1-100 ")
      sword1 = True
      print("Drats! You didn't give me enough time to think of a number! Here take the sword and get out of my sight!")
  elif player_pos == 4:
    print('Entering this room reveals a small library of sorts. On closer inspection all the books start with the letter "K".')
  elif player_pos == 5:
    if sword1 == True:
      print("Walking around with the sword for a while you begun to realize that the old man scammed you! This sword is made out of meat! opening the door a crack, you immediately hear insistent barking. With quick thinking you throw the sword in the corner of the room hoping the dog falls for it. Peaking in you see him eating your once 'sword'. You sneak towards the stairs.")
      input("\nPress enter to acsend: ")
      floor1 = False
      floor2 = True
      break

    else:
      print("You open the door a crack and immediately hear insistent barking. A chihuahua charges you! He stars gnawing your leg like a piranha. You fail to get him off and pathetically die to him.\n\nEND")
      exit()

  map()
  player_move()

# Floor 2's code or the boss room. It runs the Tictactoe functions.
while floor2 == True:
  os.system('cls' if os.name == 'nt' else 'clear')

  if player_pos == 0:
    print('Lord Faodsyhfuiashfuo, "You must play this intense game of Tictactoe in order to beat me!"')
    input("\nPress enter to start: ")
    start_tictactoe()
  elif player_pos == 1:
    if cat_free0 == True:
      print("The room is empty besides the cage.")
    else:
      print("Opening the door to the room you find a caged.. I'll let you guess... Cat!\n\nWill you: OPEN?")
    if pos.lower() == 'open':
      cat_free0 = True
      if cat_free0 is True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Setting the cat free he bites you and runs out.      (!) Under the cat you see the letter "K"')
  elif player_pos == 2:
    print("Inside the room you find a minitature white dwarf star. You notice it is the same model your dad bought you for your 5th birday.")
  elif player_pos == 3:
    print('A sign reads, "Why did you trust the arrow? It could have been a trap." You knock the sign over. ')

  elif player_pos == 4:
    print('<----------')
  elif player_pos == 5:
    if sword1 == True:
      print("The staircase disapears when you turn around.")

  map()
  player_move()