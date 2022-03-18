a,b=1,2
print('------------and-----------------')
print(a==1 and b==2)    #T
print(a==1 and b<2)     #F
print(a!=1 and b==2)    #F
print(a!=1 and b!=2)    #F

print('--------------or----------------')
print(a==1 or b==2)    #T
print(a==1 or b<2)     #T
print(a!=1 or b==2)    #F
print(a!=1 or b!=2)    #F

print('--------------not    对bool类型操作数取反-----------------')
f=True
f2=False
print(not f)
print(not f2)

print('--------in 与 not in-----------------------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)     #F
print('k' not in s)     #T

