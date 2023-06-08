# this is the inventory for the user
Inventory = []

objects = {"pencil": {"description":"nice you found pencil.", "location": "home room"}}


def view_inventory():
  print("the following items are in your inventory")
  for item in Inventory:
    print(item)


def search(room):
  print("you decide to look around the room.")
  for item in objects: 
    if objects[item]["location"] == room:
      print(f"wow you found an {item}.")
      answer = input(f"would u like to keep the {item}?(yes, no) ")
      if answer == "yes":
        Inventory.append(item)
        print(f"{item} has been added to inventory")
      elif answer == "no":
        print(f"you leave the {item}")
      else: 
        print("invalid")