#ANCHOR - Delete Restricted Items    
"""
Set of items and set of restricted (terbatas) items are given, based on the beach type (family or normal) the list of items should be printed to the console. 
Restricted items are not allowed to family beach and everything else can be taken to normal beach except drugs.

general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}
 
restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }


Example Input

Select Beach Type (1 - Family beach, 2 - Normal Beach): 1

Example Output

See below the list of items that you can take.
    Alcholic Drinks
    Sand toys
    Snacks
    Sunglasses
    Hats
    Beach umbrella
    Beach towels
    Camp chair
    Camera

"""


general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}
 
restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }

i_beach_type = input("Select Beach Type (1 - Family beach, 2 - Normal Beach): ")

if i_beach_type == 1:
  for element_ in restricted_items:
    general_items.discard(element_)
  print("See below the list of items that you can take.")
  for element_family in general_items:
    print(element_family)
else:
  print("See below the list of items that you can take.")
  general_items.discard("Drugs")
  for element_normal in general_items:
    print(element_normal)
    
    
"""
OR 
user_input = input("Select Beach Type (1 - Family beach, 2 - Normal Beach):  ")
if user_input == "1":
    for item in restricted_items:
        general_items.discard(item)
else:
    general_items.discard("Drugs")
print("See below the list of items that you can take.")
for item in general_items:
    print(f"\t{item}")
"""


"""
OR using remove method with try-catch
user_input = input("Select Beach Type (1 - Family beach, 2 - Normal Beach):  ")
if user_input == "1":
    for item in restricted_items:
        try:
            general_items.remove(item)
        except KeyError:
            print(f"skipping {item}..")
            continue
else:
    try:
        general_items.remove("Drugs")
    except:
        print(f"skipping Drugs..")
print("See below the list of items that you can take.")
for item in general_items:
    print(f"\t{item}")
            
"""
    