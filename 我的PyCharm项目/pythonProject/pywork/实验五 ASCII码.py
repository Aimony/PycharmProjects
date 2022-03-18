#1.从控制台窗口读取一个字符，并显示其 ASCII 码。
# a=int(input())
# print(chr(a))

#2.已知字符 A 的 ASCll 码值是 65,字符 a 的 ASCll 码是 97,打印所有大小写字母的 ASCll 值,打印结果按格式 A：65 B:66,每 6 个字符换行
a = list(range(65,91))
a.extend(range(97,123))
s=''
for x in a:
    s=s+"  ".join([chr(x),':',str(x),"  "])
    if (a.index(x)+1) % 6 ==0:
        s = s +'\n'
print(s)


#3.从键盘输入一个字符，输出与该字符前后相邻的两个字符及对应的ASCII 码，要求输出时按 ASCII 码从小到大的顺序输出

# x=int(input())
# print(chr(x-1),chr(x),chr(x+1))


