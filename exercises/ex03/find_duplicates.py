"""Finding duplicate letters in a word."""

__author__ = "730466575"

word: str = input("Enter a word: ")
i: int = 0
counter: int = 0
dup: bool = False

while i < len(word):
    j: int = i + 1
    character: str = word[i]
    while j < len(word) - 1:
        if character == word[j]:
            dup = True
        j += 1
    i += 1

print("Found duplicate: " + str(dup))