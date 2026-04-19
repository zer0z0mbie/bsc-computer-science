"""
Task
Write a program that demonstrates the use of both local and global variables.
Create a series of functions that manipulate variables, showing how local and global scopes work.
Experiment by printing the values of variables inside and outside of functions to observe how scopes change.
"""

health_points = 100

def damage_calculator():
    global health_points
    health_points -= damage

def minor_healing_potion():
    global health_points
    minor_healing_potion_points = 25
    health_points += minor_healing_potion_points

    # Ensures health_points does not exceed 100 after healing
    if health_points > 100:
        health_points = 100

    # Prints the local function inside the function
    print(f"Inside the minor_healing_potion function: minor_healing_points local variable = {minor_healing_potion_points}")
    print()
    # Prints the HP after using the potion chosen
    print(f"You have used a minor healing potion. Your HP is now {health_points}")

def major_healing_potion():
    global health_points
    major_healing_potion_points = 50
    health_points += major_healing_potion_points

    # Ensures health_points does not exceed 100 after healing
    if health_points > 100:
        health_points = 100

    # Prints the local function inside the function
    print(f"Inside the major_healing_potion function: major_healing_points local variable = {major_healing_potion_points}")
    print()
    # Prints the HP after using the potion chosen
    print(f"You have used a major healing potion. Your HP is now {health_points}")

def supreme_healing_potion():
    global health_points
    supreme_healing_potion_points = 75
    health_points += supreme_healing_potion_points

    # Ensures health_points does not exceed 100 after healing
    if health_points > 100:
        health_points = 100

    # Prints the local function inside the function.
    print(f"Inside the supreme_healing_potion function: supreme_healing_points local variable = {supreme_healing_potion_points}")
    print()
    # Prints the HP after using the potion chosen.
    print(f"You have used a supreme healing potion. Your HP is now {health_points}")

def potion_used():
    # Calls
    if potion_choice == "minor":
        minor_healing_potion()
    elif potion_choice == "major":
        major_healing_potion()
    elif potion_choice == "supreme":
        supreme_healing_potion()

def show_health():
    print(f"Reading global health_points inside function: {health_points}")

while True:
    while True:
        try:
            damage = int(input("Damage taken (0–100): "))
            if 0 <= damage <= 100:
                break
            else:
                print("Enter 0–100 only")
        except ValueError:
            print("Numbers only")
    print()

    if damage == 100:
        print(f"You took {damage} damage. You died.")
        break
    elif damage == 0:
        print(f"You took {damage} damage. You don't need healing.")
        break
    else:
        damage_calculator()
        print(f"You took {damage} damage and your HP is now {health_points}.")
        while True:
            show_health()
            try:
                # Allows the user to choose which potion they want to use
                potion_choice = input("Which potion do you want to use (minor/major/supreme)? ").lower()
                if potion_choice == "minor" or potion_choice == "major" or potion_choice == "supreme":
                    break
                else:
                    print("Please type minor, major, or supreme")
            except ValueError:
                print("Please type minor, major, or supreme")

        potion_used()

        while True:
            play_again = input("Do you want to play again (y/n)? ").lower()
            if play_again == "y":
                print("Next round...")
                break
            elif play_again == "n":
                print("Thanks for playing")
                quit_game = True
                break
            else:
                print("Please type y or n")
        if play_again == "n":
            break  # breaks the OUTER loop

print()
print("About global and local variables:")
print()

print("Global variables:")
print("health_points and damage are global variables and can be accessed outside the functions")
print(f"health_points: {health_points}")
print(f"damage: {damage}")
print()

print("Local variables:")
try:
    print(minor_healing_potion_points)
    print(major_healing_potion_points)
    print(supreme_healing_potion_points)
except NameError:
    print("minor_healing_potion_points, major_healing_potion_points, and supreme_healing_potion_points are local and cannot be accessed outside the functions")

