
import random

number = random.randint(1, 10)
attempts = 0

print("Welcome to my first Python project!")
print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed correctly.")
        print("Attempts:", attempts)
        break
