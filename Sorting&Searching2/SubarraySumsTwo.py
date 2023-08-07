import sys
# sys.stdin = open("SubarraySumsTwo.in")
input = sys.stdin.readline
from collections import defaultdict

n, x = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
ans, cur, freq[0] = 0, 0, 1
for xi in arr:
    cur += xi
    ans += freq[cur - x]
    freq[cur] += 1
print(ans)
'''
this was the closest I could find
probably works in cpp
'''