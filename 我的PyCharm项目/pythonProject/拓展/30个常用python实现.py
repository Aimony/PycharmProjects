# 1、冒泡排序
# lis = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]
# def sortport():
#     for i in range(len(lis)-1):
#         for j in range(len(lis)-1-i):
#             if lis[j] > lis[j+1]:
#                 lis[j],lis[j+1] = lis[j+1],lis[j]
#     return lis
#
# print(sortport())



#2、计算x的n次⽅的⽅法
# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(2,3))




#3、计算a*a + b*b + c*c + ……
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc(1,2,3))



#4、计算阶乘 n!
# def fac():
#     num = int(input('请输入一个数字:'))
#     factorial = 1
# #查看数字是负数，0，或 正数
#     if num < 0:
#         print('负数无阶乘')
#     elif num == 0:
#         print('0的阶乘为1')
#     else:
#         for i in range(1,num + 1):
#             factorial = factorial * i
#         print('%d 的阶乘为 %d' % (num,factorial))
#
# print(fac())




# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
#
# print(factorial(5))



# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))
# # print(fact(0))
# # print(fact(-3))           #maximum recursion depth exceeded in comparison




#5、列出当前⽬录下的所有⽂件和⽬录名
# import os
# print([d for d in os.listdir('.')])





#6、把⼀个list中所有的字符串变成⼩写：
# L = ['Hello','World','IBM','Apple']
# print([s.lower() for s in L])






#7、输出某个路径下的所有⽂件和⽂件夹的路径--------？
# import os
# def print_dir():
#     filepath = input('请输入一个路径:')
#     if filepath == "":
#         print('请输入正确的路径')
#     else:
#         for i in os.listdir(filepath):
#             print(os.path.join(filepath,i))
#
# print_dir(print_dir())






#8、输出某个路径及其⼦⽬录下的所有⽂件路径

#9、输出某个路径及其⼦⽬录下所有以.html为后缀的⽂件


#10、把原字典的键值对颠倒并⽣产新的字典
# dict1 = {'A':'a','B':'b','C':'c'}
# dict2 = {y:x for x,y in dict1.items()}
# print(dict2)






#11、打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#         #print('{} × {} = {} \t'.format(j,i,j*i),end='')
#         print('%d × %d = %d \t' %(i,j,i*j),end='')
#     print()




#12、替换列表中所有的3为3a
# num = ["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,87686,98,76]
# # print(num.count(3))         #3的个数
# # print(num.index(3))         #返回第一个3的索引位置
# for i in range(num.count(3)):
#     ele_index = num.index(3)
#     num[ele_index] = '3a'
#     print(num)





#13、打印每个名字
# L = ['James','Meng','Xin']
# for i in range(len(L)):
#     print('Hello,%s' %L[i])





#14、合并去重
# lst1 = [2,3,8,4,9,5,6]
# lst2 = [5,6,10,17,11,2]
#
# lst3 = lst1 + lst2
# print(lst3)
# print(set(lst3))
# print(list(set(lst3)))





#15、随机⽣成验证码的两种⽅式
# import random
# lst = []
# for i in range(65,91):
#     lst.append(chr(i))
# for j in range(97,123):
#     lst.append(chr(j))
# for k in range(48,58):
#     lst.append(chr(k))
# m = random.sample(lst,6)        #从lst列表中随机选出6个
# print(m)
# m = ''.join(m)                  #str.join(sequence)     将str插入到sequence中链接，生成新字符串
# print(m)




# import random,string
# str1 = '0123456789'
# str2 = string.ascii_letters
# str3 = string.punctuation
# str4 = str1 + str2 + str3
# m = random.sample(str4,8)
# # print(m)
# m = ''.join(m)
# print(m)


#随机数小游戏
# import random
# i = 1
# a = random.randint(0,100)
# b = int(input('请输入0-100中的一个数\n然后查看是否和电脑一样：'))
# while a != b:
#     if a > b:
#         print('你第%d输入的数字小于电脑随机数字' %i)
#         b = int(input('请再次输入数字：'))
#     else:
#         print('你第%d输入的数字大于电脑随机数字' %i)
#         b = int(input('请再次输入数字：'))
#     i += 1
# else:
#     print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' %(i,b))




#16、计算平⽅根
# num = float(input('请输入一个数字：'))
# num_sqrt = num ** 0.5
# print('%0.3f 的平方根为 %0.1f' % (num,num_sqrt))




#17、判断字符串是否只由数字组成
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError,ValueError):
#         pass
#
#     return False
#
# print(is_number(10))







#18、判断奇偶数
# num = int(input('请输入一个数字'))
# if (num % 2 ) == 0:
#     print('{} 是偶数'.format(num))
# else:
#     print('{} 是奇数'.format(num))




# while True:
#     try:
#         num = int(input('请输入一个整数'))
#     except ValueError:
#         print('输入的不是整数！')
#         continue
#     if num % 2 == 0:
#         print('偶数')
#     else:
#         print('奇数')




#19、判断闰年
# while True:
#     year = int(input('请输入一个年份：'))
#     if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 == 0):
#         print('{}是闰年'.format(year))
#     else:
#         print('{}不是闰年'.format(year))


# while True:
#     year = int(input('请输入一个年份：'))
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print('{}是闰年'.format(year))
#             else:
#                 print('{}不是闰年'.format(year))
#         else:
#             print('{}是闰年'.format(year))
#     else:
#         print('{}不是闰年'.format(year))




# import calendar
# year = int(input('请输入年份：'))
# check_year = calendar.isleap(year)
# if check_year == True:
#     print('%d是闰年' % year)
# else:
#     print('%d是平年' % year)







#20、获取最⼤值
# n = int(input('请输入需要对比大小数字的个数'))
# print('请输入需要对比的数字')
# num =[]
# for i in range(1,n+1):
#     temp = int(input('输入第 %d 个数字：' % i))
#     num.append(temp)
#
# print('您输入的数字为：',num)
# print('最大值为：',max(num))



# n = int(input('输入需要对比大小数字的个数： \n'))
# num = [ int(input('请输入第 %d 个对比数字： \n' % i))for i in range(1,n+1)]
# print('您输入的数字为：',num)
# print('最大值为：',max(num))





#21、斐波那契数列
# nterms = int(input("你需要几项？"))
# n1,n2,count = 0,1,2
# if nterms <= 0:
#    print("请输入一个正整数。")
# elif nterms == 1:
#    print("斐波那契数列：")
#    print(n1)
# else:
#    print("斐波那契数列：")
#    print(n1,",",n2,end=" , ")
#    while count < nterms:
#        nth = n1 + n2
#        print(nth,end=" , ")
#        n1 = n2
#        n2 = nth
#        count += 1




#22进制转换






#23、
# 最大公约数


# def hcf(x,y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1,smaller + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#
#     return hcf
#
# num1 = int(input('请输入第一个数'))
# num2 = int(input('请输入第二个数'))
#
# print(num1,'和',num2,'最大公约数为',hcf(num1,num2))



#最⼩公倍数


# def lcm(x,y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#
#     while True:
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
#
# num1 = int(input('请输入第一个数'))
# num2 = int(input('请输入第二个数'))
#
# print(num1,'和',num2,'最小公倍数为',lcm(num1,num2))




#24、简单计算器

# def add(x,y):
#     return x + y
#
# def subtract(x,y):
#     return x - y
#
# def multiply(x,y):
#     return x * y
#
# def divide(x,y):
#     return x / y
#
# print('选择运算：、\n1.相加\n2.相减\n3.相乘\n4.相除')
#
# choice = input('输入你的选择(1/2/3/4):')
#
# num1 = int(input('输入第一个数'))
# num2 = int(input('输入第二个数'))
#
# if choice == '1':
#     print(num1,'+',num2,'=',add(num1,num2))
# elif choice == '2':
#     print(num1,'-',num2,'=',subtract(num1,num2))
# elif choice == '3':
#     print(num1,'*',num2,'=',multiply(num1,num2))
# elif choice =='4':
#     if num2 != 0:
#         print(num1, '/', num2, '=', divide(num1, num2))
#     else:
#         print('分母不能为0')
# else:
#     print('输入错误')





#25、⽣成⽇历


# import calendar
# while True:
#     yy = int(input('输入年份：'))
#     mm = int(input('输入月份：'))
#
#     print(calendar.month(yy, mm))



#26、文件IO





#27、字符串判断

#28、字符串大小写转换




#29、计算每个月天数
# import calendar
# monthRange = calendar.monthrange(2021,11)
# print(monthRange)


#30、获取昨天的日期
import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=1)
#     yesterday = today - oneday
#
# print(getYesterday())



#CSDN:
import datetime

# 获取今天（现在时间）
today = datetime.datetime.today()
# 昨天
yesterday = today - datetime.timedelta(days=1)
# 明天
tomorrow = today + datetime.timedelta(days=1)

# 获取当前日期
date = datetime.date.today()
# 获取一秒后的时间
s = today + datetime.timedelta(seconds=1)
# 获取一分钟后的时间
m = today + datetime.timedelta(minutes=1)
# 获取一小时后的时间
h = today + datetime.timedelta(hours=1)
# 获取一年后的时间
y = today + datetime.timedelta(days=365)

print('获取今天（现在时间）：{}\n'.format(today),
      '昨天：{}\n'.format(yesterday),
      '明天：{}\n'.format(tomorrow),
      '获取当前日期：{}\n'.format(date),
      '一秒后的时间：{}\n'.format(s),
      '一分钟后的时间：{}\n'.format(m),
      '一小时后的时间：{}\n'.format(h),
      '一年后的时间：{}'.format(y))
