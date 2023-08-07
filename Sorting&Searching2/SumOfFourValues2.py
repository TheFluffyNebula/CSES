import sys # 24/26 testcases as of now
sys.stdin = open("SumOfFourValues.in")

n, target = map(int,input().split())
b = list(map(int,input().split()))
a = [(b[i], i + 1) for i in range(n)]
a.sort()

def solve():
    if n < 4:
        print("IMPOSSIBLE")
        return
    
    # split array into two halves
    a1 = a[:n//2]
    a2 = a[n//2:]
    # pair sums for each list
    sum_a1 = [(a1[i][0] + a1[j][0], (a1[i][1], a1[j][1])) for i in range(len(a1)) for j in range(i + 1, len(a1))]
    sum_a1.sort()
    sum_a2 = [(a2[i][0] + a2[j][0], (a2[i][1], a2[j][1])) for i in range(len(a2)) for j in range(i + 1, len(a2))]
    sum_a2.sort(reverse=True)  # To facilitate the two pointers approach
    print(sum_a1, sum_a2)

    # two pointers approach to find the pairs that sum to target
    l = 0
    r = 0
    while l < len(sum_a1) and r < len(sum_a2):
        if sum_a1[l][0] + sum_a2[r][0] == target:
            pairs1 = sum_a1[l][1]
            pairs2 = sum_a2[r][1]
            if len(set(pairs1 + pairs2)) == 4:  # Ensure no index is used more than once
                print(*pairs1, *pairs2)
                return
        elif sum_a1[l][0] + sum_a2[r][0] < target:
            l += 1
        else:
            r += 1
    # also perform two pointers on each of the individual arrays
    sum_a2.reverse()
    L = 0
    R = len(sum_a1) - 1
    while L < R:
        if sum_a1[L][0] + sum_a1[R][0] == target:
            pairs1 = sum_a1[L][1]
            pairs2 = sum_a1[R][1]
            if len(set(pairs1 + pairs2)) == 4:  # Ensure no index is used more than once
                print(*pairs1, *pairs2)
                return
        elif sum_a1[L][0] + sum_a1[R][0] < target:
            L += 1
        else:
            R -= 1
    L = 0
    R = len(sum_a2) - 1
    while L < R:
        if sum_a2[L][0] + sum_a2[R][0] == target:
            pairs1 = sum_a2[L][1]
            pairs2 = sum_a2[R][1]
            if len(set(pairs1 + pairs2)) == 4:  # Ensure no index is used more than once
                print(*pairs1, *pairs2)
                return
        elif sum_a2[L][0] + sum_a2[R][0] < target:
            L += 1
        else:
            R -= 1
    print("IMPOSSIBLE")
solve()