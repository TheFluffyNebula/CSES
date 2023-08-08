import sys
# sys.stdin = open("CountingRooms.in")
from collections import deque
n, m = map(int,input().split())


colors = [input() for _ in range(n)]
# print(*colors, sep = "\n")
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def out(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return True
    return False

def floodfill(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if out(nx, ny) or visited[nx][ny]:
                continue
            if colors[nx][ny] == '.':
                q.appendleft((nx, ny))
                visited[nx][ny] = True
    return

visited = [[False] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if colors[i][j] == '.' and not visited[i][j]:
            floodfill(i,j)
            ans += 1
            # print(i,j)
print(ans)

'''
flood fill
'''