scores={'张三':100,'李四':98,'王五':45}
a = scores.keys()              #获取所有的key
print(a)
print(type(a))
print(list(a))          #转成列表

b = scores.values()             #获取所有的value值
print(b)
print(type(b))
print(list(b))

c = scores.items()              #获取所有key-value对
print(c)
print(list(c))                  #转化后的元素是由元组组成


