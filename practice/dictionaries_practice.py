"""Practice with dictionaries."""

from random import randint

player1: str = "Kayla"
player2: str = "Sarah"
player3: str = "Heather"

point_totals: dict[str, int] = {
    player1: 0,
    player2: 0,
    player3: 0}

while point_totals[player1] != 10 and point_totals[player2] != 10 and point_totals[player3] != 10:
    if randint(0, 3) == 0:
        point_totals[player1] += 1
    elif randint(0, 3) == 1:
        point_totals[player2] += 1
    elif randint(0, 3) == 2:
        point_totals[player3] += 1
    else:
        continue


days_of_the_week: dict[str, str] = {"monday": "start off tame", "tuesday": "keep it classy", "wednesday": "let loose a little", "thursday": "get restless", "friday": "get nasty", "saturday": "let it all hang out", "sunday": "pick up the pieces"}

user_choice: str = input("What day of the week is it? ").lower()

print(f"When planning your outfit {days_of_the_week[user_choice]}")
