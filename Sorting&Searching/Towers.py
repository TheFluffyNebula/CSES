import sys
# sys.stdin = open("Towers.in")

n = int(input())
a = list(map(int,input().split()))

towers = []
for i in range(n):
    L = 0
    R = len(towers) - 1
    idx = -1
    while L <= R:
        mid = L + (R - L) // 2
        if a[i] < towers[mid]: # we want to find a smaller tower
            idx = mid
            R = mid - 1
        else: # we want to find a larger tower that theh block can go on
            L = mid + 1
    if idx == -1:
        towers.append(a[i])
    else:
        towers[idx] = a[i]
# print(towers)
print(len(towers))