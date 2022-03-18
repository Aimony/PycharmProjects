# def demo(s):
#     results = []
#     for i in s:
#         if
#
# def demo(s):
#     d = {}
#     for i in set(s):
#         d[i] = s.count(i)
#         print(tuple(d))
#
# print(demo('dgehege64g14'))

# str = "xxx"
# result = {}
# for i in set(str):#set将字符串转为集合对象，用于去重，减少计算量
#     result[i] = str.count(i)
# print result


# intcount=[]
# upstrcount=[]
# lowstrcount=[]
# othercount=[]
# def number(a):
#     for i in a:
#         if i.isdigit():
#             intcount.append(i)
#         elif i.isupper():
#             upstrcount.append(i)
#         elif i.islower():
#             lowstrcount.append(i)
#         else:
#             othercount.append(i)
#     return intcount,upstrcount,lowstrcount,othercount
# a=input('请输入一个字符串：')
# a,b,c,d=number(a)
# print('大写字母的个数：{}'.format(len(a)))
# print('小写字母的个数：{}'.format(len(b)))
# print('数字的个数：{}'.format(len(c)))
# print('其他数字的个数：{}'.format(len(d)))
# a=tuple(a)
# b=tuple(b)
# c=tuple(c)
# d=tuple(d)
# print(a,b,c,d)


# def judge(s):
#     cap, small, num, other = 0, 0, 0, 0
#     for i in s:
#         if i.isupper():
#             cap = cap + 1
#         elif i.islower():
#             small = small + 1
#         elif i.isdigit():
#             num = num + 1
#         else:
#             other = other + 1
#     print('大写字母个数：{0}\n小写字母个数：{1}\n数字个数：{2}\n其他字符个数：{3}\n'.format(cap,small,num,other))
#
#
# string = input('输入字符串：')
# judge(string)




# import math
# result = lambda x:1 + 2 * x if x <= 4 else 2 + math.log(x,10)
#
# print(result(4))
# print(result(5))




# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


