for item in 'Python':
    print(item)

print('-------------------')

for i in range(10):     #range()产生一个整数序列，也是一个可迭代对象
    print(i)

print('--------------------')

for _ in range(5):      #如果在循环体中不需要使用到自定义变量，可将自变量写为“_”
    print('啊哈哈哈哈哈')

print('用for循环计算1~100的偶数和')
sum=0
for item in range(1,101):
    if item%2==0:
        sum+=item
print('1~100的偶数和为',sum)


