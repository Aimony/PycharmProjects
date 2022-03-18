#计算1+2+...+100的值
# s = 0
# for i in range(1,101):
#     s += i
# print(s)
# print(sum(range(1,101)))
#


# for i in range(1,101):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i,end=' ')



#水仙花数
# for i in range(10**2,10**3):
#     b,s,g = map(int,str(i))
#     if b**3+s**3+g**3 == i:
#         print(i)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{} = {}'.format(i,j,i*j).ljust(6),end=' ')
#     print()


# def demo(data,k=3):
#     assert k == 3,'k must be 3'
#     for i in data:
#         if i == 0:
#             continue
#         ii = i*100
#         for i in data:
#             if j == i:
#                 continue
#             jj = j*10
#             for k in data:
#                 if k !=i and k!=j:
#                     print(ii+jj+k)


import random


x = []
while True:
    if len(x) == 20:
        break
    n = random.randint(1,100)
    if n not in x:
        x.append(n)

print(x)
print()
print(len(x))
print()
print(sorted(x))
