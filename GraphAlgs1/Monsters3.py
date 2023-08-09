import sys # attempt 3, no more progress
# sys.stdin = open("Monsters.in")
from collections import deque
input = sys.stdin.readline
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

# step 1: find all border cells in the same connected component as A
# if run into # or M: continue
def findA():
    for i in range(n):
        if 'A' in board[i]:
            return i, board[i].index('A')
def find_valid_border(x, y):
    ret = []
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        if x == 0 or y == 0 or x == n - 1 or y == m - 1:
            ret.append((x,y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out(nx, ny) or visited[nx][ny] or board[nx][ny] == '#' or board[nx][ny] == 'M':
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return ret

visited = [[False] * m for _ in range(n)]
A_x, A_y = findA()
# Check if 'A' is already on the edge of the board
if A_x == 0 or A_y == 0 or A_x == n - 1 or A_y == m - 1:
    print("YES")
    print(0)  # No moves needed
    exit()  # Exit the script
# print("A Location: ", A_x, A_y)
possible_border = find_valid_border(A_x,A_y)
# print(possible_border)

def find_AM(x, y):
    q = deque([(x, y, 0)])  # Adding a depth (distance) to the BFS queue
    visited[x][y] = True
    aDist, mDist = float('inf'), float('inf')
    foundA, foundM = False, False
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out(nx, ny) or visited[nx][ny] or board[nx][ny] == '#':
                continue
            if board[nx][ny] == 'A':
                aDist = min(aDist, dist + 1)  # Return the distance to the target character
                foundA = True
                if foundA and foundM:
                    return aDist, mDist
            elif board[nx][ny] == 'M':
                mDist = min(mDist, dist + 1)
                foundM = True
                if foundA and foundM:
                    return aDist, mDist
            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True
    return aDist, mDist

valid = False
for i in range(len(possible_border)):
    visited = [[False] * m for _ in range(n)]
    start_x, start_y = possible_border[i][0], possible_border[i][1]
    dist_A, dist_M = find_AM(start_x, start_y)
    if dist_A < dist_M:
        valid = True
        # print(dist_A,dist_M,start_x,start_y)
        # valid_x, valid_y = start_x, start_y
        # if valid, start_x and start_y will be correct
        break

def valid_ff(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    prev = [[''] * m for _ in range(n)] # previous
    
    if board[x][y] == 'A':
        return True, x, y, prev

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if out(nx, ny) or visited[nx][ny] or board[nx][ny] == '#' or board[nx][ny] == 'M':
                continue
            prev[nx][ny] = dir[i]
            if board[nx][ny] == 'A':
                return True, nx, ny, prev
            q.append((nx, ny))
            visited[nx][ny] = True
    return False, None, None, None

if valid:
    visited = [[False] * m for _ in range(n)]
    valid, end_x, end_y, prev = valid_ff(start_x,start_y)
    print("YES")
    # print(end_x, end_y, "prev", prev)
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
    # path = path[::-1]  # no need to reverse, we are going down the path
    print(len(path))
    print(''.join(path))
else:
    print("NO")



'''
new idea
instead of trying all border cells, see which ones are in the same connected component as A
only then, brute force all possible cells

if it doesn't work:
this time, two functions on every border cell(valid)
find_nearest_monster
find_nearest_a
f_n_m and f_n_a

3rd attempt:
instead of doing the same flood fill twice,
see whether we find A or M first
'''