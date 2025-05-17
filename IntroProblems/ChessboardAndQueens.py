import sys
# sys.stdin = open("ChessboardAndQueens.in")

board = [input() for _ in range(8)]
# print(*board, sep = '\n')

ans = 0
cols = [False] * 8
diag1 = [False] * 15  # r + c
diag2 = [False] * 15  # r - c + 7

def backtrack(row):
    global ans
    if row == 8:
        ans += 1
        return
    for col in range(8):
        if board[row][col] == '*':
            continue
        if cols[col] or diag1[row + col] or diag2[row - col + 7]:
            continue
        cols[col] = diag1[row + col] = diag2[row - col + 7] = True
        backtrack(row + 1)
        cols[col] = diag1[row + col] = diag2[row - col + 7] = False

backtrack(0)
print(ans)

'''
function backtrack(state):
    if is_solution(state):
        record_solution(state)
        return

    for move in valid_moves(state):
        make_move(state, move)

        if is_valid(state):             # optional pruning step
            backtrack(state)

        undo_move(state, move)
'''
