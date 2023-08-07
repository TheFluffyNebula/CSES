'''
okay, here is where I discover that I need a sorted set so to cpp we go
have to look for the closest friend, not the lowest
this doesn't work but it has the right idea
sortedset doesn't allow for unique elements LOL
'''
import sys
sys.stdin = open("MovieFestivalTwo.in")
from sortedcontainers import SortedSet

n, k = map(int,input().split())
friends = SortedSet([0]*k)
times = [tuple(map(int,input().split())) for _ in range(n)]
times.sort(key=lambda x: x[1])
print(times)

ans = 0
for i in range(n):
    friend = friends.bisect_right(times[i][0])
    if friend > 0:
        friends.remove(friends[friend-1])
        ans += 1
        friends.add(times[i][1])

print(ans)
