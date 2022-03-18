lst = [0,1,2,3,4,5,6,7,8,9]
print(lst[::])
print(lst[::-1])
print(lst[::2])
print(lst[1::2])
print(lst[3::])

print(lst[:11:])
print(lst[:10:])
print(lst[:9:])
print(lst[:1100000:])

print(lst[11:])
print(lst[10:])
print(lst[9:])

print('---------------------------------')

a = [3,5,7]
print(a[len(a):])
a[len(a):] = [9]
print(a)

a[:3] = [1,2,3]
print(a)

a=list(range(10))
print(a)

a[::2]=[0]*(len(a)//2)
print(a)