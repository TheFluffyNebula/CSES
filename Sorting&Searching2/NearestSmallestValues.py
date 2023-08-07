import sys
# sys.stdin = open("NearestSmallestValues.in")
n = int(input())
b = list(map(int,input().split()))
a = []
for i in range(n):
    a.append((i + 1, b[i]))
# print(a)

stack = []
ans = [0] * n
for i in range(n):
    while stack and stack[-1][1] >= a[i][1]:
        stack.pop()
    if stack:
        ans[i] = stack[-1][0] # index, value
    stack.append(a[i])
print(*ans)

'''
https://usaco.guide/CPH.pdf#page=89
stack time
'''