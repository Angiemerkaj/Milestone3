#Enxhi Merkaj 11/21/2023
#The name for this game would be "Untraveled"
#Chapter three

# Get user input to start the game
start_game = input("Press 'Y' to start the game: ")

# Check if the user pressed 'Y' (case-insensitive)
if start_game.lower() == 'y':
    print("After walking for an hour they finally see an old temple. However, there was someone before them already searching with guards and weapons. They are EVERYWHERE!!")
else:
    print("Game not started. Goodbye!")

def narrator_story():
 print("Brother: Shhh! We have to be quiet!")
 print("You: What should we do! How did they find it? I think the treasure is inside the temple.")
 print("Brother: Yes. We need to take them out one by one slowly and quietly.")
 print("You: Okay!")

narrator_story()

def approach_guard():
    input("Press Enter to approach the guard quietly...")
    print("You approach the guard silently.")

# use function
approach_guard()

def knock_down_enemy():
    user_input = input("Press 'y' to knock down the enemy: ").lower()

    if user_input == 'y':
        print("You successfully knocked down the enemy.")
    else:
        print("You choose not to knocked down the enemy.")

knock_down_enemy()
approach_guard()
knock_down_enemy()
approach_guard()
knock_down_enemy()

print("Brother: Okay. I think our coast is clear now. Lets take their weapons and get inside.")

import keyboard
import time

def steal_loadouts():
    print("Press and hold the letter 'p' for one second to steal loadouts.")

    start_time = None
    while True:
        if keyboard.is_pressed('p'):
            if start_time is None:
                start_time = time.time()
        else:
            if start_time is not None:
                held_duration = time.time() - start_time
                if held_duration >= 1:
                    print("You successfully stole loadouts!")
                    break
                start_time = None

if __name__ == "__main__":
    steal_loadouts()
print("The brothers start walking towards the temple. They get inside it.")

def end_chapter3():
    print("Congratulations! You've reached the end of chapter three.")
    input("Press Enter to exit...")

# Call the end_chapter1 function
end_chapter3()
