import random

def main():
    # 1. Import Random library (done above)
    # Assign a random play to the computer from a list of options
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    # 2. Take input from the player
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose: rock, paper, or scissors")
    player_choice = input("Your choice: ").lower().strip()
    
    # Print error message if input is incorrect
    if player_choice not in options:
        print("Error: Invalid input! Please choose rock, paper, or scissors.")
        return
    
    # Display choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # 3. Compare player's input to computer's and print game result
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Enhanced version with replay option
def play_game():
    while True:
        main()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()