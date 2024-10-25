import math

def area_circle(radius):
    return math.pi * radius * radius

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

radius = float(input("Enter radius of circle: "))
side = float(input("Enter side of square: "))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

print("Area of circle:", area_circle(radius))
print("Area of square:", area_square(side))
print("Area of rectangle:", area_rectangle(length, width))
