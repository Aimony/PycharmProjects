import string
s = input('请输入一个字符串:\n')
letters = 0   # 统计字母个数
space = 0     # 统计空格个数
digit = 0     # 统计数字个数
others = 0    # 统计其他字符个数
i = 0
while i < len(s):
    oneword = s[i]  # 获取每个位置的值
    i += 1
    if oneword.isalpha():  # 判断是否是字母
        letters += 1
    elif oneword.isdigit(): # 判断是否为数字
        digit += 1
    elif oneword.isspace(): # 判断是否为空格
        space += 1
    else:
        others += 1
print("[%s]中字母个数=%d,数字个数=%d,空格个数=%d,其他字符个数=%d" % (s,letters,digit,space,others))