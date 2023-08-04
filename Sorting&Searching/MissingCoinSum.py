import sys
# sys.stdin = open("MissingCoinSum.in")

n = int(input())
a = list(map(int,input().split()))
a.sort()
# print(a)
pf = [0]
for i in range(n):
    pf.append(pf[-1] + a[i])
# print(pf)

def solve():
    for i in range(n):
        if a[i] > pf[i] + 1:
            print(pf[i] + 1)
            return
    print(sum(a) + 1)
solve()

'''
hmm, by looking at some cases, the answer is always one of the prefix sums plus one
for example, here it's 5 + 1 and if were a bunch of 1's it would be total sum + 1
if the increasing rate of pf ever jumps by more than 1 it ends there
ex. 1 2 3 4 -> 11
1 2 3 5 -> 7
'''