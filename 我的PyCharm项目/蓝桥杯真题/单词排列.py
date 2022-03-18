import itertools

s = list('LANQIAO')
print(itertools.permutations(s))
print(set(itertools.permutations(s)))
print(len(set(itertools.permutations(s))))

