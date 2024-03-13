'''The 1st method uses only if, if-else, for, while loops and random functions but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of mainly on While loop and Random Function *

Project Description:
Guessing a word letter by letter '''

#Method 1(Jenny’s Lecture):
import random

list=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
chose_random=random.choice(list)
print(chose_random)
display=[]
lives=6
for i in range(len(chose_random)):
  display += "_"
print(display)
game_over = False
while not game_over:
  letter=input("Guess a Letter: ").lower()
  for j in range(len(chose_random)):
    if letter == chose_random[j]:
      display[j]=letter
  if letter not in chose_random:
      lives-=1
      print(f"You have {lives} lives left")
      if lives ==0:
        game_over=True
        print("You Lose")
  print(display)

  if "_" not in display:
    game_over=True
    print("You Win")

#Method 2(Chat GPT):

import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "melon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts -= 1
                print(f"Wrong guess! Attempts left: {attempts}")
        
        displayed = display_word(word_to_guess, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You've guessed the word.")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")

hangman()
