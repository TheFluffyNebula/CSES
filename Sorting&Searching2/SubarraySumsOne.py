import sys
# sys.stdin = open("SubarraySumsOne.in")

n, target = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
L = 0
x = 0
for R in range(n):
    x += a[R]
    while x > target:
        x -= a[L]
        L += 1
    if x == target:
        ans += 1
    
print(ans)