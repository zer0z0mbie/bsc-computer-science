### To do:

## Import game_map and game_rooms modules
import game_map as display_map
import game_rooms as rooms

## Define Variables:
player_stats = {
    "Health Points": 100,
    "Stamina Points": 100
}

inventory = {
    # Health Potions
    "Health Potions": {
        "Minor Health Potions": 0,
        "Major Health Potions": 0,
        "Supreme Health Potions": 0
    },
    # Stamina Potions
    "Stamina Potions": {
        "Minor Stamina Potions": 0,
        "Major Stamina Potions": 0,
        "Supreme Stamina Potions": 0
    },
    # Equipment
    "Equipment": {
        "Sword": False,
        "Shield": False
    },
    # Map
    "Map": False,
    # Golden Key
    "Golden Key": False
}

## Define program body
# Tracking the current room
current_room = 1

while True:
    if current_room == 1:
        current_room = rooms.room_1()
    elif current_room == 2:
        current_room = rooms.room_2()
    elif current_room == 3:
        current_room = rooms.room_3()
    elif current_room == 4:
        current_room = rooms.room_4()
    elif current_room == 5:
        current_room = rooms.room_5()
    elif current_room == 6:
        current_room = rooms.room_6()
    elif current_room == 7:
        current_room = rooms.room_7()
    elif current_room == 8:
        current_room = rooms.room_8()
    elif current_room == 9:
        current_room = rooms.room_9()
    elif current_room == 10:
        current_room = rooms.room_10()
    elif current_room == 11:
        current_room = rooms.room_11()
    else:
        pass # work on the else statement!