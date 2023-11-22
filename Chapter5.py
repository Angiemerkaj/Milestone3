#Enxhi Merkaj 11/21/2023
#The name for this game would be "Untraveled"
#Chapter five

# Get user input to start the game
start_game = input("Press 'Y' to start the game: ")

# Check if the user pressed 'Y' (case-insensitive)
if start_game.lower() == 'y':
    print("They walk towards the other door on the temple. And there it was, so close yet so far. It was getting dark and late.")
else:
    print("Game not started. Goodbye!")

def dialouge():
    print("You: There should be some way we can decode this door.")
    print("Brother: Maybe it's inside the map.")
    print("You: Give me the map.")
    print("He reaches out the bag to pull out the map. Hands it to you.")
dialouge()

import keyboard

def examine_map():
    print("You examine the map.")

def set_map_away():
    print("You set the map aside.")

def examine():
    print("Press 'x' to examine the map or 'y' to set the map away.")

    while True:
        key_pressed = keyboard.read_event(suppress=True).name

        if key_pressed == 'x':
            examine_map()
        elif key_pressed == 'y':
            set_map_away()
            break  # Exit the loop after setting the map away

if __name__ == "__main__":
    examine()

print("You: We should move the disks on the door to create this flower symbol.Look!")

#The flower symbol
import turtle

# Function to draw a petal
def draw_petal():
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50)
    turtle.right(135)

# Function to draw a flower
def draw_flower(num_petals):
    for _ in range(num_petals):
        draw_petal()
        turtle.right(360 / num_petals)

# Set up the turtle
turtle.speed(2)  # Set turtle speed (1=slowest, 10=fastest)

# Draw a flower with 6 petals
draw_flower(6)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()

def move_discs():
    input("Press Enter to start moving the discs")
    print("You successfully created the pattern. The door is open")

# Call the function
move_discs()

print("Behind the door there is what they been looking for. All the treasure enough to make them buy the whole Eldorida.")
print("Brother: I can't believe we made it.")
print("You: Let's take what we can and go home.")

def end_chapter5():
    print("Congratulations! You finished the game!")
    input("Press Enter to exit...")

# Call the end_chapter1 function
end_chapter5()
