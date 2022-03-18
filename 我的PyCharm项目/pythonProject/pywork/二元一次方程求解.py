import math
print('解一元二次方程:  ax**2+bx+c')
print('请输入a,b,c的值')
s = input('a,b,c:')
a,b,c = map(float,s.split())
delta = b*b-4*a*c
print('%dx**2+%dx+%d' %(a,b,c))
if delta >= 0:
    x1 = (-b + math.sqrt(delta)) // (2 * a)
    x2 = (-b - math.sqrt(delta)) // (2 * a)
    print('解1:%.2f\n解2:%.2f' %(x1,x2))
else:
    print('方程无解')

