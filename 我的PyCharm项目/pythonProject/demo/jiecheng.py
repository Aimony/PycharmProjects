n = int(input("请输入一个正整数： "))
sums = 0
for i in range(1,n+1):
    j = 1
    factorial = 1
    while j <= i:
        factorial *= j
        j += 1
    sums += factorial
print(sums)
