# Practicing-Python
Practicing Python with my Friend Ahmed
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
