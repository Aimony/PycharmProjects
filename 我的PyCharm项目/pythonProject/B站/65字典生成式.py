item = ['Fruits','Books','Others']
prices = [96,78,85]     #prices = [96,78,85,55,43]      类似木桶效应生成


d = {item:prices    for item,prices in zip(item,prices)}       # .upper()可以将字符串转化为大写
print(d)
