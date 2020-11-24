from replit import clear
import random
from art import logo
print(logo)
print('Do you want to start the game: ')
start=input('Type y or n: ')
deck={'Ace':11, '_2_':2, '_3_':3, '_4_':4, '_5_': 5, '_6_':6, '_7_':7, '_8_':8, '_9_':9, '_10_':10, 'King':10, 'Queen':10, 'Jack':10}
game_start=True

def sumup(lst):
  total=0
  for el in lst:
    total+=deck[el]
  total_aces=lst.count('Ace')
  while(('Ace' in lst) and total>21 and total_aces>0):
    total-=10
    total_aces-=1
  return total


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def random_value():
  return random.choice(list(deck.keys()))

while(game_start):
  computers_deck=[]
  computers_deck.append(random_value())
  computers_deck.append(random_value())
  print(f"Computer's cards: ['{computers_deck[0]}',___]" )
  while(sumup(computers_deck)<17):
    computers_deck.append(random_value())

  players_deck=[]
  players_deck.append(random_value())
  players_deck.append(random_value())
  print(f"Your cards are : {players_deck} - {sumup(players_deck)} ")
  
  pick='y'
  while(pick=='y' and sumup(players_deck)<22):
    print('-'*10,'\nDo you want to go again:')
    pick=input('Type y or n: ')
    if(pick=='n'):
      print(f"Computer's cards: {computers_deck} - {sumup(computers_deck)}" )
      print(f"Your cards are : {players_deck} - {sumup(players_deck)} ")
      break
    players_deck.append(random_value())
    print(f"Computer's cards: ['{computers_deck[0]}',___]" )
    print(f"Your cards are : {players_deck} - {sumup(players_deck)} ")
  print(compare(sumup(players_deck),sumup(computers_deck)))
  print('Do you want to end the game: ')
  endgame=input('Type y or n: ')
  if(endgame=='y'):
    game_start=False
  elif(endgame=='n'):
    game_start=True
    clear()
    print(logo)
