import random

class Guesser:
    def __init__(self, min_num=1, max_num=100, max_guesses=4, max_hints=3):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.max_guesses = max_guesses
        self.remaining_guesses = max_guesses
        self.max_hints = max_hints
        self.remaining_hints = max_hints
        
    def get_factors(self):
        """Get all factors of the secret number"""
        factors = []
        for i in range(1, self.secret_number + 1):
            if self.secret_number % i == 0:
                factors.append(i)
        return factors
    
    def get_multiples(self):
        """Get multiples of the secret number within the range"""
        multiples = []
        multiple = self.secret_number
        multiplier = 1
        while multiple <= self.max_num:
            multiples.append(multiple)
            multiplier += 1
            multiple = self.secret_number * multiplier
        return multiples
    
    def get_random_hint(self):
        """Generate a random hint based on the three categories"""
        if self.remaining_hints <= 0:
            return "Sorry, you have no hints remaining!"
        
        self.remaining_hints -= 1
        hint_categories = ['a', 'b', 'c']
        category = random.choice(hint_categories)
        
        if category == 'a':  # Factors or multiples
            factors = self.get_factors()
            multiples = self.get_multiples()
            
            # Check if factors or multiples are applicable
            has_factors = len(factors) > 2  # More than 1 and itself
            has_multiples = len(multiples) > 1  # More than just the number itself
            
            if has_factors and has_multiples:
                choice = random.choice(['factors', 'multiples'])
            elif has_factors:
                choice = 'factors'
            elif has_multiples:
                choice = 'multiples'
            else:
                # If neither applicable, the number is 1
                return f"Hint: The number is 1!"
            
            if choice == 'factors':
                # Exclude 1 and the number itself for a better hint
                useful_factors = [f for f in factors if f != 1 and f != self.secret_number]
                if useful_factors:
                    factor = random.choice(useful_factors)
                    return f"Hint: The number is divisible by {factor}."
                else:
                    factor = random.choice(factors)
                    return f"Hint: The number is divisible by {factor}."
            else:  # multiples
                if len(multiples) > 1:
                    multiple = random.choice(multiples[1:])  # Exclude the number itself
                    return f"Hint: {multiple} is a multiple of the number."
                else:
                    return f"Hint: The number has multiples within the range."
        
        elif category == 'b':  # Larger or smaller
            # Choose randomly between larger or smaller
            choices = []
            if self.secret_number > self.min_num:
                choices.append('smaller')
            if self.secret_number < self.max_num:
                choices.append('larger')
            
            if not choices:
                return f"Hint: The number is at the boundary of the range!"
            
            direction = random.choice(choices)
            if direction == 'smaller':
                smaller_num = random.randint(self.min_num, self.secret_number - 1)
                return f"Hint: The number is larger than {smaller_num}."
            else:
                larger_num = random.randint(self.secret_number + 1, self.max_num)
                return f"Hint: The number is smaller than {larger_num}."
        
        else:  # category == 'c' - Parity
            if self.secret_number % 2 == 0:
                return "Hint: The number is even."
            else:
                return "Hint: The number is odd."
    
    def check_guess(self, guess):
        """Check if the guess is correct"""
        try:
            guess_num = int(guess)
            return guess_num == self.secret_number
        except ValueError:
            return False
    
    def is_valid_guess(self, guess):
        """Check if the guess is a valid number in range"""
        try:
            guess_num = int(guess)
            return self.min_num <= guess_num <= self.max_num
        except ValueError:
            return False

class NumberGuesserChatbot:
    def __init__(self):
        self.guesser = Guesser()
        
    def start_game(self):
        """Start the number guessing game"""
        print("🎯 Welcome to the Number Guesser Game! 🎯")
        print(f"I've guessed a number between {self.guesser.min_num} and {self.guesser.max_num}.")
        print(f"You have {self.guesser.max_guesses} guesses to find it!")
        print(f"You can also request up to {self.guesser.max_hints} hints by typing 'hint'.")
        print("Let's begin!\n")
        
        while self.guesser.remaining_guesses > 0:
            self.display_remaining()
            user_input = input("Enter your guess or type 'hint': ").strip().lower()
            
            if user_input == 'hint':
                if self.guesser.remaining_hints > 0:
                    hint = self.guesser.get_random_hint()
                    print(f"💡 {hint}")
                else:
                    print("😔 Sorry, you have no hints remaining!")
            
            elif self.guesser.is_valid_guess(user_input):
                if self.guesser.check_guess(user_input):
                    print(f"🎉 Congratulations! You guessed it right! The number was {self.guesser.secret_number}!")
                    return
                else:
                    self.guesser.remaining_guesses -= 1
                    if self.guesser.remaining_guesses > 0:
                        print("❌ Wrong guess! Try again.")
                    else:
                        print(f"💔 Game Over! You've run out of guesses. The number was {self.guesser.secret_number}.")
                        return
            
            else:
                print(f"⚠️ Invalid input! Please enter a number between {self.guesser.min_num} and {self.guesser.max_num}, or type 'hint'.")
            
            print()  # Add spacing
    
    def display_remaining(self):
        """Display remaining guesses and hints"""
        print(f"📊 Remaining guesses: {self.guesser.remaining_guesses} | Remaining hints: {self.guesser.remaining_hints}")

def main():
    """Main function to run the game"""
    # Create an object of the class
    chatbot = NumberGuesserChatbot()
    
    # Start the game
    chatbot.start_game()
    
    # Ask if user wants to play again
    while True:
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            print("\n" + "="*50 + "\n")
            chatbot = NumberGuesserChatbot()  # Create new game
            chatbot.start_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()