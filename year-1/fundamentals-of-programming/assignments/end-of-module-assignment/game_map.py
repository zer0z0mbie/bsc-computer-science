def current_room(room):
    # Takes the current room and returns the map showing the player's position
    current_room_map = "" # Creates an empty string to build the updated map

    # Go through each character in game_map
    for char in game_map:
        # If the character is one of the rooms (a–k), replace it
        if char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]:
            if char == room:
                current_room_map += "X" # Mark the player's current position
            else:
                current_room_map += "." # Other rooms
        else:
            current_room_map += char # Keep walls, paths, etc. the same

    return current_room_map # Returns the map with the player's current position

# game_map is a multiline string that stores the full map of the game.
# It includes 11 rooms labeled a–k, along with walls, paths, and directions.
# The letters make it easier for the function to find and replace rooms.
# This variable is used by the current_room function to display the player's position.
# The function reads this map and updates it depending on which room the player is in.
game_map = """
- > - > - > - > - > - > - > - > - > - > - >
^                                         '
'         #########                N      v
^         #   k   #                ↑      '
'         #########             W ← → E   v
^                                  ↓      '
'   #####################          S      v
^   #         j         #                 '
'   #####################                 v
^   #     #       #  i  #                 '
'   #  f  #   g   #######                 v
^   #     #       #  h  #                 '
'   #####################                 v
^   #  d  #   c   #  e  #                 '
'   #####################                 v
^      #      b      #                    '
'      ###############                    v
^         #   a   #                       '
'         #########                       v
^                                         '
- < - < - < - < - < - < - < - < - < - < - <
"""
