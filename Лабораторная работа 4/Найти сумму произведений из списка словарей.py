# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    total = 0
    for dictionary in data:
        total += dictionary["score"] * dictionary["weight"]
    return round(total, 3)


print(task())
