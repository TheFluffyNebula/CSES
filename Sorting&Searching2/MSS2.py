import sys
# sys.stdin = open("MaximumSubarraySumTwo.in")
from collections import deque

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

pf = [0]*(n+1)
for i in range(n):
    pf[i+1] = pf[i] + a[i]

dq = deque()
ans = float('-inf')
for i in range(x, n+1):
    while dq and dq[0] < i - y: 
        dq.popleft()
    while dq and pf[dq[-1]] > pf[i - x]: 
        dq.pop()
    dq.append(i - x)
    ans = max(ans, pf[i] - pf[dq[0]])

print(ans)
