import sys # TLE last case
# sys.stdin = open("SubarrayDivisibility.in")
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
freq = defaultdict(int)
ans, cur, freq[0] = 0, 0, 1
for xi in a:
    cur += xi
    cur %= n
    ans += freq[cur]
    freq[cur] += 1
print(ans)

''' what almost worked for subarray sums II
freq = defaultdict(int)
ans, cur, freq[0] = 0, 0, 1
for xi in arr:
    cur += xi
    ans += freq[cur - x]
    freq[cur] += 1
print(ans)
'''