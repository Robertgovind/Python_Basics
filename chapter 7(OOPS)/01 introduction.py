# OOP is about modeling real world objects into a computer program
# It introduces the concept of class and objects

#obj is the default parameter used in class that significies the particular 
class Car:
    def set_information(obj):
        obj.color = input("Enter the color of the car: ")
        obj.model = input("Enter the model of the car: ")
        obj.plate_no = input("Enter the plate no of the car: ")

    def print_information(obj):
        print("The color of the car is: ", obj.color)
        print("The model of the car is: ", obj.model)
        print("The plate no of the car is: ", obj.plate_no)


c = Car()
c.set_information()
c.print_information()

car2 = Car()
car2.set_information()
car2.print_information()
