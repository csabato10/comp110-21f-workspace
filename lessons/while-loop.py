"""An example of a while-loop"""

counter: int = 0
maximum: int = int(input("Count up to, but not including what number? "))

while counter < maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter += 1

print("Done.")