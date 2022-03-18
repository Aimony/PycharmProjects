lst=[13,46,17,88,76,59,95]
print('排序前：',lst,id(lst))
lst.sort()
print('排序后：',lst,id(lst))


lst.sort(reverse=True)                  #reverse=True降序     reverse=False降序
print(lst)
lst.sort(reverse=False)
print(lst)

print('--------------使用内置函数sorted()对列表进行排序，将产生新的列表对象----------------')
lst=[13,46,17,88,76,59,95]
print('原列表',lst)
new_list=sorted(lst)
print(lst)
print(new_list)

desc_list=sorted(lst,reverse=True)
print(desc_list)

