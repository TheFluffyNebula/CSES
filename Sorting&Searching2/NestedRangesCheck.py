# attempting to recreate the cpp solution in python
# will definitely also learn the sort(key = lambda x) way
# TLE :/
import sys
# sys.stdin = open("NestedRangesCheck.in")
input = sys.stdin.readline

class Interval:
    def __init__(self, l, r, index):
        self.l = l
        self.r = r
        self.index = index

    def __lt__(self, other): 
        if self.l == other.l:
            return self.r > other.r
        return self.l < other.l

n = int(input())
contained, contains = [False] * n, [False] * n
ranges = []
for i in range(n):
    a, b = map(int,input().split())
    ranges.append(Interval(a, b, i))
ranges.sort()

maxEnd = 0
for i in range(n):
    if ranges[i].r <= maxEnd:
        contained[ranges[i].index] = True
    maxEnd = max(maxEnd, ranges[i].r)

minEnd = 1e9 + 1
for i in range(n - 1, -1, -1):
    if ranges[i].r >= minEnd:
        contains[ranges[i].index] = True
    minEnd = min(minEnd, ranges[i].r)

print(' '.join(map(str, map(int, contains))))
print(' '.join(map(str, map(int, contained))))