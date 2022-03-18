f = lambda x,y,z:x+y+z
print(f(1,2,3))

g = lambda x,y = 2,z = 3:x+y+z
print(g(1))
print(g(2,y=4,z=5))

L = [(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]
print(L[0](2),L[1](2),L[2](2))

D = {'f1':(lambda :2+3),'f2':(lambda :2*3),'f3':(lambda :2**3)}
print(D['f1'](),D['f2'](),D['f3']())

m = [1,2,3,4,5]
print(list(map((lambda x:x+100),m)))



print('-------------------------')
import random
x = [[random.randint(1,10) for j in range(4)] for i in range(5)]
for item in x:
    print(item)
