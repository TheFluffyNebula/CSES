import sys
# sys.stdin = open("ShortestRoutesOne.in")
from collections import defaultdict

n, m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}
weights = defaultdict(int)
for i in range(m):
    a, b, c = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    if (a,b) in weights:
        weights[(a,b)] = min(weights[(a,b)], c)
        weights[(b,a)] = min(weights[(b,a)], c)
    else:
        weights[(a,b)] = c
        weights[(b,a)] = c
# print(adj, weights)

import heapq

def dijkstra(s):
    global cost, adj, weights
    q = [(0, s)]  # priority queue: the priority is the distance
    cost[s] = 0
    while q:
        current_cost, current_node = heapq.heappop(q)
        if current_cost != cost[current_node]:
            continue  # this is an old, suboptimal path; we've found a better one since
        for neighbor in adj[current_node]:
            new_cost = cost[current_node] + weights[(current_node, neighbor)]
            if new_cost < cost[neighbor]:
                # we've found a shorter path to `neighbor`
                cost[neighbor] = new_cost
                heapq.heappush(q, (new_cost, neighbor))

# everything else is the same as before, except `bfs` is replaced with `dijkstra`



cost = [1e15] * (n + 1)
cost[1] = 0
dijkstra(1)
print(*cost[1:])