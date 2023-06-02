##############################################################################
#School_Search
#CS 30
#june 2nd, 2023
#Rayan Siddiqui
#Version 003
##############################################################################
'''This assigment is a code that constructs a map in which allows the 
character to move into a different room in the map
'''
##############################################################################
# Imports and Global Variables -----------------------------------------------
# create a 4x5 map with each block containing a setting
map = [
    ["home room", "janitor closet", "locker room", "washroom", "cafeteria"],
    ["cafeteria", "home room", "janitor closet", "locker room", "washroom"],
    ["washroom", "cafeteria", "home room", "janitor closet", "locker room"],
    ["locker room", "washroom", "cafeteria", "homeroom", "janitor closet"]
]
# define the starting point of the character
x, y = 0, 0

# this is the inventory for the user
Inventory = []

rooms = {"home room": {"description":"you have entered homeroom."},
       "janitor closet": {"description":"you have entered the janitor closet "
                          + "time to mope the floor."},
       "locker room": {"description":"you have entered the locker room dont " 
       +"peep at anyone!"},
       "washroom": {"description": "You have entered the washroom the worst "
                    + "place."},
       "cafeteria": {"description": "you have entered the cafeteria smell the "
                     + "disgusting school food."}}

objects = {"pencil": {"description":"nice you found pencil.", "location": "home room"}}

# Functions ------------------------------------------------------------------
# define a function to describe the setting of the block
def describe_setting(setting):
  for room in rooms: 
    if room == setting:
      print(rooms[room]["description"])



def movement():
    '''Determines where the character will move '''
    global x, y
    thinking = True
    warning = "You have reached the edge of the map! Make another selection."
    while thinking:
        #ask the user where to move next
        direction = input("where do you want to go? (north, south, east, "
                          + "west) ")
        #update the characters position based on the useres input
        if direction == "north":
          if y != 0:
            y -= 1
            thinking = False
          else:
            print(warning)
        elif direction == "south":
          if y != 3:
            y +=1
            thinking = False
          else:
            print(warning)
        elif direction == "west":
          if y != 0:
            y -=1
            thinking = False
          else:
            print(warning)
        elif direction == "east":
            if y !=4:
              x +=1
              thinking = False
            else:
              print(warning)
        else:
            print("Invalid")


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


# Main -----------------------------------------------------------------------
#loop through map and describe the setting when character moved into block
while True:
    setting = map[y][x]
    describe_setting(setting)

    # ask user where to move next
    mainMenu = input("what do you want to do? (walk, view inventory, search) ")

    # update the characters position off input
    if mainMenu == "walk":
        movement()
    elif mainMenu == "search":
        search(setting)
    elif mainMenu == "view inventory":
        view_inventory()
    else:
        print("Invalid")