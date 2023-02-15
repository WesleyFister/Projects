import random
import os


def card_game_war():
  player1 = input('What is your name player1? ')
  player2 = input('What is your name player2? ')
  deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
  cards1 = []
  cards2 = []
  points1 = []
  points2 = []
  
  
  
  # Function that determines who has won or tied and hands out the cards to the winner.
  def scoring():
    if cards1[0] > cards2[0]:
      print(player1, 'won! And takes', player2 + '\'s cards.')
      points1.append(cards2.pop(0))
      points1.append(cards1.pop(0))
  
    elif cards2[0] > cards1[0]:
      print(player2, 'won! And takes', player1 + '\'s cards.')
      points2.append(cards2.pop(0))
      points2.append(cards1.pop(0))
  
    elif cards1[0] == cards2[0]:
      if len(cards1) <= 4 or len(cards2) <= 4:
        cards1.remove(cards1[0])
        cards2.remove(cards2[0])
  
      else:
        print(player1, 'places 3 cards face down and draws', cards1[3])
        print(player2, 'places 3 cards face down and draws', cards2[3])
        
        if cards1[3] > cards2[3]:
          for i in range(4):
            points1.append(cards2.pop(0))
            points1.append(cards1.pop(0))
    
        elif cards2[3] > cards1[3]:
          for i in range(4):
            points2.append(cards2.pop(0))
            points2.append(cards1.pop(0))
    
        elif cards1[3] == cards2[3]:
          scoring()
      
    if len(cards1) == 0 or len(cards2) == 0:
      if len(points1) > len(points2):
        print(player1, 'wins the game!')
        exit()
      if len(points2) > len(points1):
        print(player2, 'wins the game!')
        exit()
      if len(points1) == len(points2):
        print('Both players tied!')
        exit()
  
  # Splits a 52 card deck into 2 decks of 26 that are shuffled
  for i in range(26):
    cards1.append(deck.pop(random.randint(0, deck.index(deck[-1]))))
    cards2.append(deck.pop(random.randint(0, deck.index(deck[-1]))))
  
  while True:
    #Player1
    input('press enter to draw your card. ')
    print(player1, 'drew', cards1[0])
    print('Points:', len(points1), '\n')
    #print(cards1)
  
    #Player2
    input('press enter to draw your card. ')
    print(player2, 'drew', cards2[0])
    print('Points:', len(points2), '\n')
    #print(cards2)
  
    scoring()
    input('Start next round.')
    os.system('cls' if os.name == 'nt' else 'clear')

card_game_war()