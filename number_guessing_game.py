import random

class NUMBER_GUESSING_GAME:

    def __init__(self, number_range):
        self.number_range = number_range
        self.random_number = self.number_to_be_guessed()
        self.guesses = 0

    def number_to_be_guessed(self):
        random_number = random.randint(1, self.number_range)
        return random_number
        
    def get_users_guess(self):
        while True:
            try:
                user = int(input(f"Guess a number between 1 and {self.number_range}: "))
                if not 1 <= user <= self.number_range:
                    print(f"Please enter a number between 1 and {self.number_range}.")
                    continue
                
                self.guesses += 1
                if user < self.random_number:
                    print("Guess higher")
                elif user > self.random_number:
                    print("Guess lower")
                else:
                    print(f"You got it in {self.guesses} guesses.")
                    break
            
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            

number_guess = NUMBER_GUESSING_GAME(100)

number_guess.get_users_guess()
