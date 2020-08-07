import keyboard
import random

instruct = {1 : "rock", 2 : "paper", 3 : "scissor"}
print("Welcome to the rock paper scissor!")
def main():
    player = 0
    bot = random.randint(1,3)
    print("Starting the game...\n")
    print("Its your turn!")

    while True:
        if keyboard.is_pressed('1'):
            player = 1
            break
        elif keyboard.is_pressed('2'):
            player = 2
            break
        elif keyboard.is_pressed('3'):
            player = 3
            break
    print("You chose ", instruct[player])
    print("The bot  chose ", instruct[bot])
    if player == bot :
        print("Tied")
    elif player == 1 and bot == 2:
        print("You lose")
    elif player == 1 and bot == 3:
        print("You win")
    elif player == 2 and bot == 1:
        print("You win")
    elif player == 2 and bot == 3:
        print("You lose")
    elif player == 3 and bot == 1:
        print("You lose")
    elif player == 3 and bot == 2:
        print("You win")
    print("Restarting the game")
main()
