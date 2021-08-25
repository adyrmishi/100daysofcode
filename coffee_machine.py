from main import MENU
from main import resources

print(MENU)
print(resources)

coffee_machine = True

while coffee_machine:
    drink_option = input("What would you like to drink? (Coffee/latte/cappucino)\n").lower()
    if drink_option == "off":
        break
    elif drink_option == "report":
        continue
