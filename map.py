import numpy as np

# this is the file name
filename = "school.txt"

# create a 4x5 map with each block containing a setting
map = [
    ["home room", "janitor closet", "locker room", "washroom", "cafeteria"],
    ["cafeteria", "home room", "janitor closet", "locker room", "washroom"],
    ["washroom", "cafeteria", "home room", "janitor closet", "locker room"],
    ["locker room", "washroom", "cafeteria", "homeroom", "janitor closet"]
]
# this describes the rooms with written descripitons
rooms = {"home room": {"description":"you have entered homeroom."},
       "janitor closet": {"description":"you have entered the janitor closet "
                          + "time to mope the floor."},
       "locker room": {"description":"you have entered the locker room dont " 
       +"peep at anyone!"},
       "washroom": {"description": "You have entered the washroom the worst "
                    + "place."},
       "cafeteria": {"description": "you have entered the cafeteria smell the "
                     + "disgusting school food."}}


def describe_setting(setting):
  '''define a function to describe the setting of the block
  the setting describes your characters location.'''
  for room in rooms: 
    if room == setting:
      print(rooms[room]["description"])


def written_map():
  '''This function writes the schools map in a file'''
  school = np.array(map)
  with open(filename, "w") as file:
      file.write(str(school))


def read_map():
  '''this function read the schools map in a file'''
  with open(filename, "r") as file:
    content = file.read()
  print(content)