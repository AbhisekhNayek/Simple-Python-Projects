'''The 1st method uses only recursion function, if, while loops but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of mainly on function and recursion function, means we created the some function and calling that function in last *

Project Description:
                enter a number by user if that matches with system number its correct, wrong means again user needs to guess and enter the number.
If user choose hard only 5 attempts, easy means 10 attempts.

Note:     the os.system('cls') command didn't work on Online compiler, better do in vs code and in that also need to do some setting so for that 
watch jenny's Lecture's "Python Project for beginners #5| Silent Auction Program-Complete Code | Python for Beginners #lec72" titled video'''


#Method 1(Jenny’s Lecture):
import random
easyattempts=10
hardattempts=5

def difficulty(level):
  if level=='easy':
    return easyattempts
  elif level=='hard':
    return hardattempts

def check_answer(user_input,answer,attempts):
  if user_input> answer:
    print("\nIt is too high")
    return attempts-1 
  elif user_input< answer:
    print("\nIt is too low")
    return attempts-1
  else :
    print(f"\n\n\t\t\t\t\t\tYeah You're Right, The number is {user_input}")

def game():
  print("Let me think of a number from 1 to 50")
  answer=random.randint(1,50)
  print("\n\n",answer)
  level=input("\nEasy or Hard: ").lower()
  attempts=difficulty(level)
  user_input=0
  while user_input!=answer:
    print(f"\nYour have {attempts} attempts remaining")
    user_input=int(input("\nEnter the number you guessed: "))
    attempts=check_answer(user_input,answer,attempts)
    if attempts==0:
      print("You are out of Chances")
      return 
    elif user_input!=answer:
      print("\nGuess Again")

game()

#Method 2 (chatGPT):

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to Guess the Number!")
    print("I've chosen a number between 1 and 100. Try to guess it.")

    attempts = 0

    while True:
        # Get the user's guess
        user_guess = int(input("Your guess: "))
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Run the game
guess_the_number()

