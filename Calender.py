import calendar

# year
yy = 2024
# month
i = 1
# printing calender
for i in range(12):
    print(calendar.month(yy, i + 1))
