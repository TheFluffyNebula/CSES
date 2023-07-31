import sys
# sys.stdin = open("AppleDivision.in")
n = int(input())
a = list(map(int,input().split()))
tot = sum(a)

all = [bin(i)[2:].zfill(n) for i in range(2**n)]
best = 1e10
for i in range(len(all)):
    first = 0
    for j in range(n):
        if all[i][j] == '1':
            first += a[j]
    second = tot - first
    best = min(best, abs(first - second))
print(best)

'''
I'm pretty sure this is aka the partition problem
the easiest of the np-hard category
input is n < 20 so I'm going to try everything using bitmasks
count in binary up to 2^20
nevermind, it's too slow at 10^6 * n
however, gray code gave me a silly fun idea
I can do the same thing but since I'm only changing one bit,
I can add/subtract in o(1) time so it's hopefully just 2^n
'''