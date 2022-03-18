import datetime

x = datetime.datetime(1921,7,23,12,0,0)
y = datetime.datetime(2020,7,1,12,0,0)
print((y - x).days)                         #datetime.timedelta类型转换为int类型：x.days
print((y - x).days * 24 * 60)
