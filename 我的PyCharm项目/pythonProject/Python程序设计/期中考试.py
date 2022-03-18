# s =5
# for i in range(10):
#   if i % 3 ==0:
#     continue
#   s = s+i
# print(s)


# def arb_sum(a,*b):
#   t = a
#   for i in b:
#     t = t+i
#   return t
#
# print(arb_sum(10,20))
# # print(arb_sum(10,'20'))
# print(arb_sum('10'))
# print(arb_sum('10','20','30'))

# a=['We', 'love']
# b = ['Python', '!']
#
#
# print(b.insert(0,a))
# print(a.append(b))
# print(a+b)
# print(a.extend(b))


# print(type([101,'张三']))

# print(10/3)
# print(10//3)
# print(10**3)
# print(10%3)

# s = 'abcdef'
# print(s[2])
# print(s[1-len(s)])
# print(s[-5])
# print(s[1])

# goods = {'钢笔':10, '笔盒':20, '书包':40}
# print(goods['书包'])



# from math import pi,cos,sqrt
# #(#
# x = input('请输入两边及半径：')
# a,b,r = map(float,x.split())                              #从键盘输入三角形的两个边长及夹角
# #)#
# #(#
# c=sqrt(a**2 + b**2 - 2*a*b*cos((pi*r)/180))
# #)#
# print('另一条边边长:{:.2f}'.format(c))


# scores={'zhang':45,'li':78,'wang':40,'zhou':96,'zhao':65}
# highest=max(scores.values())
# lowest=min(scores.values())
# #(#
# average=sum(scores.values())/len(scores)
# #)#
# highperson=[name for name, score in scores.items() if score==highest]
# #(#
# lowperson=[name for name, score in scores.items() if score == lowest]
# #)#
# print('平均分{}'.format(average),end=', ')
# print('{}最高分{}'.format(highperson,highest),end=', ')
# print('{}最低分{}'.format(lowperson,lowest))



# import math
#
# point1=input("请输入x1,y1:")
# #(#
# x1,y1=eval(point1)
# #)#
# point2=input("请输入x2,y2:")
# x2,y2=eval(point2)
# #(#
# d=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
# #)#
#
# print("两点之间的距离是:{:.2f}".format(d))



# from math import sqrt
# for k in range(2):
#     n=input('请输入一个整数:')
#     n=int(n)
#     m=int(sqrt(n)+1)
#     #(#
#     for i in range(2,m):
#     #)#
#     #(#
#         if n % i == 0:
#     #)#
#             print(n,'不是素数')
#             break
#     else:
#         print(n, '是素数')



# import math
# def fun(x):
#     x = float(input('请输入x的值：'))
#     if x <= 4:
#         m = abs(math.sin(x) + math.log(10,x))
#         return ('y = %.4f' % m)
#     else:
#         n = math.sqrt(1 + math.e ** x)
#         return ('y = %.4f' % n)
#
# print(fun(4))


# import itertools
# def foods(*foods):
#     return list(itertools.combinations([*foods],2))
#
# print(foods('芦笋','香菇','虾仁'))
#from math import *
#a,b,r=int(input())
#c=sqrt(a**2+b**2-2*a*b*cos(pi*r/180))
#print('另一条边长:{:.2f}'.format(c))
#scores={'zhang':45,'li':78,'wang':40,'zhou':96,'zhao':65}
#highest=max(scores.values())
#lowest=min(scores.values())
#average=sum(scores)/len(scores)
#highperson=[name for name,score in scores.items() if score==highest]
#lowperson=[name for name,score in scores.items() if score==lowest]


# import math
# point1=input("请输入x1,y1:")\
# x1,y1=eval(point1)
# point2=input("请输入x2,y2:")
# x2,y2=eval(point2)
# d=math.sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))
# print("两点之间的距离是:{:.2f}".format(d))


