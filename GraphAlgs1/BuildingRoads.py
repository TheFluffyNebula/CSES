import sys
# sys.stdin = open("BuildingRoads.in")

n, m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(s):
    stack = [s]
    visited[s] = True
    while stack:
        c = stack.pop()
        for u in adj[c]:
            if not visited[u]:
                stack.append(u)
                visited[u] = True
    return

visited = [False] * (n + 1)
ans = 0
cities = []
for i in range(1, n + 1):
    if not visited[i]:
        ans += 1
        dfs(i)
        cities.append(i)
print(ans - 1)
for i in range(len(cities) - 1):
    print(cities[i], cities[i + 1])

'''
# of components - 1
'''