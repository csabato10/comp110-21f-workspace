"""Counting letters in a string."""

__author__ = "730466575"


# Begin your solution here...

letter: str = input("What letter do you want to look for? ")
word: str = input("Enter a word: ")
i: int = 0
count: int = 0
while i <= (len(word) - 1):
    if word[i] == letter:
        count = count + 1
        i = i + 1
    else:
        i = i + 1
    

print("Count: " + str(count))