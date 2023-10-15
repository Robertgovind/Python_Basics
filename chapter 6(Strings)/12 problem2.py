# Write a program to chack if a string is palindrome or not
str = "abccba"

new_str = str[::-1]
if str == new_str:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
