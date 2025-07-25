#ANCHOR - Blind Auction (Lelang Buta)
"""
1. Start
2. import logo and show logo
3. Ask bidder name
4. Ask for bid amount
5. add name and bid amound in dictionary as key and value pairs
6. Check if there is anyone who want to bid. if YES, back to point number 3. if NO, next bellow
7. Loop through dictionary and find the highest bid and print the result as winner
8. End
"""

# from clear import clear
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Works on Windows and macOS/Linux

from logo import logo


def find_highest_bid(p_dict):
  highest_bid = 0
  highest_name_of_bid = ''
  
  for key_, value_ in p_dict.items():
    if value_ > highest_bid:
      highest_bid = value_
      highest_name_of_bid = key_
    
  detail_ = f"{highest_name_of_bid} with {highest_bid}"  
  return detail_



def main():
  # print(logo)
  detail_bid = dict()
  i_question = 'Y'
  
  while i_question == 'Y':
    print(logo)
    i_name = input("Your name : ")
    i_bid = float(input("Your bid : "))
    
    detail_bid[i_name] = i_bid
    
    i_question = input("Anyone ? Y/N \n").upper()
    if i_question == "N":
      print(detail_bid)
      print(find_highest_bid(detail_bid))
      i_question = "N"
    elif i_question == "Y":
      clear()


if __name__ == "__main__":
 
  main()
    
  
  
  


