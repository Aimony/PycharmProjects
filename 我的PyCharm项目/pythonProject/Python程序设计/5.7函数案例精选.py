# #1.计算圆的面积
# from math import pi as PI
# def circleArea(r):
#     if isinstance(r,(int,float)) and r > 0:
#         return PI * r * r
#     else:
#         return ('数据错误')
#
# print(circleArea(3))



# #2
# def demo(*para):
#     avg = sum(para)/len(para)
#     g = [i for i in para if i > avg]
#     # g = []
#     # for i in para:
#     #     if i > avg:
#     #         g.append(i)
#     return (avg,) + tuple(g)
#
# print(demo(1,2,3))


# #3、
# def demo(s):
#     result = [0,0]
#     for i in s:
#         if 'a' <= i <= 'z':
#             result[1] += 1
#         elif 'A' <= i <= 'Z':
#             result[0] += 1
#     return tuple(result)
# print(demo('sHHohoIHHUU'))


#4、
# def demo(lst,k):
#     x = lst[:]
#     x[:k] = reversed(x[:k])
#     x[k:] = reversed(x[k:])
#     x.reverse()
#     return x
#
#
# lst = list(range(1,21))
# print(demo(lst,5))


# lst = list(range(1,21))
# x= lst[:]
# x[:5] = reversed(x[:5])
# x[5:] = reversed(x[5:])
# x.reverse()
# print(x)




#6、
# import random
# def demo(lst):
#     m = min(lst)
#     result = (m,) + tuple((index for index,value in enumerate(lst) if value == m))
#     return result
#
# x = [random.randint(1,20) for i in range(50)]
# print(x)
# print(demo)


