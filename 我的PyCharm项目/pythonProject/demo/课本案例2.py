print(ord('A'))
print(chr(65))
print(chr(ord('A')+1))
print(str(1))
print(str(1234))
print([1,2,3])
print(str(('123')))

import random
a=[random.randint(1,100) for i in range(10)]
print(a)
print(max(a),min(a),sum(a))
print(max(['aa','b'],key=len))

print(list())
print(list(range(5)))
print(tuple(range(5)))

x=list(range(11))
import random
random.shuffle(x)   #shuffle()随机打顺序
print(x)
print(sorted(x))
print(sorted(x,key=str))

x=['aaaa','bc','d','b','ba']
print(sorted(x,key=lambda item:(len(item),item)))
#num=ramdom.chices(range(1,10),k=5)
#print(num)

range(5)
range(0,5)
print(list(range(5)))
print(list(range(1,10)))    #指定start和stop参数
print(list(range(1,10,2)))  #同步指定start，stop，step参数
print(list(range(9,0,-2)))  #步长为负数时，start应比stop大
print(list(range(5,10,-1))) #否则不会包含任何函数

print(list(zip('abcdef',[1,2,3])))  #压缩字符串和列表   结果数量取决于最短的参数
print(list(zip('123','abc',',.!'))) #可以处理任意多个可迭代对象
x=zip('abcd','1234')
print(list(x))                      #zip对象中的函数只能遍历一次，访问过的函数就不存在，enumerate、filter、map对象以及生成器对象也有这个特点

#x=input('please input:')
#print(type(x))
#<class 'str'>

# print(3,5,7,srp=":")
# print(3,5,7,sep=",")

# for i in range(10,20):
#     print(i,end='')

aList=[3,4,5]
aList=aList+[7]
print(aList)

aList.append(9)
print(aList)

a=[1,2,3]
print(id(a))
