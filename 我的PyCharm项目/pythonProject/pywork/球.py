import math
r=int(input("请输入半径："))
c=2*math.pi*r
s=math.pi*r*r
sb=4*math.pi*r*r
v=4/3*math.pi*r**3
print ( "圆的周长: %.2f"% c)
print ( "圆的面积: %.2f"% s)
print ( "球的表面积: %.2f"% sb)
print ( "球的体积: %.2f" % v)