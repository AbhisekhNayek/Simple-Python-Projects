'''
Project Description :
Asking answers to user for Quiz Question and questions are saved in other files and using as Database  '''

from quiz_db import Question_bank

from quiz_db import options

print("Welcome to the Quizzz")

def answer_check(guess, expected_answer):
	if guess==expected_answer:
		return True
	else:
		return False
		
score=0	
for i in range(len(Question_bank)): #0 1 2 3 4
	print(Question_bank[i]["text"],"\n")
	for j in options[i]:
		print(j,"\n")
	guess=input("Choose from Options: \t").upper()
	correct=answer_check(guess,Question_bank[i]["answer"])
	if correct:
		print("\nCorrect Answer\n")
		score+=1
	else:
		print("\nWrong Answer\n")
	print(f"Your Score is {score}/{i+1}\n")

print("Your Final Score is ",score," Correct answers\n")
print(f"Your Final Score is{(score/len(Question_bank)*100)}%\n")
