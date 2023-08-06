import sys
# sys.stdin = open("TasksAndDeadlines.in")

n = int(input())
vals = [tuple(map(int,input().split())) for _ in range(n)]
vals.sort() # automatically sorts by first element

t = 0
ans = 0
for i in range(n):
    t += vals[i][0]
    ans += vals[i][1] - t
print(ans)
'''
the theorem here is to sort by time needed since
point values are the same, 
it's better to have as many markers as close to the beginning as possible
for less penalty
'''