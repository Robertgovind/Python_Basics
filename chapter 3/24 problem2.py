# Mirror operation where "a" changed to "z","b" is changed to "y"
st1 = "abcdefghijklmnopqrstuvwxyz"
st2 = st1[::-1]


dict1 = dict(zip(st1, st2))


string_input = input("Enter the string: ")
n = int(input("Enter the position: "))

prefix = string_input[0 : n - 1]
suffix = string_input[n - 1 :]

mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

final_string = prefix + mirror
print(final_string)
