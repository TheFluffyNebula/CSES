import sys
# sys.stdin = open("SubarrayDistinctValues.in")

n, k = list(map(int,input().split()))
vals = list(map(int,input().split()))
x, L = dict(), 0
res = 0
for R in range(n):
    if vals[R] in x:
        x[vals[R]] += 1
    else:
        x[vals[R]] = 1
    while len(x) > k:
        x[vals[L]] -= 1
        if x[vals[L]] == 0:
            del x[vals[L]]
        L += 1
    res += R - L + 1
print(res)