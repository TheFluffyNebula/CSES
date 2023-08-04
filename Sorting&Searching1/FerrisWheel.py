import sys
# sys.stdin = open("FerrisWheel.in")
input = sys.stdin.readline

n, mx_weight = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

L = 0
R = n - 1
ans = 0

while a[R] >= mx_weight:
    ans += 1
    R -= 1

while L < R:
    if a[L] + a[R] > mx_weight:
        ans += 1
        R -= 1
    else:
        ans += 1
        L += 1
        R -= 1

if L == R:
    ans += 1
# print(L, R)
print(ans)