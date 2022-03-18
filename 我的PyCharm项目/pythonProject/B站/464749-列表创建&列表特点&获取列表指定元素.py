#使用[]
lst=['hello','world',12345678,'就这','ABC']
print(lst)
print(lst[0],lst[2],lst[-1],lst[-4])
#print(lst[10])     #IndexError: list index out of range
'''
    获取单个元素：
        正向索引从0到N-1
        逆向索引从-N到-1
        指定索引不存在，抛出IndexError
'''

#使用内置函数list()
lst2=list(['hello','world',1234567890])
print(lst2)

'''
    特点：
        列表元素按顺序有序排列
        索引映射唯一数据
        可储存重复数据
        任意数据类型混存
        根据需要动态分配和回收内存
'''