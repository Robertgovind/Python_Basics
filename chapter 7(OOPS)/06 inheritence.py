# Inheritence is the process of inheriting the properties of the parent or superclass to the child or subclass


class Person:
    def get_person(obj, name):
        obj.name = name


class Student(Person):
    def get_student(obj, id):
        obj.id = id

    def print_student(obj):
        print("Name: ", obj.name)
        print("ID: ", obj.id)


student1 = Student()
student1.get_person("Govind")
student1.get_student(23232)
student1.print_student()
