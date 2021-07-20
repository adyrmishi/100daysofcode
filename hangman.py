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

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print("Welcome to Hangman.")
print(stages[6])

display = ['_'] * len(chosen_word)

remaining_to_be_found = display.count('_')

while remaining_to_be_found != 0 and lives != 0:
  guess = input("Guess a letter: ").lower()
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = chosen_word[i]
  if guess not in chosen_word:
    lives -= 1
  print(display)
  print(stages[lives])
  print(f"You have {lives} lives remaining.")
else:
  if remaining_to_be_found == 0:
    print("You've won!")
  else:
    print("You've lost.")