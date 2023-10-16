class Sum:
    def sum(self, a, b):
        return self.a + self.b

    def sum(self, c, d, e):
        return self.c + self.d + self.e


s = Sum()
print(s.sum(2, 5))
print(s.sum(4, 5, 6))
