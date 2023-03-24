"""
  Ahmed's code
"""
import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

while True:
    player_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(options)
    print(f"Computer chooses {computer_choice}.")

    if player_choice not in options:
        print("Invalid choice. Try again.")
        continue

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors"
         or player_choice == "paper" and computer_choice == "rock"
         or player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
"""
Mohamed's code
"""

import sys
import random
from time import sleep
print("ROCK , PAPER , SCISSORS")

wins = 0
loses = 0
ties = 0


while True:
    print(f"{wins} wins , {loses} loses , {ties} ties")
    while True:
        print("Rock (r) , Paper (p) , Scissors (s) , Quit (q)")
        userChoice = input()
        if userChoice == 'q':
            sys.exit()
        elif userChoice == 'r' or userChoice == 'p' or userChoice == 's':
            break
        print('Type one of r, p, s, or q.')
    if userChoice == 'r':
        print("Rock vs ...")
    elif userChoice == 'p':
        print("Paper vs ...")
    elif userChoice == 's':
        print("Scissors vs ...")
    sleep(1)
    randomNumber = random.randint(1 , 3)
    computerMove = ' '
    if randomNumber == 1:
        print("Rock !!!")
        computerMove = 'r'
    elif randomNumber == 2:
        print("Paper !!!")
        computerMove = 'p'
    elif randomNumber == 3:
        print("Scissors !!!")
        computerMove = 's'
    # checking is the user winning or losing
    sleep(1)
    if userChoice == computerMove:
        print("It's a tie")
        ties += 1
    elif userChoice == 'r' and computerMove == 's':
        print("You win !!!")
        wins += 1
    elif userChoice == 'r' and computerMove == 'p':
        print("You lose")
        loses += 1
    elif userChoice == 'p' and computerMove == 'r':
        wins += 1
        print("You win !!!")
    elif userChoice == 'p' and computerMove == 's':
        loses += 1
        print("You lose")
    elif userChoice == 's' and computerMove == 'p':
        wins += 1
        print("You win !!!")
    elif userChoice == 's' and computerMove == 'r':
        loses += 1
        print("You lose")


