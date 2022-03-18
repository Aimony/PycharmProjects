first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
message = f'Hello,{full_name.title()}'      #首字母大写
print(message)


str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12


num = 321_1332_1233_1320
print(num)



import this

a = []
for i in range(1,101):
    a.append(i**2)
print(a)

print('------------------')
b = [i**2 for i in range(1,11)]
print(b)



for i in range(1,100000):
    print(i)
# print(sum(i))


for i in range(3,31):
    if i % 3 == 0:
        print(i,end='    ')


c = [i**3 for i in range(1,11)]
print('\n',c)






