#Enxhi Merkaj 11/21/2023
#The name for this game would be "Untraveled"
#Chapter two

import random

# Get user input to start the game
start_game = input("Press 'Y' to start the game: ")

# Check if the user pressed 'Y' (case-insensitive)
if start_game.lower() == 'y':
    print("The forest was so dense you couldn’t see anything from a mile. The brothers had decided to go for the treasure and they are walking in the middle of a forest in search for the right path.")
else:
    print("Game not started. Goodbye!")

#Choose left or right
def explore():
    while True:
        print("You find yourself at a crossroads. Which way would you like to go?")
        direction = input("Choose 'left' or 'right': ").lower()

        if direction == 'left':
            print("You turn left and find yourself back where you started.")
        elif direction == 'right':
            print("You turn right and come across a magnificent great wall.")
            break  # Exit the loop if 'right' is chosen
        else:
            print("Invalid choice. Please choose 'left' or 'right'.")

if __name__ == "__main__":
    explore()

# Run the exploration
explore()

print("You: Look brother.There are some latin letters on it. Give me the map.")

def handle_map():
    while True:
        choice = input("Press 'Y' to handle the map or 'Q' to quit: ").upper()

        if choice == 'Y':

            print("Your brother carefully handles the map to you.")
            break
        elif choice == 'Q':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please press 'Y' to handle the map or 'Q' to quit.")

# Run the game
handle_map()

print("You: Here it says that only the fist letter is always a solution. We need to remove the brick with letter A. ")

def generate_bricks():
    alphabet = "ABCDE"
    bricks = [random.choice(alphabet) for _ in range(5)]
    return bricks

def display_bricks(bricks):
    print("Bricks:")
    for i, brick in enumerate(bricks, start=1):
        print(f"{i}. {brick}")

def remove_letterA():
    bricks = generate_bricks()
    display_bricks(bricks)

    while True:
        try:
            choice = int(input("Choose a brick to remove (1-5): "))
            if 1 <= choice <= 5:
                break
            else:
                print("Invalid input. Please choose a number between 1 and 5.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    removed_brick = bricks.pop(choice - 1)

    if removed_brick == 'A':
        print("The wall creates a path in the middle.")
    else:
        print("Oops! The wall starts falling into the brother. You lost the game!")

if __name__ == "__main__":
    remove_letterA()

def end_chapter2():
    print("Congratulations! You've reached the end of chapter two.")
    input("Press Enter to exit...")

# Call the end_chapter1 function
end_chapter2()
