import sys
# sys.stdin = open("MessageRoute.in")
from collections import deque

n, m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(s):
    parent = [0 for _ in range(n+1)]  # Keep track of the parent of each node.
    visited[s] = True
    q = deque([s])
    while q:
        c = q.popleft()
        if c == n:  # If we've reached 'n', reconstruct the path.
            path = []
            while c != 0:
                path.append(c)
                c = parent[c]
            path.reverse()
            print(len(path))
            print(*path)
            return
        for u in adj[c]:
            if not visited[u]:
                q.append(u)
                visited[u] = True
                parent[u] = c  # Record the parent of 'u'.
    print("IMPOSSIBLE")

visited = [False] * (n + 1)
bfs(1)
