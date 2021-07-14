bill = float(input("What is the cost of the bill?\n"))
number_of_people = int(input("How many people are you splitting the bill between?\n"))
tip = float(input("What size tip do you want to give, 10, 12 or 15?\n"))/100

final_cost = round(bill * (1 + tip) / number_of_people, 2)

final_cost = "{:.2f}".format(final_cost)

print(f"You each need to pay £{final_cost}.")