import sys
# sys.stdin = open("RoundTrip.in")
from collections import deque
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
adj = {i: [] for i in range(1, n + 1)}
for _ in range(m):
	u, v = map(int, input().split())
	adj[u].append(v)
	adj[v].append(u)
# print(adj)

# find a cycle of length 3 or greater
def dfs(node, parent, depth):
    color[node] = 1  # mark node as visited
    depths[node] = depth
    for neighbor in adj[node]:
        if color[neighbor] == 0:  # if neighbor is unvisited
            parents[neighbor] = node
            if dfs(neighbor, node, depth + 1):
                return True
        elif neighbor != parent:  # if neighbor is visited and is not the parent
            cycle_length = depths[node] - depths[neighbor] + 1
            if cycle_length >= 3:  # if the cycle is of length 3 or more
                # print('Cycle of length 3 or more detected:')
                cycle = [node]
                while node != neighbor:
                    node = parents[node]
                    cycle.append(node)
                print(len(cycle) + 1)
                print(*(cycle + [cycle[0]]))
                return True
    color[node] = 2  # mark node as fully processed
    return False

color = [0] * (n + 1)  # initially all nodes are unvisited
depths = [0] * (n + 1)  # the depth of each node
parents = [0] * (n + 1)  # the parent of each node
good = False
for i in range(1, n + 1):
    if color[i] == 0:
        if dfs(i, None, 0):
            good = True
            break
if not good:
    print("IMPOSSIBLE")