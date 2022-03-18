import time

year = int(input('year:\n'))
month = int(input('month\n'))
day = int(input('day:\n'))
holidays = int(input('holiday\n'))

if (month > 12) or (day > 31):
    print('data error')

day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0) or ((year % 400 == 0) and (year % 100 != 0)):
    day_month[1] = 29

sum_days = day + holidays
while sum_days >= 31:
    sum_days -= day_month[month-1]
    if month > 12:
        month -= 12
        year += 1
        if (year % 4 == 0) or ((year % 400 == 0) and (year % 100 != 0)):
            month = day_month

day = sum_days

print(year,month,day)