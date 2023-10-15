# Synatax
# def __init__(parameters)


class Rectangle:
    # Constructor
    def __init__(obj, length, breadth):
        obj.length = length
        obj.breadth = breadth

    def print_dimension(obj):
        print()
        print("The length of the rectangle is: ", obj.length)
        print("The breadth of the rectangle is: ", obj.breadth)

    def area(obj):
        return obj.length * obj.breadth

    def perimeter(obj):
        return 2 * (obj.length + obj.breadth)


r1 = Rectangle(4, 5)
r1.print_dimension()
area = r1.area()
print("The area of the rectangle is: ", area)
perimeter = r1.perimeter()
print("The perimeter of the rectangle is:", perimeter)

r2 = Rectangle(9.5, 7.5)
r2.print_dimension()
area = r2.area()
print("The area of the rectangle is: ", area)
perimeter = r2.perimeter()
print("The perimeter of the rectangle is:", perimeter)
