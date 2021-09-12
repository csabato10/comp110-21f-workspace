"""Finding duplicate letters in a word."""

__author__ = "730466575"

word: str = input("Enter a word: ")
i: int = 0
counter: int = 0

while i < len(word):
    j: int = i + 1
    character: str = word[i]
    while j < len(word) - 1:
        if character == word[j]:
            counter += 1
        j += 1
    i += 1

if counter > 0:
    print("True")
else:
    print("False")