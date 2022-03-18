# num = int(input('请输入你所要判断的数：'))
# for i in range(2, num):
#     if (num % i == 0):
#         print('%d不是素数' % num)
#         break
#     else:
#         print('%d是素数' % num)


# import math
# def isprime(n):
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#
#     for k in range(6,math.sqrt(n) + 2,6):
#         if n % (k - 1) == 0 or n % (k + 1) == 0:
#             return False
#
# print(isprime(7))



while True:
    num = int(input('请输入一个数字:'))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, '不是质数')
                break
        else:
            print(num, '是质数')
    else:
        print(num, '不是质数')

