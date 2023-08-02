import sys
# sys.stdin = open("Apartments.in")
n, m, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
# n is len(a), m is len(b)

L, ans = 0, 0
for R in range(n):

    while L < m and b[L] < a[R] - k:
        L += 1

    if L < m and abs(a[R] - b[L]) <= k:
        ans += 1
        L += 1
    
    if L >= m:
        break

print(ans)


'''
two pointers
'''