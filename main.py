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
import character
import map
import inventory

# Functions ------------------------------------------------------------------


# Main -----------------------------------------------------------------------
map.written_map()
#loop through map and describe the setting when character moved into block
while True:
    setting = map.map[character.y][character.x]
    map.describe_setting(setting)

    # ask user where to move next
    mainMenu = input("what do you want to do? (walk, view inventory, search, view map) ")

    # update the characters position off input
    if mainMenu == "walk":
        character.movement()
    elif mainMenu == "search":
        inventory.search(setting)
    elif mainMenu == "view inventory":
        inventory.view_inventory()
    elif mainMenu == "view map":
        map.read_map()
    else:
        print("Invalid")
