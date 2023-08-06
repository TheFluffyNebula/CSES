import sys
# sys.stdin = open("ReadingBooks.in")

n = int(input())
a = list(map(int,input().split()))
a.sort()
# print(a, a[:n - 1])
if sum(a[:n - 1]) >= a[-1]:
    print(sum(a))
else:
    print(a[-1] * 2)


'''
trying a few different strategies
1. partition based on mx books
reasoning: one person reading a long book while another is seems optimal
thoughts: it probably won't work since it just flat out does not for the partition problem
2. mx order but add to lesser list
reasoning: 1 1 1 1000000000 1 1 1 1 1 1
thoughts: this probably also won't work
went from 3 right testcases to 8
if 3 doesn't work then I'm going to look at the solution
3. direct simulation
TC:
3
7 6 4
ans: 17
as p1 starts reading 7, p2 reads 4
at t = 4, p2 switches to 6
at t = 7, p1 switches to 4
at t = 10, p2 switches to 7
both finish at time t = 17, which just so happens to be the sum of the books' times
hmm, right now I think that if elements sum is geq to the max element, it's just sum(elements)
else, it's 2 * max(elements)
ayyyy logic for the win!
'''