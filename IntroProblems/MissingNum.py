import sys
# sys.stdin = open("MissingNum.in")
n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(n - 1):
    if a[i] != i + 1:
        print(i + 1)
        exit()
print(n)