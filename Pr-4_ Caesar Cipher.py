'''The 1st method uses only functions, if, for, while loops and random functions but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of mainly on functions *

Project Description:
eg: input is "hello" and 3 
    output is khoor
means, in 25 alphabet (count from 0 to 25 like index)so H index is 7, 7 + input 3 = 10, 10 is K in Alphabet (start of output).
like this need to print for all alphabet in input

#this mod 26 is like eg: message: jenny key: 3, y index 24 z is 25 after no words will geterror
# to solve this Mod % --> eg: 24(y) % 26 is 2, 2 is b so probelem solved,y + 2 =b(crossinz,a) '''

#Method 1(Jenny’s Lecture):

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  

def encryption(plain_text,shift_key):
  cipher=""
  for i in plain_text:
    if i in alphabet:
      position = alphabet.index(i)
      new_position=(position+shift_key)%26 
      cipher+=alphabet[new_position]
    else:
      cipher+=i
  print(cipher)
  print()

def decryption(cipher_text,shift_key):
  plain=""
  for i in text:
    if i in text:
      position = alphabet.index(i)
      new_position=(position-shift_key)%26 
      plain+=alphabet[new_position]
    else:
      plain+=i             
  print(plain)
  print()
a= False
while not a:
  process=input("What you need to do 'encrypt' or 'decrypt': ")
  print()
  text=input("Type your Message: ")
  print()
  shift=int(input("Enter the shift number: "))
  print()
  if process == "encrypt":
    encryption(plain_text=text,shift_key=shift)
  elif process == "decrypt": 
    decryption(cipher_text=text,shift_key=shift)

  play_again=input("Play again Yes or No: ")
  print()
  if play_again == 'no':
    a=True
    print("BYE")


#Method 2(Chat GPT):

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert the character to its alphabetical index (0-25)
            char_index = ord(char.lower()) - ord('a')
            # Apply the shift and wrap around if necessary
            new_index = (char_index + shift) % 26
            # Convert back to the ASCII value of the corresponding letter
            new_char = chr(new_index + ord('a'))
            # Convert back to uppercase if the original character was uppercase
            result += new_char.upper() if is_upper else new_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    return result

# Example usage:
text = input("Enter the text: ")
shift = int(input("Enter the shift: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text:", encrypted_text)

# To decrypt, use the same function with a negative shift
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted Text:", decrypted_text)

  
