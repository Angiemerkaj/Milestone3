#Enxhi Merkaj 11/21/2023
#The name for this game would be "Untraveled"
#Chapter four


# Get user input to start the game
start_game = input("Press 'Y' to start the game: ")

# Check if the user pressed 'Y' (case-insensitive)
if start_game.lower() == 'y':
    print("A strong wind closed the door and there was no way going back.")
else:
    print("Game not started. Goodbye!")

def dialouge():
    print("Villain: Who are you boys?")
    print("Brother: I would ask the same question.")
    print("Villain: There is only one way out of here and that would be only me.")
    print("Brother: I doubt that.")
dialouge()

import keyboard

def fight():
    print("Press 'x' to take out the gun.")


    keyboard.wait('x')
    print("Gun is drawn. Press Enter to start shooting.")


    keyboard.wait('enter')
    print("You: He's on the ground")

if __name__ == "__main__":
    fight()

    print("Brother: Okay, let's tie him up!")

def tie_up():
    print("Press 'y' to tie up the villain.")

    # Wait for 'y' key to be pressed
    keyboard.wait('y')
    print("Brother: This should hold him.")

if __name__ == "__main__":
    tie_up()

def end_chapter4():
    print("Congratulations! You've reached the end of chapter four.")
    input("Press Enter to exit...")

# Call the end_chapter1 function
end_chapter4()

