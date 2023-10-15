class Rectangle:
    def set_dimensions(obj, length, breadth):  # Arguments for setting data
        obj.length = length
        obj.breadth = breadth

    def print_dimension(obj):
        print("The length of the rectangle is: ", obj.length)
        print("The breadth of the rectangle is: ", obj.breadth)

    def area(obj):
        return obj.length * obj.breadth

    def perimeter(obj):
        return 2 * (obj.length + obj.breadth)


r1 = Rectangle()
r1.set_dimensions(4, 5)
r1.print_dimension()
area = r1.area()
print("The area of the rectangle is: ", area)
perimeter = r1.perimeter()
print("The perimeter of the rectangle is:", perimeter)

r2 = Rectangle()
r2.set_dimensions(4.5, 9.5)
r2.print_dimension()
area = r2.area()
print("The area of the rectangle is: ", area)
perimeter = r2.perimeter()
print("The perimeter of the rectangle is:", perimeter)
