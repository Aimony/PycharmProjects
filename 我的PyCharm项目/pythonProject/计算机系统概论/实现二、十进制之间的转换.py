input('请输入你想转换的类型：(二转十e  十转二s)')
e,s = '',''
a = input()
if a == e:
    y = input('输入二进制；\n')
    print(int(y,2))
else:
    x = int(input('输入十进制；\n'))
    print(bin(x).strip("0b"))
