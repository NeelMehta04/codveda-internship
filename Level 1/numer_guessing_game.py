import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number.")

if guess != secret_number:
    print(f"Game Over! The number was {secret_number}.")
