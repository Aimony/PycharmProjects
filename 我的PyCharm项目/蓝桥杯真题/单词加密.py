letter = input()
arr = []
new_arr = []
for i in letter:
    arr.append(i)
for j in arr:
    value = ord(j) + 3
    new_arr.append(chr(value))
ans = ''.join(new_arr)
print(ans)
