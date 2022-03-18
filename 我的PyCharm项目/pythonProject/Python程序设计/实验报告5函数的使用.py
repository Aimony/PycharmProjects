# def sub(x,y):
#     s = 0
#     for i in range(x,y+1):
#         s += i
#     return s
#
# print(sub(1,3))         #6


# import math
# def fenduanFunc(x):
#     y = 0
#     if x < 4:
#         y = 1 + 2 * x
#         print('y =',y)
#     elif x == 4:
#         print('y =',1 + 2 * x,'或','y =',2 + math.log(x))
#     else:
#         print('y =',2 + math.log(x))
#
#
# print(fenduanFunc(2))
# print(fenduanFunc(4))
# print(fenduanFunc(5))





# import random
# def func():
#     operator = ["+", "-", "*", "/"]
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     operators = random.choice(operator)
#     ques = str('问题：{} {} {}'.format(int(num1),operators,int(num2)))
#     print(ques)
#     you_ans = int(input('请输入你的答案'))
#     correct_ans = num1,operators,num2           #
#     if you_ans == correct_ans:
#         print('True',end='  ')
#         return you_ans
#     else:
#         print('False',end='  ')
#         return you_ans
#
# print(func())





# import random
# score = 0 #score of user
# questions = 0 #number of questions asked
# operator = ["+","-","*"]
# number1 = random.randint(1,20)
# number2 = random.randint(1,20)
# print("You have now reached the next level!This is a test of your addition and subtraction")
# print("You will now be asked ten random questions")
# while questions<10: #while I have asked less than ten questions
#     operator = random.choice(operator)
#     question = '{} {} {}'.format(number1, operator, number2)
#     print("What is " + str(number1) +str(operator) +str(number2), "?")
#     answer = input()
#     if answer ==(number1,operator,number2):
#         print("You are correct")
#         score =score+1
#     else:
#         print("incorrect")









# import random
# operator = ["+", "-", "*", "/"]
# print(type(random.choice(operator)))
#
# print(type(1+2))



# while True:
#     a = [ '+','-','*','/' ]
#     import random
#     Fuhao = random.choice(a)
#     if Fuhao == '/':
#         Num1 = random.randint(0, 10)
#         Num2 = random.randint(1, 10)
#         print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
#         Answer = input('请输入答案【有小数请保留小数点后三位】: ')
#         Correct_Answer = float(Num1 / Num2)
#     if Fuhao == '*':
#         Num1 = random.randint(0, 10)
#         Num2 = random.randint(0, 10)
#         print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
#         Answer = float(input('请输入答案: '))
#         Correct_Answer = Num1 * Num2
#     if Fuhao == '+':
#         Num1 = random.randint(0, 10)
#         Num2 = random.randint(0, 10)
#         print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
#         Answer = float(input('请输入答案: '))
#         Correct_Answer = Num1 + Num2
#     if Fuhao == '-':
#         Num1 = random.randint(0, 10)
#         Num2 = random.randint(0, 10)
#         print('%.d %s %.d=?' % (Num1, Fuhao, Num2))
#         Answer = float(input('请输入答案: '))
#         Correct_Answer = Num1 - Num2
#     if Fuhao == '/':
#         if Correct_Answer % 1 != 0:
#             Correct_Answer = ('%.3f' %Correct_Answer)
#     if Answer == Correct_Answer:
#         print('正确！')
#     else:
#         print('错误！')











# def solution():
#     lst1 = [2,7,11,15]
#     target = 9
#     for i in range(lst1.index(0),lst1.index(4)):



# def solution(nums,target):
#
#     nums = [2,7,11,15]
#     target = 9
#
#     dict1 = {}
#     for i in range(0, len(nums)):
#         num = target - nums[i]
#         if num not in dict1:
#             dict1[num[i]] = i
#         else:
#             return [dict1[num, i]]
#
# print(solution(4,9))


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         index_list = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):                 #面向对象
#                 if nums[i] + nums[j] == target:
#                     index_list.append(i)
#                     index_list.append(j)
#         print(list(set(index_list)))
#         return index_list
#
# print(Solution())