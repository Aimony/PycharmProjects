import time

a = input('请输入你的目标日(y m d)')
# a = input('y,m,d:')
y,m,d = map(float,a.split())


date = time.localtime()
year, month, day = date[:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
rday = 365


if (year % 4 == 0) and (year % 400 == 0):
    day_month[1] = 29
    rday = rday + 1


if month == 1:
    print(rday - day)
else:

    month = int(month)
    n = sum(day_month[:month-1]) + day
    print(rday - n)