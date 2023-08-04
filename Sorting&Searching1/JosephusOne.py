import sys
# sys.stdin = open("JosephusOne.in")
from collections import deque

n = int(input())

ans = []
def josephus(n, k):
    # Prepare a queue of people
    queue = deque(range(1, n + 1))
    
    while queue:
        # Skip k - 1 people
        queue.rotate(-k+1)
        ans.append(queue.popleft())

josephus(n, 2)
print(*ans)


'''
had to look this one up :/
'''