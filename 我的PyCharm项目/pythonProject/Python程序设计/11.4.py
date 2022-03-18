# #(#
# if True:
# 	#)#
# 	x = eval(input("请输入一个浮点数"))
# #(#
# while type(x)==type(0.1):
# #)#
# 	print("输入正确！")
# 	break
# else:
# 	print("输入错误！")


#输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理

try:
    x = input('请输入第一个整数')
    y = input('请输入第二个整数')
    z = int(x) / int(y)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('请输入整数')
else:
    print(x,'/',y,'=',z)



