print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You're at a cross road. Which way do you want to go, left or right?\n")
if left_or_right.lower() == "left":
  swim_or_wait = input("You arrive at a lake. Do you choose to swim to the island in the middle or wait for a boat?\n")
  if swim_or_wait.lower() == "wait":
    door = input("You arrive at a house with three doors, red, yellow and blue. Which door do you walk through?\n")
    if door.lower() == "blue":
      print("Oh no! You've been eaten by a dragon. Game over.")
    elif door.lower() == "red":
      print("Oh no! You walked into a fire and burned. Game over.")
    elif door.lower() == "yellow":
      print("You found the treasure! You win!")
    else:
      print("You fell into a vortex. Game over.")
  else:
    print("Oh no! You got attacked by a trout. Game over.")
else:
  print("Oh no! You fell into a hole. Game over.")
