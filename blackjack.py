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

continue_playing = True

while continue_playing:
  play = input("Type 'start' to begin your game of Blackjack: ").lower()
  if play == "start":

    dealer_score = 0
    dealer = []

    while dealer_score < 17:
      dealer.append(random.choice(cards))
      dealer_score = sum(dealer)
    
    player = [random.choice(cards), random.choice(cards)]
    player_score = sum(player)

    if player_score == 21:
      if dealer_score == 21:
        print(f"Your hand = {player}. Your current score is {player_score}.\nThe dealer's score = {dealer_score}.\nYou both got Blackjack! You draw.")
      else:
        print(f"Your hand = {player}. Your current score is {player_score}.\nThe dealer's score = {dealer_score}.\nYou got Blackjack! You win.")
    else:
      print(f"Your hand = {player}. Your current score is {player_score}.\nThe dealer's hand = {dealer[0]}.")
      hit_or_stand = 'hit'
      while hit_or_stand == 'hit' and player_score < 21:
        hit_or_stand = input("Type 'hit' if you want another card or 'stand' to end the game: ").lower()
        if hit_or_stand == 'hit':
          player.append(random.choice(cards))
          player_score = sum(player)
          if player[-1] == 11:
            if player_score > 21:
              player[-1] = 1
              player_score = sum(player)
          print(f"Your hand = {player}. Your current score is {player_score}.\nThe dealer's hand = {dealer[0]}.")
      else:
        if dealer_score == player_score:
          if dealer_score == 21:
            print("You both got Blackjack! You draw.")
          else:
            print(f"You both got {dealer_score}. You draw!")
        elif dealer_score == 21 and player_score != 21:
          print(f"Your score is {player_score}. The dealer got Blackjack. You lose.")
        elif dealer_score != 21 and player_score == 21:
          print(f"The dealer got {dealer_score}. You got Blackjack. You win!")
        elif player_score > 21:
          print(f"The dealer got {dealer_score}. Your score is {player_score}. You lose.")
        elif dealer_score > 21:
          print(f"The dealer got {dealer_score}. Your score is {player_score}. You win!")
        elif dealer_score > player_score:
          print(f"The dealer got {dealer_score}. Your score is {player_score}. You lose.")
        else:
          print(f"The dealer got {dealer_score}. Your score is {player_score}. You win!")
    continue_playing = input("Would you like to play another round? Type 'y' for yes or 'n' for no: ").lower()
    if continue_playing == 'n':
      continue_playing = False
else:
  print("Goodbye!")


