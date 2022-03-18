'''
else语句的搭配：
        if...else           if条件表达式不成立时执行else
        while...else        没有碰到break时执行else
        for...else          没有碰到break时执行else
'''

for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次密码均错误')