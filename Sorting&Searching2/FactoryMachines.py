import sys
# sys.stdin = open("FactoryMachines.in")

n, k = map(int,input().split())
a = list(map(int,input().split()))

def check(x):
    prod = 0
    for i in range(n):
        prod += x // a[i]
    return prod >= k

L = 0
R = int(1e18)
ans = 0
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)

'''
this is definitely a binary search problem
'''