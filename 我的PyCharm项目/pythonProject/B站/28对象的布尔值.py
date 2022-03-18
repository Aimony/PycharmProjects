print('------------以下布尔值均为False---------------')
print(bool(False))      #False
print(bool(0))          #数值0
print(bool(0.0))
print(bool(None))       #None
print(bool(''))         #空字符串
print(bool(""))
print(bool([]))         #空列表
print(bool(list()))     #空列表
print(bool(()))         #空元祖
print(bool(tuple()))    #空元祖
print(bool({}))         #空字典
print(bool(dict()))     #空字典
print(bool(set()))      #空集合

print('--------其他布尔值均为True--------------')

age=int(input('请输入您的年龄：'))
if age:
    print(age)                  #布尔值为true
else:
    print('年龄为：',age)        #0的布尔值为False
