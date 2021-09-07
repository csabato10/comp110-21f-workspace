"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730466575"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = randint(1, 4)
if fortune > 2:
    if fortune == 3:
        print("You will be given some very good news.")
    else:
        print("You have a secret admirer.")
else:
    if fortune == 1:
        print("Expect to hear from a long lost friend.")
    else:
        print("Taking a trip right now would benefit you greatly!")


print("Now, go spread positive vibes!")