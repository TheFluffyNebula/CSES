import sys
# sys.stdin = open("JosephusTwo.in")
from collections import deque

n, skip = map(int,input().split())

ans = []
def josephus(n, k):
    # Prepare a queue of people
    queue = deque(range(1, n + 1))
    lenQueue = len(queue)
    while queue:
        # Skip k - 1 people
        queue.rotate((-k+1) % lenQueue)
        ans.append(queue.popleft())
        lenQueue -= 1
josephus(n, skip + 1)
print(*ans)