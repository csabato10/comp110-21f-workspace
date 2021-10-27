"""Practice for Quiz 3."""


def dict_transform(x: dict[int, list[int]]) -> dict[int, list[int]]:
    transformed: dict[int, list[int]] = {}
    for key in x:
        i: int = 0
        changed_list: list[int] = []
        while i < len(x[key]):
            changed_list.append(x[key][i] * key)
            i += 1
        transformed[key] = changed_list
    return transformed


print(dict_transform({3: [4, 2], 4: [2, 3]}))


def average_grades(y: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    for key in y:
        i: int = 0
        total: int = 0
        while i < len(y[key]):
            total += y[key][i]
            i += 1
        average: float = total / len(y[key])
        averages[key] = average
    return averages


print(average_grades({"John": [54, 86, 90], "Carly": [90, 94, 92]}))