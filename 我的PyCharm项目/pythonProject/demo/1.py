year = int(input('请输入年份：'))
if isinstance(year,int):
    if year > 1582:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print('该年是闰年')
        else:
            print('该年是平年')
    else:
        print('请输入1582以后的年份')
else:
    print('请输入年份')

