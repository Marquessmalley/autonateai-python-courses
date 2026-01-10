import random

secretNumber = random.randint(1, 100);
attempts = 0
correctGuess= False

while correctGuess == False:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secretNumber:
        correctGuess = True
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
    elif guess < secretNumber:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")