"""Repeating a beat in a loop."""

__author__ = "730466575"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
repeat: int = int(input("How many time do you want to repeat it? "))
count: int = 1
if repeat <= 0:
    print("No beat...")
else:
    final_repeat: str = beat
    while count < repeat:
        final_repeat = final_repeat + " " + beat
        count += 1
    print(final_repeat)