import random

def display_instructions():
    """Display game instructions to the user."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("1. Enter 'r' for Rock, 'p' for Paper, 's' for Scissors.")
    print("2. The game will randomly choose an option for the computer.")
    print("3. Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
    print("4. Let's play!\n")

def get_user_choice():
    """Prompt the user to input their choice."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_input = input("Enter your choice (r/p/s): ").strip().lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("Invalid input. Please choose 'r', 'p', or 's'.")

def get_computer_choice():
    """Randomly generate the computer's choice."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    comp_input = random.choice(list(choices.keys()))
    return comp_input, choices[comp_input]

def determine_winner(user, computer):
    """Determine the winner of the game."""
    winning_combinations = {
        'r': 's',  # Rock beats Scissors
        's': 'p',  # Scissors beat Paper
        'p': 'r'   # Paper beats Rock
    }
    if user == computer:
        return 'tie'
    elif winning_combinations[user] == computer:
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, comp_choice, winner, user_choice_name, comp_choice_name):
    """Display the results of the game."""
    print(f"\nYou chose: {user_choice_name}")
    print(f"Computer chose: {comp_choice_name}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("Congratulations, you win!")
    else:
        print("Sorry, the computer wins this round.")

def play_game():
    """Main function to control the game flow."""
    user_score, comp_score = 0, 0
    display_instructions()

    while True:
        user_choice, user_choice_name = get_user_choice()
        comp_choice, comp_choice_name = get_computer_choice()

        winner = determine_winner(user_choice, comp_choice)
        display_result(user_choice, comp_choice, winner, user_choice_name, comp_choice_name)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            comp_score += 1

        print(f"Score -> You: {user_score} | Computer: {comp_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Final score:")
            print(f"You: {user_score} | Computer: {comp_score}")
            break

if __name__ == "__main__":
    play_game()
