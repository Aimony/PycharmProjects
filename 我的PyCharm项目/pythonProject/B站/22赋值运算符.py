i=3+4
print(i)
a=b=c=20    #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('-----------支持参数赋值---------------')
a=20
a+=30   #a=a+30
print(a)
a-=10   #a=a-10
print(a)
a*=2    #a=a*2
print(a)
print(type(a))
a/=3    #a=a/3
print(a)
print(type(a))  #float
a//=2   #a=a//2
print(a)
print(type(a))
a%=3    #a=a%3
print(a)

print('-------------解包赋值-----------------')
a,b,c=20,30,40
print(a,b,c)

#a,b=20,30,40       报错，左右变量的个数和值的个数不对应

print('---------------交换两个变量的值-------------------')
a,b=10,20
print('交换前：',a,b)
a,b=b,a     #交换
print('交换后：',a,b)