import random

number = random.randint(1, 100)
guess = 0
tries = 0

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while guess != number:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        print("Total tries:", tries)
