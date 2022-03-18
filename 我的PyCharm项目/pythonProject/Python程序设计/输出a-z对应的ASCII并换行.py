al = list(range(65,91))
al.extend((range(97,123)))
s = ''
for x in al:
    s = s + ''.join([chr(x),':',str(x),'  '])
    if (al.index(x) + 1) % 6 == 0:
        s = s + '\n'
print(s)
