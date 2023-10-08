# Variables are the containers that stores the value of particular data
# The variable names must be valid and follow the rule
# In python the variable name follows snake case conventions like area_of_circle

# Integer
a = 5
print(a)
print(type(a))

# float
b = 3.124
print(b)
print(type(b))

# string
name = "Govind"
print(name)
print(type(name))

# boolean
test = True
print(test)
print(type(test))

# complex number
img = 4 + 5j
print(img)
print(type(img))
print(img.conjugate)
print(img.real)
print(img.imag)

roll = 9
name = "Govind"
print("My name is " + name + "\tMy roll no is ", roll)

# using seperator
print(a, b, name, img, roll, sep="-")
print(a, b, name, img, roll, sep=",")
