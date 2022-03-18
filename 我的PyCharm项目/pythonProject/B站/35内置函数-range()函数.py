#range()用于生成提个整数数列
#返回值是一个迭代器对象
'''
    优点：
    不管range对象表示的整数序列有多长，
    所有range对象占用的内存空间都是相同的因为仅仅需要存储start,stop和step，
    只有当用到range对象时，才会去计算序列中的相关元素
'''

#range(stop)
r=range(10)     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     #默认步长为1
print(r)        #range(0,10)
print(list(r))

#range(star,stop)                                   #默认步长为1
r=range(1,10)
print(list(r))

#range(star,stop,step)
r=range(1,10,2)             #步长为2
print(list(r))

print('----------判断整数在序列中是否存在------------')
print(10 in r)
print(9 in r)

print(10  not in r)
print(9 not in r)
