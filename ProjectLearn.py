import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    guessed = False

    while not guessed:
        guess = int(input("Guess the number (between 1 and 100): "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            guessed = True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guess_the_number()
