import time

date = time.localtime()      # 获取当前日期时间
year, month, day = date[:3]  # 获取年月日
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#判断是否为闰年,如果是闰年把二月替换成29天
if year % 4 == 0 and year % 400 == 0:
    day_month[1] = 29


if month==1:    # 如果这个月是1月
    print(day)  # 直接输出天数
else:

    month = int(month)
    n = sum(day_month[:month-1]) + day
    print(n)