# import numpy.random
#
# str1 = "这是一个变量";
# print("变量str1的值是："+str1);
# print("变量str1的地址是：%d" %(id(str1)));
# str2 = str1;
# print("变量str2的值是："+str2);
# print("变量str2的地址是：%d" %(id(str2)));
# str1 = "这是另一个变量";
# print("变量str1的值是："+str1);
# print("变量str1的地址是：%d" %(id(str1)));
# print("变量str2的值是："+str2);
# print("变量str2的地址是：%d" %(id(str2)));
#
# print('------------------------------------------------')
#
# x =3
# x += 3
# print(x)
# x -= 3
# print(x)
# x *= 3
# print(x)
# x /= 3
# print(x)
#
# print('------------------------------------')
#
# a = 10;
# a += 1;
# print (a);
# a*= 10;
# print (a);
# a**= 2;
# print (a);
#
# print('-------------------------')
# print("%d %d %d"%(1,2,3))
# print("%d %d %d"%(1.1,2.5,3.6))
# print("%e %e %e"%(1.1,2.5,3.6))
# print("%f %f %f"%(1.1,2.5,3.6))
# print("%5.2f %5.3f %6.7f"%(1.1,2.5,3.6))
# print("%10.2f %5.3f %6.7f"%(12345.12345,2.5,3.6))
#
# def solveMeFirst(a,b):
#     result = a + b
#     print('%d+%d=%d'%(a,b,result))
#
# num1=int(input('请输入第一个数'))
# num2=int(input('请输入第二个数'))
# solveMeFirst(num1,num2)


print('使用random库中的randint和range函数生成有10个100以内整数的列表，输出最大值，最小值，平均值')
import numpy
import random
list=[random.randint(0,100) for i in range(10)]
print(list)
# a = max(list)
# b = min(list)
# c = numpy.mean(list)
# print('最大值:%d\n最小值:%d\n平均值:%f', % (a,b,c))
print('最大值:',max(list))
print('最小值:',min(list))
print('平均值:',numpy.mean(list))