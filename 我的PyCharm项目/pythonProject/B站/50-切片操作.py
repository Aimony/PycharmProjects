lst=[10,20,30,40,50,60,70,80]
print('原列表',id(lst))
lst2=lst[1:6:1]         #start=1,stop=6,step=1
print('切的片段：',id(lst2))
print(lst[1:6])         #默认步长为1
print(lst[1:6:])
print(lst[1:6:2])       #start=1,stop=6,step=2
print(lst[:6:2])        #start默认，stop=6,step=2
print(lst[1::2])        #start默认，step=2,stop默认

print('------------step步长为负---------------')
print('原列表：',lst)
print(lst[::-1])
print(lst[7::-1])       #start=7,stop省略,step-1
print(lst[6:0:-2])      #start=6,stop=0,step=-2

