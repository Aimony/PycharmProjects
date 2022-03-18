''''
    会员  >=200 8折
         >=100 9折
    非会员     >=200 9折
              <200  不打折
'''
answer=input('你是会员吗？y/n')
money=float(input('请输入购物金额'))

if answer=='y':
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为 ：',money)
else:
    if money>=200:
        print('打95折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)


