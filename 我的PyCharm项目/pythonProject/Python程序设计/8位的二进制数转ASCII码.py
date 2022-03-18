# # while True:
#
# x = input('请输入一个八位二进制')
# # list = []*8
# # list.append(x)
# # print(list)
# xlist = x.split("A")
# # print(xlist)
#



# xlist = [int(xlist[i]) for i in range(len(xlist))]
# print(xlist)

# a = input('请输入一个八位二进制')
# print([int(a[i]) for i in range(len(a))])
# b = [int(a[i]) for i in range(len(a))]
#
# # for i in range(len(a)):
#     if b.index(a) > 8:
#         print('您输入的不是8位数')
#     else:
#         break




# bin=str(input('输入二进制数：'))
# count = 0
# for i in range(0,len(bin)):
#     if bin[i] == str(1):
#         sum=2**(len(bin)-i-1)
#         count=count+sum
# print(chr(count))


x = input('请输入二进制数')
print(chr(int(x,2)))

