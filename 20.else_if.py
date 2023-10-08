percentage = int(input("Enter percentage: "))

if percentage > 81 and percentage < 100:
    print("Very Good")
elif percentage > 61 and percentage < 80:
    print("Good")
elif percentage > 41 and percentage < 60:
    print("Average")
else:
    print("Fail")
