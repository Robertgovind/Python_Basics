class A:
    def function_a(self):
        print("From class A")


class B(A):
    def function_b(self):
        print("From class B")


class C(B):
    def function_c(self):
        print("From class C")


variable = C()
variable.function_a()
variable.function_b()
variable.function_c()
