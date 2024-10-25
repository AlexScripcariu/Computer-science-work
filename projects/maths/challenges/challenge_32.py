from math import pi

radius = int(input("Please enter the radius of a circle: "))

area = pi * radius ** 2
print(area)

depth = int(input("How deep is the cylinder: "))

print(round(area * depth, 3))
