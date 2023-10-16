# Defines the visibility of the class attributes and methods
# by default public
# double underscore(__) for private
# single underscore(_) for protected


# Public access modifier
class ABC:
    def __init__(self, a):
        self.a = a

    def print_info(self):
        print("The value is:", self.a)


x = ABC(5)
print(x.a)
x.print_info()


# Private access modifier
class XYZ:
    def __init__(self, __a):
        self.__a = __a

    def __print_info(self):
        print("the value is : ", self.__a)

    def print_data(self):
        print(self.__a)


x = XYZ(8)
x.print_data()


# Protected access modifier
