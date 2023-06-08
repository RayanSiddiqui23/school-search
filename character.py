# define the starting point of the character
x, y = 0, 0


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
          if y  != 0:
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
          if x != 0:
            x -=1
            thinking = False
          else:
            print(warning)
        elif direction == "east":
            if x !=4:
              x  +=1
              thinking = False
            else:
              print(warning)
        else:
            print("Invalid")