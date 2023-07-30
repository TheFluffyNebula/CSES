import sys
# sys.stdin = open("Permutations.in")
n = int(input())

if n == 1:
    print(1)
elif n <= 3:
    print("NO SOLUTION")
else:
    ans = [i for i in range(2, n + 1, 2)] + [i for i in range(1, n + 1, 2)]
    print(*ans)

'''
n=4
2, 4, 1, 3
'''