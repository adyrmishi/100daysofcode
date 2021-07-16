rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices = [rock, paper, scissors]
player_choice = choices[int(input("Choose 0 for rock, 1 for paper and 2 for scissors.\n"))]
computers_choice = choices[random.randint(0,2)]

print(player_choice)
print(computers_choice)

if player_choice == computers_choice:
  print("You drew!")
elif (player_choice == rock and computers_choice == scissors) or (player_choice == paper and computers_choice == rock) or (player_choice == scissors and computers_choice == paper):
  print("You won!")
else:
  print("You lost!")
