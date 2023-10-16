class Person:
    def get_person(obj, name):
        obj.name = name


class Student(Person):
    def get_student(obj, id):
        obj.id = id

    def print_info(obj):
        print("Name: ", obj.name)
        print("Student id: ", obj.id)


std = Student()
std.get_person("Ram")
std.get_student(5423)
std.print_info()
