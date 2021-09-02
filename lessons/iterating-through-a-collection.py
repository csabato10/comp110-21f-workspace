"""Examples with iterating through a collection"""

user_string: str = input("Give me a string! ")

i: int = 0

while i < len(user_string):
    print(user_string[i])
    i += 1