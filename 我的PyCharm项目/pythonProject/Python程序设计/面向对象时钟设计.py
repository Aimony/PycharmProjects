import time

class Clock:
    hour = 0
    min = 0
    sec = 0

    def getNow(self):
        print('当前时间')

c1 = Clock()
print(c1.hour)