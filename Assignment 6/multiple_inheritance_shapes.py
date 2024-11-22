
class Shape:
    def __init__(self, color):
        self.color = color  

    def get_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)  
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)  
        self.base = base
        self.height = height

    def calc_area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    
    rectangle = Rectangle("Blue", 5, 4)
    print(f"Rectangle Color: {rectangle.get_color()}")
    print(f"Rectangle Area: {rectangle.calc_area()}")

    
    triangle = Triangle("Red", 6, 8)
    print(f"Triangle Color: {triangle.get_color()}")
    print(f"Triangle Area: {triangle.calc_area()}")
