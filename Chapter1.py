#Enxhi Merkaj 11/21/2023
#The name for this game would be "Untraveled"
#Chapter one

# Get the name of the player
player_name = input("What is your name? ")

# Get the name of the player's brother
brother_name = input("What is your brother's name? ")

# Print a greeting
print(f"Hello, {player_name}! Welcome to the game.")

# Print a message mentioning the player's brother
print(f"Say hi to your brother, {brother_name}!")

# Get user input to start the game
start_game = input("Press 'Y' to start the game: ")

# Check if the user pressed 'Y' (case-insensitive)
if start_game.lower() == 'y':
    print("It was a hot summer day, and the two brothers were gambling on the streets of Eldorida with an old man.")
else:
    print("Game not started. Goodbye!")

#Dice game, you need 7 to win
import random

def roll_dice():
    return random.randint(1, 6)

def dice_game(dice1, dice2):
    input("Press Enter to roll the dice...")

    total = dice1 + dice2

    print(f"You rolled: {dice1} and {dice2}")

    if total == 7:
         print("Haha! We won old man!")
    else:
        print(f"Old Man: You lost. The treasure is mine.")
# Run the dice game
dice_game(3, 4)

print("The old man frustrated decides to gamble his old treasure map")
print("Old Man: Let's play one more round.")

dice_game(1, 3)

#Start a fight to steal the map

def fight():
    print("You engage in a fight!")

def steal_map():
    print("You steal the map.")

def game():
    while True:
        choice = input("Press 'Y' to fight or 'X' to steal the map. Press 'Q' to quit: ").upper()

        if choice == 'Y':
            fight()
        elif choice == 'X':
            steal_map()
            break
        elif choice == 'Q':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please press 'Y' to fight, 'X' to steal the map, or 'Q' to quit.")

# Run the game
game()

print("Nice brother! We should leave now before the cops arrive!")

def end_chapter1():
    print("Congratulations! You've reached the end of chapter one.")
    input("Press Enter to exit...")

# Call the end_chapter1 function
end_chapter1()
