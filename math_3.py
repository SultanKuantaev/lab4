import math
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))


def area(sides,length):
    apothem = length / (2 * math.tan(math.pi/sides))
    area = (sides * length * apothem ) / 2
    return int(area)

area = area(sides,length)
print(f"The area of the polygon is: {area}")