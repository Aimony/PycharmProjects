lst = [3,5,7,9,11,13,3,5]
print(lst)
del lst[4]
print(lst)


print(lst.pop(3))
print(lst)

lst.remove(3)
print(lst)

print('-----------------------------------')

x = [1,2,1,2,1,1,1]
for i in x:
    i
    if i==1:
        x.remove(1)
print(x)


y = [1,2,3,4,5,6,7,8,9,2,5,4,5,5,5,5,5,5,10]
print(y.count(5))
