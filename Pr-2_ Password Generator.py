'''
The 1st method  based on only for loop and random functions but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of only for loop and Random Function *

Project Description:
Explanation:
1.	Here I made the letters, symbols and numbers as string so that the program won’t be complicated.
2.	I created an empty list to add what are all we get that in I,j,k loops, its just like password =0 that 
we use int variables on loops but 1st we make empty string only like password= ’’ , we need to show that 
random generated password with shuffle is better then random generated password so we need list 
3.	After that we need the password as proper string, to convert it into string again I use L loop at last. '''

#Method 1(Jenny’s Lecture):

import random

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols=[ '!','@','#','$','%','^','&','*','(',')','_','+']

numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator!")

nr_letters=int(input("How many letters would you like in your password?\n"))

nr_symbols=int(input("How many symbols would you like?\n"))

nr_numbers=int(input("How many numbers would you like?\n"))

password=[]

for i in range(1,nr_letters+1):
  char=random.choice(letters)
  password+=char

for j in range(1,nr_symbols+1):
  char=random.choice(symbols)
  password+=char

for k in range(1,nr_numbers+1):
  char=random.choice(numbers)
  password+=char

print("Your password without shuffle ",password)
random.shuffle(password)

print("Your password with shuffle ",password)
password_str=""
for l in password:
  password_str+=l
  
print(password_str)




#Method 2(Chat GPT):

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
# Generate a password of default length (12 characters)
password = generate_password()
print("Generated Password:", password)

Explanation:
1.	string.ascii_letters contains all uppercase and lowercase letters.
2.	string.digits contains digits 0-9.
3.	string.punctuation contains commonly used punctuation characters.
4.	random.choice is used to randomly select characters from the combined set of allowed characters (characters) for the specified length.
5.	The function generate_password takes an optional parameter length which defaults to 12 characters.
6.	password is the generated random string which will be a combination of letters (uppercase and lowercase), digits, and punctuation characters.
7.	You can adjust the length parameter when calling generate_password() to get passwords of different lengths. Also, ensure to balance security with usability when choosing the length and complexity of passwords.


