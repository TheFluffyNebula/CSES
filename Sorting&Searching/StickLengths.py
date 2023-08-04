import sys
# sys.stdin = open("StickLengths.in")

n = int(input())
a = list(map(int,input().split()))
a.sort()

# pretty sure this type of problem it's just take the difference of everything from the median
median = a[(n - 1) // 2]
ans = sum([abs(median - a[i]) for i in range(n)])
print(ans)