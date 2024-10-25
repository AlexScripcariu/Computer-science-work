import math


def list_objects(arr: list[str]) -> None:
    for item, value in enumerate(arr):
        print(f"{item + 1}) {value}")


def square_formula(l, w):
    return l * w


def triangle_formula(b, h):
    return b * h / 2


selection = ["Square", "Triangle"]
methods = [square_formula, triangle_formula]
list_objects(selection)

choice = -1

while choice not in range(1, len(selection) + 1):
    choice = int(input("Please enter a valid option: "))

area = 0
index = choice - 1

if choice == 1:
    length = int(input("Please enter the length of the square: "))
    width = int(input("Please enter the width of the square: "))
    area = methods[index](length, width)
elif choice == 2:
    base = int(input("Please enter the base of the triangle: "))
    height = int(input("Please enter the height of the triangle: "))
    area = methods[index](base, height)

print(f"{area}cm squared.")
