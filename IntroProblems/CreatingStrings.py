import sys
# sys.stdin = open("CreatingStrings.in")
from itertools import permutations

s = input()
p = sorted(set(permutations(s)))

print(len(p))
for permutation in p:
    print(''.join(permutation))