# n = int(input())
# s_num = input()
# list_num = s_num.split(' ')
# list_num1 = list(map(int,list_num))
# list_num1.sort()
# list_num2 = map(str,list_num1)
# print(' '.join(list_num2))



def jump(x):
    safe = []
    for i in range(1,101):
        if (i % x) != 0:
            if (i % 10 != x):
                if (i // 10 != x):
                    safe.append(i)

    return safe

if __name__ == "__main__":
    x = int(input('请输入数字：'))
    print(jump(x))