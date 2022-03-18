name = "Li hua"
age = 24
print("Hello "+name+", you are " + str(age) + " years old")



name = "Li hua"
age = 24
print("Hello %s, you are %d years old" % (name, age))


# %s                  字符串（使用str()方法转换任何Python对象）
# %d                  十进制整数
# %f                  十进制浮点数(小数), 自动保留六位小数。


''''

>>> "%s  %s  %s" % ("hello", 3, 3.1415)
'hello  3  3.1415'
>>> "%s  %d  %d" % ("hello", 3, 3.1415)
'hello  3  3'
>>> "%s  %d  %f" % ("hello", 3, 3.1415)
'hello  3  3.141500'
>>> "%s  %f  %f" % ("hello", 3, 3.1415)
'hello  3.000000  3.141500'

'''



# 字符串的格式化
#   %s 表示简单的字符串
#   %d 表示整数
#   %f 表示一个浮点数 .x表示允许输出的浮点数位数. x表示一个整数,意为浮点数后面出现的位数
# %2f,  %.2f,  %.02f,  %+.2f
a = 100.0000
b = 200
c = 300
d = 400

print("A是 %2d" % a) # a 为浮点数,格式化后输出一个整数
print("A是 %2f" % a) # %2f 的写法也是不正确的,输出结果跟实际需求可能不符
print("B是 %.1f" % b) # %.1f 表示一位,%.2f表示两位,以此类推
print("B是 %.2f" % b)
print("B是 %.3f" % b)
print("C是 %.02f" % c) # 这里%.02f的表达方式应该是不正确的,但是它的输出结果跟上面相同
print("C是 %.03f" % c)
print("D是 %+.2f" % d)

# 一般情况下建议使用 str.format()
age = 18
name = "小鱼儿"
home = "中国"
print("我今年{0}岁了, 我的名字叫{1}, 我来自{2}".format(age,name,home))

# 使用%s %d 也是可以的
print("我今年%d岁了, 我的名字叫%s, 我来自%s" % (age,name,home))