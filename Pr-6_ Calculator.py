'''The 1st method uses only recursion function, if, Dictionaries, while loops but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of mainly on recursion function, means we created the calculator function and calling that function in last *

Project Description:
                It is a Calculator with 2 options, 1st time we do 2 input and got 1 output with that 1 output we can make another calculation as Input 1 with new input 2, 
or make another calculation with 2 new inputs

Note:     the os.system('cls') command didn't work on Online compiler, better do in vs code and in that also need to do some setting so for that 
watch jenny's Lecture's "Python Project for beginners #5| Silent Auction Program-Complete Code | Python for Beginners #lec72" titled video'''


#Method 1(Jenny’s Lecture):

import OS
print("C A L C U L A T O R")
def add(a,b):
  return a+b
def subract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b

operations_dict={
  '+': add,
  '-': subract,
  '*': multiply,
  '/': divide
}
def calculator():
  number1=int(input("\n\nEnter the 1st Number: "))
  for i in operations_dict:
    print(i)
  symbol=input("\nWhich operation You are going to use: ")
  continue_flag=False
  while not continue_flag:
    number2=int(input("\nEnter the 2nd Number: "))
    calculator_function=operations_dict[symbol]
    output=calculator_function(number1,number2)
    print("\n The answer is ",output)

    anothercal=input(f"\n Press Y for calculation with {output}, press N to new Calculation, press Q to quit: ").lower()

    if anothercal == 'q':
      continue_flag= True
    if anothercal == 'y':
      number1=output
    if anothercal == 'n':
      continue_flag= True #breaking while loop and again calling function to start from scratch
      os.system('cls')
      calculator()
      
calculator()



