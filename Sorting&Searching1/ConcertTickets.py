import sys #TLE
# sys.stdin = open("ConcertTickets.in")
input = sys.stdin.readline
import bisect

n, m = map(int,input().split())
prices = list(map(int,input().split()))
customer = list(map(int,input().split()))
prices.sort()
# print(prices)

ans = []
for i in range(m):
    target = customer[i]
    index = bisect.bisect(prices, target)
    if prices:
        x = prices[index - 1]
        if x <= target:
            prices.pop(index - 1)
            ans.append(x)
        else:
            ans.append(-1)
    else:
        ans.append(-1)
    # print(prices)
print(*ans, sep = "\n")