import sys
# sys.stdin = open("StaticSumQueries.in")
input = sys.stdin.readline

n, q = map(int,input().split())
a = list(map(int,input().split()))
pf = [0]
for i in range(n):
    pf.append(pf[-1] + a[i])

for i in range(q):
    a, b = map(int,input().split())
    print(pf[b] - pf[a - 1])