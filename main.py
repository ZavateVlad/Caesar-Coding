#Import string module
from string import ascii_letters, punctuation, digits, whitespace

#Use the string module and transform as lists
alphabet = list(ascii_letters)
symbols = list(punctuation) + list(digits) + list(whitespace)
should_end = False

print(len(symbols))
print(len(alphabet))
#create function, which take:
#plain_text represents the input text of the user
#shift_amount is by how much words the user would like to shift the text
#direction_input can be either encode or decode

def caesar(plain_text, shift_amount, direction_input):
  #the output of the function
  cipher_text = ''

  #loop through the input text
  for letter in plain_text:

    #check for word
    if letter in alphabet:
      alphabet_index = alphabet.index(letter)
      
      if direction_input == 'encode':
        new_position = (alphabet_index + shift_amount) % 26
      if direction_input == 'decode':
       new_position = (alphabet_index - shift_amount) % 26

      new_letter = alphabet[new_position]

    #check for symbols
    elif letter in symbols:
      symbols_index = symbols.index(letter)
      
      if direction_input == 'encode':
        new_position = (symbols_index + shift_amount) % 24
      if direction_input == 'decode':
       new_position = (symbols_index - shift_amount) % 24
      
      new_letter = symbols[new_position]
        
    cipher_text += new_letter
  print(f"The {direction_input}d text is: {cipher_text}")

#User input
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  #Restart the encryption/decryption
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")