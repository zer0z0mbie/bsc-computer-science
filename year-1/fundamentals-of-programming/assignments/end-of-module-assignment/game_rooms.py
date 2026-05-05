room_directions = {
    1: {
        "N": {"Coordinate": "North", "New Room": 2}
    },
    2: {
        "N": {"Coordinate": "North", "New Room": 3},
        "S": {"Coordinate": "South", "New Room": 1}
    },
    3: {
        "N": {"Coordinate": "North", "New Room": 7},
        "S": {"Coordinate": "South", "New Room": 2},
        "W": {"Coordinate": "West", "New Room": 4},
        "E": {"Coordinate": "East", "New Room": 5}
    },
    4: {
        "N": {"Coordinate": "North", "New Room": 6},
        "E": {"Coordinate": "East", "New Room": 3}
    },
    5: {
        "N": {"Coordinate": "North", "New Room": 8},
        "W": {"Coordinate": "West", "New Room": 3}
    },
    6: {
        "N": {"Coordinate": "North", "New Room": 10},
        "S": {"Coordinate": "South", "New Room": 4},
        "E": {"Coordinate": "East", "New Room": 7}
    },
    7: {},  # death room
    8: {
        "N": {"Coordinate": "North", "New Room": 9},
        "S": {"Coordinate": "South", "New Room": 5},
        "W": {"Coordinate": "West", "New Room": 7}
    },
    9: {
        "N": {"Coordinate": "North", "New Room": 10},
        "S": {"Coordinate": "South", "New Room": 8},
        "W": {"Coordinate": "West", "New Room": 7}
    },
    10: {},  # boss
    11: {}   # win
}

def player_movement(current_room):
    while True:
        print("You can move:")
        for direction in room_directions[current_room]:
            print(f"- {room_directions[current_room][direction]['Coordinate']} (Type '{direction}')")

        coordinate = input("Where do you go? ").upper()

        if coordinate in room_directions[current_room]:
            go_to_direction = room_directions[current_room][coordinate]
            print(f"You move {go_to_direction['Coordinate']} and go to Room {go_to_direction['New Room']}")
            return go_to_direction["New Room"]
        else:
            print("Invalid coordinate. Choose between:", end=" ")
            for direction, destination  in room_directions[current_room].items():
                print(f"{destination ['Coordinate']} (Type '{direction}')", end=" ")
            print()

def room_1():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 1

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_2():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 2

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_3():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 3

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_4():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 4

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_5():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 5

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_6():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 6

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_7():
    pass # Player dies here

def room_8():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 8

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_9():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 9

    # ------ Room actions start here ------ #
    # Player current location
    print(f"You're now in room {current_room}")
    # Room event
    print("There will be an event here. After it, call movement.")

    # Next room
    next_room = player_movement(current_room)
    print()
    return next_room

def room_10():
    pass # Boss

def room_11():
    pass # Win
