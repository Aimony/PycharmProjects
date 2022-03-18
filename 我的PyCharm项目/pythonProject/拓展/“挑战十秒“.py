import time
from datetime import datetime
print("10秒大挑战！")
time.sleep(0.5)
start=input("请按回车开始...")
start_time = datetime.now()
end=input("按回车结束...")
end_time = datetime.now()
cost_time = end_time-start_time
print(cost_time)
print("9.5秒--10.5秒之间胜出哦！")

