import random

class NUMBER_GUESSING_GAME:

    def __init__(self, number_range):
        self.number_range = number_range
        self.random_number = self.number_to_be_guessed()

    def number_to_be_guessed(self):
        random_number = random.randint(1, self.number_range)
        return random_number
        
    def get_users_guess(self):
        print(self.random_number)
        user = int(input(f"Guess number bewtween 0 and {self.number_range}: "))

        if user == self.random_number:
            print("You got it.")
        elif user < self.random_number:
            print("Guess higher")
        else:
            print("Guess lower")

number_guess = NUMBER_GUESSING_GAME(10)

number_guess.get_users_guess()
