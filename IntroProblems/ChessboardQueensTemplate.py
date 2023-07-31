# gpt solution to 8 queens problem
# I've modified it a bit to see how it works
# I think I'll have to wait on this, seems out of my skillset for now
ans = []
def solve_queens(n):
    def can_place(pos, ocuppied_rows):
        for i in range(ocuppied_rows):
            if pos[i] == pos[ocuppied_rows] or \
                pos[i] - pos[ocuppied_rows] == ocuppied_rows - i or \
                pos[i] - pos[ocuppied_rows] == i - ocuppied_rows:
                return False
        return True

    def place_queens(pos, target_rows, ocuppied_rows):
        if ocuppied_rows == target_rows:
            ans.append(pos)
            return

        for i in range(target_rows):
            pos[ocuppied_rows] = i
            if can_place(pos, ocuppied_rows):
                place_queens(pos, target_rows, ocuppied_rows + 1)

    pos = [-1] * n
    place_queens(pos, n, 0)

# Example usage:
solve_queens(8)
print(len(ans)) # so there are 92