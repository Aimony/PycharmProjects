#index()获取列表索引
lst=['hello','我的','名字','叫','xxx','hello']
print(lst.index('hello'))       #如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
#print(lst.index('python'))      #如果查询元素在列表中不存在，会抛出ValueError
#print(lst.index('hello',1,5))   #可在指定的start和stop之间进行查找
print(lst.index('hello',1,6))
