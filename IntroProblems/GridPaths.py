import sys
sys.stdin = open("GridPaths.in")
input = sys.stdin.readline

s = input().strip()
# print(s)

# up, right, down, left
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[False] * 7 for _ in range(7)]
def out(a, b):
    if a < 0 or a >= 7 or b < 0 or b >= 7:
        return True
    return False

# print(visited)
ans = 0
# letter i
def backtrack(i, r, c):
    global ans
    # kinda like dp tbh
    if r == 6 and c == 0:
        if i == 48:
            ans += 1
        return

    # If the current path is already completed, no need to go further
    if i >= 48:
        return

    # check if there's a character already here
    if s[i] == 'U':
        newR = r - 1
        newC = c
        if not out(newR, newC) and not visited[newR][newC]:
            visited[newR][newC] = True
            backtrack(i + 1, r - 1, c)
            visited[newR][newC] = False
    elif s[i] == 'R':
        newR = r
        newC = c + 1
        if not out(newR, newC) and not visited[newR][newC]:
            visited[newR][newC] = True
            backtrack(i + 1, r, c + 1)
            visited[newR][newC] = False
    elif s[i] == 'D':
        newR = r + 1
        newC = c
        if not out(newR, newC) and not visited[newR][newC]:
            visited[newR][newC] = True
            backtrack(i + 1, r + 1, c)
            visited[newR][newC] = False
    elif s[i] == 'L':
        newR = r
        newC = c - 1
        if not out(newR, newC) and not visited[newR][newC]:
            visited[newR][newC] = True
            backtrack(i + 1, r, c - 1)
            visited[newR][newC] = False
    else:
        for move in moves:
            newR = r + move[0]
            newC = c + move[1]
            if out(newR, newC) or visited[newR][newC]:
                continue
            visited[newR][newC] = True
            backtrack(i + 1, newR, newC)
            visited[newR][newC] = False
backtrack(0, 0, 0)
print(ans)
