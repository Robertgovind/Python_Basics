class Person:
    def get_person(self, name):
        self.name = name


class Student:
    def get_student(self, marks):
        self.marks = marks


class Result(Person, Student):
    def print_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


res = Result()
res.get_person("Govind")
res.get_student(79)
res.print_info()
