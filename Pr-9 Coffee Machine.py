'''This is the project which contains what are all we learned in before projects except recursion. 
Project Description:
                Check Pr-9 Description File'''

#Method 1(Jenny’s Lecture):

#Database
'..........................................................'
menu={
  'latte':
  {
    'ingredients':{
      'water':200,
      'milk':150,
      'coffee':24
    },
    'cost':150
  },
  'espresso':
  {
    'ingredients':
    {
      'water': 50,
      'coffee': 18
    },
    'cost' : 100
  },
  'cappuccino':{
    'ingredients':{
      'water':250,
      'milk':100,
      'coffee':24
    },
    'cost':200
  }
}
resources={
  'water':500,
  'milk':200,
  'coffee':100
}
'..........................................................'

profit=0

#functions
def check_resources(resources,coffee_type):
  for item in coffee_type:
    if coffee_type[item]>resources[item]:
      print("\nSorry we have low in resources")
      return False
  return True

def insert_coins():
  total=0
  print("\nPlease Enter the coins: ")
  coin_five=int(input("\nHow many 5 rupees coin: "))
  coin_ten=int(input("\nHow many 10 rupees coin: "))
  coin_twenty=int(input("\nHow many 20 rupees coin: "))
  total=coin_five*5+coin_ten*10+coin_twenty*20
  return total
  
def payment_successful(money_recieved, cost_coffee):
  if money_recieved>=cost_coffee:
    global profit  # here we're modifying a global variable (profit) so we make it as global in function too 
    profit+=cost_coffee
    change=money_recieved-cost_coffee
    print("\nHere is your ",change)
    return True
  else:
    print("\nMoney is not enough")
    return False
    
def make_coffee(coffee_name,coffee_ingredients):
  for item in coffee_ingredients:
    resources[item]-=coffee_ingredients[item]
  print(f"\nEnjoy your {coffee_name}")

#main code intitiating the functions
is_on= True
while is_on:
  ask=input("\nWhat would you like to have? (latte/espresso/cappuccino): ")
  
  if ask == 'report':
    print(f"\nWater = {resources['water']}ml")
    print(f"\nMilk = {resources['milk']}ml")
    print(f"\nCoffee = {resources['coffee']}g")
    print(f"\nProfit = Rs.{profit}")
    
  elif ask=='off':
    is_on = False
    
  else:
    coffee_type=menu[ask]
    print(coffee_type)
    
    if check_resources(resources,coffee_type['ingredients']):# to avoid cost in comparison, "coffee_type['ingredients']" is used.
      payment=insert_coins()
      
      if payment_successful(payment,coffee_type['cost']):
        make_coffee(ask,coffee_type['ingredients'])
