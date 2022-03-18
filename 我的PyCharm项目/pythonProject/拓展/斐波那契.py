a = input('输入')

def rFib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return rFib(x - 1) + rFib(x - 2)
print(rFib(30))