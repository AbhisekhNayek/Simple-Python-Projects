'''
The 1st method based on only if, elif and random functions but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of only IF and Random Function *

Project Description:
Playing Stone, paper Sicssor game with Computer '''

#Method 1(Jenny’s Lecture):

import random

print("Welcome to the Stone Paper Sicssor Game")
print()
print("Rules: \n 0 for Rock \n 1 for Paper \n 2 for Sicssor")
print()
user_input=int(input("Enter your choice: "))
print()
if user_input > 3:
  print("Invalid Number, so You Lose")
else:
  #computer_choice=0 for Checking Purpose
  computer_choice=random.randint(0,3)
  print(f"The Computer Choice is {computer_choice}")
  print()
  
  if user_input==computer_choice:
    print("Draw")  
  elif user_input==0 and computer_choice==2:
    print("You Win")
  elif user_input==2 and computer_choice==0:
    print("You Lose") 
  elif computer_choice > user_input:
    print("You Lose")
  elif user_input > computer_choice:
    print("You Win")



#Method 2(Chat GPT):

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice - 'stone', 'paper', or 'scissors': ").lower()
        if user_choice in ['stone', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'stone', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    print("Let's play Stone-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()


