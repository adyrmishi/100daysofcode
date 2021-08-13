############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random

def sum(list):
  sum = 0
  for i in range(len(list)):
    sum = sum + list[i]
  return sum

# continue_playing = True

# while continue_playing:

play = input("Type 'start' to begin your game of Blackjack. ").lower()
if play == "start":
  dealer = [random.choice(cards), random.choice(cards)]
  player = [random.choice(cards), random.choice(cards)]
  dealer_score = sum(dealer)
  player_score = sum(player)
  print(f"Your hand = {player}. Your current score is {player_score}.\nThe dealer's hand = {dealer[0]}.")
