import sys
# sys.stdin = open("SumOfTwoValues.in")
input = sys.stdin.readline

n, target = map(int,input().split())
b = list(map(int,input().split()))
a = [(b[i], i + 1) for i in range(n)] # (value, index) pairs
a.sort()

def solve():
    L = 0
    R = n - 1
    while L < R:
        if a[L][0] + a[R][0] > target:
            R -= 1
        elif a[L][0] + a[R][0] < target:
            L += 1
        else:
            print(a[L][1], a[R][1])
            return
    print("IMPOSSIBLE")

solve()

# attach the element to the index in the input