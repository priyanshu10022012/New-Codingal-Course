import math
def polygon_area(n,s):
    """
    Calculate the area of a regular polygon.
    """
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area
if __name__ == "__main__":
    print("Regular Polygon Area Calculator")
    try:
        n = int(input("Enter the number of sides: "))
        s = float(input("Enter the length of a side: "))
        area = polygon_area(n, s)
        print(f"The area of the polygon is: {area}")
    except ValueError as e:
        print(f"Error: {e}")