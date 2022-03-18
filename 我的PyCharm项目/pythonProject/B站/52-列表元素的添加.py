lst=[10,20,30]
print('添加前：',lst,id(lst))
lst.append(100)
print('添加后：',lst,id(lst))
lst2=['hello','world']
lst.append(lst2)            #将lst2作为一个元素添加到列表的末尾
lst.extend(lst2)            #向列表的末尾一次性添加多个元素

lst.insert(1,90)            #在任意位置上添加一个元素
print(lst)

lst3=[True,False,'hello']
lst[1:]=lst3                #在任意位置添加N多个元素
print(lst)


''''
    append()        在列表末尾添加一个元素
    extend()        在列表的末尾至少议案家一个元素
    insert()        在列表的任意位置添加一个元素
    切片             在列表的任意位置至少添加一个元素
'''