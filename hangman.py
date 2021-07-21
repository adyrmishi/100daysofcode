stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

import hangman_words
import hangman_art
import random

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
print(hangman_art.logo)

display = ['_'] * len(chosen_word)

remaining_to_be_found = display.count('_')

while remaining_to_be_found != 0 and lives != 0:
  guess = input("Guess a letter: ").lower()
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess and guess in display:
      print("You've already guessed that letter.")
    elif chosen_word[i] == guess and guess not in display:
        display[i] = chosen_word[i]
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word.")
    lives -= 1
  print(display)
  print(hangman_art.stages[lives])
  print(f"You have {lives} lives remaining.")
else:
  if remaining_to_be_found == 0:
    print("You've won!")
  else:
    print("You've lost.")
