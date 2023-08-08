import sys
# sys.stdin = open("Labyrinth.in")
from collections import deque

n, m = map(int,input().split())
colors = [input() for _ in range(n)]
# print(*colors, sep = "\n")

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = ['U', 'R', 'D', 'L']

def out(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return True
    return False

def floodfill(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    pred = [[''] * m for _ in range(n)]
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out(nx, ny) or visited[nx][ny] or colors[nx][ny] == '#':
                continue
            if colors[nx][ny] == '.' or colors[nx][ny] == 'B':
                q.appendleft((nx, ny))
                visited[nx][ny] = True
                pred[nx][ny] = dir[i]
            if colors[nx][ny] == 'B':
                return True, nx, ny, pred
    return False, None, None, None

visited = [[False] * m for _ in range(n)]
getOutOfLoop = False
for i in range(n):
    for j in range(m):
        if colors[i][j] == 'A':
            valid, end_x, end_y, pred = floodfill(i,j)
            getOutOfLoop = True
            break
    if getOutOfLoop:
        break

if valid:
    print("YES")
    path = []
    x, y = end_x, end_y
    while colors[x][y] != 'A':
        path.append(pred[x][y])
        if pred[x][y] == 'U':
            x += 1
        elif pred[x][y] == 'D':
            x -= 1
        elif pred[x][y] == 'R':
            y -= 1
        elif pred[x][y] == 'L':
            y += 1
    path = path[::-1]  # reverse the path to get it from start to end
    print(len(path))
    print(''.join(path))
else:
    print("NO")
