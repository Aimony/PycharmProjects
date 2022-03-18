money=1000
s=int(input('请输入取款金额'))
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)