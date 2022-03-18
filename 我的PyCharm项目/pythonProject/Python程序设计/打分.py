numbers = []
while True:
    x = input('请输入一个成绩')
    try:
        numbers.append(float(x))
    except:
        print('不是合法成绩')
    while True:
        flag = input('继续输入吗？(y/n)')
        if flag.lower() not in ('y','n'):
            print('只能输入y或n')
        else:
            break
    if flag.lower() == 'n':
        break

numbers.sort()
del numbers[0]
del numbers[-1]

print(sum(numbers)/len(numbers))
