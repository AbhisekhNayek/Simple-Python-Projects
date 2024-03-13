'''The 1st  method uses only functions, if, Dictionaries, while loops but 2nd method by chat GPT use some other functions also so that it looks pretty than my code.
* I done this base upon learning of mainly on Dictionaries *

Project Description:
                This is a Silent auction like IPL Auctions, means peoples can bid their money by entering the name and bid amount, but because of cls command people can't see 
others bidding amount so when we give no then all bidding details will occur and winner details will occur.

      Note:     the os.system('cls') command didn't work on Online compiler, better do in vs code and in that also need to do some setting so for that 
watch jenny's Lecture's "Python Project for beginners #5| Silent Auction Program-Complete Code | Python for Beginners #lec72" titled video'''

#Method 1(Jenny’s Lecture):

import os

def findwinner(bidderdetails): #{jenny: 10000, Ram 30000, Shyam: 5000}
  higherbid=0 #30000
  winner=''
  for i in bidderdetails:  #jenny
    bidderprice=bidderdetails[i] #30000
    if bidderprice>higherbid:
      higherbid=bidderprice
      winner=i
  print('\n',f"The highest bid by {winner} an amount of {higherbid}")

bidding_data={}
s= False
while not s:
  name=input("What is your Name: \t")
  price=int(input("\nWhat is the price: "))
  mydict={name : price}
  print('\n', mydict)
  bidding_data[name]=price
  yesno=input("\nDo you need to add some more bid yes/no: "'\n')
  if yesno == 'no':
    for k in bidding_data.items():
      print(k,'\n')
    findwinner(bidding_data)
    
    s = True
  elif yesno =='yes':
    os.system('cls')


#Method 2(Chat GPT):

class SilentAuction:
    def __init__(self):
        self.bids = {}

    def place_bid(self, bidder, amount):
        self.bids[bidder] = amount
        print(f"Bid placed by {bidder} for ${amount}")

    def show_bids(self):
        print("\nCurrent Bids:")
        for bidder, amount in self.bids.items():
            print(f"{bidder}: ${amount}")

    def determine_winner(self):
        if not self.bids:
            print("No bids placed. No winner.")
            return None

        winner = max(self.bids, key=self.bids.get)
        winning_amount = self.bids[winner]
        print(f"\nThe winner is {winner} with a bid of ${winning_amount}")
        return winner, winning_amount


def main():
    print("Welcome to the Silent Auction Program!")

    auction = SilentAuction()

    while True:
        bidder_name = input("\nEnter your name (or 'quit' to end): ")
        if bidder_name.lower() == 'quit':
            break

        try:
            bid_amount = float(input("Enter your bid amount: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        auction.place_bid(bidder_name, bid_amount)

    auction.show_bids()
    auction.determine_winner()


if __name__ == "__main__":
    main()
