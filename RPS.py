#RPS.py
#Name: Salsabiel Khair Allah
#Date: Sep.14
#Assignment: Lab 3
import random

def main():
    wins = 0
    ties = 0
    losses = 0

    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    play_again = "Y"
    while play_again.upper() == "Y":
        # Randomly choose the computer between 'R', 'P', or 'S'
        computer = random.choice(list(choices.keys()))

        # Prompt the user for their RPS selection
        player = input("Select Rock, Paper, or Scissors (R, P, S): ").upper()

        if player not in choices:
            print("Invalid choice. Try again.")
            continue

        print(f"Player chose: {choices[player]}")
        print(f"Computer chose: {choices[computer]}")

        # Determine winner
        if player == computer:
            print("It's a tie!")
            ties += 1
        elif (player == "R" and computer == "S") or \
             (player == "P" and computer == "R") or \
             (player == "S" and computer == "P"):
            print("You win!")
            wins += 1
        else:
            print("You lose.")
            losses += 1

        # Ask the user if they would like to play again.
        play_again = input("Would you like to play again? (Y/N): ")

    # In the end, print the stats
    print("\nFinal Stats:")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties, "\t", losses)

if __name__ == '__main__':
    main()

