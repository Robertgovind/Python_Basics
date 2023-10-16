class A:
    def function_a(self):
        print("From class A")


class B(A):
    def function_b(self):
        print("From class B")


class C(A):
    def function_c(self):
        print("From class C")


class D(A):
    def function_d(self):
        print("From class D")


variable1 = B()
variable1.function_b()
variable1.function_a()
variable2 = C()
variable2.function_c()
variable2.function_a()
variable3 = D()
variable3.function_d()
variable3.function_a()
