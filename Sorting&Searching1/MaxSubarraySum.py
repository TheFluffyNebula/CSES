import sys
sys.stdin = open("MaxSubarraySum.in")
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

pf = [0]
for i in range(n):
    pf.append(pf[-1] + a[i])
print(pf)

pm = [0]
for i in range(n):
    pm.append(min(pm[i], pf[i]))
# print(pm)

ans = -1e10
for i in range(1, n + 1):
    ans = max(ans, pf[i] - pm[i])
# print(ans)

# prefix sums, prefix minimums of the prefix sums