#比较运算符的结果为bool类型
a,b=10,20
print('a>b吗?',a>b)      #F
print('a<b吗?',a<b)      #T
print('a<=b吗?',a<=b)    #T
print('a>=b吗?',a>=b)    #F
print('a==b吗?',a==b)    #F
print('a!=b吗?',a!=b)    #T

'''
    =为赋值运算符     ==为比较运算符
    变量由三部分组成：标识、类型、值
    ==比较的是值
    比较对象的标识使用   is
'''

a=10
b=10
print(a==b)     #T      value相等
print(a is  b)  #T      id标识相等

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)       #value      T
print(lst1 is lst2)     #id         F
print(id(lst1))
print(id(lst2))
print(a is not b)       #F      a的id与b的id不相等
print(lst1 is  not lst2)#T

