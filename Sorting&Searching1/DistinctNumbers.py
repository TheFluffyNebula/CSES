import sys
import bisect
input = sys.stdin.readline

# okay, last attempt but this is really dumb
# the plan is to sort and then perform bisect a bunch of times
# sort is n log n and bisect n times is also n log n
# LOL IT WORKED
n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
i = 0
while i < n:
    i = bisect.bisect(a, a[i])
    ans += 1
print(ans)

# this got TLE somehow...
# n = int(input())
# print(len(set(map(int,input().split()))))

# this as well
# n = int(input())
# a = list(map(int,input().split()))
# b = dict()
# ans = 0
# for i in range(n):
#     if a[i] not in b:
#         ans += 1
#         b[a[i]] = 1
# print(ans)