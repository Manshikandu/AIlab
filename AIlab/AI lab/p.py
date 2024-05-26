import random

def generate_random_number():
    return random.randint(1, 10)

def roll_dice():
    return random.randint(1, 6)

def play_game():
    import random

def generate_random_number():
    return random.randint(1, 10)

def play_game():
    random_number = generate_random_number()
    attempts = 0
    max_attempts = 5

    print("Welcome to the Random Number Game!")
    print("I've chosen a number between 1 and 10. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low! Try guessing higher.")
        elif guess > random_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly in {attempts + 1} attempts!")
            return

        attempts += 1

    print(f"Sorry, you've used all your attempts. The number I had chosen was {random_number}.")

    guess = input("Do you think the next roll of the dice will be higher or lower than this number? (h/l): ").lower()

    if guess not in ['h', 'l']:
        print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
        return

    dice_roll = roll_dice()
    print("The dice rolled:", dice_roll)

    if (guess == 'h' and dice_roll > random_number) or (guess == 'l' and dice_roll < random_number):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")

if __name__ == "__main__":
    play_game()
