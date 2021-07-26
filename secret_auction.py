from replit import clear

any_other_bidders = "yes"
number_of_bidders = 1

bids = {}

while any_other_bidders == "yes":
  name = input("What is your name? ")
  bid = int(input("What's your bid? £"))
  bids[name] = bid
  any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  number_of_bidders += 1
  clear()
else:
  max_key = max(bids, key=bids.get)
  max_value = bids[max_key]

print(f"The winning bid was {max_key} with £{max_value}.")
