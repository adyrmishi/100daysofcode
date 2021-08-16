import random 

difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'hard':
  attempts = 5
else:
  attempts = 10

number = random.randint(1,100)
guess = 0

while attempts > 0 or guess != number:
  if attempts == 0:
    print(f"You've run out of attempts. The right answer was {number}.")
    break
  
  guess = int(input(f"You have {attempts} attempts left to guess the number.\nMake a guess: "))

  if guess == number:
    print(f"You've guessed the right number which was {number}!")
    break
  else:
    attempts -= 1
    if guess < number:
      print("Too low.")
    elif guess > number:
      print("Too high.")
