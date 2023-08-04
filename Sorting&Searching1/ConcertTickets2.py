# import sys # Charles Tang's solution
# sys.stdin = open("ConcertTickets.in")
# input = sys.stdin.readline

from bisect import *

n, m = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()

offers = list(map(int, input().split()))

for offer in offers:
    index = bisect_right(prices, offer)
    if index:
        print(prices.pop(index-1))
    else:
        print(-1)

# wait what, that's what I thought I did but more concise
# nevermind also TLE