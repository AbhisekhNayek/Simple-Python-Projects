'''The 1st method uses only function, if, while loops and calling a file as database. 

* I done this base upon learning of mainly on saving data in a new file and calling it in another file, means we created the some function and calling that function in last *

Project Description:
                Here we have a Database called "Sat" with details of some celebrities like their name, followers count, Work description and Country. with that Computer asks
randomly 2 persons details except follower count. we need to guess which celebrity detail has higher follower count. If out Guess corrct score will add one by one, wrong 
means game over.

Note:     the os.system('cls') command didn't work on Online compiler, better do in vs code and in that also need to do some setting so for that 
watch jenny's Lecture's "Python Project for beginners #5| Silent Auction Program-Complete Code | Python for Beginners #lec72" titled video

we didn't use this above method, to use clear in Compilers create a clear function and do as per line 20,21 and 61'''


#Method 1(Jenny’s Lecture):

import sat
import random
import os

score=0
def clear():
  os.system('clear' if os.name == 'posix' else 'cls')
  
def check_answer(follower_count_1,guess,follower_count_2):
  if follower_count_1<follower_count_2:
    if guess==1:
      return False
    else:
      return True
  else:
    if guess==1:
      return True
    else:
      return False
      
def account_info(account):
  name=account['name']
  description=account['description']
  country=account['country']
  return (f"{name}, a {description}, from {country}")

account_2=random.choice(sat.data)

continue_flag = False
while not continue_flag:
  account_1=account_2
  account_2=random.choice(sat.data)
  while account_1==account_2:
    account_2=random.choice(sat.data) 

# While is for, 1st time account 1 and 2 same means it will gets change by random, 2nd time also got same means 
# it needs to do change as random automatically for that, while loop is used here 


  print("\nCompare 1: ",account_info(account_1))
  print("\nCompare 2: ",account_info(account_2))

  guess=int(input("\n Which one Type 1 or Type 2 ? "))

  follower_count_1=account_1['follower_count']
  follower_count_2=account_2['follower_count']

  is_correct=check_answer(follower_count_1,guess,follower_count_2)  
  
  clear() # Use clear() to clear the screen

  if is_correct is  True:
    score +=1
    print(f"\n Your Score is {score}")
  else:
    print(f"\n You Lose, Your Final Score is {score}")
    continue_flag = True

  
  
