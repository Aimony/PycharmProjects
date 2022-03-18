'''
    所有元素均为键值对（key-value）    key可以重复，value不可重复
    元素是无序的
    key是不可变对象
    可根据需要动态伸缩
    是一种使用空间换时间的数据结构
'''

d={'name':'张三','name':'李四'} #{'name': '李四'}  key不允许重复
print(d)

d={'name':'张三','name-':'张三'}    #{'name': '张三', 'name-': '张三'}
print(d)

lst=[10,20,30]
lst.insert(1,100)
print(lst)
