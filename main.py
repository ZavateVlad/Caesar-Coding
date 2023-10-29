import string

alphabet = list(string.ascii_letters)
symbols = list(string.punctuation) + list(string.digits) + list(string.whitespace)
should_end = False

def caesar(plain_text,shift_amount,direction_input):
  cipher_text = ''
  for letter in plain_text:
    if letter in alphabet:
      alphabet_index = alphabet.index(letter)
      if direction_input == 'encode':
        new_position = (alphabet_index + shift_amount) % 26
      if direction_input == 'decode':
        new_position = (alphabet_index - shift_amount) % 26
      new_letter = alphabet[new_position]
    if letter in symbols:
      symbols_index = symbols.index(letter)
      new_letter = symbols[symbols_index]
    cipher_text += new_letter
  print(f"The {direction_input}d text is: {cipher_text}")

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))

  caesar(text,shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")