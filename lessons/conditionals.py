"""An example of condtional if/else statements"""

SECRET: int = 3

print("I am thinking of a number between 1 and 5.")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("Correct")
    print("Have a wonderful day!")
else:
    print("Incorrect")
    if guess > SECRET:
        print("Guess is too high.")
    else:
        print("Guess is too low.")

print("Game over.")