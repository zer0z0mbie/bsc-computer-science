### To do:

# Import game_map and rooms
import game_map
import game_rooms

# Define Variables:
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

# Define program body