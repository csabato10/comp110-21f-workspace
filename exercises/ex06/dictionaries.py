"""Practice with dictionaries."""

__author__ = "730466575"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    new_dictionary: dict[str, str] = {}
    for key in a:
        check_key: str = a[key]
        count: int = 0
        for key in a:
            if a[key] == check_key:
                count += 1
        if count > 1:
            raise KeyError("Two of the same key.")
    for key in a:
        new_dictionary[key] = key
    return new_dictionary




def favorite_color(colors: dict[str, str]) -> str:
    tally: dict[str, int] = {}
    for name in colors:
        count: int = 0
        color: str = colors[name]
        for name in colors:
            if color == colors[name]:
                count += 1
        tally[color] = count
    popular_color: str
    votes: int = 0
    for color in tally:
        if tally[color] > votes:
            popular_color = color
            votes = tally[color]
    return popular_color


def count(class_schedule: list[str]) -> dict[str, int]:
    final_dict: dict[str, int] = {}
    for value in class_schedule:
        if value in final_dict:
            final_dict[value] += 1
        else:
            final_dict[value] = 1
    return final_dict
