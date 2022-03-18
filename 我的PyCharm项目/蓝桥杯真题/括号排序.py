import itertools

def check(ls):
    if ls[0] == ')':
        return False
    stack = []
    for i in ls:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() !='(':
                return False
    return True

ans = set()
ls = list(itertools.permutations(['(',')','(',')','(',')','(',')']))
for i in ls:
    if check(i):
        ans.add(i)
# print(ans)
print(len(ans))




