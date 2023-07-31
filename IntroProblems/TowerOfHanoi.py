import sys
# sys.stdin = open("TowerOfHanoi.in")
n = int(input())
ans = []
def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)
        ans.append((source, target))
        hanoi(n - 1, helper, source, target)

hanoi(n, 1, 2, 3)
print(len(ans))
for line in ans:
    print(*line)

'''
we go pattern searching again
n=1:
1 3

n=2:
1 2
1 3
2 3

n=3:
1 3
1 2
3 2
1 3
2 1
2 3
1 3
nevermind I'm going to look this up
'''