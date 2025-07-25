#ANCHOR - Calculated total price
"""
Instruction
Create a program calculates the total price of items that we want to buy.
When program starts it will display the list of items, using available_parts dictionary.
Then program asks to select an item
Then based on user selected item, the program checks if the item exist in the store or not.
Because when quantity of item is 0 then it is out of stock
Finally, if it is not out of stock we calculate total price of items and decrease quantity from the stock.
This continues until user select 0.
And when the loop is terminated the total price is printed to the console
"""


available_parts = {
  "1" : "Computer", 
  "2" : "Monitor", 
  "3" : "Keyboard", 
  "4" : "Mouse",
  "5" : "HDMI Cable",
  "6" : "DVD Drive"
}

price_and_stock_quantity = {
  "Computer" : {
    "Price" : 500,
    "Quantity" : 10
  },
  "Monitor" : {
    "Price" : 1000,
    "Quantity" : 50
  },
  "Keyboard" : {
    "Price" : 200,
    "Quantity" : 0
  },
  "Mouse" : {
    "Price" : 300,
    "Quantity" : 3
  },
  "HDMI Cable" : {
    "Price" : 150,
    "Quantity" : 30
  },
  "DVD Drive" : {
    "Price" : 100,
    "Quantity" : 50
  }
}

def display_menu(p_available_parts):
  print("Please add option from the list : ")
  for key_, value_ in p_available_parts.items():
    print(f"{key_} : {value_}")
  print("0 : Calculate")

def main():
  display_menu(available_parts)
  total_ = 0
  # choose_items = None
  while True:    
    choose_items = input("Please input item to add :")
    if choose_items == "0":
      print(f"total = {total_}")
      break
    
    part_name = available_parts.get(choose_items)     #NOTE - or we can use -> part_name = available_parts[choose_items]
    
    if not part_name: 
      print("Invalid input. Please choose valid option")
    
    item_info = price_and_stock_quantity.get(part_name)      #NOTE - or we can use -> item_info = price_and_stock_quantity[part_name]
    if item_info["Quantity"] == 0:
      print(f"{part_name} is out of stock")
    else:
      total_ += item_info["Price"]
      item_info["Quantity"] -= 1
      print(f"Remaining Quantity of {part_name} is {item_info["Quantity"]}") 
      
if __name__ == "__main__":     #TODO - __name__ is built-in var in python
  main()
      