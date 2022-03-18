def isPrime(x):
    if x < 2:
        print(x,'不是素数')
    else:
        for i in range(2,x):
            if x % i == 0:
                print(x,'不是素数')
                break
            else:
                print(x,'是素数')

    return



print(isPrime(3))
print(isPrime(6))
print(isPrime(0))
