def movement(room_dictionary):
    while True:
        print("You can move:")
        for direction in room_dictionary:
            print(f"- {room_dictionary[direction]['Coordinate']} (Type '{direction}')")

        coordinate = input("Where do you go? ").upper()

        if coordinate in room_dictionary:
            go_to_direction = room_dictionary[coordinate]
            print(f"You move {go_to_direction['Coordinate']} and go to Room {go_to_direction['New Room']}")
            return go_to_direction["New Room"]
        else:
            print("Invalid coordinate. Choose between:", end=" ")
            for direction, destination  in room_dictionary.items():
                print(f"{destination ['Coordinate']} (Type '{direction}')", end=" ")
            print()

def room_1():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 1
    room_1_directions = {
        "N": {"Coordinate": "North", "New Room": 2}
    }

    # ------ Room actions start here ------ #
    #print(f"You're now in room {current_room}")
    #print("There will be an event here. After it, call movement.")

    #next_room = movement(room_1_directions)
    #print(f"(DEBUG) Next room is {next_room}")

def room_2():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 2
    room_2_directions = {
        "N": {"Coordinate": "North", "New Room": 3},
        "S": {"Coordinate": "South", "New Room": 1}
    }

def room_3():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 3
    room_3_directions = {
        "N": {"Coordinate": "North", "New Room": 7},
        "S": {"Coordinate": "South", "New Room": 2},
        "W": {"Coordinate": "West", "New Room": 4},
        "E": {"Coordinate": "East", "New Room": 5}
    }

def room_4():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 4
    room_4_directions = {
        "N": {"Coordinate": "North", "New Room": 6},
        "E": {"Coordinate": "East", "New Room": 3}
    }

def room_5():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 5
    room_5_directions = {
        "N": {"Coordinate": "North", "New Room": 8},
        "W": {"Coordinate": "West", "New Room": 3}
    }

def room_6():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 6
    room_6_directions = {
        "N": {"Coordinate": "North", "New Room": 10},
        "S": {"Coordinate": "South", "New Room": 4},
        "E": {"Coordinate": "East", "New Room": 7}
    }

def room_7():
    pass # Player dies here

def room_8():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 8
    room_8_directions = {
        "N": {"Coordinate": "North", "New Room": 9},
        "S": {"Coordinate": "South", "New Room": 5},
        "W": {"Coordinate": "West", "New Room": 7}
    }

def room_9():
    # ------ Variables, Data Structures, and Functions ------ #
    current_room = 9
    room_9_directions = {
        "N": {"Coordinate": "North", "New Room": 10},
        "S": {"Coordinate": "South", "New Room": 8},
        "W": {"Coordinate": "West", "New Room": 7}
    }

def room_10():
    pass # Boss

def room_11():
    pass # Win

# testing functions
room_1()