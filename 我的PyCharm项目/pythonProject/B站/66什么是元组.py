'''
    元组是python内置数据结构之一，是不可变序列
'''
'''
        不可变序列：字符串，元组（无增删改操作）
        可变序列：列表，字典（可增删改，对象地址不改变）
'''

lst = [10,20,30]
print(id(lst))
lst.append(100)
print(id(lst))

print('---------------')

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))

