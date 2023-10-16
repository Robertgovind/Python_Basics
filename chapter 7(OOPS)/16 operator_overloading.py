class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, second):
        return Complex(self.real + second.real, self.img + second.img)


c1 = Complex(3, 2)
c2 = Complex(4, 2)
c3 = c1 + c2
print(c3.real, "+i", c3.img)
