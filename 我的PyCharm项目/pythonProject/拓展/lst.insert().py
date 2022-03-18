#insert()方法是将元素插入到索引对应元素的前面


lst = [2,2,2,2,2,2]
lst.insert(0,0)# index=0时，从头部插入obj
print(lst)  #[0, 2, 2, 2, 2, 2, 2]

lst = [2,2,2,2,2,2]
lst.insert(6,7)# index > 0 且 index < len(list)时，在index的位置插入obj
print(lst)  #[2, 2, 2, 2, 2, 2, 7]

lst = [2,2,2,2,2,2]
lst.insert(-2,6)# 当index < 0 且 abs(index) < len(list)时，从中间插入obj
print(lst)  #[2, 2, 2, 2, 6, 2, 2]

lst = [2,2,2,2,2,2]
lst.insert(-20,10)# 当index < 0 且 abs(index) >= len(list)时，从头部插入obj
print(lst)  #[10, 2, 2, 2, 2, 2, 2]

lst = [2,2,2,2,2,2]
lst.insert(30,20)# 当index >= len(list)时，从尾部插入obj
print(lst)  #[2, 2, 2, 2, 2, 2, 20]