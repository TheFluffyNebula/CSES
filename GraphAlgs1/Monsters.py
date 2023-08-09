import sys # too sloppy to work
# sys.stdin = open("Monsters.in")
from collections import deque

n, m = map(int,input().split())
board = [input() for _ in range(n)]
# print(*board, sep = "\n")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = ['D', 'L', 'U', 'R']
def out(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return True
    return False

def floodfill(x, y): 
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    prev = [[''] * m for _ in range(n)] # previous
    if board[nx][ny] == 'A':
        return True, x, y, prev
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out(nx, ny) or visited[nx][ny] or board[nx][ny] == '#' or board[nx][ny] == 'M':
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            prev[nx][ny] = dir[i]
            if board[nx][ny] == 'A':
                return True, nx, ny, prev
    return False, None, None, None



visited = [[False] * m for _ in range(n)]
getOutOfLoop = False
valid = False
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or i == n - 1 or j == m - 1:
            if not visited[i][j] and board[i][j] == ".":
                valid, end_x, end_y, prev = floodfill(i,j)
                if valid:
                    getOutOfLoop = True
                    break
    if getOutOfLoop:
        break

# print(prev, end_x, end_y)
if valid:
    print("YES")
    path = []
    x, y = end_x, end_y
    while x != 0 and y != 0 and x != n - 1 and y != m - 1:
        path.append(prev[x][y])
        if prev[x][y] == 'U':
            x -= 1
        elif prev[x][y] == 'D':
            x += 1
        elif prev[x][y] == 'R':
            y += 1
        elif prev[x][y] == 'L':
            y -= 1
        # print(x,y)
    path = path[::-1]  # reverse the path to get it from start to end
    print(len(path))
    print(''.join(path))
else:
    print("NO")