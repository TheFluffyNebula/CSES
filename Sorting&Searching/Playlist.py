import sys
# sys.stdin = open("Playlist.in")
from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

nums = defaultdict(int)
L = 0
ans = 0

for R in range(n):
    if a[R] in nums and nums[a[R]] >= L:
        L = nums[a[R]] + 1 # as soon as you see the duplicate, move the left pointer such that it isn't there anymore
    nums[a[R]] = R
    ans = max(ans, R - L + 1)

print(ans)

'''
I might be calling max too many times
yep, tle
fixed
'''