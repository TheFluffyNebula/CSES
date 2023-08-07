import sys
# sys.stdin = open("ArrayDivision.in")

n, k = map(int,input().split())
a = list(map(int,input().split()))

def check(x):
    arraysNeeded = 1
    curSum = 0
    for i in range(n):
        if a[i] > x:
            return False
        if curSum + a[i] > x:
            arraysNeeded += 1
            curSum = a[i] # if it goes over, put a[i] in the next array
        else:
            curSum += a[i] # otherwise, add it to the current one
    return arraysNeeded <= k

L = 0
R = int(1e15)
ans = -1
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
    # print(mid, check(mid))
print(ans)

'''
binary search for least maximum sum in an optimal split
[0, ,0, 1, 1] find the first 1
'''