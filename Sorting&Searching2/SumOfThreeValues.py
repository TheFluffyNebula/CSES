import sys
# sys.stdin = open("SumOfThreeValues.in")

n, target = map(int,input().split())
b = list(map(int,input().split()))
a = [(b[i], i + 1) for i in range(n)]
a.sort()

def solve():
    if n < 3:
        print("IMPOSSIBLE")
        return
    for i in range(n): # lock element i
        L = 0
        R = n - 1
        while L < R:
            if L == i:
                L += 1
            elif R == i:
                R -= 1
            if a[L][0] + a[R][0] > target - a[i][0]:
                R -= 1
            elif a[L][0] + a[R][0] < target - a[i][0]:
                L += 1
            else:
                print(a[L][1], a[R][1], a[i][1])
                return
    print("IMPOSSIBLE")

solve()
''' sum 2 values solution:
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
o(n^2) solution, lock one value and then use two pointers on everything else
'''