lst=[10,20,30,40,50,60,30]
lst.remove(30)                  #从列表中移除一个元素，如有重复的元素只移除第一个元素
print(lst)
#lst.remove(100)                #ValueError: list.remove(x): x not in list


lst.pop(1)                      #pop()根据索引移除元素
print(lst)
#lst.pop(5)                      #IndexError: pop index out of range        指定元素不存在，抛出异常
lst.pop()                       #如果不指定参数（索引），将删除列表中最后一个元素
print(lst)

print('---------------------------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)

lst[1:3]=[]                 #不产生新对象，而是删除原列表中的内容
print(lst)

lst.clear()                 #清除列表中所有元素
print(lst)

del lst                     #将列表对象删除
#print(lst)                 #NameError: name 'lst' is not defined