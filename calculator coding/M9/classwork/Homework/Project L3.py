import math

# Base class (Parent)
class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Square class
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Main function with loop
def main():
    while True:
        print("\n--- Area Calculator ---")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            rect = Rectangle(l, b)
            print("Area of Rectangle:", rect.area())

        elif choice == "2":
            s = float(input("Enter side: "))
            sq = Square(s)
            print("Area of Square:", sq.area())

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            tri = Triangle(base, height)
            print("Area of Triangle:", tri.area())

        elif choice == "4":
            r = float(input("Enter radius: "))
            cir = Circle(r)
            print("Area of Circle:", cir.area())

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()
