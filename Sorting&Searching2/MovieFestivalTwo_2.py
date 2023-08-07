# attempting to use a prioQ this time
import sys
# sys.stdin = open("MovieFestivalTwo.in")
from queue import PriorityQueue

n, k = map(int,input().split())
# n movies, k people
pq = PriorityQueue()
for i in range(k):
    pq.put(0)
times = [tuple(map(int,input().split())) for _ in range(n)]
times.sort(key = lambda x: x[1])
# print(times)
ans = 0
for i in range(n):
    x = pq.get()
    if x <= times[i][0]:
        ans += 1
        pq.put(times[i][1])
    else:
        pq.put(x)
print(ans)