alist=[3,4,5]
# alist=alist + [1,2]
# print(alist)

alist.append(1)
print(alist)


import time
result = []
start = time.time()
for i in range(10000):
    result = result + [i]
print(len(result),',',time.time()-start)

result = []
start = time.time()
for i in range(10000):
    result.append(i)
print(len(result),',',time.time()-start)


print('-----------------------------')

a = [1,2,3]
print(id(a))
a = [1,2]
print(id(a))
a.append(4)
a.remove(4)
a[0]=100
print(a)
print(id(a))

a.extend([7,8,9])
print(a)

a.insert(1,999)
print(a)

print(a*3)

x = [[None]*2]*3
print(x)
x[0][1]=666
print(x)





