import sys # AC NO WAY!!!! hashing to get it down to O(n^2)
# sys.stdin = open("SumOfFourValues.in")
input = sys.stdin.readline
from collections import defaultdict

n, target = map(int,input().split())
a = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        idx = a[i] + a[j]
        d[idx].append((i, j))
# print(d)

# Traverse through all pairs again and search for X – (current pair sum) in the hash table.
for i in range(n):
    for j in range(i + 1, n):
        rem = target - (a[i] + a[j])
        for ent in d[rem]:
            k, l = ent[0], ent[1]
            if i != k and i != l and j != k and j != l:
                valid = sorted([i + 1, j + 1, k + 1, l + 1])
                print(valid[0], valid[1], valid[2], valid[3])
                exit()

print("IMPOSSIBLE")

'''
3Sum approach: n^3
2P on sorted pair sums: n^2 log n
hashing: n^2 <-- can this solve the CSES version!?
'''