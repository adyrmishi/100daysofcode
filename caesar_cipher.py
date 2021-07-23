alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
  output_text = ""
  for letter in text:
    if letter not in alphabet:
      output_text += letter
    else:
      if direction == "encode":
        output_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
      if direction == "decode":
        output_text += alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
  print(output_text)

play_again = "yes"

while play_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)
  play_again = input("Do you want to go again? Type 'yes' or 'no'.").lower()
else:
  print("Goodbye.")
