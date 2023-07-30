import sys
# sys.stdin = open("WeirdAlg.in")
n = int(input())
ans = []
while n > 1:
    ans.append(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
ans.append(1)
print(*ans)