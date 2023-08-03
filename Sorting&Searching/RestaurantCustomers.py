import sys
# sys.stdin = open("RestaurantCustomers.in")
input = sys.stdin.readline
from bisect import bisect_left, bisect

# "You may assume that all arrival and leaving times are distinct."
n = int(input())
enter = []
all = []
for i in range(n):
    a, b = map(int,input().split())
    enter.append(a)
    all.append(a)
    all.append(b)
enter.sort()
all.sort()
# print(enter, all)

cur = 0
ans = 0
for i in range(n * 2):
    event = all[i]
    # use bisect instead to find (if event in enter) in log n time instead of n
    if bisect(enter, event) - bisect_left(enter, event) == 1:
        cur += 1
        ans = max(cur, ans)
    else: # the event is someone leaving
        cur -= 1
print(ans)

# oops, I see that now for my original solution I used coordinate compression
# and then standard interval appraoch