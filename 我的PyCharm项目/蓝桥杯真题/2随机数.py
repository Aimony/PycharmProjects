import os
import sys


n = int(input())
lst = map(int,input().split())
0
l = list(set(lst))
l.sort()

print(len(l))
print(*l,sep=' ')