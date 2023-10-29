alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text,shift_amount,direction_input):
  cipher_text = ''
  for letter in plain_text:
    alphabet_index = alphabet.index(letter)
    if direction_input == 'encode':
      new_position = (alphabet_index + shift_amount) % 26
    if direction_input == 'decode':
      new_position = (alphabet_index - shift_amount) % 26
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The {direction_input}d text is {cipher_text}")

caesar(text,shift, direction)
