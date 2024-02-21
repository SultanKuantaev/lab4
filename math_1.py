import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Enter angle in degrees: "))

radians = degrees_to_radians(degrees)

print(f"{degrees} degrees is equal to {radians} radians.")


