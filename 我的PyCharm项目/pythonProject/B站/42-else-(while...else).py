a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码正确')
    a+=1
else:
    print('三次密码均输错')